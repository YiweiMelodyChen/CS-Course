""" Lab 04 """


this_file = __file__

def skip_add(n):
    """ Takes a number n and returns n + n-2 + n-4 + n-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'skip_add',
    ...       ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def s_add(n, sum):
        sum = sum + n
        if n - 2 < 0:
            return sum
        else:
            return s_add(n - 2, sum)
    return s_add(n, 0)

def summation(n, term):

    """Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    "*** YOUR CODE HERE ***"
    def sub_summation(x, f, sum):
        sum = sum + f(x)
        if x == n:
            return sum
        else:
            return sub_summation(x+1, f, sum)
    return sub_summation(1, term, 0)

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    def sub_gcd(div, a, b):
        if a % div == 0 and b % div == 0:
            return div
        else:
            return sub_gcd(div - 1, a, b)
    return sub_gcd(a, a, b)

def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    def sub_path(m, n):
        if m == 1 and n == 1:
            return 1
        elif m == 1:
            return sub_path(m, n-1)
        elif n == 1:
            return sub_path(m-1, n)
        else:
            return sub_path(m-1, n) + sub_path(m, n-1)
    return sub_path(m, n)


def max_subseq(n, l):
    """
    Return the maximum subsequence of length at most l that can be found in the given number n.
    For example, for n = 20125 and l = 3, we have that the subsequences are
        2
        0
        1
        2
        5
        20
        21
        22
        25
        01
        02
        05
        12
        15
        25
        201
        202
        205
        212
        215
        225
        012
        015
        025
        125
    and of these, the maxumum number is 225, so our answer is 225.

    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # note that 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # 0 is of length 0
    0
    >>> max_subseq(12345, 1)
    5
    """
    "*** YOUR CODE HERE ***"
    if l == 0:
        return 0
    if pow(10, l - 1) > n:
        return n

    def create_list(list, n):
        list.append(n % 10)
        if n < 10:
            return list
        else:
            return create_list(list, n//10)

    def create_max_subseq(list, l, max_seq):
        max = 0
        max_num = 0
        for i in range(len(list) - l + 1):
            if list[i] > max:
                max = list[i]
                max_num = i
        max_seq = max_seq * 10 + max
        new_list = []
        for i in range(max_num+1, len(list)):
            new_list.append(list[i])
        l = l - 1
        if l == 0:
            return max_seq
        else:
            return create_max_subseq(new_list, l, max_seq)

    list = []
    new_list = create_list(list, n)
    new_list.reverse()
    return create_max_subseq(new_list, l, 0)

# print(max_subseq(20125, 5))