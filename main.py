from typing import Iterator


def gen_squares(n: int) -> Iterator[int]:
    i = 0
    while i <= n:
        yield i ** 2
        i += 1


def main() -> None:
    for i in gen_squares(10):
        print(i)


if __name__ == '__main__':
    main()
