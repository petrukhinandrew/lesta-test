from collections import deque


class CircularBuffer:
    def get(self) -> any:
        pass

    def put(self, x: any) -> bool:
        pass

    def size(self) -> int:
        pass

    def __len__(self) -> int:
        return self.size()


class TwoPointerCB(CircularBuffer):
    def __init__(self, capacity: int) -> None:
        assert capacity > 0
        self.__storage = [None for _ in range(capacity + 1)]
        self.__capacity = capacity + 1
        self.__ri = 0
        self.__wi = 0

    def __advance_ri(self):
        self.__ri = (self.__ri + 1) % self.__capacity

    def __advance_wi(self):
        self.__wi = (self.__wi + 1) % self.__capacity

    def get(self) -> any:
        if self.__ri == self.__wi:
            return None
        res = self.__storage[self.__ri]
        self.__advance_ri()
        return res

    def put(self, x: any) -> bool:
        if (self.__wi + 1) % self.__capacity == self.__ri:
            return False
        self.__storage[self.__wi] = x
        self.__advance_wi()
        return True

    def size(self) -> int:
        delta = self.__wi - self.__ri
        if delta < 0:
            delta += self.__capacity
        return delta


class DequeCB(CircularBuffer):
    def __init__(self, capacity: int) -> None:
        self.__storage = deque(maxlen=capacity)
        self.__capacity = capacity

    def get(self) -> any:
        if len(self.__storage) == 0:
            return None

        return self.__storage.pop()

    def put(self, x: any) -> bool:
        if len(self.__storage) == self.__capacity:
            return False
        self.__storage.appendleft(x)
        return True

    def size(self) -> int:
        return len(self.__storage)


def test_buf(buf: CircularBuffer, capacity: int) -> None:
    assert buf1.get() is None, "buffer must be empty here"
    for _ in range(3):
        for i in range(1, capacity + 1):
            assert buf1.put(i), "unexpected overflow"
            assert (s := buf1.size()) == i, "expected size {i}, got {s}".format(
                i=i, s=s
            )
        assert not buf1.put(0), "expected overflow"
        for i in range(1, capacity + 1):
            assert (cur := buf1.get()) == i, "expected {i}, got {cur}".format(
                i=i, cur=cur
            )
            assert (
                s := buf1.size()
            ) == capacity - i, "expected size {i}, got {s}".format(i=i, s=s)
    assert buf1.get() is None, "buffer must be empty here"


if __name__ == "__main__":
    buf_len = 3
    
    buf1 = TwoPointerCB(buf_len)
    test_buf(buf1, buf_len)

    buf2 = DequeCB(buf_len)
    test_buf(buf2, buf_len)
