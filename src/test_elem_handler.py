import unittest
from elem_handler import Elem

class TestElemMethods(unittest.TestCase):

    def test_is_blob(self):
        folder = Elem("/jlgm/QuakeParser/tree/master/log")
        blob = Elem("/jlgm/QuakeParser/blob/master/log/quake.log")
        self.assertFalse(folder.is_blob())
        self.assertTrue(blob.is_blob())

    def test_name(self):
        blob = Elem("/jlgm/QuakeParser/blob/master/log/quake.log")
        folder = Elem("/jlgm/QuakeParser/tree/master/log")
        self.assertEqual(blob.name(), "quake.log")

    def test_blob_to_raw(self):
        blob = Elem("/jlgm/QuakeParser/blob/master/log/quake.log")
        folder = Elem("/jlgm/QuakeParser/tree/master/log")
        raw = blob.blob_to_raw()
        self.assertEqual(raw, "/jlgm/QuakeParser/raw/master/log/quake.log")
        with self.assertRaises(NameError) as context:
            folder.blob_to_raw()
        self.assertEqual("not a blob!", str(context.exception))

    def test_extension(self):
        blob = Elem("/jlgm/QuakeParser/blob/master/log/quake.log")
        folder = Elem("/jlgm/QuakeParser/tree/master/log")
        self.assertEqual(blob.extension(), "log")
        with self.assertRaises(NameError) as context:
            folder.blob_to_raw()
        self.assertEqual("not a blob!", str(context.exception))

if __name__ == '__main__':
    unittest.main()
