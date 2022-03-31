'''
Manual

- persyaratan = sarjana and <30tahun
- P and R = >30tahun
- S Or T = <30tahun
- Q and T = diploma
- R or S = sarjana

Pelamar P dan R tidak memenuhi syarat karena berumur >30tahun
Pelamar Q dan T tidak memenuhi syarat karena memiliki tingkat pendidikan diploma

berarti yang tersisa dari ke-5 pelamar adalah S
'''

#input
def pelamar():
    print ('pelamar : \nP \nQ \nR \nS \nT')

pelamar()

a1='sarjana'
a2='diploma'
b1='<30thn'
b2='>30thn'

opt = str(input('Masukan pelamar: '))
syarat = a1 and b1

#process
if opt.upper() == 'P':
    data1 = b2
    if data1 == syarat:
        print('Data memenuhi syarat! \n Anda diterima sebagai staf administrasi!')
    else:
        print('Maaf, data tidak sesuai dengan persyaratan!')

elif opt.upper() == 'Q':
    data2 = a2
    if data2 == syarat:
        print('Data memenuhi syarat! \n Anda diterima sebagai staf administrasi!')
    else:
        print('Maaf, data tidak sesuai dengan persyaratan!')

elif opt.upper() == 'R':
    data3 = b2 and (a1 or a2)
    if data3 == syarat:
        print('Data memenuhi syarat! \n Anda diterima sebagai staf administrasi!')
    else:
        print('Maaf, data tidak sesuai dengan persyaratan!')

elif opt.upper() == 'S':
    data4 = (a1 or a2) and (b1 or b2)
    if data4 == syarat:
        print('Data memenuhi syarat! \n Anda diterima sebagai staf administrasi!')
    else:
        print('Maaf, data tidak sesuai dengan persyaratan!')

elif opt.upper() == 'T':
    data5 = (b1 or b2) and a2
    if data5 == syarat:
        print('Data memenuhi syarat! \n Anda diterima sebagai staf administrasi!')
    else:
        print('Maaf, data tidak sesuai dengan persyaratan!')

else:
    print('data pelamar tidak terdaftar')


