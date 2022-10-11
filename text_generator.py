import random
from collections import Counter

from nltk import WhitespaceTokenizer, trigrams

f = open("/Users/tatiana/Desktop/corpus.txt", "r", encoding="utf-8")

# path = input()
# f = open(path, "r", encoding="utf-8")

f = f.read()

tk = WhitespaceTokenizer()
text = tk.tokenize(f)

bigrm = list(trigrams(text))

# print("Number of bigrams: " + str(len(bigrm)))

chain_dict = {}

for head1, head2, tail in bigrm:
    head = head1 + " " + head2
    chain_dict.setdefault(head, [])
    chain_dict[head].append(tail)

suffixes = (".", "!", "?")
index = 0

while index <= 9:
    prev_word = random.choice(list(chain_dict.keys()))
    head = prev_word.split()

    if prev_word[0].isupper() and not head[0][-1].endswith(suffixes):
        #print(head, head[0][-1])
        sentence = ["".join(prev_word[0::])]

        tail_list = chain_dict[prev_word]
        freq = dict(Counter(tail_list))
        res = random.choices(list(freq.keys()), weights=tuple(freq.values()), k=10)

        index = index + 1

        while True:
            if len(sentence) >= 4 and sentence[-1].endswith(suffixes):
                break
            tail_list = chain_dict[prev_word]
            freq = dict(Counter(tail_list))
            cur_word = random.choices(list(freq.keys()), weights=tuple(freq.values()))
            sentence.append(cur_word[0])
            head = prev_word.split()
            prev_word = head[-1] + ' ' + sentence[-1]

        print(" ".join(sentence))
