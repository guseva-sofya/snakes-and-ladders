from typing import Dict
from snakes_and_ladders import game


def test_game_without_snakes_and_ladders() -> None:
    start = 0
    end = 99
    snakes: Dict[game.Vertex, game.Vertex] = {}
    ladders: Dict[game.Vertex, game.Vertex] = {}

    number_of_steps = game.find_minimum_number_of_steps(start, end, snakes, ladders)

    assert 17 == number_of_steps


def test_game_with_snakes_and_ladders() -> None:
    start = 0
    end = 99
    snakes: Dict[game.Vertex, game.Vertex] = {}
    ladders = {2: 97}

    number_of_steps = game.find_minimum_number_of_steps(start, end, snakes, ladders)

    assert 2 == number_of_steps


def test_game_with_many_snakes_and_ladders():
    start = 0
    end = 99
    snakes = {
        16: 6,
        48: 26,
        49: 11,
        56: 53,
        62: 19,
        64: 60,
        87: 24,
        93: 73,
        95: 75,
        98: 78,
    }
    ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 99}

    number_of_steps = game.find_minimum_number_of_steps(start, end, snakes, ladders)

    assert 7 == number_of_steps
