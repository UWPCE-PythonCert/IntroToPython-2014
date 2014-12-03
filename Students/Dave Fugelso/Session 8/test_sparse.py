'''
Sparse array unit tests.

Note: I didn't see that there was a test_sparse_array in solutions...

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
        with self.assertRaises(IndexError) as context:
            i = s[-1]
        self.assertEqual(context.exception.message, 'Sparse Array out of range')

        with self.assertRaises(IndexError) as context:
            i = s[100]
        self.assertEqual(context.exception.message, 'Sparse Array out of range')

        with self.assertRaises(IndexError) as context:
            s[-1] = 5
        self.assertEqual(context.exception.message, 'Sparse Array out of range')

        with self.assertRaises(IndexError) as context:
            s[100] = 5
        self.assertEqual(context.exception.message, 'Sparse Array out of range')

        with self.assertRaises(IndexError) as context:
            del (s[100])
        self.assertEqual(context.exception.message, 'Sparse Array out of range')

        with self.assertRaises(IndexError) as context:
            del(s[-1])
        self.assertEqual(context.exception.message, 'Sparse Array out of range')

        #with self.assertRaises(IndexError) as context:
        #    s[0] = 5
        #self.assertEqual(context.exception.message, 'Sparse Array out of range')

    def test_resize (self):
        s = Sparse (100)
        self.populate_array(s)  

        # test smaller
        s.length = 50
        with self.assertRaises(IndexError) as context:
            a = s[55]
        self.assertEqual(context.exception.message, 'Sparse Array out of range')

        # test back to larger
        s.length = 100
        s[55] = 100
        assert (s[55] == 100)
        
    def test_iteration (self):
        s = Sparse (100)
        self.populate_array(s) 
        index = 0
        for val in s:
            print index, val
            assert val == s[index]
            index += 1
         

    
if __name__ =='__main__':
    unittest.main()
   