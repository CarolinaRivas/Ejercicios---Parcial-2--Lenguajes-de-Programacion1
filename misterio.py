def ins(e, ls):
    yield [e, *ls]
    if ls:
        for i in ins(e, ls[1:]):
            yield [ls[0], *i]


def misterio(ls):
    if ls:
        for m in misterio(ls[1:]):
            for i in ins(ls[0], m):
                yield i
    else:
        yield []


def suspenso(ls):
    if ls:
        for m in misterio(ls[1:]):
            for i in ins(ls[0], m):
                for x in i:
                    yield x
    else:
        yield []


for x in misterio(['a', 'b', 'c']):
    print(x)

for x in suspenso(['a', 'b', 'c']):
    print(x)
