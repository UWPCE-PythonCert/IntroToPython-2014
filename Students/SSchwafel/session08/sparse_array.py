#!/usr/bin/python


#class sparse_array(object):
#    
#    def __init__(self, values=None):
#        if values == None:
#    
#            self.values = []
#
#        else:
#            
#            self.values = values
#    
#    def len(self):
#
#        return len(self.values)
#
#    def getitem(self, key):
#    
#        return self.values[key]
#
#sample = sparse_array(0,1,2)
#
#print sample

class sparse_array(object):
    
    def __init__(self,iterable):
        self.values{}
        self.length = len(iterable)

        for i, val in enumerate(iterable):
            if val:
                self.values[i] = val

        print self.values
            
    def __getitem__(self,index):

        if index >= self.length: 
            raise IndexError("Sparse array index out of range")

        else:
            
            self.values.get(index, 0)    
            
    def __len__(self):
        return self.length
    
    def __setitem__(self, index, value):

        if index >= self.length: 
            raise IndexError("Sparse array index out of range")
        else:
            if value == 0:
                self..values.pop(index, None) 
            else:
                self.values[index] = valu
