import re


def is_literal(s):
    return re.match('^"[^"]*"$', str(s)) or s == "\n" or s == "\t"


def is_number(s):
    return re.match('^-?\\d+$', str(s))


def is_variable(s):
    return re.match('^[a-z]$', str(s))


def is_command(s):
    return s in commands.keys()


def split(line):
    line = [i for i in re.split('(-?\\d+)|("[^"]*")', re.sub("….*…", "", line)) if i]
    parsed = []
    for i in line:
        if not is_literal(i) and not is_number(i) and i != " ":
            for j in i:
                parsed.append(j)
        elif i != " ":
            parsed.append(i)

    for index, el in enumerate(parsed):
        parsed[index] = {"el": el, "used": False}
    return parsed


variables = dict()


def command_input():
    i = input()
    if is_number(i):
        return int(i)
    return '"' + i + '"'


def command_print(a):
    if is_variable(a):
        if a in variables.keys():
            print(str(variables[a]).replace('"', ''), end="")
        else:
            print("\"undefined\"", end="")
        return

    if is_number(a) or is_literal(a):
        print(a.replace('"', ''), end="")
        return


def command_set(a, b):
    if is_variable(a):
        variables[a] = b


def command_add(a, b):
    if is_variable(a):
        if a in variables.keys():
            a = variables[a]
        else:
            a = "\"undefined\""

    if is_variable(b):
        if b in variables.keys():
            b = variables[a]
        else:
            b = "\"undefined\""

    if is_number(a) and is_number(b):
        return a + b
    return '"' + str(a).replace('"', '') + str(b).replace('"', '') + '"'


def command_sub(a, b):
    if is_variable(a):
        if a in variables.keys():
            a = variables[a]
        else:
            a = "\"undefined\""

    if is_variable(b):
        if b in variables.keys():
            b = variables[a]
        else:
            b = "\"undefined\""

    if is_number(a) and is_number(b):
        return a - b
    return "\"undefined\""


def command_mul(a, b):
    if is_variable(a):
        if a in variables.keys():
            a = variables[a]
        else:
            a = "\"undefined\""

    if is_variable(b):
        if b in variables.keys():
            b = variables[a]
        else:
            b = "\"undefined\""

    if is_number(a) and is_number(b):
        return a * b
    return "\"undefined\""


def command_div(a, b):
    if is_variable(a):
        if a in variables.keys():
            a = variables[a]
        else:
            a = "\"undefined\""

    if is_variable(b):
        if b in variables.keys():
            b = variables[a]
        else:
            b = "\"undefined\""

    if is_number(a) and is_number(b):
        return a / b
    return "\"undefined\""


def command_modulo(a, b):
    if is_variable(a):
        if a in variables.keys():
            a = variables[a]
        else:
            a = "\"undefined\""

    if is_variable(b):
        if b in variables.keys():
            b = variables[a]
        else:
            b = "\"undefined\""

    if is_number(a) and is_number(b):
        return a % b
    return "\"undefined\""


def command_exp(a, b):
    if is_variable(a):
        if a in variables.keys():
            a = variables[a]
        else:
            a = "\"undefined\""

    if is_variable(b):
        if b in variables.keys():
            b = variables[a]
        else:
            b = "\"undefined\""

    if is_number(a) and is_number(b):
        return a ** b
    return "\"undefined\""


def command_not(a):
    if is_variable(a):
        if a in variables.keys():
            a = variables[a]
        else:
            a = "\"\""

    if is_number(a):
        return +(int(a) == 0)

    if is_literal(a):
        return +(a == "\"\"")


commands = {
    ".": {
        "param_count": 1,
        "return": False,
        "callable": command_print
    },
    ",": {
        "param_count": 0,
        "return": True,
        "callable": command_input
    },
    "=": {
        "param_count": 2,
        "return": False,
        "callable": command_set
    },
    "+": {
        "param_count": 2,
        "return": True,
        "callable": command_add
    },
    "-": {
        "param_count": 2,
        "return": True,
        "callable": command_sub
    },
    "*": {
        "param_count": 2,
        "return": True,
        "callable": command_mul
    },
    "/": {
        "param_count": 2,
        "return": True,
        "callable": command_div
    },
    "%": {
        "param_count": 2,
        "return": True,
        "callable": command_modulo
    },
    "^": {
        "param_count": 2,
        "return": True,
        "callable": command_exp
    },
    "!": {
        "param_count": 1,
        "return": True,
        "callable": command_not
    }
}


def compute(command, data):
    command = commands[command]
    params = []
    a = 0
    for i in range(command["param_count"]):

        while data[i + a]["used"]:
            a += 1

        if is_literal(data[i + a]["el"]):
            params.append(data[i + a]["el"])
        elif is_number(data[i + a]["el"]):
            params.append(int(data[i + a]["el"]))
        elif is_variable(data[i + a]["el"]):
            params.append(data[i + a]["el"])
        elif is_command(data[i + a]["el"]):
            params.append(compute(data[i + a]["el"], data[i + a + 1:]))
        data[i + a]["used"] = True

    if command["return"]:
        return command["callable"](*params)

    command["callable"](*params)
    return 0


def parse(s):
    data = split(s)
    for index, el in enumerate(data):
        if el["used"]:
            continue
        if is_command(el["el"]):
            compute(el["el"], data[index + 1:])
