import math

def minimax(depth, node_index, is_maximizing_player, values):
    if depth == 3:
        return values[node_index]

    if is_maximizing_player:
        best = -math.inf
        for i in range(2): 
            val = minimax(depth + 1, node_index * 2 + i, False, values)
            best = max(best, val)
        return best
    else:
        best = math.inf
        for i in range(2): 
            val = minimax(depth + 1, node_index * 2 + i, True, values)
            best = min(best, val)
        return best

values = [3, 5, 6, 9, 1, 2, 0, -1]

best_score = minimax(0, 0, True, values)

print(f"The optimal value is: {best_score}")



    #             MAX
    #           /     \
    #        MIN       MIN
    #       /   \     /   \
    #     MAX   MAX  MAX   MAX
    #    / \   / \  / \   / \
    #   3  5  6  9  1  2  0  -1
