#!/usr/bin/python3


class MyInt(int):
    def __init__(self, num):
        self.__num = num

    def __eq__(self, num):
        return False

    def __ne__(self, num):
        return True
