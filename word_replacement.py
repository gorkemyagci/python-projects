# Word Replacement Program

def replace_word():
    text = 'This is a test sentence'
    word_to_replace = str(input('Enter the word to replace: '))
    if word_to_replace not in text:
        print('The word you want to replace is not in the text')
        return
    new_word = str(input('Enter the new word: '))
    new_text = text.replace(word_to_replace, new_word)
    print(new_text)
    
    
replace_word()
