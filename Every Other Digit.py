import re

ex = 'a1b2cde3~g45hi6'
ex = list(ex)

for i in range(len(ex)):
    if i % 2 == 1:
        ex[i] = re.sub('\\d', '*', ex[i])

result = ''.join(ex)

print(result)