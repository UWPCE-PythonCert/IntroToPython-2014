'''

Trigraph.py

Sherlock Holmes Trigraph exercise.

Read in the entire text of Sherlock Holmes and create an entire set of trigraphs for every pair of words in the novel. I'll print out some statistics, 
then attempt to write a paragraph or two.

I am going to use the punctuation in the text, including paragraph markers.

Haven't decided how to choose next work from list or what to do about dead ends.


'''

import io



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
    trigraph = {}
    while reading:
        line = text.readline()
        #TBD Check if line s end of paragraph.
        if line:
            #words = line.split(' -')
            words = line.split()
            for i in range (0, len(words)):
                first = second
                second = third
                third = words[i]
                
                #Check for punctuation
                
                
                if first != '' and second != '':
                    t = first+' '+second
                    print t, ' : ', third
                    l = trigraph.get(t, [])
                    print trigraph[t]
                    if third not in l:
                        l.append (third)
                        print trigraph[t]
                        
                #Handle punctuation
     
        else:
            reading = False

    text.close()
    return trigraph
    
def trigraphFacts(t):
    '''
    Display interesting facts on the trigraph.
    '''
    print "There are {} entries".format (t.len())
    
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
            print ' : '
            print t[key]
        
    print "\n\n\the entries with the most entries is '{}' with {} entries".format (largestName, largestNum)
    
def printTrigraph (t):
    print '\n\nTrigraphs'
    for key in t:
        print key,
        print ' : ',
        print t[key]
    print '\n\n'

if __name__ == "__main__":
    short_sherlock_source = "../../../../../sherlock_small.txt"
    sherlock_source = "../../../../../sherlock.txt"
    t = buildTrigraph (short_sherlock_source)
    #t =buildTrigraph (sherlock_source)
    printTrigraph (t)

