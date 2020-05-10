from leet import Solution
import unittest
class test(unittest.TestCase):
    def test_1(self):
        self.assertEquals(Solution().dominantIndex([1,0]) , 0)
        self.assertEquals(Solution().dominantIndex([0,0,0,1]),3)