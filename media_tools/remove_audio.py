#!/usr/bin/env python3

import argparse
from os import path
import ffmpeg


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str)
    parser.add_argument("--name", type=str)
    args = parser.parse_args()
    (name, ext) = path.splitext(args.filename)
    out = args.name if args.name else f"{name}-noaudio{ext}"

    cmd = ffmpeg.input(args.filename).output(
        out,
        an=None,
        vcodec="copy",
    )

    print(" ".join(cmd.compile()))

    cmd.run()
