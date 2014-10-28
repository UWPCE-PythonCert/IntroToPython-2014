'''

Trigraph.py

Sherlock Holmes Trigraph exercise.

Read in the entire text of Sherlock Holmes and create an entire set of trigraphs for every pair of words in the novel. I'll print out some statistics, 
then attempt to write a paragraph or two.

I am going to use the punctuation in the text, including paragraph markers.

Haven't decided how to choose next work from list or what to do about dead ends.


'''

import io
import re



def buildTrigraph (source):
    '''
    Read a tet file ad build a trigraph. Read each line, split by ' ' and '-', keeping the punctuation. Separate the 
    punctuation and add to the trigraph separately as needed.
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
    trigraph = dict()
    while reading:
        line = text.readline()
        #TBD Check if line s end of paragraph.
        if line:
            #Use a regular expression to parse the line with punctuation. Yes- getting ahead again but found this on Stack Overflow
            words = re.split('(\W+)', line)
            words = [word for word in words if word != ' ' and word != '--']
            print words

            for i in range (0, len(words)):
                first = second
                second = third
                third = words[i]
                
                
                
                if first != '' and second != '':
                    t = first+' '+second
                    ##print t, ' : ', third
                    if trigraph.has_key(t):
                        if third not in trigraph[t]:
                            trigraph[t].append (third)
                    else:
                        trigraph[t] = [third]
                    ##print trigraph[t]
                        
                #Handle punctuation
     
        else:
            reading = False

    text.close()
    return trigraph
    
def trigraphFacts(t):
    '''
    Display interesting facts on the trigraph.
    '''
    print "There are {} entries".format (len(t))
    
    #Find largest trigraph and print any that have only one member
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
    
def printTrigraph (t):
    print '\n\nTrigraphs'
    for key in t:
        print key,
        print ' : ',
        print t[key]
    print '\n\n'

if __name__ == "__main__":
    basePath = "../../../slides_sources/source/homework/"
    short_sherlock_source = basePath + "sherlock_small.txt"
    sherlock_source = basePath + "sherlock.txt"
    t = buildTrigraph (short_sherlock_source)
    #t =buildTrigraph (sherlock_source)
    #printTrigraph (t)
    #trigraphFacts(t)

