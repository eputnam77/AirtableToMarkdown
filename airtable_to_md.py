import csv
import os
from datetime import datetime

# ----------------------------
# CONFIGURATION
# ----------------------------
CSV_FILE = "airtable_export.csv"   # Airtable export as CSV
OUTPUT_DIR = "Knowledge Log"       # Folder to save markdown files

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ----------------------------
# HELPER FUNCTION
# ----------------------------
def sanitize_filename(text):
    """Return a filesystem-safe filename."""
    return "".join(c for c in text if c.isalnum() or c in (' ', '-', '_')).rstrip()

# ----------------------------
# PROCESS CSV
# ----------------------------
with open(CSV_FILE, newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        date_learned = row.get("Date learned", "").strip()
        source = row.get("Source", "").strip()
        summary = row.get("Summary", "").strip()
        notes = row.get("Notes", "").strip()
        email_folder = row.get("Email folder", "").strip()

        # Try converting date to YYYY-MM-DD format
        try:
            date_obj = datetime.strptime(date_learned, "%m/%d/%Y")
            date_str = date_obj.strftime("%Y-%m-%d")
        except:
            date_str = date_learned  # leave as-is if parsing fails

        # Create filename: YYYY-MM-DD Summary.md
        filename = f"{date_str} - {sanitize_filename(summary)[:50]}.md"
        filepath = os.path.join(OUTPUT_DIR, filename)

        # ----------------------------
        # YAML Frontmatter
        # ----------------------------
        content = f"""---
date-learned: {date_str}
source: {source}
summary: "{summary}"
email-folder: "{email_folder}"
tags: #knowledge
---

## Notes
{notes}
"""

        # Save markdown file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"✅ Created: {filename}")

print("🎯 Done! All Markdown notes saved in:", OUTPUT_DIR)
