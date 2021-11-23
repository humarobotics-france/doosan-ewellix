<a href="https://www.humarobotics.com/">
    <img src="./images/Logo_HR_bleu.png" alt="HumaRobotics logo" title="HumaRobotics" align="right" height="80" />
</a>

# Doosan Ewellix

<p align="left">
  <a href="./README.md">English</a> •
  <a href="docs/README-fr.md">Français</a>
</p>

--------------

TCP/IP interface to control the Ewellix lifting column from a Doosan robot.

This project is developed by [HumaRobotics](https://www.humarobotics.com/).

## Requirements

- A **Doosan robot**
- A **Ewellix** lifting column

## How to use

- Configure IP of the robot to match the subnetwork "192.168.1.X".

- Create a `Custom Code` and import the [ewellix.py](./ewellix.py) file (replace .py by .txt to import in the Doosan). Don't forget to remove first lines of the code (those lines are used to test the code without a robot).

- Then, look at the examples in the "examples" folder to see how to use the Ewellix class. You can begin with the [ex_basic.py](./examples/ex_basic.py) (don't forget to change the extension '.py' to '.txt' before importing it into the Doosan).

## Examples files

- [ex_basic.py](./examples/ex_basic.py): Basic example for the communication between Ewellix lifting column and Doosan robot.

## Tests files

- [test_fake_ewellix.py](./tests/test_fake_ewellix.py): Code made to simulate an Ewellix from a computer. You can run this script and then the [ewellix.py](./Ewellix.py) program in the same computer to simulate a communication.

<div align = "center" >
<img src="./images/Logo_HR_bleu.png" alt="HumaRobotics logo" title="HumaRobotics" height="200" />
</div>
