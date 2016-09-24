__author__ = 'khaile'
import unittest

class Verify(unittest.TestCase):
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
        self.failureCount = 0

    def printFailMessage(self, msg):
        self.failureCount += 1
        if msg == None:
            print 'Failed'
        else:
            print 'Failed '+msg


    def didPass(self):
        self.assertLessEqual(self.failureCount, 0, 'There are failed verifications')

    def verifyIsNotNone(self, obj, msg=None):
        """
        :param obj: object in need of verification
        :param msg: message when the verification fails
        :return: boolean
        """
        try:
            self.assertIsNotNone(obj=obj, msg=None)
            return True

        except:
            self.printFailMessage(msg)
            return False


    def verifyIsNone(self, obj, msg=None):
        """
        :param obj: object in need of verification
        :param msg: message when the verification fails
        :return: boolean
        """
        try:
            self.assertIsNone(obj=obj, msg=None)
            return True

        except:
            self.printFailMessage(msg)
            return False

    def verifyEqual(self, first, second, msg=None):
        """
        :param first: first comparison value
        :param second: second comparison value
        :param msg: message when the verification fails
        :return: boolean
        """
        try:
            self.assertEqual(first, second, msg=None)
            return True

        except:
            self.printFailMessage(msg)
            return False

    def verifyNotEqual(self, first, second, msg=None):
        """
        :param first: first comparison value
        :param second: second comparison value
        :param msg: message when the verification fails
        :return: boolean
        """
        try:
            self.assertNotEqual(first, second, msg=None)
            return True

        except:
            self.printFailMessage(msg)
            return False


    def verifyGreater(self, first, second, msg=None):
        """
        evaluate if the first is greater than the second
        :param first: first comparison value
        :param second: second comparison value
        :param msg: message when the verification fails
        :return: boolean
        """
        try:
            self.assertGreater(first, second, msg=None)
            return True

        except:
            self.printFailMessage(msg)
            return False


    def verifyGreaterEqual(self, first, second, msg=None):
        """
        evaluate if the first is greater than or equal to the second
        :param first: first comparison value
        :param second: second comparison value
        :param msg: message when the verification fails
        :return: boolean
        """
        try:
            self.assertGreaterEqual(first, second, msg=None)
            return True

        except:
            self.printFailMessage(msg)
            return False

    def verifyLess(self, first, second, msg=None):
        """
        evaluate if the first is less than the second
        :param first: first comparison value
        :param second: second comparison value
        :param msg: message when the verification fails
        :return: boolean
        """
        try:
            self.assertLess(first, second, msg=None)
            return True

        except:
            self.printFailMessage(msg)
            return False


    def verifyLessEqual(self, first, second, msg=None):
        """
        evaluate if the first is less than or equal to the second
        :param first: first comparison value
        :param second: second comparison value
        :param msg: message when the verification fails
        :return: boolean
        """
        try:
            self.assertLessEqual(first, second, msg=None)
            return True

        except:
            self.printFailMessage(msg)
            return False