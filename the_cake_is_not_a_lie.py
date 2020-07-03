# Write a function called solution(s) that,
# given a non-empty string less than 200 characters
# n length describing the sequence of M&Ms,
# returns the maximum number of equal parts
# that can be cut from the cake
# without leaving any leftovers.

def solution(s):
    # given a non-empty string less than 200 char
    # retun max number of equal parts

    # get length of s
    l = len(s)

    # exit if s >= 200
    if (l == 0) or (l >= 200): return

    # when cake cannot be devided = 1
    potential_solution = [1]

    # find number that can divide s
    div_list = [i for i in range(1,l) if (l%i == 0)]

    for i in div_list:
        # first few char
        repeat_s = s[:i]
        # how many times does this appear
        r = int(l/i)
        # make full string by repeat_s
        temp_s = repeat_s * r
        # see if it matches the input
        if temp_s == s:
            potential_solution.append(r)

    return max(potential_solution)
