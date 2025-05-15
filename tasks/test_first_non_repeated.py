from first_non_repeated import *

def test_first_non_repeated():
    s = Solution()
    assert s.first_non_repeated("") == ""
    assert s.first_non_repeated("!") == "!"
    assert s.first_non_repeated("total") == "o"
    assert s.first_non_repeated("teeter") == "r"
    assert s.first_non_repeated("Bartek") == "B"


def test_first_non_repeated_all_repeated():
    s = Solution()
    assert s.first_non_repeated("aabbcc") == ""
    assert s.first_non_repeated("aabbccddeeff") == ""


if __name__ == "__main__":
    test_first_non_repeated()
    print("All tests passed.")