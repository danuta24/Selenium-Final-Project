import unittest
import func
class TestJakis(unittest.TestCase):
    def test_f0(self):
        self.assertTrue(True)
    def test_f1__1(self):
        w = func.f1(0)
        self.assertEqual(w,0)
    def test_f1_2(self):
        c = func.f1(1)
        self.assertEqual(c,1)
    def test_f1_3(self):
        b = func.f1(2)
        self.assertEqual(b,4)
    def test_f1_4(self):
        d = func.f1(2,1)
        self.assertEqual(d, 5)



if __name__ == '__main__':
    unittest.main()