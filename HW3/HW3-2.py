import random

try: 
    raise random.choice([ZeroDivisionError, ImportError, KeyError, UnicodeError, StopIteration])
except ZeroDivisionError:
    print('ERROR ZeroDivision')
except KeyError:
    print('ERROR Keyr')
except ImportError:
    print('ERROR Import')
except UnicodeError:
    print('ERROR Unicode')
except StopIteration:
    print('ERROR StopIteration')
# StopIteration это скорее исключение, а не ошибка
