__author__ = 'khaile'
import unittest
import sys

class Assert(unittest.TestCase):
    def __init__(self):
        self._type_equality_funcs = {}
        self.addTypeEqualityFunc(dict, 'assertDictEqual')
        self.addTypeEqualityFunc(list, 'assertListEqual')
        self.addTypeEqualityFunc(tuple, 'assertTupleEqual')
        self.addTypeEqualityFunc(set, 'assertSetEqual')
        self.addTypeEqualityFunc(frozenset, 'assertSetEqual')
        try:
            self.addTypeEqualityFunc(unicode, 'assertMultiLineEqual')
        except NameError:
            # No unicode support in this build
            pass

    def didThrowError(self):
        """
        This is to catch if an exception ( error by a failed assertion) is caught
        """
        if sys.exc_info() != (None, None, None):
            return True
        else:
            return False

    def assertExists(self, obj, msg=None):
        """
        :param obj: object in need of verification
        :param msg: message when the assertion does not pass
        """
        self.assertIsNotNone(obj=obj, msg=None)

    def assertNotExists(self, obj, msg=None):
        """
        :param obj: object in need of verification
        :param msg: message when the assertion does not pass
        """
        self.assertIsNone(obj=obj, msg=None)

    # def assertEqual(self, first, second, msg=None):
    #     """
    #     :param first: first comparison value
    #     :param second: second comparison value
    #     :param msg: message when the assertion does not pass
    #     """
    #
    #     self.assertEqual(first, second, msg=None)
    #
    # def assertNotEqual(self, first, second, msg=None):
    #     """
    #     :param first: first comparison value
    #     :param second: second comparison value
    #     :param msg: message when the assertion does not pass
    #
    #     """
    #     self.assertNotEqual(first, second, msg=None)
    #
    #
    # def assertGreater(self, first, second, msg=None):
    #     """
    #     evaluate if the first is greater than the second
    #     :param first: first comparison value
    #     :param second: second comparison value
    #     :param msg: message when the assertion does not pass
    #     """
    #     self.assertGreater(first, second, msg=None)
    #
    #
    # def assertGreaterEqual(self, first, second, msg=None):
    #     """
    #     evaluate if the first is greater than or equal to the second
    #     :param first: first comparison value
    #     :param second: second comparison value
    #     :param msg: message when the assertion does not pass
    #     """
    #     self.assertGreaterEqual(first, second, msg=None)
    #
    #
    # def assertLess(self, first, second, msg=None):
    #     """
    #     evaluate if the first is less than the second
    #     :param first: first comparison value
    #     :param second: second comparison value
    #     :param msg: message when the assertion does not pass
    #     """
    #     self.assertLess(first, second, msg=None)
    #
    # def assertLessEqual(self, first, second, msg=None):
    #     """
    #     evaluate if the first is less than or equal to the second
    #     :param first: first comparison value
    #     :param second: second comparison value
    #     :param msg: message when the assertion does not pass
    #     """
    #     self.assertLessEqual(first, second, msg=None)
    #
    # def assertTrue(self, expr, msg=None):
    #     """
    #     evaluate if the express/value has True condition
    #     :param expr: expression or value
    #     :param msg: message when the assertion does not pass
    #     """
    #     self.assertTrue(expr, msg=None)
    #
    # def assertFalse(self, expr, msg=None):
    #     """
    #     evaluate if the express/value has False condition
    #     :param expr: expression or value
    #     :param msg: message when the assertion does not pass
    #     """
    #     self.assertFalse(expr, msg=None)
