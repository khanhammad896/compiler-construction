with open('../code.cbn','r') as code:
    content = code.read()
    code = list()

    for item in content:
        code.append(item)
    print(code)

    for item in code:
        print(item,end="")