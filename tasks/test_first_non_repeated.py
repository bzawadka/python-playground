# return first non-repeated character in the string
class Solution:
    input_string_empty, all_characters_repreated = '', ''

    def first_non_repeated(self, input_str: str) -> str:
        if not input_str: return self.input_string_empty

        char_counts = dict()
        for c in input_str:
            char_counts[c] = char_counts[c] + 1 if c in char_counts else 1 

        if all(char_counts[c] > 1 for c in char_counts):
            return self.all_characters_repreated

        first_non_repeated = ''
        for c in input_str:
            if char_counts[c] == 1:
                first_non_repeated = c
                break

        return first_non_repeated


def test_first_non_repeated():
    s = Solution()
    assert s.first_non_repeated("") == ""
    assert s.first_non_repeated("!") == "!"
    assert s.first_non_repeated("alalp") == "p"
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