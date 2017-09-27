print("Project Euler-Problem 1")
print("1000e kadar 3e ve 5e bölünebilen sayıların toplamı:")
toplam=0
for i in range(0,1000):
  
    if i % 3==0 or i % 5==0:        
        toplam=toplam+i
print(toplam)  