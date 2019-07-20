import numpy as np
matrixA=[]
for i in open(r'D:\NTU_ML2017_Hung-yi-Lee_HW\HW0\Q1\data\matrixA.txt'):
    row=[int(x) for x in i.split(',')]
    matrixA.append(row)
    
matrixB=[]
for i in open(r'D:\NTU_ML2017_Hung-yi-Lee_HW\HW0\Q1\data\matrixB.txt'):
    row = [int(x) for x in i.split(',')]
    matrixB.append(row)


matrixA=np.array(matrixA)
matrixB=np.array(matrixB)
ans = matrixA.dot(matrixB)
ans.sort(axis=1)
np.savetxt("Q1ans.txt",ans,fmt='%d',delimiter='\r\n')


from PIL import Image

lena = Image.open("lena.png")
lena_modified = Image.open("lena_modified.png")

w, h = lena.size
for j in range(h):
    for i in range(w):
        if lena.getpixel((i, j)) == lena_modified.getpixel((i, j)):
            lena_modified.putpixel((i, j), 255)

lena_modified.show()
lena_modified.save("ans_two.png")
