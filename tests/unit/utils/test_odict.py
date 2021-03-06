"""
Tests for `vinegar.utils.odict`.
"""

import unittest

from vinegar.utils.odict import OrderedDict


class TestOdictModule(unittest.TestCase):
    """
    Tests for the `vingear.utils.odict` module.
    """

    def test_preserves_order(self):
        """
        Test that the ``OrderedDict`` provided by the module does in fact
        preserve the insertion order.
        """
        my_dict = OrderedDict()
        my_list = [5, 1, 12, 2, 3, 6, 4]
        for i in my_list:
            my_dict[i] = i
        self.assertEqual(my_list, list(my_dict.keys()))
        self.assertEqual(my_list, list(my_dict.values()))
