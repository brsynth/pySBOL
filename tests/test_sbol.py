from unittest import TestCase

class Test_SBOL(TestCase):

               
    def test_import(self):
        b = True
        try:
            import pysbol
        except Exception as e:
            b = False
            print(e)
        self.assertTrue(b)