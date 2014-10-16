############################## SESSION01 ##############################

#IPYTHON:
"""
-typing "?" after any object gives you more information
-supports tap completion
"""


#VALUES AND TYPES:
"""
values: pieces of unanmed data
    -all values are objects
    -dir(42) shows you all the different things the object can do

types: every value belongs to a type.
    -numbers
        -floating point
        -intergers
    -text
    -boolean
    -none
    -string
    -dict
    -list
    -tuple
"""


#STATEMENTS VS. EXPRESSIONS
"""
statements: statments do not return a value, but may contain an experssion
"""
#exmaples
line_count = 42  # 42 is actually and expression, but this line is a statment
print "this" # print doesn't return a value

"""
expressions: evaluating an expression results in a value
    - expressions are made up of values and operators
"""
#examples:
3 + 7  # result is 7


#PRINT STATEMENT
"""
using the comma in a print statement allows you to suppress the newline
"""
#example
print "the vaue is", 45


#SYMBOLS
"""
symbols:  how we give names to values
    -symbols can contain any number of sundersores, letters, nd numbers
    -a symbol is bound to a value with the assignment operator
    -in most languages, symbols are called variables
    -in most languages, a symbol is a place in memory that can store values
    -this is NOT what a symbol in python is
    -a symbol can be bound to a value, but doesn't have anything to do with the
     location in memory
"""
#example
a = 5
a = b  # both a and b are referring to the same 5

# you can assign multilple symbols at the same time
i,j = 5,4
i,j = j,i  # this switches the value of j and i


#TEXT SLICING:
"""
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
"""

############################## SESSION02 ##############################


#FUNCTIONS:
"""
-begins with "def".  this means everything folloiwng is the definiton of the function.
-when you execute a fucntion, it creates a fuction object
-the name of the fucntion is now the symbol for the name
"""
#example
def name (x, y):
    return x * y


#OPERATORS:
"""
// <-- this will always ignore the interger
"""


#GIT
"""
-git is a graph.  A graph is something with "states" and "places" with paths between them.
For example your code will have many versions ("states") with points between them.
-each place in the history of git has a name that identifies it (called a "hash")
-there are labels that can point to the different places in time.
    - "Head" is the label at the current point in time that you're looking at.
    - "master" is the name that git auomatically gives to the first branch in a repository
    - "branch" is a different version of the original master branch
-creating branches allows you to submit just the specific homework you changed in
 your pull request
-when you create your pull request, you want to make sure you're comparing your
 branch to the master to PCE's repository
-you start with a local database and then pull to the web
-you always start locally; this creates a ".git" folder

-git setup:
    -have gui
    -have command line
    -have github account

-git settings:
    -system: settings for your system
    -global: settings for your user account
    -local: highest prescedence; settings specific for your local project

-initalizing a repository:
    -this can happen locally or in the cloud at github.com
    -locally:
        -"git init" turns an existing project into a git project
        -"git init <project_name> creates a new project as a git project
    -in the cloud:
        -look for "New Repository" and create a repository
        -README: this tell others about the project
        -.gitignore: this tells git which projects to ignore

-committing:
    -changes are commits
    -local commits:
        -"git status" tells you with files should be committed
        -"git add" adds files to the staging area; the purpose of the staging
         area is to give users the ability to choose which changes are part of
         which commit.
        -"git commit -m <message>" will commit the changes; each commit should
         be part of a story
    -github.com commits:
        -use the edit button on the website
        -this is good for making simple changes to text files

-diff:
    -what changes have you made to your code that hasn't been staged?
    -"git diff": this tells you how your working tree (i.e., files) differs
     from the staging area
    -"git diff --staged" this tells you how your staging area is different
     from the lastest commit in history
    -"git diff HEAD" how your working tree compares to the HEAD commit
    -"git diff --word-diff" easier to read diffs
    -"git diff --color-words" easier to read diffs
    -"git diff --stat" just tells you the files that have changed

-log:
    -"git log" shows all the commits to the repository; new on top, oldest at
     the bottom
    -"git log --oneline" shows a summary of all the commits
    -"git log --stat" shows the commit message with the files for each commit
    -"git log --patch" shows the diff between all the commits
    -"git log --graph --all --decorate --oneline"
    -you can use all of these options together

-removing files:
    -"git rm" removes the file from the directory and stages the removal
    -"git add -u ." goes through the working tree and stages all deleted files;
     the "." means that git will look at all directories in the working tree
    -"git rm --cahced <filename>" removes from the git repository but not the
     file system

-moved files:
    -"git mv <old_path> <new_path>" this will move a file; if you don't use this
     command and do the move using the file system, git will think you deleted
     then added a file.  you can fix this by deleted the old file "git rm <file>"
     and adding the new file "git add <file".
    -"git add -A ." this finds all the new files and old files and tells git that
     they have been moved

-ignore:
    -to ignore files, create a ".gitignore" file in the root of the project
    -e.g., "touch .gitignore" "git add .gitignore" "git commit -m <message>"
    -you can put file names, directories, or wildcard character (i.e., "*")
    -you can also have a .gitignore file in a sub directory, which takes presedence
    -"git ls-files --others --ignored --exclude-standard" shows all the excluded
     files

-branch:
    -new features and bug fixes should be done on a new branch
    -why use branches?
        -the master branch should be a representation of "production"
    -"git branch <name>" creates a new branch
    -"git branch -d <name>" deletes a branch
        -you cannot delete the branch you are currently on
    -"git checkout <name>"
        -this moves changes in staging area and working directory to new branch
        -can't switch to a new branch when moving to that branch affects staging
         files or working tree files
        -you might see different files when you are on different branches; this
         is fine and how git works
    -"git branch":  lists all the current branches (* is the branch you're on)
    -"git branch -v": lists all the current branches with last commit
    -"git branch --merged": lists the branches that are already merged into the
     branch you're on. branches without a "*" in front are generally fine to delete
    -"git branch --no-merged": lists the branches that contain work that hasn't
     been merged in

-more branching notes:
    -a branch is a movable pointer to one of your commits
    -when you first start a git repository, the default branch is named master
     and it points to the last commit you made
    -creating a new branch creates a new pointer for you to move around; the
     default location when you create a new branch is the commit you're currently
     on
    -how does git know what branch you're on? It keeps a special pointer named
     HEAD. HEAD is a pointer to the local branch you're currently on.
    -"git checkout" lets you switch to a new branch.  This moves HEAD to to point
     to the testing branch
    -when you make another commit after switching to a new branch, the master
     pointer stays where it is and HEAD and the branch pointer move forward
    -when switching branches, it's best practice to commit all your changes.
     this is because git won't let you switch branches if your working tree has
     uncommitted changes the conflict with the branch you're checking out
    -when there are conflicts, git will pause the merge.  run "git status" to see
     which files were not merged.  you'll have to manually change the file with
     issues.  to reslove the conflicts, add the file to the staging area. finally,
     commit to finalize the merge

-remote braches:
    -remote branches: references to the state of brances on your remote repositories.
     they are local branches that can't be moved.  instead, they're moved automatically
     when you do any network communication. remote branches act as bookmaks to
     remind you where the branches on your remote repositories were the last time
     you connected to them
    -<remote>/<branch>: this is the form of remote branches. for example, the "master"
     branch on the "origin" remote would be "origin/master"
    -when you clone a git repository from github, git automatically names it "orgin"
     and creates a pointer to the master branch named "origin/master" locally.
    -git also gives you your own master branch starting at the same place as
     "origin/master"
    -the "origin/master" pointer doesn't move as long as you stay out of contact
     with the github server
    -"git fetch origin": this command will sync your work with the server by fetching
     data from the server that you don't have and updates your local working
     directory.  this will also move "origin/master" to a new location. note,
     this does not merge any changes to "origin/master" and your local branches.
    -when your fetch brings down new branches, you don't automattically have local,
     editable copies of them.  you can either:
        -"git merge <remote/branch>" to merge the remote branch into your current
         working branch
        -"git checkout -b <local_branch> <remote/branch>": to create and checkout
         a new branch based on the remote branch.
    -the second method creates a "tracking" branch:
        -tracking branches are local branches that have a direct relationship to
         a remote branch.  therefore, if you're on a tracking branch and you
         type "git push", git automattically knows which branch to push to.
        -running "git pull" on a "tracking" branch fetches all the remote references
         and automatically merges to the corresponding remote branch
        -after cloning a repository, a master branch is created that tracks
         origin/master, so "git push" and "git pull" automattically work
        -"git checkout --track <remote/branch>" will set up the branch you're on
         to track a remote branch
    -delete a remote branch with "git push <remote> :<branch>".
    -"git push <remote> <branch>": this will push a branch to the github server

-git homework workflow:
    "git checkout master"   # checkout the local master branch
    "git pull upstream master"   # fetch/merge class repository into local master
    "git push"   # push changes from class repository to personal repository
    [do work]
    "git commit -a"   # commit local changes
    [add a message]
    "git push"   # push local changes to personal repository
    [make a pull request]   # request that changes are merged with class repository

"""


#LOCAL VS. GLOBAL SYMBOLS
"""
-global variables: can be used everywhere
-local variables: are only referenced in the function
"""


#PARAMETERS
"""
- positional parameters; they must be entered in the right
- optional parameters --> fun(x=1)
- once you've provided a keyword argument, you can no longer provide any positional aruguments
"""



# if statments
if a:
    print 'a'
elif b:   # you don't need elif
    print 'b'
elif c:
    print 'c'
else:   #you don't need else
    print 'that was unexpected'

# lists
a_list = [2, 3, 5, 9]
a_list_of_strings = ['this', 'that', 'the', 'other']

# tuples
a_tuple = (1, 2, 3, 4)

# loops
a_list = [2, 3, 5, 9]

for item in a_list:
    print item

for item in range(6): # range allows you to loop as much as you want
    print '*',

def print_multi(x):

    print locals()

    for i in range(x):
        i += 1
        if (i % 3 == 0) and (i % 5 ==0):
            print 'FizzBuzz'
        elif i % 3 == 0:
            print 'Fuzz'
        elif i % 5 == 0:
            print 'Buzz'
        else:
            print i

import math

def distance(cor1, cor2):
    print locals()
    return math.sqrt( (cor1[0]-cor2[0])**2 + (cor1[0]-cor2[1])**2 )


#DOC STRINGS
"""
if a string literal is the first thing in the fuction block following the
header, then it's a doc string
"""
# example:

def complex_function(arg1, arg2, kwarg1=u'bannana'):
    """Return a value resulting from a complex calculation."""
    # code block here

"""
doc strings can be read in the interpreter as the "__doc__" attribute of the
function object

a doc string should be:
    -a complete sentence in the form of a command describing the function
        -e.g., "Return a list of values based on blah blah..."
    -fit into a signle line
        -if more lines are needed, make the first line a complete sentence,
         then add more information later
    -be enclosed with triple quotes
"""


#RECURSION
"""
recursion:  if a function calls itself
    -like other functions, a call within a call establishes a call stack
"""

#BOOLEAN EXPRESSIONS
"""
"bool(something)" returns either true or false

-and, or, and not
    -"and": returns the first operand that evaluates to False, or the last operand
     if non are True
    -"or": returns the first operand that evaluates to True, or the last operand
     if none are True
    -"not" inverts the boolean value of its operand

-boolean types are subclasses of integer
"""

# this is common in programming
if something:
    x = a_value
else:
    x = b_value

# in python
y = 5 if x > 2 else 3   # clased a "ternary" expression


#CODE STRUCTURE, MODULES, AND NAMESPACES

"""
-you can put a one-liner after the colon; however this should only be done if
 it makes your code more readable
"""
#example
x = 12
if x > 4: print x

"""
-namespaces: these are the dots
    -e.g., "name.another_name"
    -the "." indicates that you're looking for a name in the "namespace" of a
     given object
    -the namespace of an object could be
        -name in the module
        -module in a package
        -attribute of an object
        -method of an object
-a "module" is simply a namespace
    -it could be a single file or a collection of files
    -you can think of files with ".py" as modules
-a "package" is a module with other modules in it
    -on a filesystem, this is a directory that contains one or more .py files,
     one of which must be called "__init__.py"
    -see the example below for how to import packages and modules inside
"""
#example of importing packages and modules in packages
import modulename
from modulename import this, that
import modulename as a_new_name
from modulename import this as that

"""
-importing modules complies the python code to "bytecode"
    -this creates a module.pyc file
-this process executes all code at the module scope
    -this is why it's important to avoid module-scope statments because they have
     global side-effects
-code in a module is not rerun when you import again
-you can also run modules
"""

#ways to run a python module
python hello.py # must be in current working directory
./hello.py  #!/usr/env/python at top of module (Unix).
"""
The "./" is an abbreviated way to inform the shell that the absolute path of that
file is the current directory (i.e., the directory in which the user is currently
working). This allows you to execute a script.
"""

"""
-when you import a module, the value of the symbol "__name__" is the same as the
filename.
-when you run a module, the value of the symbol "__name__" is "__main__"
-this allows you to create blocks of code that are executed only when you
 run a module
 """

#this code will only execute if you run the module, not import it
if __name__ == '__main__':
    # Do something interesting here
    # It will only happen when the module is run

