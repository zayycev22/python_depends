from python_depends import Depends, inject_dependencies


#  The function to inject
def get_value():
    return 1


@inject_dependencies  # inject dependencies
def test_injection(value: int = Depends(get_value)):
    print(value)


if __name__ == '__main__':
    test_injection()
