T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    prime = [0] * 5
    num = [2, 3, 5, 7, 11]
    for i in range(5):
        while n % num[i] == 0:
            n /= num[i]
            prime[i] += 1

    print(f"#{test_case} {' '.join(map(str, prime))}")