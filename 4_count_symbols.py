text = input()
text_occurrences = {}
for letter in text:
    if letter not in text_occurrences.keys():
        text_occurrences[letter] = 0
    text_occurrences[letter] += 1
for letter, occurrences in sorted(text_occurrences.items(), key=lambda x: x[0]):
    print(f'{letter}: {occurrences} time/s')
