from typing import List

def check_list_length(enter: str) -> int:
    return len(enter)

def check_absolute(enter: int) -> int:
    return abs(enter)

def sort_words(words: List[str]) -> List[str]:
    words.sort(key=check_list_length, reverse=True)
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=check_absolute, reverse=False)
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
