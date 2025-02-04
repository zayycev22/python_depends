import asyncio

from python_depends import Depends, inject_dependencies
from .repository import TestRepo, get_repo


@inject_dependencies
async def run_query(repo: TestRepo = Depends(get_repo)):
    data = await repo.test_query()
    print(data)


if __name__ == '__main__':
    asyncio.run(run_query())
