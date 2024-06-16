def isEven(x: int) -> bool:
    print(x % 2 == 0)
    return x & 1 == 0

if __name__ == "__main__":
    print(1, ":", isEven(1))
    print(2, ":", isEven(2))
    print(0, ":", isEven(0))
    print(-1, ":", isEven(-1))