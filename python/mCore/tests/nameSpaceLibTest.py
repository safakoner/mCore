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
## @file    sFileSystem/tests/directoryLibTest.py [ FILE   ] - Unit test module.
## @package sFileSystem.tests.directoryLibTest    [ MODULE ] - Unit test module.


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import unittest

import mCore.nameSpaceLib


#
#-----------------------------------------------------------------------------------------------------
# CODE
#-----------------------------------------------------------------------------------------------------
class NameSpaceTest(unittest.TestCase):

    NAME_SPACE_A = 'soldier:armA_01_jnt'

    NAME_SPACE_B = 'root:soldier:armA_01_jnt'

    NAME_SPACE_C = 'root:char:soldier:armA_01_jnt'

    NAME_SPACE_D = 'root:char:soldier:armA_01_jnt|root:char:soldier:armB_01_jnt'

    def test_constructorA(self):

        _nameSpace = mCore.nameSpaceLib.NameSpace(NameSpaceTest.NAME_SPACE_A)

        self.assertEqual(_nameSpace.head(), 'soldier')
        self.assertEqual(_nameSpace.tail(), 'armA_01_jnt')

    def test_constructorB(self):

        _nameSpace = mCore.nameSpaceLib.NameSpace(NameSpaceTest.NAME_SPACE_B)

        self.assertEqual(_nameSpace.head(), 'root:soldier')
        self.assertEqual(_nameSpace.tail(), 'armA_01_jnt')

    def test_setNameSpaceA(self):

        _nameSpace = mCore.nameSpaceLib.NameSpace()

        self.assertTrue(_nameSpace.setNameSpace(NameSpaceTest.NAME_SPACE_A))

        self.assertEqual(_nameSpace.head(), 'soldier')
        self.assertEqual(_nameSpace.tail(), 'armA_01_jnt')

    def test_setNameSpaceB(self):

        _nameSpace = mCore.nameSpaceLib.NameSpace()

        self.assertTrue(_nameSpace.setNameSpace(NameSpaceTest.NAME_SPACE_B))

        self.assertEqual(_nameSpace.head(), 'root:soldier')
        self.assertEqual(_nameSpace.tail(), 'armA_01_jnt')

    def test_isValid(self):

        self.assertTrue(mCore.nameSpaceLib.NameSpace.isValid(NameSpaceTest.NAME_SPACE_A))
        self.assertTrue(mCore.nameSpaceLib.NameSpace.isValid(NameSpaceTest.NAME_SPACE_B))
        self.assertTrue(mCore.nameSpaceLib.NameSpace.isValid(NameSpaceTest.NAME_SPACE_C))

        self.assertFalse(mCore.nameSpaceLib.NameSpace.isValid('notANameSpace'))

    def test_removeNameSpace(self):

        self.assertEqual(mCore.nameSpaceLib.NameSpace.removeNameSpace(NameSpaceTest.NAME_SPACE_A), 'armA_01_jnt')
        self.assertEqual(mCore.nameSpaceLib.NameSpace.removeNameSpace(NameSpaceTest.NAME_SPACE_B), 'armA_01_jnt')
        self.assertEqual(mCore.nameSpaceLib.NameSpace.removeNameSpace(NameSpaceTest.NAME_SPACE_C), 'armA_01_jnt')

        self.assertEqual(mCore.nameSpaceLib.NameSpace.removeNameSpace(NameSpaceTest.NAME_SPACE_D), 'armA_01_jnt|armB_01_jnt')

    def test_addNameSpace(self):

        self.assertEqual(mCore.nameSpaceLib.NameSpace.addNameSpace('soldier'          , 'armA_01_jnt'             , True) , 'soldier:armA_01_jnt')
        self.assertEqual(mCore.nameSpaceLib.NameSpace.addNameSpace('root:soldier'     , 'armA_01_jnt'             , True) , 'root:soldier:armA_01_jnt')
        self.assertEqual(mCore.nameSpaceLib.NameSpace.addNameSpace('root:char:soldier', 'armA_01_jnt'             , True) , 'root:char:soldier:armA_01_jnt')

        self.assertEqual(mCore.nameSpaceLib.NameSpace.addNameSpace('top:prop:sword'   , NameSpaceTest.NAME_SPACE_D, True) , 'top:prop:sword:armA_01_jnt|top:prop:sword:armB_01_jnt')
        self.assertEqual(mCore.nameSpaceLib.NameSpace.addNameSpace('top:prop:sword'   , NameSpaceTest.NAME_SPACE_D, False), 'top:prop:sword:root:char:soldier:armA_01_jnt|top:prop:sword:root:char:soldier:armB_01_jnt')


#
#-----------------------------------------------------------------------------------------------------
# INVOKE
#-----------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    unittest.main()
