from utils import arrs
import unittest

#Нечаянно сделал 100% покрытие при выполнении 3 задания, так что в 4 задании код без изменений.
#А этот коммент добавил только для коммита

class Test1(unittest.TestCase):


    def test_get(self):

        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 1, "test"), "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1), [2, 3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(arrs.my_slice([], 1, 3), [])
