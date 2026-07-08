import time
import random

def naive_search(txt, pat):
    N = len(txt)
    M = len(pat)
    ans = []
    cnt = 0
    for i in range(N - M + 1):
        j = 0
        while j < M:
            cnt = cnt + 1
            if txt[i + j] != pat[j]:
                break
            j = j + 1
        if j == M:
            ans.append(i)
    return ans, cnt

def get_lps(pat):
    M = len(pat)
    lps = [0] * M
    length = 0
    i = 1
    while i < M:
        if pat[i] == pat[length]:
            length = length + 1
            lps[i] = length
            i = i + 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i = i + 1
    return lps

def kmp_search(txt, pat):
    N = len(txt)
    M = len(pat)
    lps = get_lps(pat)
    ans = []
    cnt = 0
    i = 0
    j = 0
    while i < N:
        cnt = cnt + 1
        if pat[j] == txt[i]:
            i = i + 1
            j = j + 1
        if j == M:
            ans.append(i - j)
            j = lps[j - 1]
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i = i + 1
    return ans, cnt

def rabin_karp(txt, pat):
    N = len(txt)
    M = len(pat)
    q = 101
    d = 256
    
    h = 1
    for i in range(M - 1):
        h = (h * d) % q
        
    p_hash = 0
    t_hash = 0
    ans = []
    cnt = 0
    
    for i in range(M):
        p_hash = (d * p_hash + ord(pat[i])) % q
        t_hash = (d * t_hash + ord(txt[i])) % q
        
    for s in range(N - M + 1):
        if p_hash == t_hash:
            match = True
            for k in range(M):
                cnt = cnt + 1
                if txt[s + k] != pat[k]:
                    match = False
                    break
            if match == True:
                ans.append(s)
                
        if s < N - M:
            t_hash = (d * (t_hash - ord(txt[s]) * h) + ord(txt[s + M])) % q
            if t_hash < 0:
                t_hash = t_hash + q
                
    return ans, cnt

if __name__ == "__main__":
    txt = "AABAACAADAABAABA"
    pat = "AABA"
    
    print(f"Text: {txt}")
    print(f"Pattern: {pat}")
    
    m1, c1 = naive_search(txt, pat)
    m2, c2 = kmp_search(txt, pat)
    m3, c3 = rabin_karp(txt, pat)
    
    print(f"\nNaive -> Matches at: {m1}, Comparisons: {c1}")
    print(f"KMP -> Matches at: {m2}, Comparisons: {c2}")
    print(f"RK -> Matches at: {m3}, Comparisons: {c3}")
    
    txt_large = "".join(random.choices("ABCD", k=10000))
    patterns = ["AB", "ABCD", "ABCDAB", "ABCDABCD"]
    
    print(f"\n{'Pattern':>12} {'Naive':>10} {'KMP':>10} {'RK':>10}")
    print("-" * 50)
    for p in patterns:
        res1, c1 = naive_search(txt_large, p)
        res2, c2 = kmp_search(txt_large, p)
        res3, c3 = rabin_karp(txt_large, p)
        print(f"{p:>12} {c1:>10} {c2:>10} {c3:>10}")