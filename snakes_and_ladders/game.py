from dataclasses import dataclass
from queue import Queue
from typing import List, Dict, Set


Vertex = int


@dataclass
class QueueItem:
    """ """

    vertex: Vertex
    distance_to_start: int


def find_minimum_number_of_steps(
    start: Vertex,
    end: Vertex,
    snakes: Dict[Vertex, Vertex],
    ladders: Dict[Vertex, Vertex],
) -> int:
    """Finds a minimum number of steps in order to get to the end vertex. Uses
    breadth first search algorithm.

    Args:

    Returns:

    """

    queue: Queue[QueueItem] = Queue()
    queue.put(QueueItem(start, 0))
    visited_vertices: Set[Vertex] = set()

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

    raise Exception(
        "Could not find shortest path from start to end: this can happen if there is no path between start and end."
    )


def find_neighbors(
    current_vertex: Vertex,
    end_vertex: Vertex,
    snakes: Dict[Vertex, Vertex],
    ladders: Dict[Vertex, Vertex],
) -> List[Vertex]:
    neighbors: List[Vertex] = []
    for index in range(1, 7):
        potential_neighbor = current_vertex + index

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
