#!/usr/bin/python


def answer():
    X = 0
    Y = 0
    with open("input.txt", "r") as f:
        for inst in f.read().strip().split("\n"):
            [direc, mag] = inst.split()
            if direc == "forward":
                X += int(mag)
            elif direc == "down":
                Y += int(mag)
            elif direc == "up":
                Y += -int(mag)
    return X*Y


print(answer())
