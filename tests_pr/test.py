import unittest
from unittest.mock import patch
from .homework import (task1, task2, task3, task4,
                       task5, task6, task7, task8,
                       task9, task10, task11, task12,
                       task13, task14, task15, task16,
                       task17, task18, task19, task20)


class Test(unittest.TestCase):

    def test_task1(self):
        list1, list2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.assertListEqual(task1(list1, list2), [1, 2, 3, 5, 8, 13])

    def test_task2(self):
        self.assertEqual(task2("I am a good developer. I am also a writer "), 5)

    def test_task3(self):
        self.assertTrue(task3(27))
        self.assertFalse(task3(4))
        self.assertRaises(ValueError, task3, 9.1)

    def test_task4_equal(self):
        self.assertEqual(task4(39), 3)
        self.assertEqual(task4(48), 3)

    def test_task4_notequal(self):
        self.assertNotEqual(task4(39), 2)
        self.assertNotEqual(task4(48), 1)

    def test_task5(self):
        self.assertEqual(task5([0, 2, 3, 4, 6, 7, 10]), ([2, 3, 4, 6, 7, 10, 0]))
        self.assertEqual(task5([2, 3, 4, 6, 7, 10]), ([2, 3, 4, 6, 7, 10]))

    def test_task6_true(self):
        self.assertTrue(task6 ([1, 3, 5, 7, 9, 11, 13]))

    def test_task6_false(self):
        self.assertFalse(task6([1, 5, 10, 15, 25, 30]))

    def test_task7_equal(self):
        self.assertEqual(task7([5, 1, 4, 3, 4, 3]), [1, 5])
        self.assertEqual(task7([2, 2, 1, 4, 3, 3]), [1, 4])

    def test_task7_notequal(self):
        self.assertNotEqual(task7([5, 4, 3, 4, 3]), 3)
        self.assertNotEqual(task7([2, 2, 4, 3, 3]), 2)

    def test_task8_equal(self):
        self.assertEqual(task8([1, 2, 3, 4, 5, 7, 8, 9, 10]), [6])

    def test_task9_equal(self):
        self.assertEqual(task9([1, 2, 3, 4, (1, 2), 5]), 4)
        self.assertEqual(task9([1, 2, 3, 4, 5, (1, 2), 6]), 5)

    def test_task10_equal(self):
        self.assertEqual(task10('Hello World and Coders'), "sredoC dna dlroW olleH")

    def test_task11_equal(self):
        self.assertEqual(task11(63), "1 : 3")
        self.assertEqual(task11(72), "1 : 12")

    def test_task12_equal(self):
        self.assertEqual(task12("fun&!! time"), "time")
        self.assertEqual(task12("I love dogs"), "love")

    # @patch("", )
    def test_task_13(self):
        with patch('builtins.input', return_value="My name is Michele"):
            self.assertEqual(task13(), "Michele is name My")

    @patch("builtins.input", return_value=6)
    def test_task14(self, n):
        self.assertEqual(task14(), [1, 1, 2, 3, 5, 8])

    def test_task15(self):
        self.assertEqual(task15([1, 1, 2, 3, 5, 9]), [2, 9])

    def test_task16(self):
        self.assertEqual(task16(4), 10)

    def test_task17(self):
        self.assertEqual(task17(4), 24)

    def test_task18(self):
        self.assertEqual(task18('abcd'), 'bcdE')
        self.assertEqual(task18('abcdz'), 'bcdEA')

    def test_task19(self):
        self.assertEqual(task19('edcba'), 'abcde')

    def test_task20(self):
        self.assertEqual(task20(4, 5), True)
        self.assertEqual(task20(5, 4), False)


if __name__ == '__main__':
    unittest.main()
