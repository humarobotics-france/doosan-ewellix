# -*- coding: utf-8 -*-
"""
This class is used to simulate an ewellix lifting column in order to test Ewellix code.
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
import socket
import time


class FakeEwellix:
    """
    A fake server to simulate an Ewellix
    """

    def __init__(self, port=50001):
        """
        Initialize the server.

        Params:\n
            - 'port': port of the fake Ewellix
        """

        self.port = port
        self.type = None
        self.lim_max = None
        self.lim_min = None
        self.position = 150
        self.state = "INITIALIZED"

        try:
            self._socket = socket.socket()
            self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self._socket.bind(("", self.port))
        except Exception as e:
            print("Socket connection failed. Error: {0}".format(
                str(e)))
            raise e

        self._socket.listen(1)  # 1 connection max
        print("Listening...")
        (self._client_socket, (self.ip_client, self.port_client)) = self._socket.accept()

        print("[+] New connection for %s %s" %
              (self.ip_client, self.port_client))
        self.run()

    def run(self):
        while True:
            msg_recv = self._client_socket.recv(2048)
            dmsg_recv = msg_recv.decode().rstrip("\n")
            print("received: {}".format(dmsg_recv))

            if dmsg_recv == "get_status":
                if self.type != "LIFTKIT-601":
                    msg = "get_status,OK,CONNECTED,TYPE NOT SET"
                    print("Send: {}".format(msg))
                    self._client_socket.send(msg.encode())
                else:
                    msg = "get_status,OK," + self.state
                    print("Send: {}".format(msg))
                    self._client_socket.send(msg.encode())

            elif dmsg_recv == "get_typesAvailable":
                msg = "get_typesAvailable,OK,LIFTKIT-601,LIFTKIT-602,LIFTKIT-00"
                print("Send: {}".format(msg))
                self._client_socket.send(msg.encode())

            elif dmsg_recv == "set_type,LIFTKIT-601":
                msg = "set_type,OK"
                self.type = "LIFTKIT-601"
                self.state = "CONNECTED"
                print("Send: {}".format(msg))
                self._client_socket.send(msg.encode())

            elif dmsg_recv == "get_position":
                msg = "get_position,OK," + str(self.position)
                print("Send: {}".format(msg))
                self._client_socket.send(msg.encode())

            elif dmsg_recv.split(",")[0] == "set_virtualLimits":
                msg = "set_virtualLimits,OK"
                self.state = "READY"
                self.lim_min = int(dmsg_recv.split(",")[1])
                self.lim_max = int(dmsg_recv.split(",")[2])
                print("Send: {}".format(msg))
                self._client_socket.send(msg.encode())

            elif dmsg_recv.split(",")[0] == "moveTo_absolutePosition":
                self.state = "MOVING"
                self.position = int(dmsg_recv.split(",")[1])
                msg = "moveTo_absolutePosition,OK"
                print("Send: {}".format(msg))
                self._client_socket.send(msg.encode())
                time.sleep(2) # Simulate the movement of the liftkit
                self.state = "READY"

            else:
                msg = "error, commande unknown"
                print("Send: {}".format(msg))
                self._client_socket.send(msg.encode())
                exit()


if __name__ == "__main__":
    fake_ewellix = FakeEwellix()
