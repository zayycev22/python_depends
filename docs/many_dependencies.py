from python_depends import inject_dependencies, Depends


def injected1():
    return 1


def injected2():
    return 3


@inject_dependencies
def inject_value(value1: int = Depends(injected2), value2: int = Depends(injected1)):
    print(value1 + value2)


if __name__ == "__main__":
    inject_value()
