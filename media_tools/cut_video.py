#!/usr/bin/env python3

import sys
import argparse
from os import path
import ffmpeg
from datetime import datetime

TIME_FORMAT = "%H:%M:%S"


def time(input: str):
    datetime.strptime(input, TIME_FORMAT)
    return input


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str)
    parser.add_argument("--start", type=time, default="00:00:00")
    parser.add_argument("--end", type=time, default="23:59:59")
    parser.add_argument(
        "--dry-run",
        help="simulate actions without touching filesystem",
        action="store_true",
    )
    args = parser.parse_args()
    (name, ext) = path.splitext(args.filename)
    out = f"{name}-cut{ext}"
    cmd = ffmpeg.input(args.filename, ss=args.start, to=args.end).output(
        out,
        acodec="copy",
        vcodec="copy",
    )

    print(" ".join(cmd.compile()))

    if args.dry_run:
        sys.exit(0)

    cmd.run()
