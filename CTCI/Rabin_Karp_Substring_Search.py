import psutil
import timeit
import subprocess
import os
from sys import argv


class Solution:
    def search(self, txt, pat):
        # solution 1: sliding window
        # O(txt)
        if len(txt) < len(pat):
            return 0
        a = 0
        b = len(pat)
        result = []

        while b < len(txt):
            if txt[a: b] == pat:
                result.append(a)
                a = b
                b = b + len(pat)
            else:
                a += 1
                b += 1
        return result

    def rabin_karp_search(self, txt, pat, d, q):
        M = len(pat)
        N = len(txt)
        t = 0
        p = 0
        h = pow(d, M - 1) % q
        result = []
        for i in range(M):
            p = (d * p + ord(pat[i])) % q
            t = (d * t + ord(txt[i])) % q

        print(p, t)
        for s in range(N - M + 1):
            if p == t:
                match = True
                for j in range(M):
                    if pat[j] != txt[s + j]:
                        match = False
                        break
                if match:
                    result.append(s)
            if s < N-M:
                t = (t - h * ord(txt[s])) % q  # remove letter s
                # print(t)
                t = (d * t + ord(txt[s + M])) % q  # add letter s+M
                t = (t + q) % q
                # print(t)
        return result


def ps_stat():
    #global process_size
    ps = psutil.Process(os.getpid())
    # print(ps.memory_full_info().uss)  # in bytes
    process_size = ps.memory_full_info().uss
    return process_size


# print(process.memory_percent())


def main(loop_count):
    #global process_size
    start = timeit.timeit()
    txt = "GEEKS FOR GEEKS"

    pat = "GEEK"
    sol = Solution()
    print(sol.rabin_karp_search(txt, pat, 256, 11))
    end = timeit.timeit()
    #print("method", num)
    print("time", float((end-start) / 1000000))
    #print("output size ", len(num) / 1024, "kb")
    print("process size", ps_stat()/1024, "kb")
    # print()


loop_count = 500000
# pid = os.getpid()
# print(pid)
main(loop_count)
