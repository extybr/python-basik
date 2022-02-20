from collections.abc import Iterable


def sequence(numbers: list) -> Iterable[list]:
    if numbers == [1, 2]:
        raise BaseException('завершение')
    if numbers[0] == 1 or numbers[1] == 1:
        q_sequence = numbers
        for _ in range(2, 74):
            q_hofstadter = numbers[-numbers[-1]] + numbers[-numbers[-2]]
            q_sequence.append(q_hofstadter)
            yield q_sequence
    return


[print(index) for index in sequence([1, 1])]
