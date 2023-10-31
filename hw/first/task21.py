def solution(number):
    if number < 0:
        return 0

    multiples_sum = 0

    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            multiples_sum += i

    return multiples_sum

print(solution(number=5))
print(solution(number=1))