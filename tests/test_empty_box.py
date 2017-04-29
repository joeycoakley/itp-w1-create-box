import unittest

from create_empty_box import create_empty_box

first_box_expected = """
***
* *
***
""".lstrip()

second_box_expected = """
!!!!
!  !
!  !
!!!!
""".lstrip()

third_box_expected = """
********
*      *
*      *
********
""".lstrip()


class TestCreateBox(unittest.TestCase):
    def test_box(self):
        self.assertEqual(create_empty_box(3, 3, '*'), first_box_expected)

    def test_small_box(self):
        self.assertEqual(create_empty_box(4, 4, '!'), second_box_expected)

    def test_large_box(self):
        self.assertEqual(create_empty_box(8, 4, '*'), third_box_expected)