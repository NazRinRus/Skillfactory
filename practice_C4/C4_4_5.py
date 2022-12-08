pars = {")": "(", "]": "["}


def par_checker_mod(string):
    stack = []

    for s in string:
        if s in pars.values():
            stack.append(s)
        elif s in pars.keys():
            if len(stack) > 0 and stack[-1] == pars[s]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

print(par_checker_mod('(5+6)*(7+8)/(4+3)'))