from unittest import TestCase

class Test_SBOL(TestCase):

               
    def test_import(self):
        b = True
        try:
            import pysbol
        except:
            b = False
        self.assertTrue(b)