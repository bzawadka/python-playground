from solution import *


def test_init_solution():
    s = Solution()
    assert s.hello() == 'hello, world'


if __name__ == "__main__":
    test_init_solution()
    print("All tests passed.")