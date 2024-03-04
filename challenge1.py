def solution(A):
    total_bricks = sum(A)
    box_count = len(A)
    

    if total_bricks % box_count != 0:
        return -1