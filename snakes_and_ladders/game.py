from dataclasses import dataclass
from queue import Queue
from typing import List, Dict, Set


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
                current_item.vertex, snakes, ladders
            )
            for neighbor in neighbors:
                if neighbor not in visited_vertices:
                    queue.put(QueueItem(neighbor, current_item.distance_to_start + 1))

    raise Exception(
        "Could not find shortest path from start to end: this can happen if there is no path between start and end."
    )


def find_neighbors(
    current_vertex: Vertex, snakes: Dict[Vertex, Vertex], ladders: Dict[Vertex, Vertex]
) -> List[Vertex]:
    return []
