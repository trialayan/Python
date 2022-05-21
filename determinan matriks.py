'''
-Determinan Matriks- 

Kamus data :
ordo = var input(str)
row1_a = var input(int)
row1_b = var input(int)
row1_c = var input(int)
row1_d = var input(int)
row2_a = var input(int)
row2_b = var input(int)
row2_c = var input(int)
row2_d = var input(int)
row3_a = var input(int)
row3_b = var input(int)
row3_c = var input(int)
row3_d = var input(int)
hasil = var penampung hasil determinan

'''

# input
ordo = str(input('\n Ordo matriks (2/3/4) : '))
print('==========================')

# process
if (ordo == '2'):
    print ('---Bentuk Matriks---')
    # Baris 1
    print('--Baris 1--')
    row1_a = int(input('Baris1 kolom1 : '))
    row1_b = int(input('Baris1 kolom2 : '))
    ## Baris 2
    print('--Baris 2--')
    row2_a = int(input('Baris2 kolom1 : '))
    row2_b = int(input('Baris2 kolom2 : '))

    # output
    print('==========================')
    print(f'Matriks :\n{row1_a}  {row1_b}')
    print(f'{row2_a}  {row2_b}')
    print('==========================')

    # process determinan
    hasil = (row1_a * row2_b) - (row2_a * row1_b)
    print(f'det : {hasil}')

elif (ordo == '3'):
    print ('---Bentuk Matriks---')
    # Baris 1
    print('--Baris 1--')
    row1_a = int(input('Baris1 kolom1 : '))
    row1_b = int(input('Baris1 kolom2 : '))
    row1_c = int(input('Baris1 kolom3 : '))
    ## Baris 2
    print('--Baris 2--')
    row2_a = int(input('Baris2 kolom1 : '))
    row2_b = int(input('Baris2 kolom2 : '))
    row2_c = int(input('Baris2 kolom3 : '))
    ### Baris 3
    print('--Baris 3--')
    row3_a = int(input('Baris3 kolom1 : '))
    row3_b = int(input('Baris3 kolom2 : '))
    row3_c = int(input('Baris3 kolom3 : '))

    # output
    print('==========================')
    print(f'Matriks :\n{row1_a}  {row1_b}  {row1_c}')
    print(f'{row2_a}  {row2_b}  {row2_c}')
    print(f'{row3_a}  {row3_b}  {row3_c}')
    print('==========================')

    # process determinan
    hasil = ((row1_a * row2_b * row3_c) + (row1_b * row2_c * row3_a) + (row1_c * row2_a * row3_b)) - ((row1_c * row2_b * row3_a) + (row1_a * row2_c * row3_b) + (row1_b * row2_a * row3_c))
    print(f'det : {hasil}')

elif (ordo == '4'):
    print ('---Bentuk Matriks---')
    # Baris 1
    print('--Baris 1--')
    row1_a = int(input('Baris1 kolom1 : '))
    row1_b = int(input('Baris1 kolom2 : '))
    row1_c = int(input('Baris1 kolom3 : '))
    row1_d = int(input('Baris1 kolom4 : '))
    ## Baris 2
    print('--Baris 2--')
    row2_a = int(input('Baris2 kolom1 : '))
    row2_b = int(input('Baris2 kolom2 : '))
    row2_c = int(input('Baris2 kolom3 : '))
    row2_d = int(input('Baris1 kolom4 : '))
    ### Baris 3
    print('--Baris 3--')
    row3_a = int(input('Baris3 kolom1 : '))
    row3_b = int(input('Baris3 kolom2 : '))
    row3_c = int(input('Baris3 kolom3 : '))
    row3_d = int(input('Baris1 kolom4 : '))
    #### Baris 4
    print('--Baris 4--')
    row4_a = int(input('Baris3 kolom1 : '))
    row4_b = int(input('Baris3 kolom2 : '))
    row4_c = int(input('Baris3 kolom3 : '))
    row4_d = int(input('Baris1 kolom4 : '))


    # output
    print('==========================')
    print(f'Matriks :\n{row1_a}  {row1_b}  {row1_c}  {row1_d}')
    print(f'{row2_a}  {row2_b}  {row2_c}  {row2_d}')
    print(f'{row3_a}  {row3_b}  {row3_c}  {row3_d}')
    print(f'{row4_a}  {row4_b}  {row4_c}  {row4_d}')
    print('==========================')

    # process determinan
    hasil = ((row1_a * row2_b * row3_c * row4_d) + (row1_b * row2_c * row3_d * row4_a) + (row1_c * row2_d * row3_a * row4_b) + (row1_d * row2_a * row3_b * row4_c)) - ((row4_a * row3_b * row2_c * row1_d) + (row4_b * row3_c * row2_d * row1_a) + (row4_c * row3_d * row2_a * row1_b) + (row4_d * row3_a * row2_b * row1_c))
    print(f'det : {hasil}')

else :
    print('Masukkan ordo matriks sesuai option!')