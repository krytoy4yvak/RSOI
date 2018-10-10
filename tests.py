import unittest 
import hello

class Mytests(unittest.TestCase):
   
    def test1(self):
        self.assertEqual(12*154-8898, -7050)

    def test2(self):
        a ='Hello world'
        self.assertTrue('l' in a)
        self.assertFalse('k' in a)

    def test3(self):
        self.assertAlmostEqual(hello.func1(),'Hello World!!!')
    def test4(self):
        self.assertAlmostEqual(hello.func2(),'I~ts a trap!!')
if __name__ == '__main__':
    unittest.main()
