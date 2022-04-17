from ast import Global
from tokenize import String
from wsgiref import headers
import requests 
from dataVariable import *

#def variable global

def init():
    global klien
    global print_nama_tamu
    print_nama_tamu = ''
    klien = user

# /////////////////////////////////////////// LOGIN PAGE ////////////////////////////////////////////////

s = requests.Session()

# Authentification Login
url = 'http://192.168.1.105:8080/api/'
def login(email,password):
    # routes='/basic-auth/hubla/pass'
    global s
    payload={'email':email,'password':password}
    routes='auth/signin'
    s = requests.Session()
    r = s.post(url+routes,data=payload)
    cookie_params = r.cookies.items()
    print(r.text)

    #Store Data Tabel Klien ke Lokal - Enrico
    klien.nama = r.json()['nama']
    klien.email = r.json()['email']
    klien.telepon = r.json()['telepon']
    klien.alamat = r.json()['alamat']
    klien.asalInstitusi = r.json()['asalInstitusi']
    print_nama_tamu = "Selamat datang, " + klien.nama + " di CodexLib Bandung!"

    if(r.status_code == 200):
        print('Login Success')
        return {'status':True, 'message':'Login Success'}
    else:
        print("Login Failed")
        return {'status':False, 'message':r.json()['message']}
    


#Sign Up
def signUp(nama,email,password,alamat,institusi,telepon):
    routes = 'auth/signup'
    payload={'nama':nama,
             'email':email,
             'password':password,
             'alamat':alamat,
             'asalInstitusi':institusi,
             'telepon':telepon}
    r = requests.post(url+routes,data=payload)
    
    if(r.status_code == 200):
        print('Signup Success')
        return {'status':True, 'message':r.json()['message']}
    else:
        print("Signup Failed")
        return {'status':False, 'message':r.json()['message']}

#Sign Out
def signOut():
    routes = 'auth/signout'
    r = requests.post(url+routes)
    s.cookies.clear()
    print(r.text)

# /////////////////////////////////////////// DASHBOARD ////////////////////////////////////////////////

def get_latest_library():
    routes = 'library/getlibrary'
    r = s.get(url+routes)
    books = r.json()

    books_lib = []
    for i in books:
        _book = book()
        _book.isbn = i['isbn']
        _book.judul = i['judul']
        _book.jumlahKetersedian = i['jumlahKetersediaan']
        _book.pengarang = i['pengarang']
        _book.penerbit = i['penerbit']
        _book.kategori = i['kategori']
        books_lib.append(_book)
    return books_lib

def konfirmasi_peminjaman(email,isbn,tanggalPeminjaman,
                          durasi, tanggalPengembalian, status):
    routes = 'sirkulasi/pinjambuku'
    payload = {'email':email,
               'isbn':isbn,
               'tanggalPeminjaman':tanggalPeminjaman,
               'durasi':durasi,
               'tanggalPengembalian':tanggalPengembalian,
               'status':status}
    r = s.post(url+routes,data=payload)
    if(r.status_code == 200):
        print('Peminjaman Berhasil')
        return {'status':True, 'message':r.json()['message']}
    else:
        print("Peminjaman Gagal")
        return {'status':False, 'message':r.json()['message']}

def get_riwayat(email):
    routes = 'getriwayat'
    payload = {'email':email}
    r = s.post(url+routes,data=payload)
    print(r)
    peminjamans = r.json()

    riwayat = []
    for i in peminjamans:
        _peminjaman = pinjamBuku()
        _peminjaman.id = i['id']
        _peminjaman.email = i['email']
        _peminjaman.isbn = i['isbn']
        _peminjaman.durasi = i['durasi']
        _peminjaman.tanggalPeminjaman = i['tanggalPeminjaman']
        _peminjaman.tanggalPengembalian = i['tanggalPengembalian']
        _peminjaman.status = i['status']
        riwayat.append(_peminjaman)
    return riwayat

def konfirmasi_pengembalian(idPeminjam,status,noResi,jasaEkspedisi):
    routes = 'sirkulasi/kembalikanbuku'
    payload = {'idPeminjam':idPeminjam,
               'status':status,
               'noResi':noResi,
               'jasaEkspedisi':jasaEkspedisi}
    r = s.post(url+routes,data=payload)
    if(r.status_code == 200):
        print('Pengembalian Berhasil')
        return {'status':True, 'message':r.json()['message']}
    else:
        print("Pengembalian Gagal")
        return {'status':False, 'message':r.json()['message']}

def konfirmasi_perpanjangan(idPeminjam,durasi,tanggalPengembalian):
    routes = 'sirkulasi/perpanjangpeminjaman'
    payload = {'idPeminjam':idPeminjam,
               'durasi':durasi,
               'tanggalPengembalian':tanggalPengembalian}
    r = s.put(url+routes,data=payload)
    if(r.status_code == 200):
        print('Perpanjangan Berhasil')
        return {'status':True, 'message':r.json()['message']}
    else:
        print("Perpanjangan Gagal")
        return {'status':False, 'message':r.json()['message']}

def change_profile(email, nama, alamat, asalInstitusi, telepon):
    routes = 'profile/changeprofile'
    payload = {'email': email,
                'nama': nama,
                'alamat': alamat,
                'asalInstitusi': asalInstitusi,
                'telepon': telepon}
    r = s.put(url+routes,data=payload)

    klien.nama = r.json()['nama']
    klien.email = r.json()['email']
    klien.telepon = r.json()['telepon']
    klien.alamat = r.json()['alamat']
    klien.asalInstitusi = r.json()['asalInstitusi']

    if(r.status_code == 200):
        print('Update Profile Success')
        return {'status':True, 'message':'Update Profile Success'}
    else:
        print("Update Profile Failed")
        return {'status':False, 'message':r.json()['message']}

def password_check(passwd):
      
    SpecialSym =['$', '@', '#', '%']
    val = True
      
    if len(passwd) < 8:
        print('length should be at least 8')
        val = False
          
    # if len(passwd) > 20:
    #     print('length should be not be greater than 8')
    #     val = False
          
    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False
          
    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False
          
    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False
          
    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val


init()


# login('admin@gmail.com','Admin1234')
# riwayat = get_riwayat('admin@gmail.com')
# # riwayat = get_latest_library()
# print(riwayat[1].isbn)
# signOut()
# get_latest_library()








