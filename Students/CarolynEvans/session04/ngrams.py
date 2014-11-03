def ngrams(nkey=2,nvalue=1,filename='sherlock.txt'):

    __author__ = 'carolyn.evans'

    """
    This function builds a dictionary by looking at sets of words in the given file.
    Words are are made up of the letters 'a' through 'z' and separated by a space.
    Numbers and punctuation are removed.

    Output is written to a file called ngram.txt.

    :param nkey: Parameter nkey is the number of words to include in the dictionary key.
    :param nvalue: Parameter nvalue is the number of words to include in the dictionary value.
    :param filename: Parameter 'filename' is the name of the file containing the text to be processed.
    """

    import re # regex
    from collections import defaultdict

    wordlist = []
    # Put each word into a list.
    for line in open('sherlock.txt'):
        # Use regex (re) to get rid of everything except alphabetic characters.
        # Convert to lower case for grouping when you are playing around with the output file.
        # Split into list by splitting on the space between each word.
        wordlist.extend(re.sub("[^a-zA-Z ]+", "", line).lower().split(" "))

    # Get rid of empty entries
    wordlist = filter(None, wordlist)

    # print wordlist

    # Build the dictionary of ngrams.
    ngramdict = defaultdict(list)
    for i in range(0,len(wordlist) - nkey - nvalue):
        # Build the key
        k = str(wordlist[i])
        for j in range(i+1, i+nkey):
            k += ' ' + wordlist[j]

        #Build the value
        v = str(wordlist[i + nkey])
        for j in range(i+1+nkey, i+nkey+nvalue):
            v += ' ' + wordlist[j]

        # Append the key:value to the dictionary
        ngramdict[k].append(v)

    # print ' '
    # print ngramdict

    # Write the ngram dictionary to a file.
    ngram = open('ngram.txt', 'w')

    for item in ngramdict.iteritems():
        ngram.write(str(item))

ngrams(2,1)