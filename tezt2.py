# library
import random
import math

# Struktur data:
koordinat = [(0,0), (10,5), (20,10), (15,3)]

print("Daftar Koordinat:")

# Struktur kontrol:
for i, wp in enumerate(koordinat):
    print(i+1, "-", wp)
    
target = random.choice(koordinat)

jarak = math.sqrt(target[0]**2 + target[1]**2)

print("\nKoordinat yang dipilih:", target)

if jarak > 15:
    print("Koordinat jauh")
else:
    print("Koordinat dekat")