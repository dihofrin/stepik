def primes(left, right):
    if left == 1:
        left += 1
    while left <= right:
        if all([left % i for i in range(2, left // 2+1)]):
            yield left
        left += 1

