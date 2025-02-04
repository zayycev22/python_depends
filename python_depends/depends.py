from typing import Callable, TypeVar, AsyncGenerator, Awaitable, Union, Generator
import inspect
import asyncio

T = TypeVar("T")


async def async_anext(generator: AsyncGenerator):
    try:
        return await anext(generator)
    except StopAsyncIteration:
        return None


def sync_next(generator: Generator):
    try:
        return next(generator)
    except StopIteration:
        return None


class Depends:

    def __init__(self,
                 dependency: Callable[..., Union[T, Awaitable[T], AsyncGenerator[T, None], Generator[T, None, None]]]):
        self.dependency = dependency

    async def resolve(self):
        result = self.dependency()

        if inspect.isasyncgen(result):
            gen = result
            return await async_anext(gen), gen
        elif inspect.isgenerator(result):
            gen = result
            return sync_next(gen), gen
        elif inspect.isawaitable(result):
            return await result, None
        else:
            return result, None

    def sync_resolve(self):
        result = self.dependency()
        if inspect.isasyncgen(result):
            gen = result
            return asyncio.run(async_anext(gen)), gen
        elif inspect.isgenerator(result):
            gen = result
            return sync_next(gen), gen
        elif inspect.isawaitable(result):
            return asyncio.run(result), None
        else:
            return result, None

    @staticmethod
    async def cleanup(gen: Union[AsyncGenerator[T, None], Generator[T, None, None], None]):
        if gen is not None:
            try:
                if inspect.isasyncgen(gen):
                    await gen.aclose()
                elif inspect.isgenerator(gen):
                    gen.close()
            except Exception as e:
                raise Exception(f"Error during cleanup: {e}")
