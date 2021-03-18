# Membuat Fungsi Baru 'urai'
def urai ():

# Input Data 'Code'    
    code = 'Code'
# Variable Kosong untuk Penampungan Niai Baru
    c = ''
# Perulangan dengan 'For Loop'
    for i in code:
        c += i
        print(c)
    print('')

# Input Data 'Python'  
    python = 'Python'
# Variable Kosong untuk Penampungan Niai Baru
    p = ''
# Perulangan dengan 'For Loop'
    for i in python:
        p += i
        print(p)
    print('')

# Input Data 'Purwadhika'
    purwadhika = 'Purwadhika'
# Variable Kosong untuk Penampungan Niai Baru
    w = ''
# Variable Kosong untuk Penampungan Niai Baru
    for i in purwadhika:
        w += i
        print(w)
    print('')

# Memanggil Fungsi 'urai'
urai()

print(70*'=')
print('')

# Membuat Fungsi Baru 'rajut'
def rajut ():
    
# Input Data Manual 'CCoCodCode'  
    code = 'CCoCodCode'
# Mengambil Sebagian Nilai dengan 'negative slice'
    c = code[-4:]
    print('Huruf tak beraturan', code)
    print('Katanya adalah',c)
    print('')

# Input Data Manual 'PyPytPythPythoPython'  
    python = 'PyPytPythPythoPython'
# Mengambil Sebagian Nilai dengan 'negative slice'
    p = python[-6:]
    print('Huruf tak beraturan', python)
    print('Katanya adalah',p)
    print('')

# Input Data Manual 'PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'  
    purwadhika = 'PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'
# Mengambil Sebagian Nilai dengan 'negative slice'
    w = purwadhika[-10:]
    print('Huruf tak beraturan', purwadhika)
    print('Katanya adalah',w)
    print('')

rajut ()