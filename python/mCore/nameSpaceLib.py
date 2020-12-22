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
## @file    mCore/nameSpaceLib.py @brief [ FILE   ] - Operate on name spaces.
## @package mCore.nameSpaceLib    @brief [ MODULE ] - Operate on name spaces.


#
# ----------------------------------------------------------------------------------------------------
# IMPORT
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ CLASS ] - Class to operate on namespaces.
#
#  @code
#import sys
#import mCore.nameSpaceLib
#
#_nameSpace = mCore.nameSpaceLib.NameSpace(nameSpace='asset:soldier:armA_01_jnt')
#
#sys.stdout.write(_nameSpace.nameSpace())
# # asset:soldier:armA_01_jnt
#
#sys.stdout.write(_nameSpace.head())
# # asset:soldier
#
#sys.stdout.write(_nameSpace.tail())
# # armA_01_jnt
#
#sys.stdout.write(mCore.nameSpaceLib.NameSpace.isValid('soldier'))
# # False
#
#  @endcode
class NameSpace(object):
    #
    # ------------------------------------------------------------------------------------------------
    # PUBLIC STATIC MEMBERS
    # ------------------------------------------------------------------------------------------------
    ## [ str ] - Name space delimiter.
    NAME_SPACE_DELIMITER = ':'

    ## [ str ] - Full path delimiter.
    FULL_PATH_DELIMITER  = '|'

    #
    # ------------------------------------------------------------------------------------------------
    # PRIVATE METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Constructor.
    #
    #  @param nameSpace [ str | None | in  ] - NameSpace.
    #
    #  @exception N/A
    #
    #  @return None
    def __init__(self, nameSpace=None):

        ## [ str ] - NameSpace.
        self._nameSpace = None

        if nameSpace:
            self.setNameSpace(nameSpace)

    #
    # ------------------------------------------------------------------------------------------------
    # PROTECTED METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Get requested element of the name space.
    #
    #  @param head [ bool | True | in  ] - True for head, False for tail.
    #
    #  @exception N/A
    #
    #  @return str - Requested element of the name space.
    def _element(self, head=True):

        if not self._nameSpace:
            return None

        temp = self._nameSpace.split(self.NAME_SPACE_DELIMITER)
        if len(temp) == 1:
            return temp[0]

        # Return head
        if head:
            return ':'.join(temp[:-1])

        # Return tail
        return temp[-1:][0]

    #
    # ------------------------------------------------------------------------------------------------
    # PROPERTY METHODS
    # ------------------------------------------------------------------------------------------------
    ## @name PROPERTIES

    ## @{
    #
    ## @brief NameSpace.
    #
    #  @exception N/A
    #
    #  @return str  - NameSpace.
    #  @return None - If name space is not set.
    def nameSpace(self):

        return self._nameSpace

    #
    ## @brief Set name space.
    #
    #  @param nameSpace [ str | None | in  ] - NameSpace.
    #
    #  @return bool - Result.
    def setNameSpace(self, nameSpace):

        if not NameSpace.isValid(nameSpace):
            return False

        self._nameSpace = nameSpace

        return True

    #
    ## @}

    #
    # ------------------------------------------------------------------------------------------------
    # PUBLIC METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Get name space portion of the name space.
    #
    #  @exception N/A
    #
    #  @return str - NameSpace portion.
    def head(self):

        return self._element(head=True)

    #
    ## @brief Get the tail portion of the name space.
    #
    #  @exception N/A
    #
    #  @return str - Part portion of the name space.
    def tail(self):

        return self._element(head=False)

    #
    # ------------------------------------------------------------------------------------------------
    # CLASS METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Determine whether given string is a valid name space.
    #
    #  Whether it has NameSpace.NAME_SPACE_DELIMITER in the given string.
    #
    #  @param cls       [ object | None | in  ] - Class object.
    #  @param nameSpace [ str    | None | in  ] - NameSpace.
    #
    #  @exception N/A
    #
    #  @return bool - Result.
    @classmethod
    def isValid(cls, nameSpace):

        return cls.NAME_SPACE_DELIMITER in nameSpace

    #
    ## @brief Remove name space from the given name.
    #
    #  @param cls  [ object | None | in  ] - Class object.
    #  @param name [ str    | None | in  ] - Name.
    #
    #  @exception N/A
    #
    #  @return str - Name without name space.
    @classmethod
    def removeNameSpace(cls, name):

        return cls.FULL_PATH_DELIMITER.join([x.split(cls.NAME_SPACE_DELIMITER)[-1:][0] for x in name.split('|')])

    #
    ## @brief Add given name space to given name.
    #
    #  @param cls            [ object | None | in  ] - Class object.
    #  @param nameSpace      [ str    | None | in  ] - Name space to be added.
    #  @param name           [ str    | None | in  ] - Name.
    #  @param removeExisting [ bool   | True | in  ] - Remove existing name space from the given name before adding the new one.
    #
    #  @exception N/A
    #
    #  @return str - Name with name space.
    @classmethod
    def addNameSpace(cls, nameSpace, name, removeExisting=True):

        if removeExisting:
            name = NameSpace.removeNameSpace(name)

        nameWithNameSpace = [x for x in name.split('|') if x]

        return ''.join(['{}{}{}{}'.format(cls.FULL_PATH_DELIMITER, nameSpace, cls.NAME_SPACE_DELIMITER, x) for x in nameWithNameSpace])[1:]

