# -*- coding: utf-8 -*-
"""
A basic example to communicate between a Ewellix, using Ewellix class, and the Doosan.
Please read the README.md file before use.
Copyright (C) 2021 HumaRobotics

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

In your Task Writer/ Task Builder you need:
    - A 'CustomCode' with the 'ewellix' file
    - A 'CustomCode' with this file
    

What does this example:
!!! Caution! The column will move, so make sure nothing gets in the way !!!
    1- Connection to the ewellix
    2- Init the liftkit
    3- get the status of the liftkit
    4- Move the lifting column to 100
    5- Move the lifting column to 120
"""

# Keep thoses lines in order to test the code without a Doosan:
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from ewellix import Ewellix

# Remove lines above when you want to used this code on the robot

ewellix = Ewellix()
ewellix.get_status()
ewellix.initialise()
ewellix.get_status()
ewellix.get_position()
ewellix.move_to(100)
ewellix.get_position()
ewellix.move_to(120)
ewellix.get_position()
