import inspect
from functools import wraps
from typing import Callable, Any, Union, AsyncGenerator, Generator, List

from python_depends.depends import Depends


async def resolve_dependency(dep: Depends, gens: List[Union[AsyncGenerator, Generator]]):
    value, gen = await dep.resolve()
    gens.append(gen)
    return value


def sync_resolve_dependency(dep: Depends, gens: List[Union[AsyncGenerator, Generator]]):
    value, gen = dep.sync_resolve()
    gens.append(gen)
    return value


def inject_dependencies(func: Callable[..., Any]):
    all_generators = []
    if inspect.iscoroutinefunction(func):

        @wraps(func)
        async def wrapper(*args, **kwargs):
            nonlocal all_generators
            sig = inspect.signature(func)
            dependencies = {
                name: param.default
                for name, param in sig.parameters.items()
                if isinstance(param.default, Depends) and name not in kwargs
            }

            resolved_deps = {}

            for name, dep in dependencies.items():
                resolved_deps[name] = await resolve_dependency(dep, all_generators)

            kwargs.update(resolved_deps)
            if inspect.iscoroutinefunction(func):
                return await func(*args, **kwargs)
            else:
                return func(*args, **kwargs)

        return wrapper
    else:
        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            nonlocal all_generators
            sig = inspect.signature(func)
            dependencies = {
                name: param.default
                for name, param in sig.parameters.items()
                if isinstance(param.default, Depends) and name not in kwargs
            }

            resolved_deps = {}

            for name, dep in dependencies.items():
                resolved_deps[name] = sync_resolve_dependency(dep, all_generators)

            kwargs.update(resolved_deps)
            return func(*args, **kwargs)

        return sync_wrapper
