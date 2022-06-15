class siswa():
    def __init__(self, Nama, kls, absen, gender):
        self.Nama = Nama
        self.kls = kls
        self.absen = absen
        self.gender = gender
    def masuk (self, Nama, kls, absen, gender):
        self.Nama = Nama
        self.kls = kls
        self.absen = absen
        self.gender = gender
    def keluar (self):
        print('Nama Lengkap     :' + self.Nama)
        print('KELAS           :' + self.kls)
        print('ABSEN           :' + self.absen)
        if self.gender in [ 'L', 'l']:
            gender = 'laki-laki'
        else:
            gender ='perempuan'
        print('gender   :' + gender)
        

print('=================================')
print('     ABSEN KELAS      ')
print('=================================')
Nama    = input('Nama Lengkap              :')
kls  = input('kelas            :')
absen  =input('absen             :')
gender  = input('gender L/P   :')
print('===================================================')

proses = siswa (Nama, kls, absen, gender)
print(proses.keluar())