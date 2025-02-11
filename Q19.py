#Calcula o produto escalar de dois vetores Vi e Ui Recursivamente

def escalar(n,vi,ui):
 if n==0:
    return 0
 return vi[n-1] * ui[n-1] + escalar(n-1,vi,ui)

n = int(input())
ui = []
vi = []
for i in range(n):
    ui.append(int(input()))

for i in range(n):
    vi.append(int(input()))
print(f'Produto escalar: {escalar(n,vi,ui)}')