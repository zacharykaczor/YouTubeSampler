# YouTubeSampler
A small command line tool for downloading a segment of audio out of a YouTube video.

## Instructions

- Install [FFmpeg](https://ffmpeg.org/)
- Install requirements.txt
- ```py main.py <url> <start> <duration> <output>```

## Example
```py main.py https://www.youtube.com/watch?v=dQw4w9WgXcQ 43 2 rick```

The above example takes a 2 second audio segment starting 43 seconds into the video and saves the result to rick.mp3
