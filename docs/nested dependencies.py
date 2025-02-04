from python_depends import Depends, inject_dependencies


def injected1():
    return 1


@inject_dependencies
def injected2(value: int = Depends(injected1)):
    new_value = 3
    return new_value + value


@inject_dependencies
def inject_value(value: int = Depends(injected2)):
    print(value)


if __name__ == '__main__':
    inject_value()
