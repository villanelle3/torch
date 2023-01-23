import nltk
import numpy as np
#nltk.download("punkt")

from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(frase):
    return nltk.word_tokenize(frase)

def stem(palavra):
    return stemmer.stem(palavra.lower())

def bag(frase_tokanizada, palavras):
    frase_tokanizada = [stem(w) for w in frase_tokanizada]
    bag_of_words = np.zeros(len(palavras), dtype = np.float32)
    for index, word in enumerate(palavras):
        if word in frase_tokanizada:
            bag_of_words[index] = 1.0
    return bag_of_words

'''
sentence = ["hello", "how", "are", "you"]
words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
print(bag(sentence, words))
'''
