import random
import unittest

<<<<<<< HEAD
class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)
=======

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = list(range(10))
>>>>>>> 280ef895939c277e57ec13a273e99cb3420e860f

    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
<<<<<<< HEAD
        self.assertEqual(self.seq, range(10))

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1,2,3) )
=======
        self.assertEqual(self.seq, list(range(10)))

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))
>>>>>>> 280ef895939c277e57ec13a273e99cb3420e860f

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)

if __name__ == '__main__':
<<<<<<< HEAD
    unittest.main()
=======
    unittest.main()
>>>>>>> 280ef895939c277e57ec13a273e99cb3420e860f
