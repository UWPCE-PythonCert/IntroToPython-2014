'''
#-------------------------------------------------#
# Title: kata
# Dev:   Marty Pitts
# Date:  Nov 1, 2015
# Desc:

Look at each set of three adjacent words in a document. Use the first two words
of the set as a key, and remember the fact that the third word followed that key.
Once finished, you know the list of individual words that can follow each
In:
I wish I may I wish I might

Out:
"I wish" => ["I", "I"]
"wish I" => ["may", "might"]
"may I"  => ["wish"]
"I may"  => ["I"]

To generate new text from this analysis, choose an arbitrary word pair as a
starting point. Use these to look up a random next word (using the table above)
and append this new word to the text so far. This now gives you a new word pair
at the end of the text, so look up a potential next word based on these. Add this
to the list, and so on. In the previous example, we could start with (I may). The
'''

# -----  Data Code ------
objFileNameRead = "sherlock.txt"
objFileNameWrite = "mystory.txt"
KataDict = {}
StoryDict = {}
StorySeedKey = "his every"
StorySeedNew = "long they"
StorySeedNew2 = "while the"

StorySize = 100

#  -- processing code --
#  Create functions to do the following.
'''
1) Open a file from a prior book.
2) Build a dictionary using first two words as key and third as data item.
3) Merge the dictionary items into a list with first item key followed by merged data items.
4) Querry input for two words to build 200 word story.
'''


def BuildDict(objFileNameRead):
    ''' Build a dictionary from a file. Use the first two words as key and third element as data. '''
    WordList = []
    CleanWordList = []

    # OPen the file and read a line
    objFile = open(objFileNameRead, "r")
    FileIn = objFile.read()

    # Dump the line to a list
    WordList = FileIn.split(' ')

    # Remove Characters I do not want in dictionary
    CleanWordList = ([s.replace('-',' ') for s in WordList])
    # CleanWordList = ([s.replace(' ','') for s in CleanWordList])
    CleanWordList = ([s.replace('\n','') for s in CleanWordList])
    CleanWordList = ([s.replace('(','') for s in CleanWordList])
    CleanWordList = ([s.replace(')','') for s in CleanWordList])

    CleanWordList = ([s.replace('1','') for s in CleanWordList])
    CleanWordList = ([s.replace('2','') for s in CleanWordList])
    CleanWordList = ([s.replace('3','') for s in CleanWordList])
    CleanWordList = ([s.replace('4','') for s in CleanWordList])
    CleanWordList = ([s.replace('5','') for s in CleanWordList])
    CleanWordList = ([s.replace('6','') for s in CleanWordList])
    CleanWordList = ([s.replace('7','') for s in CleanWordList])
    CleanWordList = ([s.replace('8','') for s in CleanWordList])
    CleanWordList = ([s.replace('9','') for s in CleanWordList])
    print("Clean Word List =", CleanWordList)

    # Build a Dictionary
    DictPointer = 0
    for items in CleanWordList:
        if DictPointer < len(CleanWordList) - 4:
            CleanWordList[DictPointer] = (CleanWordList[DictPointer] + ' ')
            KeyIn = ''.join(CleanWordList[DictPointer:DictPointer+2])
            DataIn = CleanWordList[DictPointer+2]
            KataDict.update({KeyIn : DataIn})
            DictPointer = DictPointer + 1
        else: break
    # End For
    # print("Dictionary = ", KataDict)
    return(KataDict)

def BuildStory(ObjFileNameWrite):
    ''' Load the kata dictionary and use it to build a story. '''

    # OPen the file and read a line
    objFile = open(ObjFileNameWrite, "w")

    # Combine  the initial phrase
    Story = StorySeedKey + ' ' + KataDict[StorySeedKey]
    SplitKey = StorySeedKey.split()
    NewKey = SplitKey[1] + ' ' + KataDict[StorySeedKey]
    NewData = KataDict[NewKey]
    Story = Story + ' ' + NewData

    # Build a story with StorySize length
    for i in range(StorySize):
        SplitKey = NewKey.split()
        try:
            NewKey = SplitKey[1] + ' ' + KataDict[NewKey]
        except IndexError:
            NewKey = StorySeedNew
        try: 
            NewData = KataDict[NewKey]
        except KeyError:
            NewKey = StorySeedNew2
            NewData = KataDict[NewKey]
        Story = Story + ' ' + NewData
    # end for
    print("Story so far = ", Story)
    objFile.write(Story)
    objFile.close()
# Display Code
StoryDict = BuildDict(objFileNameRead)
Story = BuildStory(objFileNameWrite)
