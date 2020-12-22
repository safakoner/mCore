#
# Copyright 2020 Safak Oner.
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @file    mCore/tests/enumAbsTest.py [ FILE   ] - Unit test module.
## @package mCore.tests.enumAbsTest    [ MODULE ] - Unit test module.


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import unittest

import mCore.enumAbs



#
#-----------------------------------------------------------------------------------------------------
# CODE
#-----------------------------------------------------------------------------------------------------
class EntryType(mCore.enumAbs.Enum):

    kWIP       = 'wip'
    kPublished = 'published'
    kProduct   = 'product'
    kAll       = [kWIP, kPublished, kProduct]

class EnumTest(unittest.TestCase):

    def test_listAttributes(self):

        self.assertEqual(EntryType.listAttributes(False, False, False, False) , ['kAll'    , 'kProduct'  , 'kPublished', 'kWIP'])
        self.assertEqual(EntryType.listAttributes(False, False, True,  False) , ['All'     , 'Product'   , 'Published' , 'WIP'])
        self.assertEqual(EntryType.listAttributes(False, False, True,  True)  , ['all'     , 'product'   , 'published' , 'wIP'])
        self.assertEqual(EntryType.listAttributes(True , True , True,  False) , ['product' , 'published' , 'wip'])
        self.assertEqual(EntryType.listAttributes(False, True , True,  False) , ['product' , 'published' , 'wip', ['wip'    , 'published' , 'product']])

    def test_listAttributeElements(self):

        self.assertEqual(EntryType.listAttributeElements('kAll'), ['wip', 'published', 'product'])

    def test_getAttributeNameFromValue(self):

        self.assertEqual(EntryType.getAttributeNameFromValue('product', removeK=False), 'kProduct')

    def test_getValueFromAttributeName(self):

        self.assertEqual(EntryType.getValueFromAttributeName('kProduct'), 'product')

    def test_asDict(self):

        self.assertEqual(EntryType.asDict(), {'All': ['wip', 'published', 'product'], 'Product': 'product', 'WIP': 'wip', 'Published': 'published'})

#
#-----------------------------------------------------------------------------------------------------
# INVOKE
#-----------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    unittest.main()
