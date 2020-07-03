from operator import itemgetter

def solution(l):

    # check length if 1 to 100
    if (len(l) < 1) or (len(l) > 100): return

    #check if string
    for items in l:
        if not type(items) is str: return

    # make input "versions" into list of list of int
    versions_int_list = [[int(n) for n in no.split('.')] for no in l]

    # assign placeholder -1 to 1-digit and 2-digit versions
    for item in versions_int_list:
        if len(item) == 1: item.extend([-1,-1])
        elif len(item) == 2: item.extend([-1])

    # sort with major
    sorted_int_list = sorted(versions_int_list, key=(itemgetter(0,1,2)))

    # delete place holder -1
    for item in sorted_int_list:
        while -1 in item: item.remove(-1)

    #
    sorted_str_list = [[str(n) for n in item] for item in sorted_int_list]

    dotted_list =[".".join(version) for version in sorted_str_list]

    return dotted_list
    
