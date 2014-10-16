from ack import ack


count1 = 0
if ack(0, 0) == 1:
    count1 = count1 + 1
if ack(1, 0) == 2:
	count1 = count1 + 1
if ack(2, 0) == 3:
	count1 = count1 + 1
if ack(3, 0) == 5:
	count1 = count1 + 1
if ack(0, 1) == 2:
	count1 = count1 + 1
if ack(1, 1) == 3:
	count1 = count1 + 1
if ack(2, 1) == 5:
	count1 = count1 + 1
if ack(3, 1) == 13:
	count1 = count1 + 1
if ack(0, 2) == 3:
	count1 = count1 + 1
if ack(1, 2) == 4:
	count1 = count1 + 1
if ack(2, 2) == 7:
	count1 = count1 + 1
if ack(3, 2) == 29:
	count1 = count1 + 1
if ack(0, 3) == 4:
	count1 = count1 + 1
if ack(1, 3) == 5:
	count1 = count1 + 1
if ack(2, 3) == 9:
	count1 = count1 + 1
if ack(3, 3) == 61:
	count1 = count1 + 1
if ack(0, 4) == 5:
	count1 = count1 + 1
if ack(1, 4) == 6:
	count1 = count1 + 1
if ack(2, 4) == 11:
	count1 = count1 + 1
if ack(3, 4) == 125:
	count1 = count1 + 1

if count1 == 20:
    print "All Tests Pass"

