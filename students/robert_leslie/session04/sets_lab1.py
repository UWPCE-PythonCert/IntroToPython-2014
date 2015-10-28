#! /usr/env/bin python3


s2 = set()
s3 = set()
s4 = set()


for i in range(0, 20):
    if  i % 2 == 0:
        s2.update([i])
    if i % 3 == 0:
        s3.update([i])
    if i % 4 == 0:
        s4.update([i])

print(s2,s3,s4)

if s3.issubset(s2): print(s3)
if s4.issubset(s2): print(s4)