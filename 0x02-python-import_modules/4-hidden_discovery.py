#!/usr/bin/python3

if __name__ == "__main__":
    import py_compile
    hidden_4 = py_compile.load("hidden_4.pyc")

    mods = dir(hidden_4)
    for mod in mods:
        if mod[:2] != "__":
            print(mod)
