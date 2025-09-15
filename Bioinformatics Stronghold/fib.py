import sys

def modified_fibonacci(n, k):

    result = {1: 1, 2: 1}
    if n in result:
        return result[n]
    result[n] = modified_fibonacci(n - 1, k) + k * modified_fibonacci(n - 2, k)
    return result[n]


if __name__ == "__main__":
    n, k = [int(x) for x in sys.stdin.read().splitlines()[0].split(" ")]
    print(modified_fibonacci(n, k))