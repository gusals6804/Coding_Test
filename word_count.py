with open('ex.txt', 'r') as f:
    text = f.read()

word_list = text.replace(',', ' ').replace('.', ' ').split()

set_word = list(set(word_list))

word_count = []
for word in set_word:
     word_count.append([word_list.count(word), word])

sort_word = sorted(word_count, reverse=True)

for i in range(0, 10):
    print(sort_word[i][0], sort_word[i][1])
