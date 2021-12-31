from collections import Counter


def answer():
    with open("input.txt", "r") as f:
        gamma = ""
        eplison = ""
        for col in zip(*f.read().strip().split()):
            [(gd, _), (ed, _)] = Counter(col).most_common()
            gamma += gd
            eplison += ed
    return int(gamma, 2)*int(eplison, 2)


def answer2():
    with open("input.txt", "r") as f:
        oxy = ""
        co2 = ""
        bits = f.read().strip().split()

        obits = [x for x in bits]
        cbits = [x for x in bits]

        i = 0
        while len(obits) > 1:
            [(gd, l1), (ed, l2)] = Counter(
                (list(zip(*obits)))[i]).most_common()
            oxy += "1" if l1 == l2 else gd
            obits = list(filter(lambda x: x.startswith(oxy), obits))
            i += 1
        i = 0
        while len(cbits) > 1:
            [(gd, l1), (ed, l2)] = Counter(
                (list(zip(*cbits)))[i]).most_common()
            co2 += "0" if l1 == l2 else ed
            cbits = list(filter(lambda x: x.startswith(co2), cbits))
            i += 1

        return int(cbits[0], 2)*int(obits[0], 2)


print(answer())
print(answer2())
