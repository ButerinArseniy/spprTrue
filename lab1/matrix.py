import numpy as np

matrix  = np.array( [[ 0, 12,  6,  3,  9],
[ 1, 12,  6,  6,  2],
 [ 3,  4,  3, 12,  5],
 [ 2, 12, 11,  8,  7],
 [ 2,  3,  2,  6, 10]])
q=[0.0, 0.0, 1.0, 0.0, 0.0]
p=[0.95, 0.0, 0.05, 0.0, 0.0]
answer = {}
lower_price = max([min(x) for x in matrix])
upper_price = min([max(x) for x in matrix.T])
print(lower_price, upper_price)
if lower_price==upper_price:print("седловая точка есть", f"ответ v={lower_price}") 

else:
  buff=0
  for i,pin in zip(matrix,p):
    buff+=pin*sum([x*y for x,y in zip(i,q)])
  answer["H(P,Q)"]=buff
  for k in range(len(q)): 
    answer["H(P,B{})".format(k+1)]=sum([p[i]*matrix[i][k] for i in range(len(p))])
for i in [(x,y) for x,y in answer.items()]:
  print("Ответ выйгрыш игрока А в ситуации {0[0]} = {0[1]}".format(i))