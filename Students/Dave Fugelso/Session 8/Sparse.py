'''
Sparse Array

Note, missed class out of town so not quite sure I know what this needs to do.

But, only store elements that have values and assume that the key is 0 to n-1 where n is the total
length of the array. 

__init__ is how? 
static length or allow to grow/shrink?

Decisions:

1. Init with just a length.
2. May explicitly change size with setSize. Deletes entries out of range on shrink.
3. Use set to populate array

Implement with dictionary

'''

class Sparse(object):

    _length = 0
    array = {}
    def __init__(self, size):
        self._length = size;
        
    @property
    def length (self):
        return self._length
        
    @length.setter
    def length (self, newlength):
        '''
        if expanding just change length, but if shortening, delete entries greater than range.
        '''
        if newlength < self._length:
            for index in self.array.keys():
                if index >= self._length:
                    self.array.pop(index, None)
        self._length = newlength
        
    def __len__(self):
        '''
        Len for iteration.
        '''
        return self._length
        
    def __getitem__(self, index):
        '''
        return element at index or zero if none.
        '''
        if index < 0 or index >= self.length:
            raise IndexError ('Sparse Array out of range')
        else:
            return self.array.get(index, 0)
            
    def __setitem__ (self, index, value):
        ''' 
        Set item if in range. If value is zero, remove item.
        '''
        if index < 0 or index >= self.length:
            raise IndexError ('Sparse Array out of range')
        elif value == 0:
            self.array.pop(index, None)
        else:
            self.array[index] = value
            
    def __delitem__ (self, index):
        '''
        Delete an item.
        '''
        if index < 0 or index >= self.length:
            raise IndexError ('Sparse Array out of range')
        else:
            self.array.pop(index, None)       
           
        
            