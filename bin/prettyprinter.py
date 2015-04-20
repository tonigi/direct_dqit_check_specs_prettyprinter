# Conversion exercise Toni Giorgino CNR-IN

import jinja2
import xlrd
import csv
import sys
import re


def simplify_1(inp,fn):
    "Simplify @(x) ...x... ->  ...fieldname..."
    arg=re.search(r'@\(([a-z]+)\)',inp)
    if arg:
        inp=re.sub(r'@\(([a-z]+)\)','',inp) # remove @(v)
        inp=re.sub(r'\b'+arg.group(1)+r'\b',fn,inp) # \b v \b -> 
        inp=re.sub(r"dstr2ts\('yyyy-mm-dd','([-0-9]+)'\)",r"\1",inp) # dates
    return inp

def simplify_n(inp):
    "Simplify @(x) x.yz -> yz"
    arg=re.search(r'@\(([a-z]+)\)',inp)
    if arg:
        inp=re.sub(r'@\(([a-z]+)\)','',inp) # remove @(v)
        inp=re.sub(r'\b'+arg.group(1)+r'\.\b',"",inp)  # \b v. \b -> 
        inp=re.sub(r"dstr2ts\('yyyy-mm-dd','([-0-9]+)'\)",r"\1",inp) # dates
    return inp


if len(sys.argv)!=2:
    sys.exit("Need an argument")

filename=sys.argv[1]


"""
wb=xlrd.open_workbook(filename)
s=wb.sheet_by_index(0)          # trust 1 worksheet

header=s.row_values(0)          # get header, " "->"_"
header=list(map( lambda x: re.sub(r' ','_',x),header))

# Loop over rows to read
specs=[];
for r in range(1,s.nrows):
    rv=s.row_values(r)          # read rows, dict them
    rd=dict(zip(header,rv))
    specs.append(rd)
"""

# Dictreader is not optimal because I'd like to fix the keys
specs=[]
fn=open(filename)
dr=csv.reader(fn)
header=next(dr)
header=list(map( lambda x: re.sub(r' ','_',x),header))
for row in dr:
    rd=dict(zip(header,row))
    specs.append(rd)

    

# Re-loop to fixup
tablelist={};
for rn,rd in enumerate(specs):
    tablelist[rd['Database_table']]=1;
    if rd['Xcheck']=='x':
        rd['Error_condition_s']=simplify_n(rd['Error_condition'])
        rd['Warning_condition_s']=simplify_n(rd['Warning_condition'])
    else:
        rd['Error_condition_s']=simplify_1(rd['Error_condition'],rd['Field'])
        rd['Warning_condition_s']=simplify_1(rd['Warning_condition'],rd['Field'])
    specs[rn]=rd


    
template = jinja2.Environment(
    loader=jinja2.PackageLoader('prettyprinter', '../etc'),
    autoescape=True).get_template('template.html')

print(template.render(  LIST_OF_TABLES=tablelist.keys(),
                        SPECS=specs,
                        SPEC_FILE_NAME=filename,
                        ) )

sys.exit()
