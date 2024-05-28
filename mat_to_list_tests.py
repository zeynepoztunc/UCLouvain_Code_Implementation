
import unittest

def mat_to_list(adj_mat):
    """ Convert adjacency matrix to an adjacency list representation.

    Args:
        adj_mat (list[list[int]]): A square 0-1 matrix representing the adjacency matrix of the graph.

    Returns:
        list[list[int]]: The adjacency list of the graph.
    """
    adj_list = []
    for _ in range(len(adj_mat)):
        adj_list.append([])

    for i in range(len(adj_mat)):
        for j in range(len(adj_mat[i])):
            if adj_mat[i][j] == 1:
                adj_list[i].append(j)

    return adj_list

class TestMatToList(unittest.TestCase):
    def test_empty_graph(self):
        adj_matrix = []
        expected = []
        result = mat_to_list(adj_matrix)
        self.assertEqual(result, expected, "Failed: Empty graph test")

    def test_graph_with_no_edges(self):
        adj_matrix = [[0, 0], [0, 0]]
        expected = [[], []]
        result = mat_to_list(adj_matrix)
        self.assertEqual(result, expected, "Failed: Graph with no edges test")

    def test_graph_with_single_edge(self):
        adj_matrix = [[0, 1], [0, 0]]
        expected = [[1], []]
        result = mat_to_list(adj_matrix)
        self.assertEqual(result, expected, "Failed: Graph with a single edge test")

    def test_complete_graph(self):
        adj_matrix = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
        expected = [[1, 2], [0, 2], [0, 1]]
        result = mat_to_list(adj_matrix)
        self.assertEqual(result, expected, "Failed: Complete graph test")

    def test_mixed_graph(self):
        adj_matrix = [
            [0, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0]
        ]
        expected = [[1, 3], [2], [0], [4], [5], []]
        result = mat_to_list(adj_matrix)
        self.assertEqual(result, expected, "Failed: Mixed graph test")

if __name__ == '__main__':
    unittest.main()
