#!/usr/bin/env python3
# Copyright (C) 2013-2016 Florian Festi
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from boxes import *


class Edges(Boxes):
    """Print all registerd Edge types"""

    webinterface = False

    def __init__(self):
        Boxes.__init__(self)

    def render(self):
        self.ctx = None
        self._buildObjects()
        chars = self.edges.keys()
        for c in sorted(chars, key=lambda x: (x.lower(), x.isupper())):
            print("%s %s - %s" % (c, self.edges[c].__class__.__name__,
                  self.edges[c].__doc__))
