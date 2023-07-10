from setuptools import setup, find_packages

setup(
    name="media-tools",
    version="0.1",
    description="A set of tools for working with photos and videos.",
    url="https://github.com/roryrjb/media-tools",
    author="Rory Bradford",
    author_email="roryrjb@gmail.com",
    license="MIT",
    install_requires=["ffmpeg-python", "exifread"],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "sort-media=media_tools.sort_media:main",
            "cut-video=media_tools.cut_video:main",
            "resize-video=media_tools.resize_video:main",
        ],
    },
    zip_safe=False,
)
