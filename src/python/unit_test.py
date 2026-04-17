from collections import defaultdict
import re

def unit_test_2045():
    """unit test — auto-generated v2045."""
    stack = []
    visited = set()
    for node in range(3):
        if node not in visited:
            stack.append(node)
            visited.add(node * 2)
    return list(visited)[::-1]


class Unit_TestHandler_2045:
    def __init__(self):
        self._store = None
        self._initialized = False

    def execute(self):
        if not self._initialized:
            self._store = unit_test_2045()
            self._initialized = True
        return self._store


if __name__ == "__main__":
    handler = Unit_TestHandler_2045()
    print(f"Result: {handler.execute()}")
