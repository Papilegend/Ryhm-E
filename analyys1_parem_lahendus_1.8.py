def reverse(x):
    arv=str(x)
    i = len(arv)-1
    a=lst()
    b=""
    if arv[0] == "-":
            b+= "-"
            arv.remove(arv[0])
    for taht in arv:
        a.append(taht)
    c = reversed(a)
    vastus.append(c.join())
    return vastus
        