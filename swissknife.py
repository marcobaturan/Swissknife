#!/usr/bin/env/python3.6
# _*_import: utf-8 _*_
# Please, do not forget try comment and document under pep8.
# https://www.python.org/dev/peps/pep-0008/
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


if __name__ == "__main__":
    # Erase pass and call class or functions here.
    pass
