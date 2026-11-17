"""A safe starter for small Python automation scripts."""

from __future__ import annotations

import argparse
from pathlib import Path
import shutil


def organize_files(folder: Path, *, apply: bool = False) -> None:
    """Sort files into extension-named folders; preview changes unless --apply is set."""
    if not folder.is_dir():
        raise NotADirectoryError(f"Not a directory: {folder}")

    for source in sorted(folder.iterdir()):
        if not source.is_file() or source.name == Path(__file__).name:
            continue

        category = source.suffix.lower().lstrip(".") or "no_extension"
        destination_dir = folder / category
        destination = destination_dir / source.name

        if destination.exists():
            print(f"Skip (destination exists): {source.name}")
            continue

        print(f"{source.name} -> {category}/{source.name}")
        if apply:
            destination_dir.mkdir(exist_ok=True)
            shutil.move(str(source), str(destination))


def main() -> None:
    parser = argparse.ArgumentParser(description="Organize files by extension.")
    parser.add_argument("folder", type=Path, help="Folder whose files should be organized")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Perform the moves (without this flag, the script only previews them)",
    )
    args = parser.parse_args()

    try:
        organize_files(args.folder, apply=args.apply)
    except (NotADirectoryError, PermissionError) as error:
        parser.error(str(error))

    if not args.apply:
        print("Preview only. Add --apply to move the files.")


if __name__ == "__main__":
    main()
