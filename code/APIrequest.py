from ast import Global
from select import KQ_FILTER_SIGNAL
from wsgiref import headers
import requests 
from dataVariable import *

#def variable global

def init():
    global klien
    klien = user

# /////////////////////////////////////////// LOGIN PAGE ////////////////////////////////////////////////

s = requests.Session()

# Authentification Login
url = 'http://192.168.1.108:8080/api/'
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

    if(r.status_code == 200):
        print('Login Success')
        return {'status':True, 'message':'Login Success'}
    else:
        print("Login Failed")
        return {'status':False, 'message':r.json()['message']}
    


#Sign UP
def signUp(nama,email,password,alamat,institusi,telepon):
    routes = 'auth/signup'
    payload={'nama':nama,
             'email':email,
             'password':password,
             'alamat':alamat,
             'asalInstitusi':institusi,
             'telepon':telepon}
    r = requests.post(url+routes,data=payload)
    print(r.text)


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

def get_riwayat(email):
    routes = 'api/getriwayat'
    payload = {'email':email}
    r = s.post(url+routes,data=payload)

def konfirmasi_pengembalian(idPeminjam,status,noResi,jasaEkspedisi):
    routes = 'api/sirkulasi/kembalikanbuku'
    payload = {'idPeminjam':idPeminjam,
               'status':status,
               'noResi':noResi,
               'jasaEkspedisi':jasaEkspedisi}
    r = s.post(url+routes,data=payload)

def konfirmasi_perpanjangan(idPeminjam,durasi,tanggalPengembalian):
    routes = 'api/sirkulasi/perpanjangpeminjaman'
    payload = {'idPeminjam':idPeminjam,
               'durasi':durasi,
               'tanggalPengembalian':tanggalPengembalian}
    r = s.put(url+routes,data=payload)


<<<<<<< HEAD
# login('admin@gmail.com','Admin1234')
=======
init()
# login('admin@gmail.com','pass')
>>>>>>> 2af567d41fa9f75340c1f06818dce26e263995ea
# books = get_latest_library()
# print(books[1].kategori)
# signOut()
# get_latest_library()








