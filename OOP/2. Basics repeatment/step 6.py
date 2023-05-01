"""
https://stepik.org/lesson/794484/step/6?unit=797232

Функция inversions()
"""

def inversions(sequence):
    count = 0
    for i in range(len(sequence)):
        target = sequence[i]
        for j in range(i+1, len(sequence)):
            if target > sequence[j]:
                count += 1
    return count