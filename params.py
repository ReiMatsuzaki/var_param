import itertools

# =============== Utils =================

class CombinationsForKeys(object):
    """
    self.keys : [string]
    self.xs   : [a]     (str(a))
    iteration for hash table
    { k_0: x_0i, k_1: x_1i, ...}
    where (x_0i, x_1i, ...) is element of direct sum of xs
    """
    def __init__(self, keys, xs):
        self.keys = keys
        self.xs_permutations = itertools.combinations(xs, len(keys))
    def __iter__(self):
        return self
    def next(self):
        xs = self.xs_permutations.next()
        key_val = dict([(k,v) for (k,v) in zip(self.keys, xs)])
        return key_val


# ================    


def direct(xs):
    return xs


def combinations(keys, xs):
    return CombinationsForKeys(keys, xs)

class MyIter(object):
    def __init__(self, *numbers):
        self.numbers = numbers
        self.i = 0
    def __iter__(self):
        return self
    def next(self):
        if self.i == len(self.numbers):
            raise StopIteration()
        val = self.numbers[self.i]
        self.i += 1
        return val

#my_iter = MyIter(10, 20, 30)
#for n in my_iter:
#    print n
