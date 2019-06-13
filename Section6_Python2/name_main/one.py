#python one.py
# python, in the bkground runs __name__ = "__main__"


def func():
    print("FUNC() IN ONE.PY")

def func2():
    pass

def func3():
    pass

print("TOP LEVEL IN ONE.PY")



if __name__ == "__main__":
    # RUN THE SCRIPT
    func()
    func2()
    func3()

