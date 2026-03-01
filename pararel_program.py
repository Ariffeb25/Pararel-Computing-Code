import time
import random
from multiprocessing import Pool, cpu_count

# =========================
# SERIAL COMPUTING
# =========================
def serial_sum(data):
    total = 0
    for num in data:
        total += num
    return total


# =========================
# PARALLEL COMPUTING
# =========================
def partial_sum(sub_array):
    total = 0
    for num in sub_array:
        total += num
    return total


if __name__ == "__main__":

    N = 10_000_000
    data = [random.randint(1, 10) for _ in range(N)]

    print("Jumlah data:", N)
    print("Jumlah core CPU:", cpu_count())

    # =========================
    # SERIAL EXECUTION
    # =========================
    start = time.time()
    total_serial = serial_sum(data)
    end = time.time()

    print("\n=== SERIAL COMPUTING ===")
    print("Total:", total_serial)
    print("Waktu eksekusi:", end - start, "detik")

    # =========================
    # PARALLEL EXECUTION
    # =========================
    jumlah_core = cpu_count()
    chunk_size = len(data) // jumlah_core

    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    start = time.time()

    with Pool(jumlah_core) as p:
        results = p.map(partial_sum, chunks)

    total_parallel = sum(results)
    end = time.time()

    print("\n=== PARALLEL COMPUTING ===")
    print("Total:", total_parallel)
    print("Waktu eksekusi:", end - start, "detik")