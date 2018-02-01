import unittest
import datetime

import jalali


class TestPersian(unittest.TestCase):
    def test_gregorian_string(self):
        self.assertEqual(
            '2014-3-31',
            jalali.Persian('1393-1-11').gregorian_string()
        )
        self.assertEqual(
            '2014/3/31',
            jalali.Persian('1393/1/11').gregorian_string("{}/{}/{}")
        )

    def test_gregorian_datetime(self):
        self.assertEqual(
            datetime.date(2014, 3, 31),
            jalali.Persian(1393, 1, 11).gregorian_datetime()
        )

    def test_gregorian_tuple(self):
        self.assertEqual(
            (2014, 3, 31),
            jalali.Persian((1393, 1, 11)).gregorian_tuple()
        )


class TestGregorian(unittest.TestCase):
    def test_persian_string(self):
        self.assertEqual(
            '1393-1-11',
            jalali.Gregorian('2014-3-31').persian_string()
        )
        self.assertEqual(
            '1393',
            jalali.Gregorian(2014, 3, 31).persian_string("{0}")
        )

    def test_persian_tuple(self):
        self.assertEqual(
            (1393, 1, 11),
            jalali.Gregorian('2014,03,31').persian_tuple()
        )
