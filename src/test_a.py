print("initialing test_a")

g_name = None


def set_name(name):
    global g_name
    g_name = name


def get_name():
    global g_name
    if not g_name:
        return "default"
    return g_name


def func_a():
    print("call func_a in test_a")
