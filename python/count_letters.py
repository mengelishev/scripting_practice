#!/usr/bin/env python

# Считает количество букв в слове

def count_letters(text):
    letter_to_counter = {}
    for letter in text:
        if letter not in letter_to_counter:
            letter_to_counter[letter] = 1
        else:
            letter_to_counter[letter] += 1
    return letter_to_counter

if __name__ == '__main__':
    text = input("Введите слово: ").lower()
    print("Количество символов: " + str(count_letters(text)))