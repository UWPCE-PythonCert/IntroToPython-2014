#/usr/bin/python
import os

dir = os.getcwd()

print os.listdir(dir)

for i in os.listdir(dir):
    print os.path.abspath(i)
