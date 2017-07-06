import params
import save_if
import out_dir
import os
import shutil

def copy_file_with_replace(file_name_from, file_name_to, rep):
    """
    copy file "file_name_from" to "file_name_to" with replace represented
    by dictionary "rep"
    """
    f_to   = open(file_name_to,   "w")
    for line in open(file_name_from, 'r'):
        tmp = line
        for (k, v) in rep.items():
            val = str(v[1] if type(v) == tuple else v)
            tmp = tmp.replace("__" + k + "__", val)
        f_to.write(tmp)


def run(root, files, params, commands, out_dir, save_if = save_if.default):

    root_dir = os.path.abspath(root)
    os.chdir(root_dir)
    for ps in params:

        # directory name
        d0 = out_dir(ps)
        if not os.path.exists(d0):
            os.makedirs(d0) 

        # copy necessary files
        for f in files:
            f0 = root_dir + "/" + f
            f1 = d0 + "/" + f
            copy_file_with_replace(f0, f1, ps)

        # change directory 
        os.chdir(d0)

        # and lanch command
        os.system(commands)
        save_q = save_if()

        # come back
        os.chdir(root_dir)

        # remove calculation directories 
        if(not save_q):
            shutil.rmtree(d0)


def command(s):
    return s


if __name__ == '__main__':

    print """
import sys
import os
sys.path.append(".")
sys.path.append("../../")
import var_param as vp

def method1_is_SCF():
    contents = open('sample.in', 'r').read()
    return "SCF" in contents

file_list = [ 'sample.in' ]

cmd =  'echo "^^^^^^^^^^^^^^^^" &&'
cmd += 'pwd &&'
cmd += 'cat sample.in &&'
cmd += 'echo "vvvvvvvvvvvvvvvv" '

vp.run(
    root = os.path.dirname(__file__),
    files = file_list,
    params = vp.params.combinations(["x1", "x2"],
                                    [0.1, 0.2, 0.4]),
    commands = vp.command(cmd),
    out_dir = vp.out_dir.flat_from("results"),
    save_if = method1_is_SCF
)
"""

        
