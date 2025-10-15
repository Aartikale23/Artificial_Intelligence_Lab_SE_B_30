# Alpha–Beta Pruning Algorithm
# Author: (Your Name)
# Subject: Artificial Intelligence Lab
# Experiment: Alpha–Beta Pruning Implementation

# Global variable to count the number of nodes evaluated
nodes_evaluated = 0

def alpha_beta(depth, node_index, is_maximizing, values, alpha, beta):
    """
    Performs Alpha–Beta Pruning search.
    :param depth: current depth in the game tree
    :param node_index: current node index
    :param is_maximizing: True if maximizing player's turn
    :param values: leaf node values
    :param alpha: best value that maximizer can guarantee
    :param beta: best value that minimizer can guarantee
    :return: best value for the current player
    """
    global nodes_evaluated
    max_depth = 3  # depth of the tree

    # If we reach a leaf node, return its value
    if depth == max_depth:
        nodes_evaluated += 1
        return values[node_index]

    if is_maximizing:
        best = float('-inf')
        for i in range(2):  # two branches per node
            val = alpha_beta(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            # Beta cut-off
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):  # two branches per node
            val = alpha_beta(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            # Alpha cut-off
            if beta <= alpha:
                break
        return best


# Example leaf values (can be changed for testing)
values = [3, 5, 6, 9, 1, 2, 0, -1]

print("Leaf node values:", values)

# Initialize alpha and beta
alpha = float('-inf')
beta = float('inf')

# Run Alpha–Beta pruning
optimal_value = alpha_beta(0, 0, True, values, alpha, beta)

print("\nOptimal value (with Alpha–Beta Pruning):", optimal_value)
print("Nodes evaluated:", nodes_evaluated)

