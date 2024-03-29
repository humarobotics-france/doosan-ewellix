# -*- coding: utf-8 -*-
"""
Ewellix class is used for the dialogue between an ewellix lifting column and a Doosan robot.
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
"""

# Keep thoses lines in order to test the code without a Doosan:
import socket
import time
tp_popup = print
tp_log = print
DR_PM_MESSAGE = 'MESSAGE POPUP'
DR_PM_WARNING = 'WARNING POPUP'
DR_PM_ALARM = 'ALARM POPUP'

def client_socket_open(ip, port): 
    try:
        e_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        e_socket.connect((ip, port))
    except Exception as e:
        print("Socket connection failed. Error: {0}".format(
        str(e)))
        raise e
    print(e_socket)
    return e_socket

def client_socket_read(s, length, timeout):
    r = s.recv(1024)
    return len(r),r

def client_socket_write(s, cmd):
    s.send(cmd)

wait = time.sleep

#####################
# DON'T FORGET TO REMOVE THOSE LINES ABOVE BEFORE USED ON THE DOOSAN

class Ewellix:
    """
    Interface to use Ewellix with Doosan
    """

    def __init__(self, ip="192.168.1.100", port=50001, low_position=665):
        """
        Initialize the connection between the Ewellix and the Doosan.

        Params:\n
            - 'ip': ip of the Ewellix
            - 'port': port of the Ewellix
            - 'low_position': low position of the ewellix column (used to add an offset on move_to command)
        """

        self.ip = ip
        self.port = port
        self.timeout = 10 # 10 seconds timeout
        self.low_position = low_position

        tp_log("connection to the Ewellix")
        try:
            self._socket = client_socket_open(self.ip, self.port)
            tp_log("connection to the Ewellix ok !")
        except Exception as e:
            tp_popup("Socket connection failed. Error: {0}".format(
                str(e)), DR_PM_ALARM)
            raise e

    def write(self, cmd):
        """
        Write 'cmd' in the socket

        Params:\n
            - 'cmd': a Ewellix TCP Protocol command

        Return:\n
            - 'res': result of the writing

        Exemple:\n
            write("recognize")
        """

        # Convert cmd in ascii before sending
        cmd = bytes(cmd+"\n", encoding="ascii")

        res = client_socket_write(self._socket, cmd)

        # Check res value
        if res == -1:
            tp_log("error  " + 
                "Error during a socket write: Server not connected")
        elif res == -2:
            tp_log("error  " + "Error during a socket write: Socket error")
        elif res == 0:
            tp_log("info " + "Sending {0} command ok".format(cmd))
        return res

    def read(self, length=-1, timeout=-1):
        """
        Read the socket

        Params:\n
            - 'length': number of bytes to read (default = -1)
            - 'timeout': Waiting time (default = -1)

        Return:\n
            - 'res': result of the reading
            - 'rx_data': data received
        """

        res, rx_data = client_socket_read(self._socket, length, timeout)

        # Check res value
        if res == -1:
            tp_log("error " + 
                "Error during a socket read: Server not connected")
        elif res == -2:
            tp_log("error " + "Error during a socket read: Socket error")
        elif res == -3:
            tp_log("error " + 
                "Error during a socket read: Waiting time has expired")
        elif res > 0:
            tp_log("info" + 
                "Read res = {0} and rx_data = {1}".format(res, rx_data))

        # tp_popup("res={0}, rx_data={1}".format(res, rx_data))
        return res, rx_data.decode()

    def get_status(self):
        cmd = "get_status"
        self.write(cmd)
        res, rx_data = self.read()
        return res, rx_data

    def get_stroke(self):
        cmd = "get_stroke"
        self.write(cmd)
        res, rx_data = self.read()
        return res, rx_data

    def get_virtual_limites(self):
        cmd = "get_virtualLimits"
        self.write(cmd)
        res, rx_data = self.read()
        return res, rx_data

    def get_types_available(self):
        cmd = "get_typesAvailable"
        self.write(cmd)
        res, rx_data = self.read()
        return res, rx_data
    
    def get_position(self):
        cmd = "get_position"
        self.write(cmd)
        res, rx_data = self.read()
        return res, rx_data

    def set_type(self, type="LIFTKIT-601"):
        cmd = "set_type," + type
        self.write(cmd)
        res, rx_data = self.read()
        return res, rx_data

    def set_virtual_limits(self, min=0, max=700):
        cmd = "set_virtualLimits," + str(min) + "," + str(max)
        self.write(cmd)
        res, rx_data = self.read()
        return res, rx_data

    def move_to(self, pos):
        start_time = time.time()
        elapsed = 0
        while self.get_status()[1].split(',')[2].rstrip("\n") != "READY":
            wait(0.2)
            #tp_log("wait ewellix")
            elapsed = time.time() - start_time 
            if elapsed > self.timeout:
                tp_log("Timeout moveTo_absolutePosition")
                break

        cmd = "moveTo_absolutePosition," + str(pos-self.low_position)
        self.write(cmd)
        res, rx_data = self.read()

        start_time = time.time()
        elapsed = 0
        wait(3)
        #tp_log(self.get_status()[1].split(',')[2].rstrip("\n"))
        while self.get_status()[1].split(',')[2].rstrip("\n") != "READY":
            wait(0.4)
            #tp_log("wait ewellix")
            elapsed = time.time() - start_time 
            if elapsed > self.timeout:
                tp_log("Timeout moveTo_absolutePosition")
                break

        return res, rx_data
        
    def stop_moving(self):
        cmd = "stop_moving"
        self.write(cmd)
        res, rx_data = self.read()
        return res, rx_data

    def initialise(self, type="LIFTKIT-601", min=0, max=700):
        """Initialization of the Ewellix"""

        self.set_type(type="LIFTKIT-601")
        self.set_virtual_limits(min=min, max=max)

    def check_position(self, position, epsilon=2):
        pos_ewellix = float(ewellix.get_position()[1].split(",")[2][:-1]) + self.low_position
        if pos_ewellix > position + epsilon or pos_ewellix < position - epsilon:
            return False
        else:
            return True


if __name__ == "__main__":
    ewellix = Ewellix(ip="127.0.0.1", port=50001)
    ewellix.get_status()
    ewellix.initialise()
    ewellix.get_status()
    ewellix.move_to(1200)
    ewellix.get_position()
    ewellix.move_to(800)
    ewellix.get_position()