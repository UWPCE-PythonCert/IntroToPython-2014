'''
Sparse array unit tests.
'''

from Sparse import Sparse
import unittest


class TestSparseClass (unittest.TestCase):

    def populate_array(self, s):
        s[5] = 100
        s[15] = 99
        s[25] = 98
        s[35] = 97
        s[45] = 96
        s[55] = 95
        

    def test_create_sparse(self): 
        # Create and print a spare array w/100 elements
        s = Sparse (100)    
        print s
        
    def test_get_item (self):
        s = Sparse (100)
        self.populate_array(s)
        assert s[5] == 100
        assert s[6] == 0
        
    def test_del (self):
        s = Sparse (100)
        self.populate_array(s)
        del (s[5])
        assert s[5] == 0
        
        
        
    def test_range_set_get(self):
        s = Sparse (100)
        self.populate_array(s)
        self.assertRaises(IndexError, s[-1])
        self.assertRaises(IndexError, s[101])
        self.assertRaises(IndexError, s[-1])
        self.assertRaises(IndexError, s[-1])
        

    
if __name__ =='__main__':
    unittest.main()
   