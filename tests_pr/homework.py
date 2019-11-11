import math
import string


def task1(list1, list2):
    """
    Take two lists, say for example these two:
    a =[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b =[1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    and write a program that returns a list that contains only the elements
    that are common between the lists (without duplicates)."""

    return list(set(x for x in list1 if x in list2))


def task2(value):
    """
    Return the number of times that the letter “a” appears anywhere in the given string
    Given string is “I am a good developer. I am also a writer” and output should be 5.
    """

    return value.count("a")


def task3(value):
    """
    Write a Python program to check if a given positive integer is a power of three
    Input : 9
    Output : True
    """
    if isinstance(value, int):
        return int(math.log(value, 3)) == math.log(value, 3)
    else:
        raise ValueError("Value is not int")


def task4(value):
    """
    Write a Python program to add the digits of a positive integer repeatedly until the result has a single digit.
    Input : 48
    Output : 3
    For example given number is 59, the result will be 5.
    Step 1: 5 + 9 = 14
    Step 1: 1 + 4 = 5
    """
    while len(str(value)) > 1:
        value = sum(int(x) for x in str(value))
    return value


def task5(value):
    """
    Write a Python program to push all zeros to the end of a list.
    Input : [0,2,3,4,6,7,10]
    Output : [2, 3, 4, 6, 7, 10, 0]
    """
    return [x for x in value if x > 0] + [0] * value.count(0)


def task6(value):
    """
    Write a Python program to check a sequence of numbers is an arithmetic progression or not.
    Input : [5, 7, 9, 11]
    Output : True
    In mathematics, an arithmetic progression or arithmetic sequence is a sequence of numbers such
    that the difference between the consecutive terms is constant.
    For example, the sequence 5, 7, 9, 11, 13, 15 ... is an arithmetic progression with common difference of 2.
    """
    diff = set()
    for i in range(len(value) - 1):
        diff.add(value[i + 1] - value[i])
    return len(diff) == 1


def task7(value):
    """
    Write a Python program to find the number in a list that doesn't occur twice.
    Input : [5, 3, 4, 3, 4]
    Output : 5
    """
    return [x for x in set(value) if value.count(x) == 1]


def task8(value):
    """
    Write a Python program to find a missing number from a list.
    Input : [1,2,3,4,6,7,8]
    Output : 5
    """

    result = []
    for i in range(len(value) - 1):
        if value[i + 1] - value[i] > 1:
            result.append(value[i] + 1)
    return result


def task9(value):
    """
    Write a Python program to count the elements in a list until an element is a tuple.
    Sample Test Cases:
    Input: [1,2,3,(1,2),3]
    Output: 3
    """
    inc = 0
    for i in range(len(value) - 1):
        if not isinstance(value[i], tuple):
            inc += 1
        else:
            break
    return inc


def task10(value):
    """
    Write a program that will take the str parameter being passed and return the string in reversed order.
    For example: if the input string is "Hello World and Coders" then
    your program should return the string sredoC dna dlroW olleH.
    """
    return value[::-1]


def task11(value):
    """"
    Write a program that will take the num parameter being passed and return the number
    of hours and minutes the parameter converts to (ie. if num = 63 then the output should be 1:3).
    Separate the number of hours and minutes with a colon.
    """
    return f"{value // 60} : {value % 60}"


def task12(value):
    """
    Write a program that will take the parameter being passed and
    return the largest word in the string.
    If there are two or more words that are the same length,
    return the first word from the string with that length.
    Ignore punctuation.
    Sample Test Cases:
    Input:"fun&!! time"
    Output:time
    Input:"I love dogs"
    Output:love
    """
    prepared = value.translate(str.maketrans('', '', string.punctuation)).split()
    return max(prepared, key=lambda x: len(x))


def task13():
    """
   Write a program (using functions!) that asks the user for a long string containing multiple words.
   Print back to the user the same string, except with the words in backwards order.
   For example:
   Input: My name is Michele
   Output: Michele is name My
   """
    msg = input("Input a string: ")
    result = ' '
    msg = msg.split()
    msg = msg[::-1]
    result = result.join(msg)
    return result


def task14():
    """
    Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
    Take this opportunity to think about how you can use functions.
    Make sure to ask the user to enter the number of numbers in the sequence to generate.
    """
    n = int(input("how many Fibonnaci numbers to generate: "))
    if n == 0:
        fib = None
    elif n == 1:
        fib = [1]
    elif n == 2:
        fib = [1, 1]
    elif n > 2:
        fib = [1, 1]
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])
    return fib


def task15(lst):
    """
    Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
    Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
    """
    return [i for i in lst if i % 2 == 0]


def task16(numb):
    """
    Write a program that will add up all the numbers from 1 to input number.
    For example: if the input is 4 then your program should return 10 because 1 + 2 + 3 + 4 = 10.
    """
    res = 0
    for i in range(1, numb + 1):
        res += i
    return res


def task17(numb):
    """
    Write a program that will take the parameter being passed and return the factorial of it.
    For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24.
    """
    res = 1
    for i in range(1, numb + 1):
        res = res * i
    return res


def task18(text):
    """
    Write a program that will take the str parameter being passed and modify it using the following algorithm.
    Replace every letter in the string with the letter following it in the alphabet (ie. cbecomes d, zbecomes a).
    Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.
    """
    res = ''
    count = 0
    for i in text:
        count += 1
        if ord(i) == 122:
            res += 'A'
        else:
            n = chr((ord(i)+1))
            if str(n) in ['a', 'e', 'i', 'o', 'u']:
                res += n.upper()
            else:
                res += n
    return res


def test_task19(lst):
    """
    Write a program that will take the str string parameter being passed and return the string with the letters in
    alphabetical order (ie. hello becomes ehllo).
    Assume numbers and punctuation symbols will not be included in the string.
    """
    small = lst[0]
    small_index = 0
    for i in range(1, len(lst)):
        if lst[i] < small:
            small = lst[i]
            small_index = i
    return small_index


def task19(data):
    lst = [ord(i) for i in data]
    newels = []
    for i in range(len(lst)):
        small = test_task19(lst)
        newels.append(lst.pop(small))
    return ''.join(map(str, [chr(i) for i in newels]))


def task20(num_1, num_2):
    """
    Write a program that will take both parameters being passed and return the true if num2 is greater than num1,
     otherwise return the false. If the parameter values are equal to each other then return the string -1
    """
    if num_2 > num_1:
        return True
    elif num_1 == num_2:
        return "-1"
    return False
