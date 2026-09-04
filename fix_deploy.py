#!/usr/bin/env python3
"""Fix Docker setup and push."""
import subprocess, os

os.chdir("/opt/data/dracula_video/dashboard")

# Create static dir and move files
os.makedirs("static", exist_ok=True)
subprocess.run(["cp", "index.html", "static/"])
subprocess.run(["cp", "calendar.json", "static/"])

# Commit and push
subprocess.run(["git", "add", "-A"], check=True)
subprocess.run(["git", "commit", "-m", "Fix: serve from static directory with dockerignore"], check=True)
subprocess.run(["git", "push", "origin", "main"], check=True)

print("✅ Pushed. Now trigger deploy via Railway.")
