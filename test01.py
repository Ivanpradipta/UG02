a=float(input('jam yang akan dikonversikan ke dalam menit dan detik = '))
Menit = a*60
Detik = a*3600
print(a,'jam = ',round(Menit,3),'menit')
print(a,'jam = ',round(Detik,3),'detik')

b=float(input('menit yang akan dikonversikan ke dalam jam dan detik = '))
Jam = b/60
Detik = b*60
print(b,'menit = ',round(Jam,3),'jam')
print(b,'menit = ',round(Detik,3),'detik')

c=float(input('detik yang akan dikonversikan ke dalam jam dan menit = '))
Jam = c/3600
Menit = c/60
print(c,'detik = ',round(Jam,3),'jam')
print(c,'detik = ',round(Menit,3),'menit')

        
