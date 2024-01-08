import math


def _compute_probability_matrix(matrix):
    prob_matrix = []
    n = len(matrix)
    for row in matrix:
        temp_probs = []
        for value in row:
            temp_probs.append(float(value) / (n - 1))

        prob_matrix.append(temp_probs)

    return prob_matrix


def _compute_entropy_for_row(prob_matrix):
    entropies = []

    for row in prob_matrix:
        h = 0.0
        for value in row:
            if value != 0.0:
                h += -1 * value * math.log2(value)

        entropies.append(h)

    return entropies


def task(matrix):
    prob_matrix = _compute_probability_matrix(matrix)
    entropies = _compute_entropy_for_row(prob_matrix)

    entropy = 0.0
    for value in entropies:
        entropy += value

    return entropy


if __name__ == "__main__":
    matrix_sv = [
        [1, 0, 2, 0, 0],
        [2, 1, 2, 0, 0],
        [2, 1, 0, 1, 1],
        [0, 1, 0, 1, 1],
        [0, 1, 0, 1, 1],
        [0, 1, 0, 1, 1],
    ]

    res = task(matrix_sv)
    print(res)
