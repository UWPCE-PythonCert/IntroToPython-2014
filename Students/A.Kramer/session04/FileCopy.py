'''
Created on Oct 23, 2014

@author: db345c
'''


def fileCopy(src, dest):
    """ copy of a content of a text file into another text file """
    try:
        frm = open(src, "r")
        to = open(dest, "w")
    except IOError:
        print "Error opening either source or dest. files"
    else:
        # The actual copy
        for line in frm:
            to.write(line)
        print "Copy successful"
        try: 
            frm.close()
            to.close()
        except IOError:
            print "Error closing either source or dest. files"
    

if __name__ == "__main__":
    """ Copy single file """
    from1 = r"C:\Users\db345c\Desktop\Personal Folders\Eclipse_Wrokspaces\IntroToPythonUW\Week 4 Homework\sherlock.txt"
    to1 = r"C:\Users\db345c\Desktop\Personal Folders\Eclipse_Wrokspaces\IntroToPythonUW\Week 4 Homework\sherlock2.txt"
    fileCopy(from1, to1)