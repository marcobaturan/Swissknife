#!/usr/bin/env/python3.6
# _*_import: utf-8 _*_
# Please, do not forget try comment and document under pep8.
# https://www.python.org/dev/peps/pep-0008/
# https://github.com/Xiams1921/how_to_think_like_a_computer_scientist_learning_with_python_3
_author_ = 'Marco Baturan'
_date_ = '05/02/2020'
import math
import re
from copy import deepcopy
from functools import partial, reduce
from math import ceil
from random import randint
from re import sub


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

    if len(lista) < 255:
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


def clamp_number(num, a, b):
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


def curry(fn, *args):
    """Curries a function.

        Use functools.partial() to return a new partial
        object which behaves like fn with the given arguments,
        args, partially applied.
        
        add = lambda x, y: x + y
        add10 = curry(add, 10)

        add10(20) # 30
        
    """

    return partial(fn, *args)


def decapitalize(string, upper_rest=False):
    """
    Decapitalizes the first letter of a string.

    Decapitalize the first letter of the string and then add it with rest of the string. Omit the upper_rest parameter to keep the rest of the string intact, or set it to True to convert to uppercase.
    """
    return str[:1].lower() + (str[1:].upper() if upper_rest else str[1:])


def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


def deep_flatten(lst):
    """
    Deep flattens a list.

    Use recursion. Define a function, spread, that uses either list.extend() or list.append() on each element in a list to flatten it. Use list.extend() with an empty list and the spread function to flatten a list. Recursively flatten each element that is a list.
    """

    result = []
    result.extend(
        spread(list(map(lambda x: deep_flatten(x) if type(x) == list else x, lst))))
    return result


def difference(a, b):
    """
    Returns the difference between two iterables.

    Create a set from b, then use list comprehension on a to only keep values not contained in the previously created set, _b.
    """

    _b = set(b)
    return [item for item in a if item not in _b]


def difference_by(a, b, fn):
    """
    Returns the difference between two lists, after applying the provided function to each list element of both.

    Create a set by applying fn to each element in b, then use list comprehension in combination with fn on a to only keep values not contained in the previously created set, _b.
    """

    _b = set(map(fn, b))

    return [item for item in a if fn(item) not in _b]


def digitize(n):
    """
    Converts a number to an array of digits.

    Use map() combined with int on the string representation of n and return a list from the result.
    """

    return list(map(int, str(n)))


def every(lst, fn=lambda x: x):
    """
    Returns True if the provided function returns True for every element in the list, False otherwise.

    Use all() in combination with map and fn to check if fn returns True for all elements in the list.
    """

    return all(map(fn, lst))


def every_nth(lst, nth):
    """Returns every nth element in a list.

        Use [nth-1::nth] to create a new list that contains every nth element of the given list.
    """

    return lst[nth - 1::nth]


def factorial(num):
    """
    Calculates the factorial of a number.

    Use recursion. If num is less than or equal to 1, return 1. Otherwise, return the product of num and the factorial of num - 1. Throws an exception if num is a negative or a floating point number.
    """

    if not ((num >= 0) and (num % 1 == 0)):
        raise Exception(
            f"Number( {num} ) can't be floating point or negative ")
    return 1 if num == 0 else num * factorial(num - 1)


def fibonacci(n):
    """
    Generates an array, containing the Fibonacci sequence, up until the nth term.

    Starting with 0 and 1, use list.apoend() to add the sum of the last two numbers of the list to the end of the list, until the length of the list reaches n. If nis less or equal to0, return a list containing 0`.
    """

    if n <= 0:
        return [0]

    sequence = [0, 1]
    while len(sequence) <= n:
        next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
        sequence.append(next_value)

    return sequence


def filter_non_unique(lst):
    """Filters out the non-unique values in a list.

    Use list comprehension and list.count() to create a list containing only the unique values.
    """

    return [item for item in lst if lst.count(item) == 1]


def flatten(lst):
    """
    Flattens a list of lists once.

    Use nested list comprehension to extract each value from sub-lists in order.
    """

    return [x for y in lst for x in y]


from functools import reduce
import math


def gcd(numbers):
    """
    Calculates the greatest common divisor of a list of numbers.

    Use reduce() and math.gcd over the given list.
    """

    return reduce(math.gcd, numbers)


def group_by(lst, fn):
    """
    Groups the elements of a list based on the given function.

    Use map() and fn to map the values of the list to the keys of an object. Use list comprehension to map each element to the appropriate key.
    """
    return {key: [el for el in lst if fn(el) == key] for key in map(fn, lst)}


def has_duplicates(lst):
    """
    Returns True if there are duplicate values in a flast list, False otherwise.

    Use set() on the given list to remove duplicates, compare its length with the length of the list.
    """

    return len(lst) != len(set(lst))


def head(lst):
    """
   Returns the head of a list.

    use lst[0] to return the first element of the passed list.
    """

    return lst[0]


def in_range(n, start, end=0):
    """
    Checks if the given number falls within the given range.

    Use arithmetic comparison to check if the given number is in the specified range. If the second parameter, end, is not specified, the range is considered to be from 0 to start.
    """

    if (start > end):
        end, start = start, end
    return start <= n <= end


def initial(lst):
    """
    Returns all the elements of a list except the last one.

    Use lst[0:-1] to return all but the last element of the list.
    """

    return lst[0:-1]


def initialize_2d_list(w, h, val=None):
    """
    Initializes a 2D list of given width and height and value.

    Use list comprehension and range() to generate h rows where each is a list with length h, initialized with val. If val is not provided, default to None.
    """

    return [[val for x in range(w)] for y in range(h)]


def initialize_list_with_range(end, start=0, step=1):
    """
    Initializes a list containing the numbers in the specified range where start and end are inclusive with their common difference step.

    Use list and range() to generate a list of the appropriate length, filled with the desired values in the given range. Omit start to use the default value of 0. Omit step to use the default value of 1.
    """
    return list(range(start, end + 1, step))


def initialize_list_with_values(n, val=0):
    """
    Initializes and fills a list with the specified value.

    Use list comprehension and range() to generate a list of length equal to n, filled with the desired values. Omit val to use the default value of 0.
    """

    return [val for x in range(n)]


def intersection(a, b):
    """
    

    Returns a list of elements that exist in both lists.

    Create a set from b, then use list comprehension on a to only keep values contained in both lists.
    """

    _b = set(b)
    return [item for item in a if item in _b]


def intersection_by(a, b, fn):
    """
    Returns a list of elements that exist in both lists, after applying the provided function to each list element of both.

    Create a set by applying fn to each element in b, then use list comprehension in combination with fn on a to only keep values contained in both lists.
    """

    _b = set(map(fn, b))
    return [item for item in a if fn(item) in _b]


def is_anagram(str1, str2):
    """
    Checks if a string is an anagram of another string (case-insensitive, ignores spaces, punctuation and special characters).

    Use str.replace() to remove spaces from both strings. Compare the lengths of the two strings, return False if they are not equal. Use sorted() on both strings and compare the results.
    """

    _str1, _str2 = str1.replace(" ", ""), str2.replace(" ", "")

    if len(_str1) != len(_str2):
        return False
    else:
        return sorted(_str1.lower()) == sorted(_str2.lower())


def is_divisible(dividend, divisor):
    """Checks if the first numeric argument is divisible by the second one.

    Use the modulo operator (%) to check if the remainder is equal to 0.
    """

    return dividend % divisor == 0


def is_even(num):
    """
    Returns True if the given number is even, False otherwise.

    Checks whether a number is odd or even using the modulo (%) operator. Returns True if the number is even, False if the number is odd.
    """

    return num % 2 == 0


def is_lower_case(string):
    """
    Checks if a string is lower case.

    Convert the given string to lower case, using str.lower() and compare it to the original.
    """

    return string == string.lower()


def is_odd(num):
    """
    Returns True if the given number is odd, False otherwise.

    Checks whether a number is even or odd using the modulo (%) operator. Returns True if the number is odd, False if the number is even.
    """

    return num % 2 != 0


def is_upper_case(string):
    """Checks if a string is upper case.

    Convert the given string to upper case, using str.upper() and compare it to the original.
    """

    return string == string.upper()


def kebab(str):
    """Converts a string to kebab case.

    Break the string into words and combine them adding - as a separator, using a regexp."""

    return re.sub(r"(\s|_|-)+", "-",
                  re.sub(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+",
                         lambda mo: mo.group(0).lower(), str)
                  )


def keys_only(flat_dict):
    """Returns a flat list of all the keys in a flat dictionary.

    Use dict.keys() to return the keys in the given dictionary. Return a list() of the previous result.
    """

    return list(flat_dict.keys())


def last(lst):
    """Returns the last element in a list.

    use lst[-1] to return the last element of the passed list.
    """

    return lst[-1]


def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


def lcm(*args):
    """Returns the least common multiple of two or more numbers.

    Define a function, spread, that uses either list.extend() or list.append() on each element in a list to flatten it. Use math.gcd() and lcm(x,y) = x * y / gcd(x,y) to determine the least common multiple."""

    numbers = []
    numbers.extend(spread(list(args)))


def _lcm(x, y):
    return int(x * y / math.gcd(x, y))

    return reduce((lambda x, y: _lcm(x, y)), numbers)


def longest_item(*args):
    """Takes any number of iterable objects or objects with a length property and returns the longest one. If multiple objects have the same length, the first one will be returned.

    Use max() with len as the key to return the item with the greatest length."""

    return max(args, key=len)


def map_values(obj, fn):
    """
    Creates an object with the same keys as the provided object and values generated by running the provided function for each value.

    Use dict.keys() to iterate over the object's keys, assigning the values produced by fn to each key of a new object.
    """

    ret = {}
    for key in obj.keys():
        ret[key] = fn(obj[key])
    return ret


def max_by(lst, fn):
    """Returns the maximum value of a list, after mapping each element to a value using the provided function.

    Use map() with fn to map each element to a value using the provided function, use max() to return the maximum value."""

    return max(map(fn, lst))


def min_n(lst, n=1):
    """Returns the n minimum elements from the provided list. If n is greater than or equal to the provided list's length, then return the original list (sorted in ascending order).

    Use sorted() to sort the list, [:n]to get the specified number of elements. Omit the second argument,n`, to get a one-element list."""

    return sorted(lst, reverse=False)[:n]


def none(lst, fn=lambda x: x):
    """Returns False if the provided function returns True for at least one element in the list, True otherwise.

    Use all() in combination with map() and fn to check if fn returns False for all the elements in the list."""

    return all(map(lambda x: not fn(x), lst))


def offset(lst, offset):
    """Moves the specified amount of elements to the end of the list.

    Use lst[offset:] and lst[:offset] to get the two slices of the list and combine them before returning.
    """

    return lst[offset:] + lst[:offset]


def palindrome(string):
    """Returns True if the given string is a palindrome, False otherwise.

    Use str.lower() and re.sub() to convert to lowercase and remove non-alphanumeric characters from the given string. Then, compare the new string with its reverse."""

    s = sub('[\W_]', '', string.lower())
    return s == s[::-1]


def rads_to_degrees(rad):
    """Converts an angle from radians to degrees.

    Use math.pi and the radian to degree formula to convert the angle from radians to degrees."""

    return (rad * 180.0) / math.pi

    from random import randint


def sample(lst):
    """Returns a random element from an array.

    Use randint() to generate a random number that corresponds to an index in the list, return the element at that index."""

    return lst[randint(0, len(lst) - 1)]


def shuffle(lst):
    """Randomizes the order of the values of an list, returning a new list.

    Uses the Fisher-Yates algorithm to reorder the elements of the list."""

    temp_lst = deepcopy(lst)
    m = len(temp_lst)
    while (m):
        m -= 1
        i = randint(0, m)
        temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
    return temp_lst


def similarity(a, b):
    """

    Returns a list of elements that exist in both lists.

    Use list comprehension on a to only keep values contained in both lists."""

    return [item for item in a if item in b]


def snake(str):
    """

    Converts a string to snake case.

    Break the string into words and combine them adding _-_ as a separator, using a regexp."""

    return re.sub(r"(\s|_|-)+", "-",
                  re.sub(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+",
                         lambda mo: mo.group(0).lower(), str)
                  )


def some(lst, fn=lambda x: x):
    """

    Returns True if the provided function returns True for at least one element in the list, False otherwise.

    Use any() in combination with map() and fn to check if fn returns True for any element in the list."""

    return any(map(fn, lst))


def split_lines(str):
    """Splits a multiline string into a list of lines.

    Use str.split() and '\n' to match line breaks and create a list."""

    return str.split('\n')


def sum_by(lst, fn):
    """Returns the sum of a list, after mapping each element to a value using the provided function.

    Use map() with fn to map each element to a value using the provided function, use sum() to return the sum of the values."""

    return sum(map(fn, lst))


def symmetric_difference(a, b):
    """Returns the symmetric difference between two iterables, without filtering out duplicate values.

    Create a set from each list, then use list comprehension on each one to only keep values not contained in the previously created set of the other."""

    _a, _b = set(a), set(b)
    return [item for item in a if item not in _b] + [item for item in b if item not in _a]


def tail(lst):
    """Returns all elements in a list except for the first one.

    Return lst[1:] if the list's length is more than 1, otherwise, return the whole list."""

    return lst[1:] if len(lst) > 1 else lst


def union(a, b):
    """Returns every element that exists in any of the two lists once.

    Create a set with all values of a and b and convert to a list."""

    return list(set(a + b))


def union_by(a, b, fn):
    """Returns every element that exists in any of the two lists once, after applying the provided function to each element of both.

    Create a set by applying fn to each element in a, then use list comprehension in combination with fn on b to only keep values not contained in the previously created set, _a. Finally, create a set from the previous result and a and transform it into a list"""

    _a = set(map(fn, a))
    return list(set(a + [item for item in b if fn(item) not in _a]))


def unique_elements(li):
    """Returns the unique elements in a given list.

    Create a set from the list to discard duplicated values, then return a list from it."""

    return list(set(li))


def values_only(dict):
    """

    Returns a flat list of all the values in a flat dictionary.

    Use dict.values() to return the values in the given dictionary. Return a list() of the previous result."""

    return list(dict.values())


def zip_groups(*args, fillvalue=None):
    """Creates a list of elements, grouped based on the position in the original lists.

    Use max combined with list comprehension to get the length of the longest list in the arguments. Loop for max_length times grouping elements. If lengths of lists vary, use fill_value (defaults to None)."""

    max_length = max([len(lst) for lst in args])
    result = []
    for i in range(max_length):
        result.append([
            args[k][i] if i < len(args[k]) else fillvalue for k in range(len(args))
        ])
    return result

def add_vectors(u, v):
    new_list = list()
    for i in range(len(u)):
        new_list.append(u[i] + v[i])
    return new_list


def scalar_mult(s, v):
    new_list = list()
    for i in v:
        new_list.append(s * i)
    return new_list

def dot_product(u, v):
    sum = 0
    for i in range(len(u)):
        sum = sum + u[i] * v[i]
    return sum
def share_diagonal(x0, y0, x1, y1):
    dy = abs(y1 - y0)
    dx = abs(x1 - x0)
    if dy == dx:
        return True
    return False

def col_clashes(bs, c):
    for i in range(c):
        if share_diagonal(i, bs[i], c, bs[c]):
            return True
    return False

def has_clashes(lst):
    for i in range(1, len(lst)):
        if col_clashes(lst, i):
            return True
    return False

def is_diagonal(lst):
    for i in range(1, len(lst)):
        temp = lst[:i+1]
        for j, num in enumerate(temp[:-1]):
            a = abs(num - temp[-1])
            b = abs(j - i)
            if a == b:
                return True
    return False

class Point:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def reflect_x(self):
        return Point(self.x, -self.y)
    
    def slope_from_origin(self):
        return self.y / self.x
    
    def get_line_to(self, pt2):
        a = (self.y - pt2.y) / (self.x - pt2.x)
        b = self.y - a * self.x
        return a, b
    
def distance(pt1, pt2):
    return ((pt1.x - pt2.x) ** 2 + (pt1.y - pt2.y) ** 2) ** 0.5

class SMS_store:
    def __init__(self):
        self.content = []
 
    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        msg = (False, from_number, time_arrived, text_of_SMS)
        self.content.append(msg)
    
    def message_count(self):
        return len(self.content)
    
    def get_unread_indexes(self):
        indexes_list = []
        for i, msg in enumerate(self.content):
            if msg[0] == False:
                indexes_list.append(i)
        return indexes_list
    
    def get_message(self, i):
        if i < len(self.content):
            self.content[i] = (True, self.content[i][1], self.content[i][2], self.content[i][3])
            return self.content[i][1], self.content[i][2], self.content[i][3]
        else:
            return None
    
    def delete(self, i):
        self.content.pop(i)
    
    def clear(self):
        self.content = []

class Rectangle:
    
    def __init__(self, posn, w, h):
        self.corner = posn
        self.width = w
        self.height = h
    
    def __str__(self):
        return "{}, {}, {}".format(self.corner, self.width, self.height)
    
    def grow(self, delta_width, delta_height):
        self.width += delta_width
        self.height += delta_height
        
    def move(self, dx, dy):
        self.corner.x += dx
        self.corner.y += dy
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return (self.height + self.width) * 2
    
    def flip(self):
        (self.width, self.height) = (self.height, self.width)
    
    def contains(self, pt):
        x_upper = self.corner.x +self.width
        x_lower = self.corner.x
        y_upper = self.corner.y +self.height
        y_lower = self.corner.y
        return x_lower <= pt.x < x_upper and y_lower <= pt.y <y_upper
    
def recursion_depth(number):
    print("{0}, ".format(number), end="")   
    recursion_depth(number + 1)

def recursive_min(lst):
    first_time = True
    min = 0
    result = 0
    for i in lst:
        if type(i) == type([]):
            result = recursive_min(i)
        else:
            result = i
        
        if first_time or result < min:
            min = result
            first_time = False
    return min

def count(target, lst):
    n = 0
    for i in lst:
        if type(i) == type([]):
            n = count(target, i) + n
        else:
            if target == i:
                n = n + 1
    return n


def get_dirlist(path):
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist


def print_files(path, prefix = ''):
    if prefix == '':
        print('Folder listing for', path)
        prefix = '| '
        
    dirlist = get_dirlist(path)
    for f in dirlist:
        print(prefix + f)
        fullname = os.path.join(path, f)
        if os.path.isdir(fullname):
            print_files(fullname, prefix + '| ')

def get_file_list(path):
    file_list = []
    dirlist = get_dirlist(path)
    for f in dirlist:
        fullname = os.path.join(path, f)
        if not os.path.isdir(fullname):
            file_list.append(fullname)
        else:
            file_list.extend(get_file_list(fullname))
    return file_list

def litter(path):
    dirlist = get_dirlist(path)
    for f in dirlist:
        fullname = os.path.join(path, f)
        if os.path.isdir(fullname):
            litter(fullname)
            fullname = os.path.join(fullname, 'trash.txt')
            print('file created: {}'.format(fullname))
            file = open(fullname, 'w')
            file.close()
            
def delete(path):
    dirlist = get_dirlist(path)
    for f in dirlist:
        fullname = os.path.join(path, f)
        if os.path.isdir(fullname):
            delete(fullname)
            fullname = os.path.join(fullname, 'trash.txt')
            if os.path.exists(fullname):
                os.remove(fullname)
                print('file removed:{}'.format(fullname))
            else:
                print('no such files!')
                

def recursion_depth(number):
    print("Recursion depth number", number)
    try:
        recursion_depth(number + 1)
    except:
        print("I cannot go any deeper into this wormhole.")
        
def readposint():
    temp = input()
    try:
        temp = int(temp)
    except:
        print('wrong')

def recursion_depth(number):
    print("Recursion depth number", number)
    try:
        recursion_depth(number + 1)
    except:
        print("I cannot go any deeper into this wormhole.")

def count_letter(string):
    count_dict = {}
    for i in string.lower():
        count_dict[i] = count_dict.get(i, 0) + 1
    count_dict.pop(' ')
    count_list = list(count_dict.items())
    count_list.sort()
    return count_list


class MyTime:
    def __init__(self, hrs=0, mins=0, secs=0):
        totalsecs = hrs*3600 + mins*60 + secs
        self.hours = totalsecs // 3600 # Split in h, m, s
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60
        
    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds
    
    def between(self, t1, t2):
        return t1.to_seconds() <= self.to_seconds() < t2.to_seconds()
    
    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()
    
    def increment(self, seconds):
        total_secs = self.to_seconds() + seconds
        return MyTime(0, 0, total_secs)
    
    def __str__(self):
        return str(self.hours) + ' ' + str(self.minutes) + ' ' + str(self.seconds)

class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next
    
    def __str__(self):
        return str(self.cargo)
    
    def print_backward(self):
        if self.next is not None:
            tail = self.next
            tail.print_backward()
        print(self.cargo, end=' ')
    
def print_list(node):
    print("[", end ='')
    while node is not None:
        print(node, end='')
        if node.next is not None:
            print(',', end =' ')
        node = node.next
    print(']')
    

def print_backward(list):
    if list is None: return
    head = list
    tail = list.next
    print_backward(tail)
    print(head, end=' ')

def remove_second(list):
    if list is None: return
    first = list
    second = list.next
    first.next = second.next
    second.next = None
    return second

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        
    def print_backward(self):
        print("[", end=" ")
        if self.head is not None:
            self.head.print_backward()
        print("]")

    def add_first(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length += 1
        
def how_many_odd_nums(lst):
    count = 0
    for i in lst:
        if i % 2 == 1:
            count = count + 1
    return count

def sum_all_even_nums(lst):
    sum_1 = 0
    for i in lst:
        if i % 2 == 0:
            sum_1 = sum_1 + i
    return sum_1

def sum_all_negative_nums(lst):
    sum_2 = 0
    for i in lst:
        if i < 0:
            sum_2 = sum_2 + i
    return sum_2

def count_length_5(lst):
    count = 0
    for i in lst:
        if len(i) == 5:
            count = count + 1
    return count

def sum_all_but_first_even(lst):
    count = 0
    sum_3 = 0
    for i in lst:
        if i % 2 == 0 and count == 0:
            count = 1
            continue
        sum_3 = sum_3 + i
    return sum_3

def find_sam(lst):
    count = 0
    for i in lst:
        count = count + 1
        if i == 'sam':
            break
    if count == len(lst) and i !='sam':
        return 0
    else:
        return count

def newton_sqrt(num):
    guess = num / 2.0
    while True:
        better = (guess + num/guess) / 2.0
        if abs(better - guess) < 0.0001:
            return better
        guess = better
        print("better")

def print_triangular_numbers(n):
    for i in range(1, n+1):
        sum_1 = 0
        for j in range(i+1):
            sum_1 = sum_1 + j
        print(i, '\t', sum_1)

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


def num_digits(n):
    if n == 0:
        return 1    
    n_1 = abs(n)
    count = 0
    while n_1 // (10**count) != 0:
        count = count + 1
    return count

def num_even_digits(n):
    num_str = str(n)
    count = 0
    for i in num_str:
        if int(i) % 2 == 0:
            count = count + 1
    return count

def sum_of_squares(xs):
    sum_1 = 0
    for i in xs:
        sum_1 = sum_1 + i**2
    return sum_1

def count_letters(string, letter, location=0):
    count = 0
    start = location
    while True:
        start = string.find(letter, start) + 1
        if start == 0:
            break
        count = count + 1
    if count == 0:
        return -1
    return count

def func_1(string):
    import string
    new_para = ''
    for i in para:
        if i not in string.punctuation:
            new_para = new_para + i
    word_list = new_para.split()
    count_1 = len(word_list)
    count_2 = 0
    for i in word_list:
        if 'e' in i:
            count_2 = count_2 + 1
    print('Your text contains {} words, of which {} ({:.2f}%) contain an "e".'.format(count_1, count_2, count_2/count_1*100))
    
def reverse(string):
    new_string = ''
    for i in range(len(string)):
        new_string = new_string + string[-(i+1)]
    return new_string


def mirror(string):
    return string + reverse(string)

def remove_letter(letter, string):
    new_string = ''
    for i in string:
        if i != letter:
            new_string = new_string + i
    return new_string

def count_how_many(word, string):
    x=len(word)
    string_list = [string[i:x+i] for i in range(len(string)-x+1)]
    count = 0
    for i in string_list:
        if i == word:
            count = count + 1
    return count

def remove(word, string):
    if word not in string:
        return string
    else:
        x=len(word)
        string_list = [string[i:x+i] for i in range(len(string)-x+1)]
        new_string = ''
        for i, letter in enumerate(string_list):
            if letter == word:
                break
            new_string = new_string + letter[0]
        new_string = new_string + string[i+x:]
        return new_string
   
def remove_2(word, string):
    n = string.find(word)
    x = len(word)
    if n == -1:
        return string
    else:
        return string[:n] + string[n+x:]
    
def remove_all(word, string):
    temp = string
    while True:
        temp = remove_2(word, temp)
        if temp.find(word) == -1:
            break
    return temp


if __name__ == "__main__":
    # Erase pass and call class or functions here.
    pass
