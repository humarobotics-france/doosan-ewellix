# -*- coding: utf-8 -*-
"""
A basic example to communicate between a Ewellix, using Ewellix class, and the Doosan.
Please read the README.md file before use.
Copyright (C) 2021 HumaRobotics

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

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
