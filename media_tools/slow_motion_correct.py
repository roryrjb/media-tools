#!/usr/bin/env python3

import sys
import argparse
from os import path
import ffmpeg


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str)
    parser.add_argument("--in-frame-rate", type=int, required=True)
    parser.add_argument("--out-frame-rate", type=int, default=30)
    parser.add_argument("--name", type=str)
    parser.add_argument(
        "--dry-run",
        help="simulate actions without touching filesystem",
        action="store_true",
    )
    args = parser.parse_args()
    (name, ext) = path.splitext(args.filename)
    out = args.name if args.name else f"{name}-slow{ext}"
    factor = args.in_frame_rate / args.out_frame_rate

    cmd = ffmpeg.input(args.filename).output(
        out,
        vf=f"setpts={factor}*PTS",
        r="30",
    )

    print(" ".join(cmd.compile()))

    if args.dry_run:
        sys.exit(0)

    cmd.run()
