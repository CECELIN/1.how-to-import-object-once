

class Phone():
    def __init__(self, os,number,is_Water_Proof):
        self.os=os
        self.number=number
        self.is_Water_Proof=is_Water_Proof

    def show(self):
        print('This is lib')
        print(self.os, str(self.number), str(self.is_Water_Proof))

    def add(self, value):
        return value+1

    def Qpt_os(self):
        print("os: " + self.os)

    def Qpt_number(self):
        print("number: " + str(self.number))

    def Qpt_is_Water_Proof(self):
        print("is_Water_Proof: " + str(self.is_Water_Proof))

    def Qpt_os_2(self, os):
        print("os: " + os)

    def Qpt_number_2(self, number):
        print("number: " + str(number))

    def Qpt_is_Water_Proof_2(self, is_wp):
        print("is_Water_Proof: " + str(is_wp))
