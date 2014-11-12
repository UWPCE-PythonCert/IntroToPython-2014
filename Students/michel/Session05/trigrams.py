# -*- coding: utf-8 -*-
"""
Created on Sun Nov 02 16:48:08 2014

@author: Michel
"""

def readText(fileName):
    ''' 
    Reads the raw text from a text file 
    fileName is a string with path and file name
    Returns a string with the text read in it
    '''
    sourceText = open(fileName, 'r')
    text = sourceText.read()
    sourceText.close()
    return text

    
def cleanText(text):
    '''
    Cleans the text by transforming it into lower cases
    removing all punctuation except period
    Returns a clean text ready for processing
    '''
    text = string.lower(text)
    text = string.replace(text, '\n', ' ')
    text = string.replace(text, '--', ' ')
    charList = '''!"#$%&()*+,-/:;<=>?@[\]^_`{|}~0123456789'''
    for i in charList:
        text = string.replace(text, i, ' ')
    text = ' '.join(text.split())
    return text
    

def buildDict(text):
    '''
    Splits the text in sentences and builts pairs of words for each sentence
    Returns a dictionary of trigrams with all pairs of words and their 
    list of following words
    '''
    sentenceList = []
    pairsDict = {}
    wordCount = 0
    sentenceList = text.split('.')
    
    for sentence in sentenceList:
        wordList = []
        sentence = string.strip(sentence, ' ')
        sentence = string.replace(sentence, '.', '')
        wordList = string.split(sentence, ' ')
        wordCount = len(wordList)        
        
        for i in range(wordCount):
            if  (wordCount < 2) or (i > wordCount - 3):
                break
            else:
                wordTuple = ()                          
                wordTuple = (wordList[i], wordList[i+1])
                pairsDict.setdefault(wordTuple, []) 
                if wordList[i+2] not in pairsDict[wordTuple]:
                    pairsDict[wordTuple].append(wordList[i+2])
                    
    return pairsDict


def createSentence(pairsDict):
    '''
    Creates one trigram sentence
    If a pair of words is not found in the dictionary, the sentence ends
    Returns a string sentence    
    '''
    sentenceLength = random.randint(5, 15)
    startKey = ()
    sentence = []
    textSentence = ''
    
    keyList = pairsDict.keys()  
    
    # Starts a sentence
    startKey = keyList[random.randint(0, len(pairsDict)-1)]
    sentence = [startKey[n] for n in range(2)]
    word = pairsDict[startKey][random.randint(0, len(pairsDict[startKey])-1)]
    if word == 'i':
        word = 'I'
    sentence.append(word)
    ending =(':', '!', '?', '.', '...')
    
    # Continues a sentence
    for j in range(sentenceLength-2):
        tempKey = (sentence[-2], sentence[-1])
        if pairsDict.has_key(tempKey):
            word = pairsDict[tempKey][random.randint(0, len(pairsDict[tempKey])-1)]
            sentence.append(word)
        else:
            break
        
    textSentence = ' '.join(sentence)
    textSentence = string.capitalize(textSentence) + \
    ending[random.randint(0, len(ending)-1)]

    return textSentence

        
def createText(pairsDict):
    '''
    Creates a random text based on the dictionary of trigrams
    Text is made of 40 to 50 random sentences of variable length.
    Returns a string text
    '''
    textLength = random.randint(40, 50)
    text = ''
    
    # Creates a text made of sentences
    for i in range(textLength):
        textSentence = ''
        textSentence = createSentence(pairsDict)
        text = text + ' ' + textSentence
        
    return text
    

if __name__ == '__main__':
    import string
    import random
    text = readText('sherlock.txt')
    text1 = cleanText(text)
    dico = buildDict(text1)
    paragraph = createText(dico)
    print paragraph
    