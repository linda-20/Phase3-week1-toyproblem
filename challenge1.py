def solution(A):
    total_bricks = sum(A)
    box_count = len(A)
    

    if total_bricks % box_count != 0:
        return -1

         # Calculate the target number of bricks per box
    target_bricks = total_bricks // box_count
    moves = 0

# Iterating over all boxes except the last one
    for i in range(box_count - 1):  
        bricks_needed = target_bricks - A[i]
        A[i] += bricks_needed
        A[i + 1] -= bricks_needed  # Adjusts the next box
        moves += abs(bricks_needed)
    
    return moves

# Test cases
print(solution([7, 15, 10, 8]))  # Output: 7
print(solution([11, 10, 8, 12, 8, 10, 11]))  # Output: 6
print(solution([7, 14, 10]))  # Output: -1