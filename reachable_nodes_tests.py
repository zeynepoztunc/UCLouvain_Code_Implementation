
import unittest

def reachable(adj_list, start_node):
    """ Compute the nodes reachable from a start node

    Parameters:
    -----------
    adj_list : the adjacency list of the graph
    start_node: the index of the start node

    Returns:
    --------
    reachable: set(int) the set of nodes reachable from start_node
    """
    if not adj_list or start_node >= len(adj_list) or start_node < 0:
        return set()

    visited = set()  # set of visited nodes
    queue = [start_node]  # initially single element

    while queue:  # while there are vertices in the queue
        current_node = queue.pop(0)  # dequeue, use pop(0) to simulate a queue
        visited.add(current_node)  # the current node is visited
        for adjacent in adj_list[current_node]:
            if adjacent not in visited:  # if the adjacent node is not visited before
                queue.append(adjacent)  # enqueue
    return visited

class TestReachableFunction(unittest.TestCase):
    def test_empty_graph(self):
        adj_list = []
        start_node = 0
        expected = set()
        result = reachable(adj_list, start_node)
        self.assertEqual(result, expected)

    def test_graph_with_no_edges(self):
        adj_list = [[], []]
        start_node = 0
        expected = {0}
        result = reachable(adj_list, start_node)
        self.assertEqual(result, expected)

    def test_graph_with_single_edge(self):
        adj_list = [[1], []]
        start_node = 0
        expected = {0, 1}
        result = reachable(adj_list, start_node)
        self.assertEqual(result, expected)

    def test_complete_graph(self):
        adj_list = [[1, 2], [0, 2], [0, 1]]
        start_node = 0
        expected = {0, 1, 2}
        result = reachable(adj_list, start_node)
        self.assertEqual(result, expected)

    def test_mixed_graph(self):
        adj_list = [
            [1, 3], [2], [0], [4], [], []
        ]
        start_node = 0
        expected = {0, 1, 2, 3, 4}
        result = reachable(adj_list, start_node)
        self.assertEqual(result, expected)

# Running the tests
if __name__ == '__main__':
    unittest.main()