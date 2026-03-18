"""
bio_generator.py — Generates bios and cover letters from profile.json
Usage: python3 bio_generator.py
"""

import json
import os

PROFILE_FILE = "profile.json"


def load_profile():
    if not os.path.exists(PROFILE_FILE):
        print(f"Error: {PROFILE_FILE} not found.")
        exit(1)
    with open(PROFILE_FILE) as f:
        return json.load(f)


def short_bio(p):
    skills_preview = ", ".join(p["skills"][:4])
    return (
        f"{p['name']} is an {p['role']} based in {p['location']}. "
        f"With expertise in {skills_preview}, and more, they bring a strong technical foundation "
        f"to every project they work on."
    )


def full_bio(p):
    all_skills = ", ".join(p["skills"])
    projects = ", ".join(proj["name"] for proj in p.get("projects", []))
    return (
        f"About {p['name']}\n"
        f"{'=' * 50}\n"
        f"{p['name']} is a skilled {p['role']} based in {p['location']}.\n\n"
        f"Technical Skills:\n{all_skills}.\n\n"
        f"Notable Projects: {projects}.\n\n"
        f"Contact: {p['email']}"
    )


def cover_letter(p, company="[Company Name]", position=None):
    position = position or p["role"]
    skills_preview = ", ".join(p["skills"][:5])
    return f"""Dear Hiring Manager at {company},

I am writing to express my interest in the {position} position at {company}.
As an experienced {p['role']} based in {p['location']}, I have built a strong
background in {skills_preview}, among other areas.

Throughout my career, I have demonstrated the ability to manage and support complex
IT environments, ensuring reliability, security, and performance. I am confident that
my skills and commitment to excellence make me a strong candidate for this role.

I would welcome the opportunity to discuss how my experience aligns with your team's
needs. Please feel free to reach me at {p['email']}.

Sincerely,
{p['name']}
"""


def save_output(filename, content):
    with open(filename, "w") as f:
        f.write(content)
    print(f"  Saved: {filename}")


def main():
    profile = load_profile()

    print("\n" + "=" * 50)
    print("         BIO & COVER LETTER GENERATOR")
    print("=" * 50)
    print("  1. Short bio")
    print("  2. Full bio")
    print("  3. Cover letter")
    print("  4. Generate all")
    print("=" * 50)

    choice = input("\nChoose an option (1-4): ").strip()

    if choice == "1":
        print("\n--- Short Bio ---\n")
        print(short_bio(profile))

    elif choice == "2":
        print("\n--- Full Bio ---\n")
        print(full_bio(profile))
        save = input("\nSave to file? (yes/no): ").strip().lower()
        if save in ["yes", "y"]:
            save_output("bio.txt", full_bio(profile))

    elif choice == "3":
        company = input("Enter company name (or press Enter to skip): ").strip() or "[Company Name]"
        position = input(f"Enter position (or press Enter for '{profile['role']}'): ").strip() or None
        letter = cover_letter(profile, company, position)
        print("\n--- Cover Letter ---\n")
        print(letter)
        save = input("Save to file? (yes/no): ").strip().lower()
        if save in ["yes", "y"]:
            save_output("cover_letter.txt", letter)

    elif choice == "4":
        save_output("bio_short.txt", short_bio(profile))
        save_output("bio_full.txt", full_bio(profile))
        save_output("cover_letter.txt", cover_letter(profile))
        print("\nAll files generated.")

    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
