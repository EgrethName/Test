def judge_half(pos, neg):
    return pos >= neg


def judge_any(pos, neg):
    return pos >= 1


def judge_all(pos, neg):
    return neg == 0


class multifilter:
    def judge_half(pos, neg):
        return pos >= neg

    def judge_any(pos, neg):
        return pos >= 1

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.iterable) == self.i:
            raise StopIteration
        current_value = self.iterable[self.i]
        self.i += 1
        pos = 0
        neg = 0
        for function in self.funcs:
            if function(current_value):
                pos += 1
            else:
                neg += 1
        result = self.judge(pos, neg)
        if result:
            yield current_value
        else:
            yield self.__next__()


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]
print(list(multifilter(a, mul2, mul3, mul5)))
print(list(multifilter(a, mul2, mul3, mul5, judge=judge_half)))
print(list(multifilter(a, mul2, mul3, mul5, judge=judge_all)))