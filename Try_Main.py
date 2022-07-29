import test_lib

class Phone():
    def __init__(self, os,number,is_Water_Proof):
        self.os=os
        self.number=number
        self.is_Water_Proof=is_Water_Proof

QPT=Phone("ios",13,True)

test_lib.show()
print(test_lib.add(3))

test_lib.Qpt_os(QPT)
test_lib.Qpt_number(QPT)
test_lib.Qpt_is_Water_Proof(QPT)
