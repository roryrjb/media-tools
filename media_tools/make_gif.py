#!/usr/bin/env python3

import argparse
from datetime import datetime
from os import path
import ffmpeg

DEFAULT_SCALE = 320
TIME_FORMAT = "%H:%M:%S"


def time(input: str):
    datetime.strptime(input, TIME_FORMAT)
    return input


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str)
    parser.add_argument("--start", type=time, default="00:00:00")
    parser.add_argument("--end", type=time, default="23:59:59")
    parser.add_argument("--fps", "-f", type=int, default=10)
    parser.add_argument("--scale", type=int, default=DEFAULT_SCALE)
    parser.add_argument("--name", type=str)

    args = parser.parse_args()
    (name, _) = path.splitext(args.filename)
    out = args.name if args.name else f"{name}-cut.gif"

    (name, _) = path.splitext(args.filename)
    out = f"{name}.gif"
    cmd = ffmpeg.input(args.filename, ss=args.start, to=args.end).output(
        out,
        vf=f"scale={args.scale}:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse,fps={args.fps}",
    )

    print(" ".join(cmd.compile()))
    cmd.run()
