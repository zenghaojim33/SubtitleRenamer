# SubtitleRenamer

![Python application](https://github.com/zenghaojim33/SubtitleRenamer/actions/workflows/python-app.yml/badge.svg)

(https://github.com/zenghaojim33/SubtitleRenamer/actions/workflows/python-app.yml)
This is a Python script that renames subtitles for TV shows to match the corresponding video file names. It can be used to automatically rename a large batch of subtitles in a specified directory.

## Usage

To run the script, use the following command in the terminal:

python rename_subtitles.py -d [directory]


Where [directory] is the path to the directory that contains the subtitles and video files.

The script looks for video files with extensions .mp4, .avi, and .mkv, and subtitle files with extensions .srt, .sub, and .idx. It matches video and subtitle files whose names contain the same season and episode number, in the format S01E01.

If a match is found between a video file and a subtitle file, the subtitle file is renamed to match the video file name.

## Requirements

This script requires Python 3 to run. No additional third-party libraries are required. The script has been tested on macOS and Windows operating systems.

## License

This script is released under the MIT license. See the LICENSE file for more details.
