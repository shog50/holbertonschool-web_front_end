# video_check.py
import sys

filename = '38-styleguide.html'

video_src_expected = "https://intranet-projects-files.s3.amazonaws.com/webstack/BigBuckBunny.mp4"

try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print(f"File {filename} not found.")
    sys.exit(1)

if video_src_expected in content:
    print("video has correct source")
else:
    print("video source not found or incorrect")

