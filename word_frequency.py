import re

def word_frequency(text):
    # return {"hello": 1}
    punc_removed = re.sub(r'[,.!-]', "", text).lower()
    words = punc_removed.split()
    how_many = {}
    for i in words:
        if i in how_many:
            how_many[i] += 1
        else:
            how_many[i] = 1
    return how_many

def main():
    # sample = open('sample.txt')
    with open('sample.txt') as g:
        text = g.read()
        how_many = word_frequency(text)
        how_many = sorted(how_many.items(), key=lambda c: c[1], reverse=True)
        how_many = how_many[:20]
        for pair in how_many:
            print(pair)


if __name__ == '__main__':
    main()
