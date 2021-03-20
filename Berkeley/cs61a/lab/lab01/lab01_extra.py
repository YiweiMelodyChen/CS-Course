"""Optional questions for Lab 1"""

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    fac = 1
    for i in range(0, k):
        fac = fac * (n-i)
    return fac

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    list = []
    num = 0
    while n > 0:
        list.append(n % 10)
        n = int(n / 10)
    for i in range(0, len(list)):
        if list[i] == 8:
            num = num+1
     if num%2 == 0:
         return True
     else:
         return False
