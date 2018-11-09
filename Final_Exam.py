# 1. 8 % 6, 8 + 3
# 2. 10
# 3. 40
# 4. first + str(second) + third
# 5. max(s1.count(letter), s2.count(letter))
# 6. s1.startswith(prefix) and s2.startswith(prefix)
# 7. lst = ['a', 'b', 'c']
#   moogah(lst[0], len(lst))
# 7. frooble([moogah('', 0)])
# 7. moogah('a', frooble(['a']))
# 8. i = i + n
# 9. k in d:
# 10. len(L2[i]) != L1[i]:
# 11. d = {1: 10, 2: 20, 3: 30}
#     double_values(d)
# 11. d = {1: 10, 2: 20, 3: 30}
#     double_values(d)

def get_negative_nonnegative_lists(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the negative ints in the
    inner lists of L and the second item is a list of the non-negative ints
    in those inner lists.

    Precondition: the number of rows in L is the same as the number of
    columns.

    >>> get_negative_nonnegative_lists([[-1,  3,  5], [2,  -4,  5], [4,  0,  8]])
    ([-1, -4], [3, 5, 2, 5, 4, 0, 8])
    '''

    nonneg = []
    neg = []
    for row in range(len(L)):
        for col in range(len(L)):
            val = L[row][col]
            if val < 0:
                neg.append(val)
            else:
                nonneg.append(val)

    return (neg, nonneg)

print(get_negative_nonnegative_lists([[-1,  3,  5], [2,  -4,  5], [4,  0,  8]]))

