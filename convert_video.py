#!/usr/bin/env python3

import argparse
from os import path
import ffmpeg


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", type=str, nargs="+")
    parser.add_argument("--extension", "-e", type=str, default="mkv")
    parser.add_argument(
        "--dry-run",
        help="simulate actions without touching filesystem",
        action="store_true",
    )
    args = parser.parse_args()

    for filename in args.filenames:
        (name, _) = path.splitext(filename)
        out = f"{name}.{args.extension}"
        cmd = ffmpeg.input(filename).output(
            out,
            acodec="copy",
            vcodec="copy",
        )

        print(" ".join(cmd.compile()))

        if args.dry_run:
            continue

        cmd.run()


if __name__ == "__main__":
    main()
