from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from .db import get_session

from python_depends import Depends, inject_dependencies


class TestRepo:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def test_query(self):
        result = self.session.execute(text("SELECT 1"))
        return await result


@inject_dependencies
def get_repo(session: AsyncSession = Depends(get_session)):
    return TestRepo(session)
