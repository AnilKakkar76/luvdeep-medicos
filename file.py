import os
import random
import subprocess
from datetime import datetime, timedelta


commit_messages = [
    # UI / Frontend changes
    "Update hero section layout", "Fix navbar responsiveness on mobile",
    "Adjust product card grid spacing", "Improve button hover effects",
    "Refine typography and font sizes", "Fix overlapping elements in footer",
    "Update color scheme for better contrast", "Add smooth scroll behavior",
    "Fix image aspect ratio on product cards", "Improve gallery section alignment",
    "Update topbar styling", "Fix broken layout on tablet view",
    "Add subtle animations to CTA section", "Adjust padding and margins sitewide",
    "Improve service bar design", "Fix sticky header z-index issue",
    "Update brand logo styling", "Refine contact section layout",

    # Content updates
    "Add new medicine category", "Update product descriptions",
    "Fix typo in about section", "Add pharmacist credentials",
    "Update store address details", "Add new gallery images",
    "Update business hours", "Add customer testimonial section",
    "Update footer copyright year", "Add new service offering",
    "Improve meta description", "Update page title and keywords",

    # Bug fixes
    "Fix broken image links", "Resolve CSS grid overflow issue",
    "Fix navigation menu toggle bug", "Correct WhatsApp float position",
    "Fix console errors", "Patch broken anchor links",
    "Fix mobile menu closing issue", "Resolve font loading flash",

    # Refactoring / maintenance
    "Refactor CSS variables", "Clean up unused styles",
    "Reorganize asset folder structure", "Optimize image file sizes",
    "Minify CSS for production", "Improve code formatting",
    "Remove deprecated styles", "Update dependencies",

    # Feature additions
    "Add Google Maps embed", "Add prescription upload section",
    "Add WhatsApp quick contact", "Add product search bar",
    "Add FAQ section", "Add newsletter signup form",
    "Add social media links", "Add delivery information section"
]

# Date range: Jan 1 2026 to May 31 2026
start_date = datetime(2026, 1, 1)
end_date = datetime(2026, 5, 31)

total_days = (end_date - start_date).days
total_commits = 0

print(f"Generating backdated commits from {start_date.date()} to {end_date.date()}...")

# Loop through each day
for i in range(total_days + 1):
    current_date = start_date + timedelta(days=i)
    
    # Randomly decide commits per day (realistic distribution)
    roll = random.randint(1, 100)
    
    if roll <= 25:
        commits_today = 0
    elif roll <= 60:
        commits_today = random.randint(1, 2)
    elif roll <= 85:
        commits_today = random.randint(3, 5)
    else:
        commits_today = random.randint(6, 10)

    # Skip Sundays sometimes to look realistic
    if current_date.weekday() == 6 and random.randint(1, 100) <= 70: # 6 is Sunday
        commits_today = 0

    if commits_today == 0:
        continue

    for _ in range(commits_today):
        # Random time between 9 AM and 11 PM
        hour = random.randint(9, 22)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)

        commit_date = current_date.replace(hour=hour, minute=minute, second=second)
        
        # Format for Git (ISO 8601 format works best for Python)
        git_date = commit_date.strftime("%Y-%m-%d %H:%M:%S")

        # Pick a random commit message
        msg = random.choice(commit_messages)

        # Make a small change to a log file so Git registers a commit
        with open(".commit-log.txt", "a", encoding="utf-8") as f:
            f.write(f"Commit at {git_date} - {msg}\n")

        # Set environment variables for this specific commit
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = git_date
        env["GIT_COMMITTER_DATE"] = git_date

        # Stage and commit using subprocess
        subprocess.run(["git", "add", "."], env=env, stdout=subprocess.DEVNULL)
        subprocess.run(["git", "commit", "-m", msg, "--quiet"], env=env)
        
        total_commits += 1

print("\n==========================================")
print(f"DONE! Created {total_commits} backdated commits.")
print("Now run: git push origin main")
print("==========================================")