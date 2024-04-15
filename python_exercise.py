def type_inspector(obj):
    if isinstance(obj, tuple):
        print('is immutable')
    elif isinstance(obj, int):
        print('is immutable')
    elif isinstance(obj, float):
        print('is immutable')
    elif isinstance(obj, complex):
        print('is immutable')
    elif isinstance(obj, bool):
        print('is immutable')
    elif isinstance(obj, str):
        print('is immutable')
    else: 
        print('is mutable')
print(type(1.))
    