'''

Trigram.py

Sherlock Holmes Trigram exercise.

Read in the entire text of Sherlock Holmes and create an entire set of trigrams for every pair of words in the novel. I'll print out some statistics, 
then attempt to write a paragraph or two.

I am going to use the punctuation in the text, including paragraph markers.

Haven't decided how to choose next work from list or what to do about dead ends.


'''

import io
import re
import string
import random



def buildTrigram (source):
    '''
    Read a text file and build a trigram. Read each line, split by ' ' and '-', keeping the punctuation. Separate the 
    punctuation and add to the trigram separately as needed.
    '''
    
    try:
        text = io.open(source, 'r')
    except:
        print 'File not found.'
        return
        
    reading = True
    first = ''
    second = ''
    third = ''
    trigram = dict()
    while reading:
        line = text.readline()

        if line:
            line = line[:len(line)-1]
            #Use a regular expression to parse the line with punctuation. Yes- getting ahead again but found this on Stack Overflow.
            words = re.split('(\W+)', line)
            words = [word for word in words if word != u' ' and word != u'--' and word != u'-' and word != u'']
        
            for i in range (0, len(words)):
                first = second
                second = third
                third = words[i].strip()
                if first != '' and second != '':
                    if second[0] in string.punctuation:
                        key = first+second
                    else:
                        key = first+' '+second
                    key = key.strip()
                    if trigram.has_key(key):
                        if third not in trigram[key]:
                            trigram[key].append (third)
                    else:
                        trigram[key] = [third]
                        
                first = second
                second = first
                
            # add a paragraph, which we'll mark with 'PP' and clear first, second
            if len(words) == 0:
                key = second+'.'
                if trigram.has_key(key):
                    if 'PP' not in trigram[key]:
                        trigram[key].append('PP')
                else:
                    trigram[key] = ['PP']
                first = ''
                second = ''
        else:
            reading = False

    text.close()
    return trigram
    
def trigramFacts(t):
    '''
    Display interesting facts on the trigram.
    '''
    print "There are {} entries".format (len(t))
    
    #Find largest trigram and print any that have only one member
    largestName = ''
    largestNum = 0
    print 'The following entries have only one entry:'
    for key in t:
        if len(t[key]) > largestNum:
            largestNum = len(t[key])
            largestName = key
        if len(t[key]) == 1:
            print key,
            print ' : ',
            print t[key]
        
    print "\n\nThe entries with the most entries is '{}' with {} entries".format (largestName, largestNum)
    
    
def createParagraph(t, n):
    ''' 
    Create a paragraph or two using the built trigram - up to n words.
    '''
    num = 0
    
    #create a list of trigrams starts with a capital letter (doesn't work all that well with proper nouns... no time to fix)
    starters = list()
    for key in t.keys():
        if key[0].isupper():
            starters.append(key)
            
    while num < n:
        #Get a starting point with no punctuation and starts with a cap letter?
        start = starters[random.randrange(0, len(starters)-1)]
        print start,
        print ' ',
        num += 2
        buildingSentence = True
        key = start

        while buildingSentence:
            num += 1
            key = key.strip()
            if t.has_key(key):
                if len(t[key]) == 1:
                    nextword = t[key][0]
                else:
                    nextword = t[key][random.randrange(0, len(t[key]) -1)]
                if nextword == 'PP':
                    print 
                    print
                    buildingSentence = False
                else:
                    print nextword,
                    if nextword[0] == '.':
                        #print '. '
                        buildingSentence = False
                    else:
                        # get next key
                        oldkey = key.split()
                        if len(oldkey) == 1:
                            key = key[len(key)-1]
                        else:
                            key = oldkey[1]
                        
                        if nextword[0] in string.punctuation:
                            key = key + nextword
                        else:
                            key = key + ' ' + nextword
            else:
                #dead end, we could discard this sentence or back track, but I'm going put a period on it.
                print 'deadend ['+key+']',
                print '.'
                buildingSentence = False

def printTrigram (t):
    '''
    Print out trigram dictionary for testing purposes.
    '''
    print '\n\nTrigraphs'
    for key in t:
        print key,
        print ':',
        print t[key]
    print '\n\n'

if __name__ == "__main__":
    basePath = "../../../slides_sources/source/homework/"
    short_sherlock_source = basePath + "sherlock_small.txt"
    sherlock_source = basePath + "sherlock.txt"
    #t = buildTrigram (short_sherlock_source)
    t =buildTrigram (sherlock_source)
    printTrigram (t)
    #trigramFacts(t)
    createParagraph(t, 100)

