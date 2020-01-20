HOME = '/Users/alexaksentyev/REPOS/NICA-FS/'

el_dict = {
    'DRIFT': ('DL', 1),
    'QUADRUPOLE': ('QUAD', 2),
    'SBEND': ('SBEND', 3),
    'RBEND': ('RBEND', 3),
    'SOLENOID': ('SOLENOID',2)
    }


fout = open(HOME+'src/setups/nica_24sol_rbend-sequence.fox','w')
with open(HOME+'madx-scripts/nica_24sol_rbend.seq', 'r') as fin:
    for cnt, line in enumerate(fin):
        try:
            com, elem = line.split(sep='\t')
            com = com.strip(':')
            elem = elem.strip(';\n').split(',')
            elem_name, n_arg = el_dict[elem[0]]
            n_zeros = n_arg-len(elem[1:])
            elem.extend(['name=0' for i in range(n_zeros)])
            out_string = el_dict[elem[0]][0] + ' '
            for par in elem[1:]:
                par_val = par.split('=')[1]
                if (par_val.find('+',1)>0 or par_val.find('-',1)>0):
                    par_val = '('+par_val+')'
                out_string += par_val+' '
            out_string += ';' + '{' + com + '}\n'
            fout.write(out_string)
            print(cnt+1, out_string)
            out_string=''
        except ValueError:
            fout.close()
        
fout.close()
