from python_depends import Depends, inject_dependencies
import asyncio


async def injected():
    return 1


@inject_dependencies
async def inject_value(value: int = Depends(injected)):
    print(value)


if __name__ == '__main__':
    asyncio.run(inject_value())
