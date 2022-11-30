import csv
import re

from os import listdir
from os.path import isfile, join, splitext
from vocaparser.settings import BASE_DIR

DIR_PATH = join(BASE_DIR, 'dataset/legacy')
SUPPORT_EXTENSIONS = ['.csv']
DELIMITERS = [',', '|', '.', ';']


def get_dataset_filepath(dir_path: str = None, support_extensions: [str] = None) -> list[str]:
    """
    Get all static datasets in full path.
    Example Args:
        dir_path: '/tmp/Voca-testgenerator/dataset/'
            Default: DIR_PATH
        support_extensions: ['.csv']
            Default: ['.csv']
    Example Return:
        ['/tmp/Voca-testgenerator/dataset/english-toefl.csv']
    """
    if dir_path is None:
        dir_path = DIR_PATH
    if support_extensions is None:
        support_extensions = SUPPORT_EXTENSIONS

    filepaths = list()

    for file in listdir(dir_path):
        full_filepath = join(dir_path, file)
        (_, extension) = splitext(full_filepath)

        if extension not in support_extensions:
            continue

        if not isfile(full_filepath):
            continue

        filepaths.append(full_filepath)

    return filepaths


def parse_csv_data(full_filepath: str) -> list[dict[str or list[str]]]:
    """
    Parse the CSV data of `full_filepath`.
    Example Args:
        full_filepath: '/tmp/Voca-testgenerator/dataset/english-toefl.csv'
    Example Return:
        [
            {'word': 'abstract', 'meanings': ['추상적인', '관념적인']},
            {'word': 'affirmation', 'meanings': ['확언', '단언', '긍정']},
        ]
    """
    assert isfile(full_filepath)

    (_, extension) = splitext(full_filepath)
    assert extension == '.csv'

    data = list()

    with open(file=full_filepath, mode='r', encoding='utf-8') as file:
        for row in csv.reader(file):
            word = parse_word_data(raw_word=row[0])
            if not word:
                continue

            meanings = parse_meaning_data(raw_meanings=row[1])
            if len(meanings) == 0:
                continue

            data.append(dict({
                'word': word,
                'meanings': meanings,
            }))

    return data


def parse_string_data(raw_input: str) -> list[dict[str or list[str]]]:
    """
    Parse the raw string which is similar to CSV format.
    Not guaranty operation well.
    Example Args:
        raw_input: invulnerable,불사신의|공격할 수 없는|반박할 수 없는
                   introspect,내성하다|자기 반성하다|내관하다
                   tug of war,줄다리기|세력 싸움|쟁탈전
    Example Return:
        [
            {'word': 'abstract', 'meanings': ['추상적인', '관념적인']},
            {'word': 'affirmation', 'meanings': ['확언', '단언', '긍정']},
        ]
    """
    contents = re.findall(
        pattern='[^,\n]+,[^,\n]+\n',
        string=raw_input.strip() + '\n',
    )

    data = list()

    for content in contents:
        row = content.split(',', 1)
        word = parse_word_data(raw_word=row[0])
        if not word:
            continue

        meanings = parse_meaning_data(raw_meanings=row[1])
        if len(meanings) == 0:
            continue

        data.append(dict({
            'word': word,
            'meanings': meanings,
        }))

    return data


def parse_word_data(raw_word: str) -> str:
    """
    Derive a word from raw string.
    Example Args:
        raw_word: 'acute'
    Example Return:
        'acute'
    """
    word = raw_word.strip()
    delimiters = ''.join(DELIMITERS)
    is_multiple_words = re.search(
        pattern=f'[{delimiters}]+',
        string=word,
    )

    if is_multiple_words:
        return str()
    else:
        return word


def parse_meaning_data(raw_meanings: str) -> list[str]:
    """
    Derive meanings from raw string.
    Example Args:
        raw_meanings: "줄이다, 완화하다, 감소하다"
    Example Return:
        ['줄이다', '완화하다', '감소하다']
    """
    delimiters = ''.join(DELIMITERS)
    splits = re.split(
        pattern=f'[{delimiters}]+',
        string=raw_meanings.strip(),
    )

    meanings = list()
    for raw_meaning in splits:
        if not raw_meaning:
            continue

        intermediate = re.sub(
            pattern=r'[^( \[\]…~?!\u3131-\u3163\uac00-\ud7a3)]+',
            repl=str(),
            string=raw_meaning.strip(),
        )
        meaning = re.sub(
            pattern=r'\[[^]]*\]*',
            repl=str(),
            string=intermediate,
        ).strip()

        if not meaning:
            continue
        else:
            meanings.append(meaning)

    return meanings
