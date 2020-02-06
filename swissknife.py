#!/usr/bin/env/python3.6
# _*_import: utf-8 _*_
# Please, do not forget try comment and document under pep8.
# https://www.python.org/dev/peps/pep-0008/
_author_ = 'Marco Baturan'
_date_ = '05/02/2020'
# imports
from re import sub
from math import ceil
from functools import reduce

"""Put here the documentation. TODO:... Follow PEP8. """  # Documentation
# https://devguide.python.org/documenting/ 
# gobal vars
# class
#   init function
#   class inner function
# heritage class
#   heritage class functions
def is_lower_case(string):
    """is_lower_case

    Checks if a string is lower case.
    Convert the given string to lower case,
    using str.lower() method and compare
    it to the original.
    
    """
    return string == string.lower()

def keys_only(flat_dict):
    """keys_only

        Function which accepts a dictionary of
        key value pairs and returns a new flat
        list of only the keys.

        Uses the .items() function with a for
        loop on the dictionary to track both the
        key and value and returns a new list by
        appending the keys to it. Best used on 1
        level-deep key:value pair dictionaries
        (a flat dictionary) and not nested data-structures
        which are also commonly used with dictionaries.
        (a flat dictionary resembles a json and a flat
        list an array for javascript people).

    """
    lst = []
    for k, v in flat_dict.items():
        lst.append(k)
    return lst

def all_equal(lst):
    """

        Checks if all elements in a list are equal.

        Use [1:] and [:-1] to compare all the values in the given list.
    """
    return lst[1:] == lst[:-1]

def all_unique(lst):
    """
        Returns True if all the values in a list are unique,
        False otherwise.

        Use set() on the given list to remove duplicates,
        use len() to compare its length with the length of the list.
    """
    return len(lst) == len(set(lst))

def average(*args):
    """
        Returns the average of two or more numbers.

        Use sum() to sum all of the args provided,
        divide by len(args).
    """
    return sum(args, 0.0) / len(args)

def average_by(lst, fn=lambda x: x):
    """
        Returns the average of a list, after mapping
        each element to a value using the provided function.

        Use map() to map each element to the value returned
        by fn. Use sum() to sum all of the mapped values,
        divide by len(lst).
        average_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda x: x['n']) # 5.0
    """
    return sum(map(fn, lst), 0.0) / len(lst)

def bifurcate(lst, filter):
    """
        Splits values into two groups. If an element in filter
        is True, the corresponding element in the collection belongs
        to the first group; otherwise, it belongs to the second group.

        Use list comprehension and enumerate() to add elements to groups,
        based on filter. Example:
        bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True]) # [ ['beep', 'boop', 'bar'], ['foo'] ]
    """
    return [
        [x for i, x in enumerate(lst) if filter[i] == True],
        [x for i, x in enumerate(lst) if filter[i] == False]]

def bifurcate_by(lst, fn):
    """
        Splits values into two groups according to a function,
        which specifies which group an element in the input list
        belongs to. If the function returns True, the element
        belongs to the first group; otherwise, it belongs to the
        second group.

        Use list comprehension to add elements to groups,
        based on fn.
        bifurcate_by(
          ['beep', 'boop', 'foo', 'bar'], 
          lambda x: x[0] == 'b'
        ) # [ ['beep', 'boop', 'bar'], ['foo'] ]
    """
    return [
        [x for x in lst if fn(x)],
        [x for x in lst if not fn(x)]]

def byte_size(s):
    """
        Returns the length of a string in bytes.

        Use s.encode('utf-8') to encode the given
        string and return its length.
    """
    return len(s.encode('utf-8'))

def camel(s):
    """
    Converts a string to camelcase.

    Use re.sub() to replace any - or _ with a space,
    using the regexp r"(_|-)+". Use title() to capitalize
    the first letter of each word convert the rest to lowercase.
    Finally, use replace() to remove spaces between words.
    """
    s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
    return s[0].lower() + s[1:]

def capitalize(s, lower_rest=False):
    """
        Capitalizes the first letter of a string.

        Capitalize the first letter of the string and
        then add it with rest of the string. Omit the
        lower_rest parameter to keep the rest of the
        string intact, or set it to True to convert to lowercase.
    """
    return s[:1].upper() + (s[1:].lower() if lower_rest else s[1:])

def capitalize_every_word(s):
    """
        Capitalizes the first letter of every word in a string.

        Use s.title() to capitalize first letter of every word
        in the string.
    """
    return s.title()

def cast_list(val):
    """
        Casts the provided value as a list if it's not one.

        Use isinstance() to check if the given value is
        enumerable and return it by using list() or encapsulated
        in a list accordingly.
    """
    return list(val) if isinstance(val, (tuple, list, set, dict)) else [val]

def check_prop(fn, prop):
    """
        Given a predicate function, fn, and a prop string,
        this curried function will then take an object to
        inspect by calling the property and passing it to
        the predicate.

        Return a lambda function that takes an object and
        applies the predicate function, fn to the specified
        property.
        Example:
            check_age = check_prop(lambda x: x >= 18, 'age')
            user = {'name': 'Mark', 'age': 18}

            check_age(user) # True
    """
    return lambda obj: fn(obj[prop])

def chunk(lst, size):
    """Chunks a list into smaller lists of a specified size.

        Use list() and range() to create a list of the desired
        size. Use map() on the list and fill it with splices of
        the given list. Finally, return the created list.
    """
    return list(
        map(lambda x: lst[x * size:x * size + size],
            list(range(0, ceil(len(lst) / size)))))

def working_memory(lista):
    """Optimal working memory.

        Working memory divide a large
        list into smaller list based
        in own metric.
        
        it's inspired in human working memory.
        Where the proccesor takes an argument
        like a list, and based in the length
        it self then take one or other metric
        for divide the main block in smaller
        chunks.
        
    """
    buffer = []
    if len(lista) <= 50:
        opr = 50
        block = opr // 10
        result = chunk(lista, block)

    if len(lista)<255:
        opr = len(lista) - 100
        block = opr // 10
        result = chunk(lista, block)

    if len(lista) > 255:
        opr = len(lista) - 255
        block = opr // 10
        result = chunk(lista, block)

    for iteration in range(len(result)):
        line = ';{};'.format(len(result[iteration]))
        line += ';'.join(result[iteration])
        buffer.append(line)

    return buffer

def clamp_number(num,a,b):
    """
        Clamps num within the inclusive range specified
        by the boundary values a and b.

        If num falls within the range, return num.
        Otherwise, return the nearest number in the range.
        
    """
    return max(min(num, max(a, b)), min(a, b))

def compact(lst):
    """Removes falsey values from a list.

        Use filter() to filter out falsey
        values (False, None, 0, and "").
        
    """
    return list(filter(bool, lst))



def compose(*fns):
    """Performs right-to-left function composition.

        Use functools.reduce() to perform right-to-left
        function composition. The last (rightmost) function
        can accept one or more arguments; the remaining
        functions must be unary.
        Example:
            add5 = lambda x: x + 5
            multiply = lambda x, y: x * y
            multiply_and_add_5 = compose(add5, multiply)

            multiply_and_add_5(5, 2) # 15
    """
    return reduce(lambda f, g: lambda *args: f(g(*args)), fns)


def compose_right(*fns):
    """Performs left-to-right function composition.

    Use functools.reduce() to perform left-to-right
    function composition. The first (leftmost) function
    can accept one or more arguments; the remaining
    functions must be unary.
    
    Example:
        add = lambda x, y: x + y
        square = lambda x: x * x
        add_and_square = compose_right(add,square)

        add_and_square(1, 2) # 9
    
    """
    return reduce(lambda f, g: lambda *args: g(f(*args)), fns)

def count_by(arr, fn=lambda x: x):
    """from math import floor
        count_by([6.1, 4.2, 6.3], floor) # {6: 2, 4: 1}
        count_by(['one', 'two', 'three'], len) # {3: 2, 5: 1}
    """
    key = {}
    for el in map(fn, arr):
        key[el] = 1 if el not in key else key[el] + 1
    return key

def count_occurrences(lst, val):
    """Counts the occurrences of a value in a list.

        Increment a counter for every item in the
        list that has the given value and is of the same type.
    """
    return len([x for x in lst if x == val and type(x) == type(val)])

from functools import partial

def curry(fn, *args):
    """Curries a function.

        Use functools.partial() to return a new partial
        object which behaves like fn with the given arguments,
        args, partially applied.
        
        add = lambda x, y: x + y
        add10 = curry(add, 10)

        add10(20) # 30
        
    """
    
    return partial(fn,*args)

if __name__ == "__main__":
    # Erase pass and call class or functions here.
    pass
