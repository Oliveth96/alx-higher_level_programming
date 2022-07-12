#!/usr/bin/python3
"""
    Unittest for Base class
"""
import unittest
from models.base import Base


class TestBaseclass(unittest.TestCase):
    """
    Test cases Base class
    """
    def setUp(self):
        """
        Test raise height
        """
        self.inst = Base(5)

    def tearDown(self):
        """
        Test raise height
        """
        Base._Base__nb_objects = 0

    def test_nb_objs_yes(self):
        """
        Test raise height
        """
        self.assertEqual(self.inst._Base__nb_objects, 0)

    def test_nb_objs_no(self):
        """
        Test raise height
        """
        self.inst = Base()
        self.assertEqual(self.inst._Base__nb_objects, 1)

    def test_id(self):
        """
        Test raise height
        """
        self.assertEqual(self.inst.id, 5)
