def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))


# Define the solution function to find the maximum sum of two numbers
def solution(A):
    digit_sums = {}
    total_sum = -1
    
 # Iterates through each number in the list
    for num in A:
        digit_sum = sum_of_digits(num)
        if digit_sum in digit_sums:
            total_sum = max(total_sum, num + digit_sums[digit_sum])
        else:
            digit_sums[digit_sum] = num
 
# return total sum
    return total_sum   


print(solution([51, 71, 17, 42])) 
print(solution([42, 33, 60]))     
print(solution([51, 32, 43]))      