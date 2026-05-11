import re


def parse_srt(file_path):

    subtitles = []

    with open(
        file_path,
        'r',
        encoding='utf-8'
    ) as file:

        content = file.read()

    blocks = content.strip().split('\n\n')

    for block in blocks:

        lines = block.split('\n')

        if len(lines) >= 3:

            index = lines[0]

            times = lines[1]

            text = ' '.join(lines[2:])

            start, end = times.split(' --> ')

            subtitles.append({

                'start': start,
                'end': end,
                'text': text,

            })

    return subtitles