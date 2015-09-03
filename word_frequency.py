import re

def word_frequency(text):
    # return {"hello": 1}
    punc_removed = re.sub(r'[,.!-]', "", sample).lower()
    words = punc_removed.split()
    how_many = {}
    for i in words:
        if i in how_many:
            how_many[i] += 1
        else:
            how_many[i] = 1
    return how_many

def main():
    sample = open('sample.txt')
    text = sample.read()
    how_many = word_frequency(text)
    how_many = sorted(how_many.items(), key=lambda c: c[1], reverse=True)
    how_many = how_many[:20]
    for pair in how_many:
        print(pair)
    text.close()

if __name__ == '__main__':
    main()
