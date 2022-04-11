from collections import Counter

if __name__ == '__main__':
    def can_be_poly(string: str) -> bool:
        """
        Функция проверяет, можно ли получить из строки палиндром
        :param string: str
        :return: bool
        """
        return len(list(filter(lambda x: x % 2, Counter(string).values()))) <= 1


    text_1 = can_be_poly('ababc')
    text_2 = can_be_poly('abbbc')
    print(text_1)
    print(text_2)

    # with open('README.md', 'r', encoding='utf-8') as text:
    #     result = Counter(text.read().strip()).most_common(100)
    #     print(result)
