#!usr/bin/env python3
# -*- coding: utf-8 -*-


def f(A, B):
    n = len(A)
    A.sort()
    B.sort()
    result = []
    heap = []
    heap.append((A[0] + B[0], 0, 0))

    for _ in range(n**2 - 1):
        sum, i, j = heap.pop(0)
        result.append(sum)
        
        if j < n - 1:
            heap.append((A[i] + B[j+1], i, j+1))

        if j == 0 and i < n - 1:
            heap.append((A[i+1] + B[j], i+1, j))

        heap.sort()

    return result


if __name__ == "__main__":
    A = [2, 4, 8, 6]
    B = [3, 1, 5, 9]
    print(f"А = {A}\nB = {B}")
    print(f"Результат: {f(A, B)}")