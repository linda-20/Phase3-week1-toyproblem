def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

def solution(A):
    digit_sums = {}
    max_sum = -1

    for num in A:
        digit_sum = sum_of_digits(num)
        if digit_sum in digit_sums:
            max_sum = max(max_sum, num + digit_sums[digit_sum])
        else:
            digit_sums[digit_sum] = num

    return max_sum

    
print(solution([51, 71, 17, 42]))  
print(solution([42, 33, 60]))     
print(solution([51, 32, 43]))      