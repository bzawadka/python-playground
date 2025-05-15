
# return first non-repeated character in the string
class Solution:
#      Create a dictionary to store the count of each character
#      if all counts are above 1 => it means that all characters are repeated
#      following the the order of characters, return the first one with a count of 1
    def first_non_repeated(self, s: str) -> str:
        if not s: return ""

        counts = dict()
        for c in s:
            counts[c] = counts[c] + 1 if c in counts.keys() else 1
            #shorter: = counts.get(c, 0) + 1

        if all(counts[k] > 1 for k in counts.keys()):
            return ""

        for c in s:
            if counts[c] == 1:
                return c
