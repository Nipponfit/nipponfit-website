# =====================================================================
# NIPPON FIT — the bodies of the three articles carried across from the
# old website.
#
# They live in their own file because the martial arts list is 185
# entries long and would drown everything else in pages_blog.py.
# =====================================================================

import blog_martial_arts


MARTIAL_ARTS_BODY = """
        <p>
          There are 180+ martial arts styles. It ranges from well-known styles (such as
          Karate, Taekwondo, Krav Maga, BJJ and MMA) to more unique martial arts styles
          (such as &ldquo;Drunken Fist&rdquo; Kung Fu, Sherlock Holmes&rsquo; Bartitsu and
          Zulu Stick Fighting).
        </p>
        <p>
          We have also broken this information into country of origin (i.e. martial arts
          that were developed in America, Japan, China or Korea) and martial arts styles
          dedicated to a &ldquo;specialty&rdquo; (i.e. weapons-based or grappling-based
          martial arts).
        </p>
        <p>
          Hopefully, this information will help you to find a martial arts style and school
          that is right for you. Many of these martial arts help participants to improve
          their overall fitness, learn self-defense, gain confidence and lose weight.
        </p>

        <h2>List of Martial Arts Styles</h2>
""" + blog_martial_arts.render_list()


ORIGIN_BODY = """
        <figure style="margin:0 0 2.4em">
          <img src="/assets/karate-characters.jpg"
               alt="The Chinese characters for kara te, meaning T'ang hand"
               loading="lazy" style="width:100%;max-width:520px;margin:0 auto">
          <figcaption style="text-align:center;font-size:13.5px;color:var(--ink-faint);margin-top:12px">
            The original writing for karate: &ldquo;kara te&rdquo;, meaning Chinese
            (T&rsquo;ang) hand.
          </figcaption>
        </figure>

        <h2>Karate</h2>
        <p>
          Karate stands for &ldquo;Empty hands&rdquo; in Japanese and is one of the martial
          art forms that originated in the Ryukyu Kingdom of the Okinawan islands as a form
          of self defense during the early 20th century, when using weapons were banned by
          the invading Japanese forces. It made its debut as an Olympic sport in the 2021
          Tokyo Olympics.
        </p>
        <p>
          Karate is a contact martial arts, predominantly a striking art using punching,
          kicking, knee and elbow strikes, and open hand techniques. A karate practitioner
          is called a <strong>&ldquo;Karateka&rdquo;</strong>.
        </p>
        <p>
          There are many theories related to the origin of Karate. One such theory states
          that it came from India thousands of years ago, and was brought to China by
          Bodhidharma (a Buddhist monk), who started teaching exercises to strengthen body
          and mind at Shaolinsi.
        </p>
        <p>
          Karate can be practiced as an art, self defense or as a combat sport. Traditional
          karate places emphasis on self development (<em>Budo</em> in Japanese). Modern
          style training emphasizes the psychological aspects incorporated into a proper
          attitude (<em>Kokoro</em> in Japanese) such as perseverance, fearlessness, virtue
          and leadership skills. Karate as a sport emphasizes exercise and competition.
        </p>
        <p>
          Karate training is divided into basics or fundamentals (<em>Kihon</em>), forms
          (<em>Kata</em>) and sparring (<em>Kumite</em>).
        </p>
        <p>
          Karate is practiced in many styles which differ in the training methods, focuses
          and culture, although these originated from the historical Okinawan parent styles
          of Naha-te, Tomari-te and Shuri-te. In modern times four styles of karate are
          popular and recognized by the World Karate Federation for international
          competition. They are: <strong>Goju-ryu, Shotokan, Shito-ryu and
          Wado-ryu</strong>.
        </p>

        <h2>Significant Dates in the History of Karate</h2>
        <div class="table-wrap">
          <table>
            <thead><tr><th>Year</th><th>Event</th></tr></thead>
            <tbody>
              <tr><td>1905</td><td>Karate is included in Okinawa&rsquo;s physical education programs at the intermediate level</td></tr>
              <tr><td>1917</td><td>Funakoshi gives the first public demonstration of karate-do</td></tr>
              <tr><td>1922</td><td>Funakoshi is invited by Dr. Jano Kano to give a demonstration at the Kodokan Dojo, bringing karate-do to Japan</td></tr>
              <tr><td>1924</td><td>The first university karate club is established in Japan, at Keio University</td></tr>
              <tr><td>1930s</td><td>Karate makes its way to Canada</td></tr>
              <tr><td>1936</td><td>Okinawan masters meet to discuss karate in Okinawa, a meeting sponsored by the newspaper Ryukyu Shimpo</td></tr>
              <tr><td>1939</td><td>Japan opens Shoto-Kan, its first formal training school</td></tr>
              <tr><td>1945</td><td>The first dojo was opened in the United States</td></tr>
              <tr><td>1949</td><td>The Japan Karate Association is formed</td></tr>
              <tr><td>1950s</td><td>Karate is introduced in the United Kingdom</td></tr>
              <tr><td>1960s</td><td>Karate makes its way to the Soviet Union and is banned and unbanned several times over the next three decades</td></tr>
              <tr><td>1964</td><td>France Shotokan Karate is created in France</td></tr>
              <tr><td>1989</td><td>Karate is legalized once again in the Soviet Union</td></tr>
            </tbody>
          </table>
        </div>

        <h2>Significant Historical Figures</h2>
        <ul>
          <li><strong>Gichin Funakoshi</strong> &mdash; Founder of Shotokan</li>
          <li><strong>Dr. Jano Kano</strong> &mdash; Founder of Japanese judo</li>
          <li><strong>Sakukawa Kanga</strong> &mdash; One of the first Okinawans to study in China</li>
          <li><strong>Itosu Anko</strong> &mdash; Often called the &ldquo;grandfather of karate&rdquo;, brought karate to Okinawan schools and simplified it for increased public acceptance</li>
          <li><strong>Chojun Miyagi</strong> &mdash; Named the G&#333;j&#363;-ryu style</li>
          <li><strong>Hironori Otsuka</strong> &mdash; Founder of the Wad&#333;-ryu style</li>
          <li><strong>Kenwa Mabuni</strong> &mdash; Founder of the Shit&#333;-ryu style</li>
        </ul>
"""


WORKOUT_BODY = """
        <p>
          Here is a quick full body tabata workout for intermediate and advanced level
          fitness enthusiasts. Beginners can tweak this workout &mdash; especially tricep
          dips, pushups and step ups &mdash; or adjust it as per your convenience.
          Professionals can use this sequence as a warmup session.
        </p>
        <p>Sequence of the 7 minute tabata workout is as follows:</p>

        <ol>
          <li>Jumping jacks</li>
          <li>Wall sits</li>
          <li>Push-ups</li>
          <li>Abdominal crunches</li>
          <li>Step ups onto a chair</li>
          <li>Squats</li>
          <li>Tricep dips on a chair</li>
          <li>Planks</li>
          <li>High knees / running in place</li>
          <li>Lunges</li>
          <li>Push-ups with rotation</li>
          <li>Side plank (left)</li>
          <li>Side plank (right)</li>
        </ol>

        <p>
          Work through the sequence in order. If any movement causes pain rather than
          effort, stop and ask an instructor &mdash; particularly the tricep dips and the
          planks, which are the two most commonly done badly.
        </p>
"""
