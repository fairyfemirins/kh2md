#!/usr/bin/env python3
"""
Kindle Highlights to Markdown (KH2MD)

Parses Kindle's "My Clippings.txt" and converts highlights into structured Markdown files.
"""

import re
import argparse
import os
from pathlib import Path


class KindleHighlight:
    """Represents a single highlight or note from Kindle."""

    def __init__(self, book_title, author, highlight, page=None, location=None, date=None):
        self.book_title = book_title
        self.author = author
        self.highlight = highlight
        self.page = page
        self.location = location
        self.date = date

    def to_markdown(self):
        """Convert the highlight to Markdown format."""
        metadata = f"> **Page**: {self.page} | **Location**: {self.location} | **Date**: {self.date}\n\n"
        return f"{metadata}{self.highlight}\n\n---\n"


def parse_clippings(file_path):
    """Parse Kindle's "My Clippings.txt" into a dictionary of highlights."""
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        content = file.read()

    # Kindle clippings are separated by "=========="
    entries = re.split(r'\r?\n==========\r?\n', content)
    highlights = {}

    for entry in entries:
        if not entry.strip():
            continue

        print(f"DEBUG: Entry:\n{entry}\n---")  # Debug print

        # Brute-force extraction
        lines = entry.strip().split('\n')
        if len(lines) < 3:
            print("DEBUG: Not enough lines")
            continue

        book_title_line = lines[0].strip()
        # Extract author from book title line (e.g., "Title (Author)")
        author = "Unknown"
        if '(' in book_title_line and ')' in book_title_line:
            author = book_title_line.split('(')[1].split(')')[0].strip()
            book_title = book_title_line.split('(')[0].strip()
        else:
            book_title = book_title_line

        highlight_text = "\n".join(lines[3:]).strip().replace("==========", "")

        print(f"DEBUG: Brute-force - Title: {book_title}, Author: {author}, Highlight: {highlight_text}")

        if book_title not in highlights:
            highlights[book_title] = []

        highlights[book_title].append(
            KindleHighlight(
                book_title=book_title,
                author=author,
                highlight=highlight_text
            )
        )

    return highlights


def generate_markdown(highlights, output_dir):
    """Generate Markdown files for each book's highlights."""
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    for book_title, book_highlights in highlights.items():
        # Sanitize book title for filename
        safe_title = re.sub(r'[\\/*?:"<>|]', "_", book_title).replace(" ", "_")
        output_path = os.path.join(output_dir, f"{safe_title}.md")

        with open(output_path, 'w', encoding='utf-8') as file:
            # Write YAML frontmatter
            file.write(f"---\ntitle: {book_title}\nauthor: {book_highlights[0].author}\n---\n\n")

            # Write highlights
            for highlight in book_highlights:
                file.write(highlight.to_markdown())


def main():
    print("DEBUG: Starting script")  # Debug print
    parser = argparse.ArgumentParser(description='Convert Kindle highlights to Markdown.')
    parser.add_argument('--input', type=str, required=True, help='Path to "My Clippings.txt"')
    parser.add_argument('--output', type=str, required=True, help='Output directory for Markdown files')
    args = parser.parse_args()

    highlights = parse_clippings(args.input)
    generate_markdown(highlights, args.output)
    print(f"Generated {len(highlights)} Markdown files in {args.output}")


if __name__ == "__main__":
    main()