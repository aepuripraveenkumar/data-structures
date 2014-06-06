def check_parens(string):
    check = 0
    open_paren = "("
    closed_paren = ")"
    for i in string:
        if check < 0:
            return -1
        elif i == open_paren:
            check += 1
        elif i == closed_paren:
            check -= 1
        else:
            pass
    if check > 0:
        return 1
    else:
        return 0
