'''
Ini merupakan materi keempat
'''
## Tipe data standar
# Angka bulat satuan (Integer)
tipe_int = 10
print('Angka = ',tipe_int)
print('Tipe angka = ', type(tipe_int))

# Angka berkoma (Float)
tipe_float = 10.0
print('\nAngka = ',tipe_float)
print('Tipe angka = ', type(tipe_float))

# Kumpulan karakter (String)
tipe_string = 'halo dunia'
print('\nTeks = ',tipe_string)
print('Tipe teks = ', type(tipe_string))

# Biner - True or False (Boolean)
tipe_biner = True
print('\nTeks = ',tipe_biner)
print('Tipe teks = ', type(tipe_biner))

## Tipe data khusus
# Bilangan complex (Complex)
tipe_complex = complex(1,2)
print('\nAngka = ',tipe_complex)
print('Tipe angka = ', type(tipe_complex))

# Tipe data dari bahasa c
from ctypes import c_double
tipe_c_double = c_double(10.2)
print('\nAngka = ',tipe_c_double)
print('Tipe angka = ', type(tipe_c_double))
