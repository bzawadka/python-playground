# cards are from 1 to 10
# I receive 9 random cards, e.g. 1 2 3 4 5 8 9 10 1
#                                2 4 1 4 5 8 9 10 1
# question: do I have a pair?
#           do I have w trio?

from typing import Counter


def is_pair_in_the_deck(deck: list[int]) -> bool:
    card_counts = {-1: -1}
    for c in deck:
        card_counts[c] = card_counts.get(c, 0) + 1

    for _, v in card_counts.items():
        if v == 2:
            return True

    return False


def is_trio_in_the_deck(deck: list[int]) -> bool:
    card_counts = {-1: -1}
    for c in deck:
        card_counts[c] = card_counts.get(c, 0) + 1

    return any(v == 3 for _, v in card_counts.items())


def is_quad_in_the_deck(deck: list[int]) -> bool:
    card_counts = Counter(deck)
    return any(v == 4 for _, v in card_counts.items())


def test_cards_pairs():
    assert is_pair_in_the_deck([1, 2, 3, 4, 5, 8, 9, 10, 6]) is False
    assert is_pair_in_the_deck([1, 2, 3, 2, 5, 8, 9, 10, 1]) is True
    assert is_pair_in_the_deck([1, 2, 3, 2, 5, 8, 8, 10, 1]) is True
    assert is_pair_in_the_deck([1, 1, 1, 1, 1, 1, 1, 1, 1]) is False


def test_cards_trios():
    assert is_trio_in_the_deck([1, 2, 3, 4, 5, 8, 9, 10, 6]) is False
    assert is_trio_in_the_deck([1, 2, 3, 2, 5, 8, 9, 10, 2]) is True
    assert is_trio_in_the_deck([1, 2, 3, 2, 5, 3, 8, 3, 1]) is True
    assert is_trio_in_the_deck([1, 1, 1, 1, 1, 1, 1, 1, 1]) is False


def test_cards_quads():
    assert is_quad_in_the_deck([1, 2, 3, 4, 5, 8, 9, 10, 6]) is False
    assert is_quad_in_the_deck([1, 2, 3, 2, 5, 8, 2, 10, 2]) is True
    assert is_quad_in_the_deck([3, 2, 3, 2, 5, 3, 8, 3, 1]) is True
    assert is_quad_in_the_deck([1, 1, 1, 1, 1, 1, 1, 1, 1]) is False
