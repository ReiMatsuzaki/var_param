import sys
sys.path.append('.')
sys.path.append('../../')
import var_param as vp

zs = [0.1,0.2,0.3,0.4]
ks = ["k1", "k2"]
#direct_prod = vp.params.DirectProduct(zs, 2)
#for x in direct_prod:
#    print x

kvs = vp.params.DirectProductForKeys(ks, zs)
i = 0
for kv in kvs:
    print i
    i += 1
    print kv


print type([1,2])
print type([1,2]) == list
print type((1,2))
print type((1,2)) == tuple



