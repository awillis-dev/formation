def fibonacci(k: int) -> int:
    if k == 0:
        return 0
    if k == 1:
        return 1
    return fibonacci(k-1) + fibonacci(k-2)


# Test Cases
print(fibonacci(0)) # 0
print(fibonacci(1)) # 1
print(fibonacci(10)) # 55
print(fibonacci(20)) # 6765


# Q. Given a target integer k, find the k-th Fibonacci sequence number.

# Examples:
# • Given an integer k: 1 // returns 1
# • Given an integer k: 10 // returns 55