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

def wpm_calculator(casedWords, typedText, time):
    typedWords = list(typedText.split(' '))
    correctChars = 0
    for word in typedWords:
        if word in casedWords:
            correctChars += len(word)
    # words per minute = ((correctly typed characters / 5) / time in seconds) * 60
    wpm = ((correctChars / 5.0) / time) * 60
    return wpm
    



