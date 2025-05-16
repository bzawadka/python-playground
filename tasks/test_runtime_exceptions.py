import pytest

class MyTest:
    def do_with_side_effects(self, input: int) -> int:
        if input % 2 == 0:
            raise RuntimeError("I don't like this number")
        return input


def test_exception_catching():
    mt = MyTest()

    with pytest.raises(RuntimeError, match="^[^\\d]+$"):
        mt.do_with_side_effects(4)

    assert mt.do_with_side_effects(33) == 33    


if "__name__" == "__main__":
    test_exception_catching()
    print('this is done')