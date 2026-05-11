import requests


def get_word_data(word):

    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()[0]

    result = {
        'word': word,
        'ipa': '',
        'definition': '',
    }

    if 'phonetic' in data:
        result['ipa'] = data['phonetic']

    if 'meanings' in data:

        meanings = data['meanings']

        if meanings:

            definitions = meanings[0].get(
                'definitions',
                []
            )

            if definitions:

                result['definition'] = definitions[0].get(
                    'definition',
                    ''
                )

    return result