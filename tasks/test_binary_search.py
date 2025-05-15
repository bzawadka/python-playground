
class BinarySearch:
    def binary_search(self, arr: list[int], target: int) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            guess = arr[mid]
            if guess == target:
                return mid
            elif guess > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
    

def test_binary_search():
    bs = BinarySearch()
    assert bs.binary_search([2, 5, 7, 9, 10, 15, 20, 30, 50, 70, 100, 190, 990], 5) == 1
    assert bs.binary_search([5, 7, 9, 15, 20, 30], 15) == 3
    assert bs.binary_search([1, 2, 3, 4, 5], 5) == 4
    assert bs.binary_search([1, 2, 3, 4, 5], 1) == 0


def test_binary_search_edge_cases():
    bs = BinarySearch()
    assert bs.binary_search([], 1) == -1
    assert bs.binary_search([42], 42) == 0
    assert bs.binary_search([42, 46, 48], 33) == -1
    assert bs.binary_search([42, 46, 48], 3) == -1
    assert bs.binary_search([42, 46, 48], 3333) == -1
    assert bs.binary_search(list(range(1000)), 999) == 999
    assert bs.binary_search(list(range(1000)), 1001) == -1


if __name__ == "__main__":
    test_binary_search()
    print("all tests run")  