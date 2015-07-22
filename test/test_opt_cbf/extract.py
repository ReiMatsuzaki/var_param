import sys
import os
sys.path.append('.')
sys.path.append('../..')
import var_param as vp
opt_cbf_root = "/Users/rei/src/git/opt_cbf"
sys.path.append(opt_cbf_root + "/script")
import opt_cbf as oc

res_dir =  os.path.dirname(__file__) + "/results/"

def read_zeta_from_dir(d):
    f = res_dir + d + "/opt_cbf.out"
    datas = open(f).readlines()
    return oc.zetas_opt_cbf(datas)

zss = [ read_zeta_from_dir(d) for d in os.listdir(res_dir)]
zss = oc.uniq_opt_cbf(zss, 0.001)

for zs in zss:
    print zs


