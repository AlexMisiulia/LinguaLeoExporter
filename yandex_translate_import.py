import re
from bs4 import BeautifulSoup

INPUT_PATH = "/home/alex/Programming/Python/LeoPort/yandex_history.html"
OUTPUT_PATH = "/home/alex/Programming/Python/LeoPort/dictionary"


def get_english_words():
    html_doc = open(INPUT_PATH, "r")
    soup = BeautifulSoup(html_doc, 'html.parser')

    result = []
    for record in soup.select("div.record-item"):
        word = record.select("div[lang=en]")[0].text
        if doesnt_contain_russian_symbols(word):
            result.append(word)
        else:
            print(f'Exclude: {word}')

    return result


def doesnt_contain_russian_symbols(word):
    russian_match = re.search(r"[а-яА-Я]", word)

    return russian_match is None


def main():
    words = get_english_words()
    f = open(OUTPUT_PATH, "w+", encoding='utf8')
    words_string = '\n'.join(words)
    f.write(words_string)
    f.close()

main()