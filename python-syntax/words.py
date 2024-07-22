def print_upper_words(words, first_letter):
    
    for word in words:
        if word[0] == first_letter:
            print(word.upper())

print_upper_words(['hello', 'hey', 'yo'], 'h')
