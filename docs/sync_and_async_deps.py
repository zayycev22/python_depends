from python_depends import Depends, inject_dependencies


async def injected():
    return 1


@inject_dependencies
def inject_value(value: int = Depends(injected)):
    print(value)


if __name__ == '__main__':
    inject_value()
