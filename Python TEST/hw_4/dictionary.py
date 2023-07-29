def create_argument_dictionary(**kwargs):
    argument_dict = {}
    for key, value in kwargs.items():
        key_str = str(key) if hashable(key) else repr(key)
        argument_dict[key_str] = value
    return argument_dict

def hashable(obj):
    try:
        hash(obj)
        return True
    except TypeError:
        return False

# Пример использования функции
result = create_argument_dictionary(a=10, b="hello", c=[1, 2, 3], d=3.14)
print(result)
