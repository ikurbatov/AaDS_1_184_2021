def output(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end = ' ')
        print()
def diagonal(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i==j:
                print(m[i][j]*3, end = ' ')
            else:
                print(m[i][j], end = ' ')
        print()
M=[[9,18,2],[15,2,1],[10,8,2]]
output(M)
print("###########################")
diagonal(M)
