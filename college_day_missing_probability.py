class AttendClass:

    def valid_ways_to_attend_classes(self, N: int) -> int:
        if N < 2:
            return 2 ** N
        if N == 2:
            return 3

        prev1 = 2
        prev2 = 3

        for i in range(3, N + 1):
            current = prev1 + prev2
            prev1, prev2 = prev2, current

        return current


def ways_to_miss_graduation_ceremony(self, N: int) -> int:
    if N < 2:
        return 2 ** (N - 1)
    if N == 2:
        return 2

    prev1 = 1
    prev2 = 1

    for i in range(3, N + 1):
        current = prev1 + prev2
        prev1, prev2 = prev2, current  

    return current


if __name__ == "__main__":
    n = 5
    obj = AttendClass()
    total_ways = obj.valid_ways_to_attend_classes(n)
    ways_missed = obj.ways_to_miss_graduation_ceremony(n)
    print(total_ways)
    print(f"{ways_missed}/{total_ways}")
