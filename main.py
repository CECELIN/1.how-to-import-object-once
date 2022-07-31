#!/usr/bin/env python2
# coding=utf-8

from lib import phone


def main():
    qpt = phone.Phone("ios",13,True)
    qpt.show()
    print(qpt.add(3))
    qpt.Qpt_os()
    qpt.Qpt_number()
    qpt.Qpt_is_Water_Proof()

    qpt.Qpt_os_2("android")
    qpt.Qpt_number_2(6)
    qpt.Qpt_is_Water_Proof_2(False)
    qpt.show()


if __name__ == '__main__':
    main()
