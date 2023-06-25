from dataclasses import dataclass
from queue import Queue
from typing import List, Dict, Set


# introduce new type type to use for vertices instead of raw ints
Vertex = int


@dataclass
class QueueItem:
    vertex: Vertex
    distance_to_start: int


def find_minimum_number_of_steps(
    start: Vertex,
    end: Vertex,
    snakes: Dict[Vertex, Vertex],
    ladders: Dict[Vertex, Vertex],
) -> int:
    """Finds a minimum number of steps in order to get to the end vertex using
    breadth first search algorithm.

    Args:
        start: An integer defined as type Vertex represents a start vertex.
        end: An integer defined as type Vertex represents an end vertex.
        snakes: A dictionary representing snakes in the game: the keys and the values
        correspond to the vertices.
        ladders: A dictionary representing ladders in the game: the keys and the values
        correspond to the vertices.

    Returns:
        current_item.distance_to_start: An integer which represents number of
        turns in order to end the game.

    Raises:
        RuntimeError: Appears in case if there is no path between start and end.
    """

    queue: Queue[QueueItem] = Queue()
    queue.put(QueueItem(start, 0))
    visited_vertices: Set[Vertex] = set()

    # Breadth-first search algorithm
    while not queue.empty():
        current_item = queue.get()
        if current_item.vertex not in visited_vertices:
            if current_item.vertex == end:
                return current_item.distance_to_start

            visited_vertices.add(current_item.vertex)

            neighbors: List[Vertex] = find_neighbors(
                current_item.vertex, end, snakes, ladders
            )
            for neighbor in neighbors:
                if neighbor not in visited_vertices:
                    queue.put(QueueItem(neighbor, current_item.distance_to_start + 1))

    raise RuntimeError(
        "Could not find shortest path from start to end: this can happen if \
        there is no path between start and end."
    )


def find_neighbors(
    current_vertex: Vertex,
    end_vertex: Vertex,
    snakes: Dict[Vertex, Vertex],
    ladders: Dict[Vertex, Vertex],
) -> List[Vertex]:
    """Finds neighbors of the current vertex. There are maximum six neighbors as
    we have a six-sided die. If neighbor vertex transfers to the snake tail or ladder top,
    function replaces the vertex with the corresponding vertex from snakes
    or ladders dictionary.

    Args:
        current_vertex: An integer that represents the current vertex.
        end_vertex:  An integer that represents the end vertex.
        ...
    Returns:
        neighbors: A list of neighbors for a current vertex.
    """

    neighbors: List[Vertex] = []

    for index in range(1, 7):
        potential_neighbor = current_vertex + index

        # go to the next iteration (in order not to add neighbors to the list)
        if potential_neighbor > end_vertex:
            continue

        if potential_neighbor in snakes:
            snake_tail = snakes[potential_neighbor]
            neighbors.append(snake_tail)
        elif potential_neighbor in ladders:
            ladder_top = ladders[potential_neighbor]
            neighbors.append(ladder_top)
        else:
            neighbors.append(potential_neighbor)

    return neighbors
