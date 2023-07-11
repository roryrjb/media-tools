#!/usr/bin/env python3

import argparse
from os import path
import ffmpeg
import sys

DEFAULT_SCALE = 640


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str)
    parser.add_argument("--scale", type=int, default=DEFAULT_SCALE)
    parser.add_argument(
        "--dry-run",
        help="Simulate actions without touching filesystem",
        action="store_true",
    )
    args = parser.parse_args()
    scale = args.scale or DEFAULT_SCALE
    (name, ext) = path.splitext(args.filename)
    out = f"{name}-small{ext}"
    cmd = ffmpeg.input(args.filename).output(out, vf=f"scale={scale}:-1")

    print(" ".join(cmd.compile()))

    if args.dry_run:
        sys.exit(0)

    cmd.run()
