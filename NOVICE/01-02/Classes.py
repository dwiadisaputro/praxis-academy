####---Scopes and Namespaces Example
# def scope_test():
#     def do_local():
#         spam = "local spam"
    
#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"

#     def do_global():
#         global spam 
#         spam = "global spam"
    
#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)

# scope_test()
# print("In global scope:", spam)

###--A First Look at Classes
# class mahasiswa():
#     jurusan = 'teknik industri'
#     __nilai = 0 #privat

#     def __init__(self, input_nama, input_nim): #sifat publik
#         self.nama = input_nama
#         self.nim = input_nim

#     def tugas(self, input_nilai):
#         self.__nilai += input_nilai
    
#     def tes(self, input_nilai):
#         self.__nilai += input_nilai

#     def check_status(self):
#         if self.__nilai <= 50 :
#             print(self.nama, 'Kurang Memenuhi')
#         else:
#             print(self.nama, 'Lulus')

# adi = mahasiswa('adiputra', 1234568)

# adi.tugas(70)
# adi.tes(90)
# adi.check_status()

#     def kegiatan(self, kondisi):
#         print(self.name, 'belajar python dasar', kondisi)
# doni = student()
# syafak = student()

# doni.name = 'Doni salman'
# syafak.name = 'Syafak Abdillah'

# print(doni.name)
# print(syafak.name)

# doni.kegiatan('back and')




# class MyClass:
#     i = 12345

#     def f(self):
#         return 'Hello MyClass'
# x = MyClass()
# def __init__(self):
#     self.data = []

# x = MyClass()

##blm ketemu
# class complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart
# # x = Complex(3.0, -4.5)
# print(x.r, x.i)

# x.counter = 1
# while x.counter < 10:
#     x.counter = x.counter * 2
# print(x.counter)
# del x.counter



# class Mahasiswa():
#     def __init__(self, nama, asal, peliharaan):
#         self.nama = nama
#         self.asal = asal
#         self.peliharaan = peliharaan
#     def id_mahasiswa(self):
#         print('nama:',self.nama, '\nasal:', self.asal, '\npeliharaan:', self.peliharaan)

# class Dosen(Mahasiswa):
#     def id_mahasiswa(self):
#         print('Kucing anggora warna pink')

 
# Mahasiswa1 = Mahasiswa('Adi', 'Pati', 'Anggora')
# Mahasiswa2 = Dosen('Adi', 'Pati', 'Anggora')

# Mahasiswa1.id_mahasiswa()
# Mahasiswa2.id_mahasiswa()


#### ------Tugas Class di module




# # menyembunyikan data(data hiding)

# class Counter:
#      __secret_count = 0
     
#      def count(self):
#          self.__secret_count += 1
#          print(self.__secret_count)

# counter = Counter()
# counter.count()
# counter.count()
##print(counter.__secret_count)


#---#
# class praxis:
#     pass
# saya = ("manusia")
# kami = ("bersatu")
# kita = ("jadisatu")
# kami = ("bersatu")

# print(saya)
# print(kami)
# print(kita)
# print(kami)

#--#
# class praxis():
#     backend = 'backend'
    
    
#     def mergawe(self, keadaan):
#         print(self.backend, "coding asyik", keadaan)

#     def design(self, ramadlan):
#         print(self.backend, "masuk kelas", ramadlan)

# kamu = praxis()
# kita = praxis()
# kami = praxis()
# saya = praxis()
# dia = praxis()

# kamu.backend = 'kamu capek'
# kita.backend = 'kita lahir'
# kami.backend = 'kami satu'
# saya.backend = 'saya sama'
# dia.backend = 'dia karma'

# kamu.mergawe('nandur')
# kita.mergawe('ngarit')
# kami.design('kata')
# saya.design('banner')
# dia.mergawe('miyang')

#---#
# class praxis:
#     tricks = [] 
    
#     def __init__ (self, name):
#         self.name = name
        
#     def add_trick(self, trick):
#         self.tricks.append(trick)
# d = praxis('adi')
# e = praxis('adi')
# d.add_trick('roll over')
# e.add_trick('play dead')
# print(d.tricks)


#--#
class MyClass:
    """A simple example class"""
    i = 12345
    
    def f(self):
        return 'hello world'

def __init__(self):
    self.data = []

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
x.r, x.i
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter


#---#
class Dog:
    kind = 'canine'     # class variable shared by all instances
    def __init__(self, name):
        self.name = name # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind) # shared by all dogs
print('e.kind')
print(d.name)
print(e.name)


# #--#
# class praxis:
#     blackend = 'timur'
#     frondend = 'barat'
# w1 = praxis()
# print(w1.blackend, w1.frondend)

# w2 = praxis()
# w2.frondend = 'tengah'
# print(w2.blackend, w2.frondend)


# #--#
# class pra?s :", praxis.jumlah_praxis)



# ##--##
# class Reverse:
#     """Iterator for looping over a sequence backwards."""
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]
# rev = Reverse('spam')
# iter(rev)
# for char in rev:
#     print(char)

# def reverse(data):
#     for index in range(len(data)-1, -1, -1):
#         yield data[index]
# for char in reverse('golf'):
#     print(char)

# print(sum(i*i for i in range(10))) 
# syafak = [10, 20, 30]
# doni = [7, 5, 3]
# print(sum(x*y for x,y in zip(syafak, doni))) 

### unique_words = set(kata demi baris di halaman demi kata di baris.split())
### pidato perpisahan = max((student.gpa, student.name) untuk mahasiswa di lulusan)
# data = 'kafays'
# print(list(data[i] for i in range(len(data)-1, -1, -1)))