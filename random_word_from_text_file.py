import random

def random_word(textpath):
    
    # open file
    
    file = open(textpath, mode = 'r', encoding='utf-8')
    
    # choose a random line from the file
    
    random_dickens_line = random.choice(file.readlines())
    
    # split the line and add to an existing word list
    
    split_list = random_dickens_line.split()
    
    # choose a word
    
    for word in split_list:
        if len(word) > 5:
            if word[0] != word[0].upper():
                if word.isalpha():
                    return word
    file.close()

if __name__ == '__main__':
    while True:
        word = random_word('TEXTFILE.TXT')
        if word != None:
            print(word)
            break
    