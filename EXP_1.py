import time
import random

def interp_search(arr, val):
    L = 0
    H = len(arr) - 1
    cnt = 0
    while L <= H and arr[L] <= val and val <= arr[H]:
        cnt = cnt + 1
        if arr[L] == arr[H]:
            if arr[L] == val:
                return L, cnt
            else:
                return -1, cnt
        
        p = L + int(((val - arr[L]) * (H - L)) / (arr[H] - arr[L]))
        
        if arr[p] == val:
            return p, cnt
        if arr[p] < val:
            L = p + 1
        else:
            H = p - 1
    return -1, cnt

def bin_search(arr, val):
    L = 0
    H = len(arr) - 1
    cnt = 0
    while L <= H:
        cnt = cnt + 1
        m = (L + H) // 2
        if arr[m] == val:
            return m, cnt
        if arr[m] < val:
            L = m + 1
        else:
            H = m - 1
    return -1, cnt

def run_bench():
    N_list = [1000, 5000, 10000, 50000, 100000]
    print(f"{'Size':>10} {'IS Time(ms)':>14} {'BS Time(ms)':>14} {'IS Comps':>12} {'BS Comps':>12}")
    print('-' * 68)
    for N in N_list:
        arr = sorted(random.sample(range(N * 10), N))
        val = arr[random.randint(0, N - 1)]
        
        t0 = time.perf_counter()
        for i in range(100):
            idx_is, c_is = interp_search(arr, val)
        t_is = (time.perf_counter() - t0) * 10
        
        t0 = time.perf_counter()
        for i in range(100):
            idx_bs, c_bs = bin_search(arr, val)
        t_bs = (time.perf_counter() - t0) * 10
        
        print(f"{N:>10} {t_is:>14.4f} {t_bs:>14.4f} {c_is:>12} {c_bs:>12}")

if __name__ == "__main__":
    arr = [2, 5, 10, 15, 23, 35, 48, 60, 75, 90, 105, 120]
    val = 35
    idx, comps = interp_search(arr, val)
    print(f"Array: {arr}")
    print(f"Searching for: {val}")
    print(f"Found at index: {idx}")
    print(f"Comparisons: {comps}")
    print()
    run_bench()