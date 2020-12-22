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
## @file    mCore/pythonUtilsLib.py @brief [ FILE   ] - Utilities.
## @package mCore.pythonUtilsLib    @brief [ MODULE ] - Utilities.


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import  os
import  sys

import  mFileSystem.directoryLib
import  mFileSystem.fileLib


#
#-----------------------------------------------------------------------------------------------------
# CODE
#-----------------------------------------------------------------------------------------------------
#
## @brief Create a Python package.
#
#  This function does nothing if a Python package with given `name` exists
#
#  @param path                  [ str  | None | in  ] - Path, where the Python package will be created.
#  @param name                  [ str  | None | in  ] - Name of the Python package.
#  @param createUnitTestPackage [ bool | None | in  ] - Whether to create unit test Python package under Python package.
#
#  @exception N/A
#
#  @return str - Root path of the Python package.
def createPythonPackage(path, name, createUnitTestPackage=True):

    path = os.path.join(path, name)

    if not os.path.isdir(path):
        os.makedirs(path)

    createPythonModule(path)

    if createUnitTestPackage and name != 'tests':
        createPythonPackage(path, 'tests')

    return path

#
## @brief Create a Python module with given name in given path.
#
#  @param path    [ str | None | in  ] - Absolute path where the Python module will be created in.
#  @param name    [ str | None | in  ] - Name of the Python module, which will be created.
#  @param content [ str | None | in  ] - Content, which will be written into the file.
#
#  @exception N/A
#
#  @return str - Absolute path of the created Python module.
def createPythonModule(path, name='__init__.py', content=None):

    if not os.path.isdir(path):
        os.makedirs(path)

    pythonModuleFilePath = os.path.join(path, name)

    if not os.path.isfile(pythonModuleFilePath):

        _file = open(pythonModuleFilePath, 'w')
        if content:
            _file.write(content)
        _file.close()

    return pythonModuleFilePath

#
## @brief Remove all files with .pyc and .pyo extension recursively.
#
#  If `path` is not provided `sys.path` will be used.
#  Function suspends `PermissionError` if raised.
#
#  @warning THIS METHOD HAS BEEN PROVIDED FOR INTERNAL USE ONLY.
#
#  @param path      [ str, list of str | None  | in  ] - Path.
#  @param verbose   [ bool             | False | in  ] - Display deleted files.
#
#  @exception N/A
#
#  @return None - None.
def removePythonObjects(path=None, verbose=False):

    if not path:
        path = sys.path
    else:
        if isinstance(path, str):
            path = [path]

    _directory = mFileSystem.directoryLib.Directory()
    _file      = mFileSystem.fileLib.File()

    for p in path:

        if not _directory.setDirectory(directory=p):
            continue

        pycFiles = _directory.listFilesRecursively(extension='pyc')
        if pycFiles:
            for i in pycFiles:
                if _file.setFile(path=i):
                    try:
                        _file.remove()
                        if verbose:
                            sys.stdout.write('{}\n'.format(i))
                    except PermissionError as error:
                        continue

        pyoFiles = _directory.listFilesRecursively(extension='pyo')
        if pyoFiles:
            for i in pyoFiles:
                if _file.setFile(path=i):
                    try:
                        _file.remove()
                        if verbose:
                            sys.stdout.write('{}\n'.format(i))
                    except PermissionError as error:
                        continue


