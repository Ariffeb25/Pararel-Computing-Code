# SERIAL COMPUTING (Single Core)

import time
import random

# fungsi menghitung total (serial)
def serial_sum(data):
    total = 0
    for num in data:
        total += num
    return total


if __name__ == "__main__":
    N = 10_000_000
    data = [random.randint(1, 10) for _ in range(N)]

    print("Jumlah data:", N)

    start = time.time()

    total = serial_sum(data)

    end = time.time()

    print("Total:", total)
    print("Waktu eksekusi (Serial):", end - start, "detik")