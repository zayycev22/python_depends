# python_depends

**python_depends** is a dependency injection library inspired by the `Depends` mechanism from FastAPI. It supports both asynchronous and synchronous functions, providing flexibility and ease of use.

## Installation

```bash
pip install depends_python
```

## Key Features

- Support for synchronous and asynchronous functions.
- Simple dependency annotation using the `@inject_dependencies` decorator.
- Support for nested dependencies.
- Ability to mix synchronous and asynchronous dependencies.

## Usage Examples

### Asynchronous Functions

```python
from python_depends import Depends, inject_dependencies
import asyncio

async def injected():
    return 1

@inject_dependencies
async def inject_value(value: int = Depends(injected)):
    print(value)

if __name__ == '__main__':
    asyncio.run(inject_value())
```

### Basic Example

```python
from python_depends import Depends, inject_dependencies

# Function to inject
def get_value():
    return 1

@inject_dependencies  # inject dependencies
def test_injection(value: int = Depends(get_value)):
    print(value)

if __name__ == '__main__':
    test_injection()
```

### Multiple Dependencies

```python
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
```

### Nested Dependencies

```python
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
```

### Mixing Synchronous and Asynchronous Dependencies

```python
from python_depends import Depends, inject_dependencies

async def injected():
    return 1

@inject_dependencies
def inject_value(value: int = Depends(injected)):
    print(value)

if __name__ == '__main__':
    inject_value()
```

## License

MIT License.

---

The **python_depends** library is designed to simplify the dependency injection process and make code cleaner and easier to test.

The name of package is **depends_python** because **python_depends** is already in use