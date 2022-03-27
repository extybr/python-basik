import functools


def singleton(cls):
    """
    Декоратор класса. Имеет только один инстанс.
    :param cls:
    :return:
    """
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton


@singleton
class Example:
    pass


my_object = Example()
my_another_object = Example()

print(id(my_object))
print(id(my_another_object))

print(my_object is my_another_object)
