import sys

sequence = []


def real_collatz(n):
    if sequence.__contains__(n):
        print("loop:", n)
        return
    sequence.append(n)
    if n % 2 == 0:
        real_collatz(n / 2)
    else:
        real_collatz(3 * n + 1)


try:
    try:
        with open('collatz_last.txt', 'r') as reader:
            n = int(reader.read())
    except OSError:
        n = 1
    while True:
        print("Collatz for", n)
        real_collatz(n)
        n += 1
        sequence = []
except KeyboardInterrupt:
    with open('collatz_last.txt', 'w') as writer:
        writer.write(str(n))
    print('--- E N D ---')
