#!/usr/bin/env python3

import argparse
from os import path
import ffmpeg

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

    if args.dry_run:
        print(" ".join(cmd.compile()))
    else:
        cmd.run()
