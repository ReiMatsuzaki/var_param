
def first_tuple_or_str(x):
    if type(x) == tuple:
        return str(x[0])
    else:
        return str(x)

def flat_from(res_dir_name):
    def __from__(ps):
        tmp = res_dir_name + "/"
        for p in ps.values():
            tmp += "_" + first_tuple_or_str(p)
        return tmp
    return __from__

def tree_from(res_dir_name):
    def _from_(ps):
        tmp = res_dir_name
        for p in ps.values():
            tmp += first_tuple_or_str(p)
        return tmp
    return _from_
