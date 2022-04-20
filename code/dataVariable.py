from codecs import namereplace_errors

class user:
    def __init__(self):
        self.email = None
        self.password = None
        self.nama = None
        self.alamat = None
        self.asalInstitusi = None
        self.telepon = None

class book:
    def __init__(self):
        self.isbn = None
        self.judul = None
        self.jumlahKetersediaan = None
        self.pengarang = None
        self.penerbit = None
        self.tahunTerbit = None
        self.kategori = None

class pinjamBuku:
    def __init__(self, id, email, isbn, durasi, tanggalPeminjaman, tanggalPengembalian,status):
        self.id = id
        self.email = email
        self.isbn = isbn
        self.durasi = durasi
        self.tanggalPeminjaman = tanggalPeminjaman
        self.tanggalPengembalian = tanggalPengembalian
        self.status = status
