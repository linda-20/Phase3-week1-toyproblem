def solution(N):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    repetitions = N // 26
    remainder = N % 26
    
    result = ''
    
    # Iterate over the alphabet to construct the result string
    for i in range(repetitions):
        result += alphabet
    result += alphabet[:remainder]
    
     # Return the resulting string
    return ''.join(result[:N])
    