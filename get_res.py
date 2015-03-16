import os, shutil
from sys import argv

def find_res(src):
    res = []
    for root, dirs, files in os.walk(src):
        files = [ fi for fi in files if fi.endswith(".xml") ]
        for f in files:
            if 'stri' in f  and 'donot' not in f or 'arra' in f and 'donot' not in f:
                res.append(str( os.path.join(root, f)))
    res[:] = [p for p in res if '/values/' in p]
    return res



def copy_res(src, dst):
    res = find_res(src)
    for path in res:
        #Concate the dst path
        head, tail = os.path.split(path)
        head = head.rsplit('/')
        head = dst + '/' + '/'.join(head[head.index('packages')::])
        #Create the dst path
        if not os.path.exists(head):
            os.makedirs(head)
        #Copy the res
        shutil.copy(path, head)
        print 'copied ' + path

if __name__ == "__main__":
        copy_res(argv[1], argv[2])

