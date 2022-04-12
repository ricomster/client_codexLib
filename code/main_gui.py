from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
from ttkwidgets import Table
import json

# Progres: table udah, search mechanism dan printing ke table juga udah bisa
# opsi solusi masalah soal pinjam: input nilai aja, unique ID aja, atau pake ISBN

# root window
root = Tk()
root.geometry('1280x720')
root.title('CodexLib @Bandung (Client App)')

#Load Images
logo_app = Image.open("aset_gui/512ppi/288ppi.png")#.resize((400, 200), Image.ANTIALIAS)
lib_logo_app = ImageTk.PhotoImage(logo_app)

logo_app_kecil = Image.open("aset_gui/512ppi/1.5x.png")#.resize((400, 200), Image.ANTIALIAS)
lib_logo_app_kecil = ImageTk.PhotoImage(logo_app_kecil)

dash_1 = Image.open("aset_gui/dash_1.jpg").resize((195, 216), Image.ANTIALIAS)
logo_dash_1 = ImageTk.PhotoImage(dash_1)
dash_2 = Image.open("aset_gui/dash_2.jpg").resize((195, 216), Image.ANTIALIAS)
logo_dash_2 = ImageTk.PhotoImage(dash_2)
dash_3 = Image.open("aset_gui/dash_3.jpg").resize((195, 216), Image.ANTIALIAS)
logo_dash_3 = ImageTk.PhotoImage(dash_3)
dash_4 = Image.open("aset_gui/dash_4.jpg").resize((195, 216), Image.ANTIALIAS)
logo_dash_4 = ImageTk.PhotoImage(dash_4)
man = Image.open("aset_gui/man.png").resize((180, 180), Image.ANTIALIAS)
logo_man = ImageTk.PhotoImage(man)
search = Image.open("aset_gui/search.png").resize((80, 80), Image.ANTIALIAS)
logo_search = ImageTk.PhotoImage(search)
search_kecil = Image.open("aset_gui/search.png").resize((10, 10), Image.ANTIALIAS)
logo_search_kecil = ImageTk.PhotoImage(search_kecil)
pinjam = Image.open("aset_gui/pinjam.png").resize((80, 80), Image.ANTIALIAS)
logo_pinjam = ImageTk.PhotoImage(pinjam)
kembali = Image.open("aset_gui/return.png").resize((80, 80), Image.ANTIALIAS)
logo_kembali = ImageTk.PhotoImage(kembali)
riwayat = Image.open("aset_gui/history.png").resize((80, 80), Image.ANTIALIAS)
logo_riwayat = ImageTk.PhotoImage(riwayat)

check = Image.open("aset_gui/check.png").resize((120, 120), Image.ANTIALIAS)
logo_check = ImageTk.PhotoImage(check)

forbidden = Image.open("aset_gui/delete.png").resize((120, 120), Image.ANTIALIAS)
logo_forbidden = ImageTk.PhotoImage(forbidden)


## Inisialisasi Tabel - tabel dan data nya
class tabel_buku:
    def __init__(self, judul, pengarang, penerbit, isbn, status):
        self.judul = judul;
        self.pengarang = pengarang
        self.penerbit = penerbit
        self.isbn = isbn
        self.status = status

list = []

judulbuku = ["Kemampuan berpikir tingkat tinggi", 
"Buku ajar fisika radiasi", 
"Fisika : buku sakti bank soal SMA/MA", 
"Insight kompetisi sains nasional (KSN) fisika SMA", 
"Buku ajar fisika bangunan", 
"Fisika gelombang", 
"Fisika statistik", 
"Asik : ayo belajar fisika", 
"Fisika di bumi nusantara"
]

nama_pengarang = ["Erni Kusrini", 
" Dr. Sarianoferni", 
"Yoga Yuda Pratama", 
"Muslihun S.Si.", 
"Sri Yuliani", 
"Indri Dayana", 
"Ibu Sitti Rahmasari", 
"Zaenal Arifin", 
"Lutfiyanti Fitriah"
]

penerbit = ["PRCI", 
"CV. Literasi Nusantara Abadi", 
"Kompas Ilmu", 
"Grasindo", 
"UNS Press", 
"Gue Media Group", 
"Ruang Karya Bersama", 
"Dwija Pustaka Group", 
"Ruang Karya Bersama"]

no_isbn = ["978-623-448-048-1", 
"978-623-329-815-5", 
"978-602-343-731-3", 
"978-602-05-2945-5", 
"978-602-397-658-4", 
"978-623-421-188-7", 
"978-623-353-204-4", 
"978-623-99651-2-9", 
"978-623-353-173-3"]

for i in range(9):
    list.append(tabel_buku(judulbuku[i], nama_pengarang[i], penerbit[i],no_isbn[i], 'tersedia'))


# create frame style
LARGEFONT =("Muli", 35)
SMALLFONT =("Muli", 18)
backgroundDasar = '#FFFFFF'

s = Style()
s.configure('1.TFrame', background=backgroundDasar)
s1 = Style()
s1.configure('2.TFrame', background='#6603fc')

# create a notebook
notebook = Notebook(root, width=1280, height=720)
notebook.pack(expand=True)

# create frames

#Frame 1 - Homepage
frame1 = Frame(notebook, width=1280, height=720, style='1.TFrame')

label1 = Label(frame1,image=lib_logo_app,background=backgroundDasar)
label1.place(anchor='center',relx=0.5, rely=0.25)


selamatdatangLabel = Label(frame1, text="Selamat Datang di CodexLib @Bandung!", font=SMALLFONT, background=backgroundDasar)
selamatdatangLabel.place(anchor='center', relx=0.5, rely=0.45)


usernameLabel = Label(frame1, text="Email: ",font=SMALLFONT,background=backgroundDasar)
usernameLabel.place(anchor='e',relx=0.47, rely=0.55)

username = StringVar()
usernameEntry = Entry(frame1, textvariable=username)
usernameEntry.place(anchor='center',relx=0.54, rely=0.55)  


#password label and password entry box
passwordLabel = Label(frame1,text="Password: ",font=SMALLFONT,background=backgroundDasar)
passwordLabel.place(anchor='e',relx=0.47, rely=0.60)
password = StringVar()
passwordEntry = Entry(frame1, textvariable=password, show='*')
passwordEntry.place(anchor='center',relx=0.54, rely=0.60) 

def next():
    notebook.select(1)

nextButton = Button(frame1, text="Login", command=next)
nextButton.place(anchor='center',relx=0.5, rely=0.75)

daftar = Label(frame1, text="Belum memiliki akun? Daftar Sekarang!", font=SMALLFONT, background=backgroundDasar)
daftar.place(anchor='center', relx=0.5, rely=0.82)

frame1.pack(fill='both', expand=True)

#Frame 2: Dashboard
frame2 = Frame(notebook, width=1280, height=720, style='1.TFrame')
footer_logo = Label(frame2,image=lib_logo_app_kecil,background=backgroundDasar)
footer_logo.place(anchor='center',relx=0.1, rely=0.9)

dash_logo = Label(frame2,image=logo_man,background=backgroundDasar)
dash_logo.place(anchor='center',relx=0.5, rely=0.2)

dash_text1 = Label(frame2, text="Selamat datang, Joshtein di CodexLib Bandung!", font=SMALLFONT, background=backgroundDasar)
dash_text1.place(anchor='center', relx=0.5, rely=0.35)

dash_text2 = Label(frame2, text="Layanan Sistem Administrasi CodexLib Bandung", font=('Muli',25,'bold italic underline'), background=backgroundDasar)
dash_text2.place(anchor='center', relx=0.5, rely=0.42)

dash_1_button = Button(frame2, image=logo_dash_1)
dash_1_button.place(anchor='center', relx=0.23, rely=0.65)

dash_2_button = Button(frame2, image=logo_dash_2)
dash_2_button.place(anchor='center', relx=0.41, rely=0.65)

dash_3_button = Button(frame2, image=logo_dash_3)
dash_3_button.place(anchor='center', relx=0.59, rely=0.65)

dash_4_button = Button(frame2, image=logo_dash_4)
dash_4_button.place(anchor='center', relx=0.77, rely=0.65)

frame2.pack(fill='both', expand=True)

#Frame 3: Cari Buku
frame3 = Frame(notebook, width=1280, height=720, style='1.TFrame')
footer_logo = Label(frame3,image=lib_logo_app_kecil,background=backgroundDasar)
footer_logo.place(anchor='center',relx=0.1, rely=0.9)

cari_buku_logo = Label(frame3,image=logo_search,background=backgroundDasar)
cari_buku_logo.place(anchor='center',relx=0.1, rely=0.1)

search_text1 = Label(frame3, text="Pencarian Buku", font=('Muli', 20, 'bold underline'), background=backgroundDasar)
search_text1.place(anchor='center', relx=0.25, rely=0.1)

#Frame 4: Peminjaman Buku
frame4 = Frame(notebook, width=1280, height=720, style='1.TFrame')
footer_logo = Label(frame4,image=lib_logo_app_kecil,background=backgroundDasar)
footer_logo.place(anchor='center',relx=0.1, rely=0.9)

pinjam_buku_logo = Label(frame4,image=logo_pinjam,background=backgroundDasar)
pinjam_buku_logo.place(anchor='center',relx=0.1, rely=0.1)

borrow_text1 = Label(frame4, text="Cari dan Pinjaman Buku", font=('Muli', 20, 'bold underline'), background=backgroundDasar)
borrow_text1.place(anchor='w', relx=0.15, rely=0.1)

borrow_text2 = Label(frame4, text="Cari berdasarkan Judul Buku:", font=('Muli', 13), background=backgroundDasar)
borrow_text2.place(anchor='w', relx=0.08, rely=0.18)

search_judul = StringVar()
judulEntry = Entry(frame4, textvariable=search_judul, width = 50)
judulEntry.place(anchor='w',relx=0.08, rely=0.22)  

value_search_judul = search_judul.get()

def enter_judul_buku():
    value_search_judul = search_judul.get()
    print("Client mencari judul:        ", value_search_judul)
    
def enter_kategori_buku():
    value_search_kategori = search_kategori.get()
    print("Client mencari kategori:        ", value_search_kategori)

search_button_judul = Button(frame4, image=logo_search_kecil, command=enter_judul_buku)
search_button_judul.place(anchor='w', relx=0.34, rely=0.22)

borrow_text3 = Label(frame4, text="Cari berdasarkan Kategori Buku:", font=('Muli', 13), background=backgroundDasar)
borrow_text3.place(anchor='w', relx=0.08, rely=0.26)

search_kategori = StringVar()
kategoriEntry = Entry(frame4, textvariable=search_kategori, width = 50)
kategoriEntry.place(anchor='w',relx=0.08, rely=0.30)

search_button_kategori = Button(frame4, image=logo_search_kecil, command=enter_kategori_buku)
search_button_kategori.place(anchor='w', relx=0.34, rely=0.30)

#Form Peminjaman Buku
def enter_no_pinjam_buku():
    value_no_pinjam = no_pinjam.get()
    print("Client ingin meminjam buku nomor:        ", value_no_pinjam)
    buku_terpilih()


borrow_text4 = Label(frame4, text="Masukkan nomor buku yang ingin dipinjam:", font=('Muli', 13, 'bold'), background=backgroundDasar)
borrow_text4.place(anchor='w', relx=0.08, rely=0.35)

no_pinjam = StringVar()
nomorEntry = Entry(frame4, textvariable=no_pinjam, width = 50)
nomorEntry.place(anchor='w',relx=0.08, rely=0.40)

button_pinjam = Button(frame4, text="Pinjam", command=enter_no_pinjam_buku)
button_pinjam.place(anchor='w', relx=0.34, rely=0.40)

#bagian Konfirmasi Peminjaman
def buku_terpilih():
    infobuku_judul= Label(frame4, text="Judul", font=('Muli', 12, 'bold'), background=backgroundDasar)
    infobuku_judul.place(anchor='w', relx=0.08, rely=0.45)

    infobuku_judul= Label(frame4, text="Pengarang", font=('Muli', 12, 'bold'), background=backgroundDasar)
    infobuku_judul.place(anchor='w', relx=0.08, rely=0.49)

    infobuku_judul= Label(frame4, text="ISBN", font=('Muli', 12, 'bold'), background=backgroundDasar)
    infobuku_judul.place(anchor='w', relx=0.08, rely=0.53)

    infobuku_judul= Label(frame4, text="Penerbit", font=('Muli', 12, 'bold'), background=backgroundDasar)
    infobuku_judul.place(anchor='w', relx=0.08, rely=0.57)

    infobuku_judul= Label(frame4, text="Status", font=('Muli', 12, 'bold'), background=backgroundDasar)
    infobuku_judul.place(anchor='w', relx=0.08, rely=0.61)

    value_infobuku_judul= Label(frame4, text="Buku ajar fisika radiasi", font=('Muli', 12), background='#dedad9')
    value_infobuku_judul.place(anchor='w', relx=0.2, rely=0.45)

    value_infobuku_judul= Label(frame4, text="Dr. Sarianoferni", font=('Muli', 12), background='#dedad9')
    value_infobuku_judul.place(anchor='w', relx=0.2, rely=0.49)
    
    value_infobuku_judul= Label(frame4, text="978-623-329-815-5", font=('Muli', 12), background='#dedad9')
    value_infobuku_judul.place(anchor='w', relx=0.2, rely=0.53)
    
    value_infobuku_judul= Label(frame4, text="CV. Literasi Nusantara Abadi", font=('Muli', 12), background='#dedad9')
    value_infobuku_judul.place(anchor='w', relx=0.2, rely=0.57)

    value_infobuku_judul= Label(frame4, text="Tersedia", font=('Muli', 12), background='#dedad9')
    value_infobuku_judul.place(anchor='w', relx=0.2, rely=0.61)

    #Form Keperluan Peminjaman
    text_durasi= Label(frame4, text="Pilih Durasi", font=('Muli', 12), background=backgroundDasar)
    text_durasi.place(anchor='w', relx=0.08, rely=0.57)

    def show():
        Label.config( text = clicked.get() )

    options= ["7 hari","14 hari"]
    # datatype of menu text
    clicked = StringVar()
    
    # initial menu text
    clicked.set("pilih durasi")

    drop = OptionMenu( frame4 , clicked , *options )
    drop.place(anchor='w', relx=0.2, rely=0.71)

    def konfirmasi_pinjam_buku():
        value_no_pinjam = no_pinjam.get()
        print("Client konfirmasi meminjam buku nomor:   ", value_no_pinjam)
        konfirmasi_ok = Label(frame4, image=logo_check, background=backgroundDasar)
        konfirmasi_ok.place(anchor='w', relx=0.34, rely=0.60)
        

    button_pinjam = Button(frame4, text="Konfirmasi Peminjaman", command=konfirmasi_pinjam_buku)
    button_pinjam.place(anchor='w', relx=0.2, rely=0.75)


#Frame 4_0: Sisi kanan Judul
frame4_0 = Frame(frame4,width=640, height=120, style='1.TFrame')
frame4_0.pack(side = TOP, anchor = 'e')

borrow_text4 = Label(frame4_0, text="Hasil Pencarian", font=('Muli', 20, 'bold underline'), background=backgroundDasar)
borrow_text4.place(anchor='w', relx=0.05, rely=0.55)

#Frame 4_1: Sisi kanan, bagian Tabel 
frame4_1 = Frame(frame4, width=640, height=720, style='1.TFrame')
frame4_1.pack(side=RIGHT, anchor = 's')

sortable = BooleanVar(frame4_1, False)
drag_row = BooleanVar(frame4_1, False)
drag_col = BooleanVar(frame4_1, False)

columns = ["No", "Judul Buku", "Penulis", "Penerbit", "ISBN", "Status"]
table = Table(frame4_1, columns=columns, sortable=sortable.get(), drag_cols=drag_col.get(),
              drag_rows=drag_row.get(), height=25)
for col in columns:
    table.heading(col, text=col)
    table.column(col, width=100, stretch=True, anchor = 'w')

table.column("No", width = 40, stretch=True, anchor = 'center')
table.column("Judul Buku", width = 160, stretch=True, anchor = 'w')
table.column("Penulis", width = 120, stretch=True, anchor = 'w')
table.column("Penerbit", width = 80, stretch=True, anchor = 'w')

# sort column A content as int instead of strings
table.column('No', type=int)

#for i in range(50):
    #table.insert('', 'end', iid=i, values=(i, i) + tuple(i + 10 * j for j in range(2, 7)))

# for i in range(9):
#     if 'fisika' in judulbuku[i]:
#         table.insert('', 'end', iid=i, 
#                         values=(i+1,judulbuku[i],nama_pengarang[i],penerbit[i],no_isbn[i], 'tersedia'))

for i in range(9):
    table.insert('', 'end', iid=i, 
                    values=(i+1,list[i].judul,list[i].pengarang,list[i].penerbit,list[i].isbn, list[i].status))


#table.insert('', 'end', iid=1, values=(1,10000,10000))
#table.insert('', 'end', iid=2, values=99999)

# add scrollbars
sx = Scrollbar(frame4_1, orient='horizontal', command=table.xview)
sy = Scrollbar(frame4_1, orient='vertical', command=table.yview)
table.configure(yscrollcommand=sy.set, xscrollcommand=sx.set)

table.grid(sticky='ewns')
sx.grid(row=1, column=0, sticky='ew')
sy.grid(row=0, column=1, sticky='ns')
frame4_1.update_idletasks()

# toggle table properties
def toggle_sort():
    table.config(sortable=sortable.get())

def toggle_drag_col():
    table.config(drag_cols=drag_col.get())

def toggle_drag_row():
    table.config(drag_rows=drag_row.get())

sortable_t = Checkbutton(frame4_1, text='Enable Sorting', variable=sortable, command=toggle_sort)#.pack(side='left')
sortable_t.place(anchor='center', relx=0.5, rely=0.987)

# Checkbutton(frame4_1, text='drag columns', variable=drag_col, command=toggle_drag_col)#.pack(side='left')
# Checkbutton(frame4_1, text='drag rows', variable=drag_row, command=toggle_drag_row)#.pack(side='left')





#Frame 5: Pengembalian Buku
frame5 = Frame(notebook, width=1280, height=720, style='1.TFrame')
footer_logo = Label(frame5,image=lib_logo_app_kecil,background=backgroundDasar)
footer_logo.place(anchor='center',relx=0.1, rely=0.9)

kembali_buku_logo = Label(frame5,image=logo_kembali,background=backgroundDasar)
kembali_buku_logo.place(anchor='center',relx=0.1, rely=0.1)

return_text1 = Label(frame5, text="Pengembalian Buku", font=('Muli', 20, 'bold underline'), background=backgroundDasar)
return_text1.place(anchor='center', relx=0.25, rely=0.1)

# add frames to notebook 

notebook.add(frame1, text='Login Page')
notebook.add(frame2, text='Dashboard')
notebook.add(frame3, text='Cari Buku')
notebook.add(frame4, text='Peminjaman Buku')
notebook.add(frame5, text='Pengembalian Buku')


root.mainloop()