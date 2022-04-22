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
    def __init__(self):
        self.id = None
        self.email = None
        self.isbn = None
        self.judul = None
        self.durasi = None
        self.tanggalPeminjaman = None
        self.tanggalPengembalian = None
        self.status = None
        self.pengarang = None
        self.penerbit = None
        self.tahunTerbit = None
        self.kategori = None

