"""
los iteradores son un objeto que se puede iterar o recorrer y permiten un ahorro de memoria
ya que sacan los valores de uno en uno a medida que se necesitan
"""
from typing import Iterator, Generator, Any, Self
import sys


NAMES = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Fred",
    "Ginny",
    "Harriet",
    "Ileana",
    "Joseph",
]


CITIES = [
    "Schenectady",
    "Albany",
]


class ReverseWord:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, word: str):
        self.word = word
        self.index = len(word)

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> str:
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1

        return self.word[self.index]


def reverse_word(word: str) -> Iterator[str]:
    for index in range(len(word) - 1, -1, -1):
        yield word[index]


def reverse(word: str) -> Iterator[str]:
    return (word[index] for index in range(len(word) - 1, -1, -1))


def gen_squares(n: int) -> Iterator[int]:
    i = 1
    while i <= n:
        yield i**2
        i += 1


def main() -> None:
    for i in gen_squares(10):
        print(i)

    print(next(gen_squares(10)))
    print(type(gen_squares(10)))

    iterator_names: Iterator[str] = iter(NAMES)
    try:
        for _ in iterator_names:
            print(next(iterator_names))
    except StopIteration as err:
        print(err)

    print(type(iterator_names))

    cities_iterator: Iterator[str] = iter(CITIES)
    try:
        print(next(cities_iterator))
        print(next(cities_iterator))
        print(next(cities_iterator))
    except StopIteration as err:
        print(err)

    iterator: Generator[int, Any, None] = (i for i in range(1000000))
    iterable = [i for i in range(1000000)]
    print(
        str(sys.getsizeof(iterator)) + " bytes",
        str(sys.getsizeof(iterable)) + " bytes",
    )

    for char in iter(ReverseWord("kevin")):
        print(char)

    for char in reverse_word("kevin"):
        print(char)

    for char in reverse("spam"):
        print(char)

    print(sum(n for n in range(10)))

    xvec = [10, 20, 30]
    yvec = [20, 40, 60]
    print(sum(x * y for x, y in zip(xvec, yvec)))

    word = "golf"
    print(list(word[i] for i in range(len(word) - 1, -1, -1)))


if __name__ == "__main__":
    main()
