.. _exercise_file_lab:

********
File LAB
********

A bit of practice with files
============================

Goal:
-----

Get a little bit of practice with handling files and parsing simple text.


Paths and File Processing
--------------------------

* write a program which prints the full path to all files in the current
  directory, one per line

* write a program which copies a file from a source, to a destination
  (without using shutil, or the OS copy command)

  - advanced: make it work for any size file: i.e. don't read the entire
    contents of the file into memory at once.

  - This should work for any kind of file, so you need to open
    the files in binary mode: ``open(filename, 'rb')`` (or ``'wb'`` for
    writing). Note that for binary files, you can't use ``readline()`` --
    lines don't have any meaning for binary files.

  - Test it with both text and binrary files (maybe jpeg or??)


File reading and parsing
------------------------


In the class repo, in:

``Examples/Session01/students.txt``

You will find the list I generated in the first class of all the students in the class, and what programming languages they have used in the past.

Write a little script that reads that file, and generates a list of all
the languages that have been used.

Extra credit: keep track of how many students specified each language.

If you've got git set up right, ``git pull upstream master`` should update
your repo. Otherwise, you can get it from gitHub:

https://github.com/UWPCE-PythonCert/IntroPython2016/blob/master/Examples/Session01/students.txt

