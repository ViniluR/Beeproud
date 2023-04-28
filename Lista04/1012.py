a, b, c = input().split(" ")
A = float(a)
B = float(b)
C = float(c)

triang = A * C / 2
circ = 3.14159 * C**2
trap = (A + B) / 2 * C
quadra = B * B
retang = A * B

print(f'TRIANGULO: {triang:.3f}')
print(f'CIRCULO: {circ:.3f}')
print(f'TRAPEZIO: {trap:.3f}')
print(f'QUADRADO: {quadra:.3f}')
print(f'RETANGULO: {retang:.3f}')