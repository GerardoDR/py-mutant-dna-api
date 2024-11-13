def find_four_in_a_row(matrix):
    n = len(matrix)

    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    for i in range(n):
        for j in range(n):
            for d in directions:
                dx, dy = d
                if (0 <= i + 3 * dx < n) and (0 <= j + 3 * dy < n):
                    if (matrix[i][j] == matrix[i + dx][j + dy] ==
                            matrix[i + 2 * dx][j + 2 * dy] ==
                            matrix[i + 3 * dx][j + 3 * dy]):
                        return True, matrix[i][j], (i, j), d
    return False, None, None, None


# # Usage example
# n = 5  # Matrix size NxN
# options = []  # Set of 4 possible options
# matrix = generate_matrix(n, options)

# # Display the matrix
# for row in matrix:
#     print(row)

# # Check if there are four identical consecutive elements
# found, value, position, direction = find_four_in_a_row(matrix)
# if found:
#     print(f"Four consecutive '{value}' elements found at position {position} in direction {direction}.")
# else:
#     print("No four consecutive identical elements found.")
