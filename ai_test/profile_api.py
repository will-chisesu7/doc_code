"""
profile_api.py — Local REST API server for profile.json
Usage: python3 profile_api.py
Endpoints:
  GET /profile          — full profile
  GET /profile/skills   — skills list
  GET /profile/projects — projects list
  GET /profile/social   — social links
"""

import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

PROFILE_FILE = "profile.json"
PORT = 8000


def load_profile():
    if not os.path.exists(PROFILE_FILE):
        return None
    with open(PROFILE_FILE) as f:
        return json.load(f)


class ProfileHandler(BaseHTTPRequestHandler):

    def send_json(self, data, status=200):
        body = json.dumps(data, indent=2).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", len(body))
        self.end_headers()
        self.wfile.write(body)

    def send_error_json(self, status, message):
        self.send_json({"error": message}, status)

    def do_GET(self):
        profile = load_profile()
        if profile is None:
            self.send_error_json(500, f"{PROFILE_FILE} not found")
            return

        routes = {
            "/profile":          profile,
            "/profile/skills":   {"skills": profile.get("skills", [])},
            "/profile/projects": {"projects": profile.get("projects", [])},
            "/profile/social":   {"social": profile.get("social", {})},
        }

        if self.path in routes:
            self.send_json(routes[self.path])
        elif self.path == "/":
            self.send_json({
                "message": "Profile API is running",
                "endpoints": list(routes.keys())
            })
        else:
            self.send_error_json(404, "Endpoint not found")

    def log_message(self, format, *args):
        print(f"  {self.address_string()} - {format % args}")


def main():
    server = HTTPServer(("localhost", PORT), ProfileHandler)
    print(f"Profile API running at http://localhost:{PORT}")
    print(f"Endpoints:")
    print(f"  GET http://localhost:{PORT}/profile")
    print(f"  GET http://localhost:{PORT}/profile/skills")
    print(f"  GET http://localhost:{PORT}/profile/projects")
    print(f"  GET http://localhost:{PORT}/profile/social")
    print(f"\nPress Ctrl+C to stop.\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")


if __name__ == "__main__":
    main()
