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
