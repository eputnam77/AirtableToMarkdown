# Airtable to Markdown Converter

This script converts an **Airtable CSV export** into **Markdown notes** that are compatible with [Obsidian](https://obsidian.md), including YAML frontmatter for use with [Dataview](https://blacksmithgu.github.io/obsidian-dataview/).

Each row from the Airtable table becomes its own `.md` file with metadata and notes ready for searching, linking, and automation inside your Obsidian vault.

---

## Features
- Converts CSV export from Airtable → Individual Markdown files.
- Adds **YAML frontmatter** fields:
  - `date-learned`
  - `source`
  - `summary`
  - `email-folder`
  - `tags`
- Easy integration with Obsidian’s **Dataview** plugin.
- Automatically names files based on `date learned` + `summary`.
- Cleans file names to make them **filesystem-safe**.

---

## Example Output

**File:**  
```
2025-08-22 - Doc rev number letter.md
```

**Content:**
```markdown
---
date-learned: 2025-08-22
source: Email
summary: "Doc rev number/letter"
email-folder: "Process/Process"
tags: #knowledge
---

## Notes
(note)
```

---

## Requirements
- Python 3.7 or higher (Windows, Mac, Linux)

---

## Setup & Usage

1. **Export Airtable as CSV**
   - In Airtable, click **View → Download CSV**.
   - Save it as `airtable_export.csv`.

2. **Save the Script**
   - Copy `airtable_to_md.py` into the same folder as your CSV file.

3. **Run the Script**
   Open a terminal or PowerShell in that folder and run:
   ```bash
   python airtable_to_md.py
   ```
   or:
   ```bash
   py airtable_to_md.py
   ```

4. **Check the Output**
   - A new folder named `Knowledge Log` will be created.
   - Inside, each row from the CSV will be a `.md` file.

5. **Move into Obsidian Vault**
   - Move the `Knowledge Log` folder into your Obsidian vault.
   - Enable the **Dataview** plugin to query entries:
     ```dataview
     TABLE date-learned, source, summary, email-folder
     FROM "Knowledge Log"
     SORT date-learned DESC
     ```

---

## Notes on CSV Columns
The script expects these CSV column headers from Airtable:
- `Date learned`  
- `Source`  
- `Summary`  
- `Notes`  
- `Email folder`  

If your Airtable headers are different, edit the script’s `row.get()` keys to match.

---

## Troubleshooting
- **"No such file or directory" error** → Ensure the script and `airtable_export.csv` are in the same directory when running.
- **Python not found** → On Windows, use `python` or `py` (not `python3`).
- **Output filenames truncated** → Summaries are shortened to 50 characters for safe filenames.

---

## License
You are free to use, modify, and adapt this script for personal or work purposes.
