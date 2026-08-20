# =====================================================================
# NIPPON FIT — local preview server
#
# Shows the website on your own computer before it goes live, at
#     http://localhost:4180
#
# TO RUN IT, open a terminal in the NipponFit_website folder and type:
#     python tools/serve.py
#
# Press Ctrl+C to stop it.
#
# The only reason this exists rather than a plain file-open is the
# addresses. Live, the pages are at /contact and /locations with no
# ".html" on the end — that is how Vercel serves them. This little server
# does the same thing, so what you see here is exactly what visitors get.
# =====================================================================

import http.server
import pathlib

PORT = 4180
ROOT = pathlib.Path(__file__).resolve().parent.parent


class CleanUrlHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def translate_path(self, path):
        """If /contact was asked for, serve contact.html — the same rule
        Vercel applies.

        The directory check matters: there is both a blog.html page and a
        blog/ folder holding the articles. Without this, the built-in
        server would redirect /blog into the folder and show nothing.
        The page always wins, which is what Vercel does too."""
        result = super().translate_path(path)
        candidate = pathlib.Path(result)

        if not candidate.suffix and not candidate.is_file():
            with_html = candidate.with_suffix(".html")
            if with_html.is_file():
                return str(with_html)

        return result

    def send_error(self, code, message=None, explain=None):
        """Show our own 404 page rather than the bare server one."""
        if code == 404:
            not_found = ROOT / "404.html"
            if not_found.exists():
                body = not_found.read_bytes()
                self.send_response(404)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
        super().send_error(code, message, explain)

    def end_headers(self):
        """Tell the browser never to keep a copy.

        Without this the browser hangs on to the last version it saw, and
        you refresh the page after a change and are shown the OLD one —
        which looks exactly like the change did not work. Only affects this
        local preview; the live site caches normally."""
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, fmt, *args):
        pass  # keep the terminal quiet


if __name__ == "__main__":
    # ThreadingHTTPServer, not the plain one: a browser holds its connection
    # open between requests, and a single-threaded server would sit blocked on
    # that one connection and refuse everything else.
    http.server.ThreadingHTTPServer.allow_reuse_address = True

    with http.server.ThreadingHTTPServer(("", PORT), CleanUrlHandler) as httpd:
        print(f"Nippon Fit website running at http://localhost:{PORT}")
        print("Press Ctrl+C to stop.")
        httpd.serve_forever()
