# create a list of x values from a to b (maybe 100 or so values to start)
# compute the function for each of those values and double them
# add them all up
# multiply by the half of the difference between a and b.
# Note that the first and last values are not doubled.


def trapz(fun=5, a=0, b=10, l=None):
    N = 100
    delta_x = ((b-a) / N) # length of each base dist- total length of line/function divided by N/100
    #for i in range(N):
        #print(i)
    trapz_area = delta_x / 2 * (N)
    #print(trapz_area)
    #if l is None:
    #    l = []
    #for i in range(100):
    #   l.append()
    #pass



#l = [i for i in range(11)]
#print(l)
#print(l[1:-1]) #prints middle with no end caps
#print([i * 2 for i in l[1:-1]]) #prints doubled middle nums
#print(sum([i * 2 for i in l[1:-1]])) #prints sum of middle nums
#print(l[0]) #first num
#print(l[-1]) #last num
#print(1 / 2 * (l[0]+ sum([i * 2 for i in l[1:-1]]) + l[-1])) #sum of all the nums

trapz()


