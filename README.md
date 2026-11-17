# Python Automation

A small, dependency-free starter project for Python automation. It includes a file organizer example that sorts files into folders by extension. The script previews changes by default; it only moves files when you explicitly pass `--apply`.

## Requirements

- Python 3.10 or newer
- No third-party packages required

## Run

Preview the proposed changes:

```bash
python main.py /path/to/folder
```

Apply the moves:

```bash
python main.py /path/to/folder --apply
```

Files that already have a destination with the same name are skipped. Test on a copy of your files first.

## Customize

Replace or extend `organize_files` in `main.py` with the automation you need. Keep a preview or dry-run mode for actions that modify files or external services.
