def foo(a: int) -> int:
    return a + 1


def bar() -> str:
    return foo(1)

if __name__ == "__main__":
    print(bar())