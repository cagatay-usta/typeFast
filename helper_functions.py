import random

def word_generator(words, case, number):
    casedWords = []
    for word in range(number):
        wordOne = random.choice(words)
        wordTwo = random.choice(words)
        if case == 'camelCase':
            casedWords.append(wordOne + wordTwo.capitalize())
        elif case == 'snakeCase':
            casedWords.append(wordOne + '_' + wordTwo)
        elif case == 'kebabCase':
            casedWords.append(wordOne + '-' + wordTwo)
    return casedWords
