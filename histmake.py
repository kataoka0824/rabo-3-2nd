import csv
import numpy as np
import matplotlib.pyplot as plt
count=np.array([0]*60)
x=np.zeros(60)

#データを取り込んで数値化
number=int(input("num="))
file="data_1_/data_1_{0}.csv".format(number)
print(file)
with open(file,"r") as f:
    reader = csv.reader(f)
    l = [row for row in reader]
l_1=[]
for i in range(50):
    for j in range(2):
        l_2=[float(s) for s in l[i]]
    l_1.append(l_2)
#データの集計
for i in range(60):
    x[i]=number-3+0.05+i/10
for i in range(50):
    for j in range(60):
        if l_1[i][1]>number-3+j/10 and l_1[i][1]<number-3+(j+1)/10:
            count[j]+=1
#グラフの作成
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xticks(np.linspace(number-3,number+3,7))
ax.set_xticks(np.linspace(number-3,number+3,31),minor=True)
ax.set_yticks(np.linspace(0,50,11))
ax.grid(axis="y")
plt.axvline(x=number,color="r")
plt.bar(x,count,width=0.1)
plt.show()
