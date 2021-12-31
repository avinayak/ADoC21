#!/usr/bin/python
# Path: Day 02/main.py

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


def answer_pt2():
    X = 0
    Y = 0
    aim = 0
    with open("input.txt", "r") as f:
        for inst in f.read().strip().split("\n"):
            [direc, mag] = inst.split()
            if direc == "forward":
                X += int(mag)
                Y += aim*int(mag)
            elif direc == "down":
                aim += int(mag)
            elif direc == "up":
                aim += -int(mag)
    return X*Y

if __name__ == "__main__":
    print(answer())
    print(answer_pt2())
