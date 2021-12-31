def slide(input, window):
    return [sum(input[i-window+1:i+1]) for i in range(window-1, len(input))]


def answer(window=1):
    with open("1_input.txt", "r") as f:
        input = map(int, f.read().strip().split())
        last = None
        inc = 0
        for depth in slide(list(input), window):
            if last is not None and depth > last:
                inc += 1
            last = depth
        return inc

print(answer()) # part 1
print(answer(3)) # part 2