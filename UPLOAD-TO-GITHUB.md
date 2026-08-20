# Getting the files onto GitHub

## Why the drag-and-drop failed

Two separate reasons, neither your fault:

**`.claude`** begins with a dot. Windows treats that as a hidden folder and does not
show it in File Explorer, so it was never in the selection — and GitHub's upload page
skips dotted folders anyway, without saying so.

**`assets`** holds 111 files spread across three levels of subfolders
(`assets`, `assets/gallery`, `assets/gallery/thumbs`). GitHub's drag-and-drop uploader
is unreliable with that much nesting and quietly drops files.

The upload page is fine for a handful of loose files. It is the wrong tool for a whole
website. **Git handles both cases without complaint**, and Git is already installed on
this computer.

---

## What I have already done

Nothing has left your computer. Locally, I have:

- Created the repository
- Added all **150 files** — including `.claude` and every one of the 111 files in
  `assets`
- Made the first commit
- Named the branch `main`
- Pointed it at `https://github.com/Nipponfit/nipponfit-website.git`

All that is left is to send it to GitHub.

---

## The one command to run

Open **Command Prompt** (press the Windows key, type `cmd`, press Enter) and paste
these two lines, pressing Enter after each:

```bash
cd /d F:\Nipponfit\NipponFit_website
```

```bash
git push -u origin main --force
```

**A browser window will open asking you to sign in to GitHub.** Sign in and allow it.
That happens once; Git remembers afterwards.

### Why `--force`

Your repository already holds the half-finished upload. `--force` tells Git to replace
what is up there with the complete set from your computer. Nothing is lost — everything
on GitHub right now is an incomplete copy of what is about to replace it.

### What success looks like

The command finishes with something like `main -> main`. Refresh your repository page on
GitHub and you should see:

- `assets`, `blog`, `css`, `js`, `tools` folders
- `index.html` and the other pages
- **150 files in total**

Click into `assets` → `gallery` and you should count 44 photographs plus a `thumbs`
folder.

---

## If the sign-in window does not appear

Your GitHub account may need a token instead of a password. If Git asks for a password
and rejects yours:

1. Go to **github.com** → your picture (top right) → **Settings**
2. Scroll to the bottom: **Developer settings**
3. **Personal access tokens** → **Tokens (classic)** → **Generate new token (classic)**
4. Name it `nipponfit-website`, tick the **repo** box, click **Generate token**
5. **Copy the token** — you only see it once
6. Run the push again, and paste the token where it asks for the password

---

## Is `.claude` even needed?

Not for the website to work. It holds one small file that lets me preview the site on
this computer. It does no harm on GitHub and it is not published to the live site, so it
is simplest to include it and stop worrying about it.

---

## After the push

Carry on from **Stage 2** in `PUBLISH.md` — importing the repository into Vercel.

From now on, whenever anything changes, these three lines send the update:

```bash
cd /d F:\Nipponfit\NipponFit_website
```

```bash
git add -A
```

```bash
git commit -m "describe what changed" && git push
```

No `--force` needed ever again — that was only to clear the half-finished upload.
