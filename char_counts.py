def char_counts(s):
    vowels = 0
    consonants = 0
    for ch in s:
        if ch in "aeiouAEIOU":
            vowels += 1
        elif ch.isalpha():
            consonants += 1
    return (vowels, consonants)
print("Character Counts: ", char_counts("Hello World!"))