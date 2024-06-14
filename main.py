import pydub
import pytube
import io
import sys

def main():
    url, start, duration, output = sys.argv[1:5]

    start = int(start)
    duration = int(duration)

    youtube = pytube.YouTube(url)
    
    stream = youtube.streams \
        .filter(only_audio = True) \
        .order_by("abr") \
        .desc() \
        .first()

    buffer = io.BytesIO()
    stream.stream_to_buffer(buffer)
    buffer.seek(0)

    audio = pydub.AudioSegment.from_file(file = buffer)
    sample = audio[start * 1000 : (start + duration) * 1000]

    sample.export(output + ".mp3", format = "mp3")

if __name__ == "__main__":
    main()