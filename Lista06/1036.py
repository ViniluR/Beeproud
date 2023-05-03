A, B, C = input().split(" ")
a = float(A)
b = float(B)
c = float(C)

delta = b**2 - (4 * a * c)

raiz = delta**(1/2)

if a == 0:
 print('Impossivel calcular')
  
elif delta < 0:
 print('Impossivel calcular')
  
elif delta == 0:
 raiz_1 = (-b + raiz) / (a * 2)
 print('Raiz = ', raiz_1)

else:
 raiz_1 = (-b + raiz) / (a * 2)
 raiz_2 = (-b - raiz) / (a * 2)
 print(f'R1 = {raiz_1:.5f}')
 print(f'R2 = {raiz_2:.5f}')