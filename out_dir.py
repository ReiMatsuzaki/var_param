
        





def flat_from(res_dir_name):
    def __from__(ps):
        tmp = res_dir_name + "/"
        for p in ps.values():
            tmp += "_" + str(p)
        return tmp
    return __from__

def tree_from(res_dir_name):
    def _from_(ps):
        tmp = res_dir_name
        for p in ps.values():
            tmp += "/_" + str(p)
        return tmp
    return _from_
