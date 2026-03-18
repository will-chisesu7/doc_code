"""
resume_generator.py — Generates an HTML resume from profile.json
Usage: python3 resume_generator.py
Output: resume.html
"""

import json
import os

PROFILE_FILE = "profile.json"
OUTPUT_FILE = "resume.html"


def load_profile():
    if not os.path.exists(PROFILE_FILE):
        print(f"Error: {PROFILE_FILE} not found.")
        exit(1)
    with open(PROFILE_FILE) as f:
        return json.load(f)


def generate_resume(p):
    skills_html = "".join(f'<span class="skill">{s}</span>' for s in p.get("skills", []))
    projects_html = "".join(
        f'<div class="project"><strong>{proj["name"]}</strong> — {proj["description"]}</div>'
        for proj in p.get("projects", [])
    )
    social_html = "".join(
        f'<a href="https://{url}">{platform.capitalize()}: {url}</a><br/>'
        for platform, url in p.get("social", {}).items()
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <title>{p['name']} — Resume</title>
  <style>
    body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 40px auto; padding: 0 20px; color: #222; }}
    h1 {{ font-size: 2rem; margin-bottom: 4px; }}
    .meta {{ color: #555; font-size: 0.95rem; margin-bottom: 20px; }}
    h2 {{ border-bottom: 2px solid #3b82f6; padding-bottom: 4px; margin: 24px 0 12px; color: #1e40af; }}
    .skill {{ display: inline-block; background: #dbeafe; color: #1e40af; padding: 4px 12px; border-radius: 12px; font-size: 0.82rem; margin: 3px; }}
    .project {{ margin: 8px 0; padding: 10px; background: #f8fafc; border-left: 3px solid #3b82f6; }}
    a {{ color: #3b82f6; }}
    @media print {{ body {{ margin: 20px; }} }}
  </style>
</head>
<body>
  <h1>{p['name']}</h1>
  <div class="meta">
    {p['role']} &nbsp;|&nbsp; {p['location']} &nbsp;|&nbsp; {p['email']}
  </div>

  <h2>Skills</h2>
  <div>{skills_html}</div>

  <h2>Projects</h2>
  <div>{projects_html}</div>

  <h2>Social</h2>
  <div>{social_html}</div>
</body>
</html>"""


def main():
    profile = load_profile()
    html = generate_resume(profile)
    with open(OUTPUT_FILE, "w") as f:
        f.write(html)
    print(f"Resume generated: {OUTPUT_FILE}")
    print(f"Open it in your browser: open {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
