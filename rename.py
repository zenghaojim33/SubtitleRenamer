import os
import re
import argparse

def rename_subtitles(folder_path):
    video_files = []
    subtitle_files = []

    # loop through all files in the folder
    for filename in os.listdir(folder_path):
        if re.match(r'.*\.(mp4|avi|mkv)$', filename):
            # if video file, add it to the video files list
            video_files.append(filename)
        elif re.match(r'.*\.srt|sub|idx$', filename):
            # if subtitle file, add it to the subtitle files list
            subtitle_files.append(filename)

    # loop through all video files and file matching subtitle files
    for video_file in video_files:
        for subtitle_file in subtitle_files:
            if re.match(r'.*S\d+E\d+', video_file) and re.match(r'.*S\d+E\d+', subtitle_file):
                # extract info from video and subtitle file names
                video_season, video_episode = re.findall(r'S(\d+)E(\d+)', video_file)[0]
                subtitle_season, subtitle_episode = re.findall(r'S(\d+)E(\d+)', subtitle_file)[0]

                if video_season == subtitle_season and video_episode == subtitle_episode:
                    # if found matching season and episode numbers, rename the subtitle file
                    video_name = re.sub(r'\.(mp4|avi|mkv)$', '', video_file)
                    subtitle_name = re.sub(r'\.(srt|sub|idx)$', '.srt', subtitle_file)
                    os.rename(os.path.join(folder_path, subtitle_file), os.path.join(folder_path, video_name + '.srt'))
                    break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Description of your program')
  # add rename directory as argument
    parser.add_argument('-d', '--directory', dest='argument1', required=True, help='Directory to rename subtitles in')
    args = parser.parse_args()

    # call rename function
    rename_subtitles(args.argument1)




