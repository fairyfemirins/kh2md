# Kindle Highlights to Markdown (KH2MD)

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)

A CLI tool to parse Kindle highlights (`My Clippings.txt`) and convert them into structured Markdown files.

## Features
- Parse `My Clippings.txt` from Kindle.
- Extract highlights, notes, and book metadata.
- Output structured Markdown files (one per book).
- Generate a searchable index.
- Optional: Summarize highlights using AI.

## Installation
```bash
pip install kh2md
```

## Usage

1. **Export your Kindle highlights**:
   - Connect your Kindle to your computer.
   - Copy `My Clippings.txt` from the `documents` folder.

2. **Run KH2MD**:
```bash
kh2md --input "My Clippings.txt" --output "highlights/"
```

3. **View the output**:
   - Each book's highlights are saved as a Markdown file in the `highlights/` directory.
   - Files are named after the book title and include YAML frontmatter for metadata.

## Technical Architecture
- **Input**: `My Clippings.txt` (Kindle's default clippings file).
- **Parser**: Python-based regex and state machine to handle Kindle's format.
- **Output**: Markdown files with YAML frontmatter for metadata.
- **Optional AI**: Summarize highlights using a local LLM (e.g., `llama-cpp`).

## License
MIT