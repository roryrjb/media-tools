# media tools

## About

This is basically a set of wrapper scripts for `ffmpeg` that I use regularly, mostly to quickly edit dog photos and videos... no seriously.

__Scripts:__

* `sort-media`
* `cut-vide`
* `resize-video`
* `convert-video`
* `make-gif`
* `remove-audio`
* `slow-motion-correct`

All of these have `--help` flags which detail the usage.

## Installation

_Technically_ this is all portable Python but I only really care about Windows, therefore there's a simple `build.bat` script that will lint and install all of the scripts. It just assumes you have the default Python for Windows installation setup. Also assumes you have `ffmpeg.exe` and `ffprobe.exe` somewhere in your `%PATH%`.