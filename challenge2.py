def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

# Define the solution function to find the maximum sum of two numbers
def solution(A):
    digit_sums = {}
    max_sum = -1

 