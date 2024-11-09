#!/usr/bin/env python3

import argparse
from datetime import datetime
import exifread
import ffmpeg
import os
import sys


EXIF_TYPES = (".jpg", ".jpeg", ".tif", ".tiff", ".wav", ".png", ".webp")
FFMPEG_TYPES = (".mkv", ".mp4", ".mov", ".avi")
proposed_filenames = []  # for use with --dry-run


def exists(args, filename):
    return (
        proposed_filenames.count(filename) > 0
        if args.dry_run
        else os.path.exists(filename)
    )


def get_exif_datetime(filename):
    with open(filename, "rb") as fh:
        try:
            tags = exifread.process_file(fh)

            if not tags:
                print(f"Couldn't find EXIF metadata in {filename}.", file=sys.stderr)
                return None

            tag_value = tags.get("Image DateTime")

            if not datetime:
                print(f"Couldn't find datetime in {filename}.", file=sys.stderr)
                return None

            return datetime.strptime(str(tag_value), "%Y:%m:%d %H:%M:%S")
        except Exception as e:
            print(f"Error reading EXIF data from {filename}: {e}.", file=sys.stderr)
            return None


def get_ffmpeg_datetime(filename):
    metadata = ffmpeg.probe(filename)
    creation_time = (
        metadata["format"]["tags"]["creation_time"]
        if "creation_time" in metadata["format"]["tags"]
        else None
    )

    if creation_time is None:
        return None

    return datetime.strptime(creation_time, "%Y-%m-%dT%H:%M:%S.%fZ")


def rename_file(args, prefix, date, filename, ext):
    if date is None:
        print(f"Date couldn't be extracted from {filename}.", file=sys.stderr)
        return

    try:
        dirname = os.path.dirname(filename)
        new_filename = f"{dirname}/{prefix}_{date.strftime('%Y%m%d_%H%M%S')}{ext}"

        if filename == new_filename:
            return

        if exists(args, new_filename):
            split = os.path.splitext(new_filename)
            counter = 1

            while True:
                new_filename = f"{split[0]}_{counter}{split[1]}"

                if exists(args, new_filename):
                    counter += 1
                else:
                    break

        if args.dry_run:
            print(f"{filename} -> {new_filename}")
        else:
            print(f"{filename} -> {new_filename}")
            os.rename(filename, new_filename)
    except Exception as e:
        print(f"Error renaming {filename}: {e}.", file=sys.stderr)


def rename_image(args, filename, ext):
    date = get_exif_datetime(filename)
    rename_file(args, "IMG", date, filename, ext)


def rename_video(args, filename, ext):
    date = get_ffmpeg_datetime(filename)
    rename_file(args, "VID", date, filename, ext)


def scan_dir_for_files(path, recursive=False):
    for entry in os.scandir(path):
        if recursive and entry.is_dir() and not entry.is_symlink():
            for entry in scan_dir_for_files(entry.path, True):
                yield entry
        elif entry.is_file():
            yield entry.path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dirs",
        help="Move files into a date-based directory tree",
        action="store_true",
    )
    parser.add_argument(
        "--recursive", help="Match files recursively", action="store_true"
    )
    parser.add_argument(
        "--dry-run",
        help="Simulate actions without touching filesystem",
        action="store_true",
    )
    args = parser.parse_args()

    for filename in scan_dir_for_files(".", args.recursive):
        ext = os.path.splitext(filename)[1].lower()

        if ext in EXIF_TYPES:
            rename_image(args, filename, ext)
        elif ext in FFMPEG_TYPES:
            rename_video(args, filename, ext)


if __name__ == "__main__":
    main()
