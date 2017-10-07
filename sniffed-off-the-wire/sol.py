'''
Check traffic: tcpstr1.txt file. All characters are of the form

ASCII notation: .[<number>;<number>H<char>
Hex notation:   1b5b<number>3b<number>48<char>

Refer to http://www.acscontrol.com/knowledgebase/article.asp?ID=63 (find 3b in the page).
Data looks like
number (1st) = row
number (2nd) = column
char = data
'''

# import pprint
import time

with open('tcpstr1.txt','r') as f:
    s = f.read()
    l1 = s.split('.[')

l1 = l1[1:len(l1)-1]
ll1 = len(l1)
print 'len l1:', ll1

R = []
C = []
RC = []
V = []
for x in l1:

    if ';' not in x:
        print 'no ;'
        time.sleep(5)
    a,b = x.split(';')
    R += [int(a)]

    if 'H' not in b:
        print 'no H'
        time.sleep(5)
    c,d = b.split('H',1)
    C += [int(c)]
    V += [d]
    RC += [(int(a), int(c))]

# print 'V:', ''.join(V)
print 'R:', set(R), len(set(R))
print 'C:', set(C), len(set(C))
print 'V:', sorted(set(V)), len(set(V))
print  'RC:', len(set(RC))
''' len(set(RC))=2k and len(RC)=20K means each element might occur 10 times '''

lr = max(R)+1
lc = max(C)+1
print 'lr:', lr, 'lc:', lc

'''
    initialize 3D array of form row * depth * column
    1st element of depth dimension stores the next index to put element into
    for a particular row and column
'''
d = ll1 / (lr*lc) + 1
mat = [[[1 for k in xrange(lc)] for j in xrange(d)] for i in xrange(lr)]
print 'mat dim:', len(mat), len(mat[0]), len(mat[0][0])

# pprint.pprint(mat)

for i in range(ll1):
    x= R[i]-1
    y = mat[R[i]-1][0][C[i]-1]
    z = C[i]-1
    # print 'pos:', x, y, z
    mat[x][y][z] = V[i]
    mat[x][0][z] += 1

for k in range(1,d):
    print k
    for i in range(lr):
        print ''.join(str(x) for x in mat[i][k])
