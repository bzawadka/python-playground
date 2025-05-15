

class Solution:
    def remove_chars(self, text: str, chars_to_remove: str) -> str:
        to_remove = set(chars_to_remove)
        result = []
        for c in text:
            if c not in to_remove:
                result.append(c)
        return "".join(result)


    def remove_chars_short(self, text: str, chars_to_remove: str) -> str:
        to_remove = set(chars_to_remove)
        return "".join([c for c in text if c not in to_remove])    


    def remove_chars_in_place(self, text: str, chars_to_remove: str) -> str:
        to_remove = set(chars_to_remove)
        text_as_list = list(text)
        dst = 0
        new_length = 0
        for i, c in enumerate(text):
            if c not in to_remove:
                text_as_list[dst] = text_as_list[i]
                dst += 1
                new_length += 1
        return "".join(text_as_list[0:new_length])
        


def test_remove_chars():
    sol = Solution()
    assert sol.remove_chars("Hello, World", "eod") == "Hll, Wrl"
    assert sol.remove_chars("Battle of the Vowels: Hawaii vs. Grozny", "aeiou") == "Bttl f th Vwls: Hw vs. Grzny"


def test_remove_chars_short():
    sol = Solution()
    assert sol.remove_chars_short("Hello, World", "eod") == "Hll, Wrl"
    assert sol.remove_chars_short("Battle of the Vowels: Hawaii vs. Grozny", "aeiou") == "Bttl f th Vwls: Hw vs. Grzny"


def test_remove_chars_in_place():
    sol = Solution()
    assert sol.remove_chars_in_place("Hello, World", "eod") == "Hll, Wrl"


if __name__ == "__main__":
    test_remove_chars()
    print('all run')