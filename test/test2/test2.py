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


    
