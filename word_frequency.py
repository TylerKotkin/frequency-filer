import re

def word_frequency(text):
    words = re.sub(r'[,.!-?0-9]', "", text).lower().split()
    how_many = {}
    for i in words:
        if i in how_many:
            how_many[i] += 1
        else:
            how_many[i] = 1
    return how_many


def main():
    with open('sample.txt') as g:
        text = g.read()
        for answer in sorted(word_frequency(text).items(), key=lambda c: c[1], reverse=True)[:20]:
            print(answer)


if __name__ == '__main__':
    main()
