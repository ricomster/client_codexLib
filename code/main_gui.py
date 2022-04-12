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

#Variables
status_pressed= 0

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

perpanjang = Image.open("aset_gui/time.png").resize((80, 80), Image.ANTIALIAS)
logo_perpanjang = ImageTk.PhotoImage(perpanjang)

check = Image.open("aset_gui/check.png").resize((90, 90), Image.ANTIALIAS)
logo_check = ImageTk.PhotoImage(check)

forbidden = Image.open("aset_gui/delete.png").resize((90, 90), Image.ANTIALIAS)
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
    global status_pressed

    def destroy_labels():
        value_infobuku_judul.destroy()
        value_infobuku_pengarang.destroy()
        value_infobuku_isbn.destroy()
        value_infobuku_penerbit.destroy()
        value_infobuku_status.destroy()
        drop.destroy()

    if (status_pressed == 1):
        #destroy_labels()
        print("not 1st try")
    else:
        print("1st try")
        
        
    #global status_pressed 
    #

    infobuku_judul= Label(frame4, text="Judul", font=('Muli', 12, 'bold'), background=backgroundDasar)
    infobuku_judul.place(anchor='w', relx=0.08, rely=0.48)

    infobuku_pengarang= Label(frame4, text="Pengarang", font=('Muli', 12, 'bold'), background=backgroundDasar)
    infobuku_pengarang.place(anchor='w', relx=0.08, rely=0.52)

    infobuku_isbn= Label(frame4, text="ISBN", font=('Muli', 12, 'bold'), background=backgroundDasar)
    infobuku_isbn.place(anchor='w', relx=0.08, rely=0.56)

    infobuku_penerbit= Label(frame4, text="Penerbit", font=('Muli', 12, 'bold'), background=backgroundDasar)
    infobuku_penerbit.place(anchor='w', relx=0.08, rely=0.60)

    infobuku_status= Label(frame4, text="Status", font=('Muli', 12, 'bold'), background=backgroundDasar)
    infobuku_status.place(anchor='w', relx=0.08, rely=0.64)

    value_infobuku_judul= Label(frame4, text="Buku ajar fisika radiasi", font=('Muli', 12), background='#dedad9')
    value_infobuku_judul.place(anchor='w', relx=0.2, rely=0.48)

    value_infobuku_pengarang= Label(frame4, text="Dr. Sarianoferni", font=('Muli', 12), background='#dedad9')
    value_infobuku_pengarang.place(anchor='w', relx=0.2, rely=0.52)
    
    value_infobuku_isbn= Label(frame4, text="978-623-329-815-5", font=('Muli', 12), background='#dedad9')
    value_infobuku_isbn.place(anchor='w', relx=0.2, rely=0.56)
    
    value_infobuku_penerbit= Label(frame4, text="CV. Literasi Nusantara Abadi", font=('Muli', 12), background='#dedad9')
    value_infobuku_penerbit.place(anchor='w', relx=0.2, rely=0.60)

    value_infobuku_status= Label(frame4, text="Tersedia", font=('Muli', 12), background='#dedad9')
    value_infobuku_status.place(anchor='w', relx=0.2, rely=0.64)

    #Form Keperluan Peminjaman
    text_durasi= Label(frame4, text="Pilih Durasi", font=('Muli', 12, 'bold'), background=backgroundDasar)
    text_durasi.place(anchor='w', relx=0.08, rely=0.71)

    def show():
        Label.config( text = clicked.get() )

    options= ["pilih durasi"," 7 hari","14 hari"]
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
        konfirmasi_ok.place(anchor='w', relx=0.35, rely=0.75)
        value_infobuku_judul.destroy()
        value_infobuku_pengarang.destroy()
        value_infobuku_isbn.destroy()
        value_infobuku_penerbit.destroy()
        value_infobuku_status.destroy()
        drop.destroy()

        if (clicked.get()==" 7 hari"):
            print("durasi peminjaman 7 hari")
        elif(clicked.get()=="14 hari"):
            print("durasi peminjaman 14 hari")
        else:
            print("invalid duration")
        
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



#########################################################################

#Frame 5: Pengembalian dan Perpanjangan Buku
frame5 = Frame(notebook, width=1280, height=720, style='1.TFrame')
footer_logo = Label(frame5,image=lib_logo_app_kecil,background=backgroundDasar)
footer_logo.place(anchor='center',relx=0.1, rely=0.9)

kembali_buku_logo = Label(frame5,image=logo_kembali,background=backgroundDasar)
kembali_buku_logo.place(anchor='center',relx=0.1, rely=0.1)

return_text1 = Label(frame5, text="Pengembalian/Perpanjangan", font=('Muli', 20, 'bold underline'), background=backgroundDasar)
return_text1.place(anchor='w', relx=0.15, rely=0.1)

#Frame 4_0: Sisi kanan Judul
frame5_0 = Frame(frame5,width=640, height=180, style='1.TFrame')
frame5_0.pack(side = TOP, anchor = 'e')

borrow_text5 = Label(frame5_0, text="Buku yang sedang dipinjam", font=('Muli', 14, 'bold'), background=backgroundDasar)
borrow_text5.place(anchor='w', relx=0.03, rely=0.75)
#Frame 5_1: Sisi kanan, bagian Tabel 
frame5_1 = Frame(frame5, width=640, height=720, style='1.TFrame')
frame5_1.pack(side=RIGHT, anchor = 'center')

sortable5 = BooleanVar(frame5_1, False)
drag_row5 = BooleanVar(frame5_1, False)
drag_col5 = BooleanVar(frame5_1, False)

columns5 = ["No", "Judul Buku", "Penulis", "ISBN", "Tgl Pengembalian", "Status"]
table5 = Table(frame5_1, columns=columns5, sortable=sortable5.get(), drag_cols=drag_col5.get(),
              drag_rows=drag_row5.get(), height=20)
for col in columns5:
    table5.heading(col, text=col)
    table5.column(col, width=100, stretch=True, anchor = 'center')

# table5.column("No", width = 40, stretch=True, anchor = 'center')
# table5.column("Judul Buku", width = 160, stretch=True, anchor = 'w')
# table5.column("Penulis", width = 120, stretch=True, anchor = 'w')
# table5.column("Penerbit", width = 80, stretch=True, anchor = 'w')

# sort column A content as int instead of strings
table5.column('No', type=int)

#for i in range(50):
    #table.insert('', 'end', iid=i, values=(i, i) + tuple(i + 10 * j for j in range(2, 7)))

# for i in range(9):
#     if 'fisika' in judulbuku[i]:
#         table.insert('', 'end', iid=i, 
#                         values=(i+1,judulbuku[i],nama_pengarang[i],penerbit[i],no_isbn[i], 'tersedia'))

for i in range(9):
    table5.insert('', 'end', iid=i, 
                    values=(i+1,list[i].judul,list[i].pengarang,list[i].penerbit,list[i].isbn, list[i].status))


# add scrollbars
sx5 = Scrollbar(frame5_1, orient='horizontal', command=table.xview)
sy5 = Scrollbar(frame5_1, orient='vertical', command=table.yview)
table.configure(yscrollcommand=sy5.set, xscrollcommand=sx5.set)

table5.grid(sticky='ewns')
sx5.grid(row=1, column=0, sticky='ew')
sy5.grid(row=0, column=1, sticky='ns')
frame5_1.update_idletasks()

# toggle table properties
def toggle_sort5():
    table5.config(sortable=sortable.get())

def toggle_drag_col5():
    table5.config(drag_cols=drag_col.get())

def toggle_drag_row5():
    table5.config(drag_rows=drag_row.get())

sortable_t = Checkbutton(frame5_1, text='Enable Sorting', variable=sortable, command=toggle_sort5)#.pack(side='left')
sortable_t.place(anchor='center', relx=0.5, rely=0.987)

#Form Pengembalian Buku
def enter_no_return_buku():
    value_no_return = no_return.get()
    print("Client ingin mengembalikan buku nomor:        ", value_no_return)
    buku_terpilih_pengembalian()

form_pengembalian= Label(frame5, text="Form Pengembalian Buku", font=('Muli', 14, 'bold'), background=backgroundDasar)
form_pengembalian.place(anchor='w', relx=0.08, rely=0.20)

return_text1 = Label(frame5, text="Masukkan nomor buku yang ingin dikembalikan:", font=('Muli', 13, 'bold'), background=backgroundDasar)
return_text1.place(anchor='w', relx=0.08, rely=0.25)

no_return = StringVar()
nomorEntry = Entry(frame5, textvariable=no_return, width = 50)
nomorEntry.place(anchor='w',relx=0.08, rely=0.30)

button_return = Button(frame5, text="Cek", command=enter_no_return_buku)
button_return.place(anchor='w', relx=0.34, rely=0.30)

status_pressed_return = 0

def buku_terpilih_pengembalian():
    global status_pressed_return

    def destroy_labels():
        value_infobuku_judul.destroy()
        value_infobuku_pengarang.destroy()
        value_infobuku_isbn.destroy()
        value_infobuku_penerbit.destroy()
        value_infobuku_status.destroy()
        drop.destroy()

    if (status_pressed_return == 1):
        #destroy_labels()
        print("not 1st try")
    else:
        print("1st try")
        status_pressed_return = 1
        
        
    #global status_pressed 
    #

    infobuku_judul= Label(frame5, text="Judul", font=('Muli', 12, 'bold'), background=backgroundDasar)
    infobuku_judul.place(anchor='w', relx=0.08, rely=0.35)

    infobuku_pengarang= Label(frame5, text="Pengarang", font=('Muli', 12, 'bold'), background=backgroundDasar)
    infobuku_pengarang.place(anchor='w', relx=0.08, rely=0.39)

    infobuku_isbn= Label(frame5, text="ISBN", font=('Muli', 12, 'bold'), background=backgroundDasar)
    infobuku_isbn.place(anchor='w', relx=0.08, rely=0.43)

    infobuku_penerbit= Label(frame5, text="Penerbit", font=('Muli', 12, 'bold'), background=backgroundDasar)
    infobuku_penerbit.place(anchor='w', relx=0.08, rely=0.47)

    infobuku_status= Label(frame5, text="Status", font=('Muli', 12, 'bold'), background=backgroundDasar)
    infobuku_status.place(anchor='w', relx=0.08, rely=0.51)

    value_infobuku_judul= Label(frame5, text="Buku ajar fisika radiasi", font=('Muli', 12), background='#dedad9')
    value_infobuku_judul.place(anchor='w', relx=0.2, rely=0.35)

    value_infobuku_pengarang= Label(frame5, text="Dr. Sarianoferni", font=('Muli', 12), background='#dedad9')
    value_infobuku_pengarang.place(anchor='w', relx=0.2, rely=0.39)
    
    value_infobuku_isbn= Label(frame5, text="978-623-329-815-5", font=('Muli', 12), background='#dedad9')
    value_infobuku_isbn.place(anchor='w', relx=0.2, rely=0.43)
    
    value_infobuku_penerbit= Label(frame5, text="CV. Literasi Nusantara Abadi", font=('Muli', 12), background='#dedad9')
    value_infobuku_penerbit.place(anchor='w', relx=0.2, rely=0.47)

    value_infobuku_status= Label(frame5, text="Belum dikembalikan", font=('Muli', 12), background='#dedad9')
    value_infobuku_status.place(anchor='w', relx=0.2, rely=0.51)

    #Form Keperluan Peminjaman
    text_durasi= Label(frame5, text="Pilih Ekspedisi", font=('Muli', 12, 'bold'), background=backgroundDasar)
    text_durasi.place(anchor='w', relx=0.08, rely=0.55)

    def show_ekspedisi():
        Label.config( text = jenis_ekspedisi.get() )

    options= ["pilih ekspedisi","JNA","NanjiExpress","TEKE","BalikinAja"]
    # datatype of menu text
    jenis_ekspedisi = StringVar()
    
    # initial menu text
    jenis_ekspedisi.set("pilih ekspedisi")

    drop = OptionMenu( frame5 , jenis_ekspedisi , *options )
    drop.place(anchor='w', relx=0.2, rely=0.55)

    resi = Label(frame5, text="Nomor resi", font=('Muli', 12, 'bold'), background=backgroundDasar)
    resi.place(anchor='w', relx=0.08, rely=0.60)

    no_resi = StringVar()
    resiEntry = Entry(frame5, textvariable=no_resi, width = 50)
    resiEntry.place(anchor='w',relx=0.2, rely=0.60)

    def konfirmasi_kembalikan_buku():
        value_no_pinjam = no_pinjam.get()
        print("Client konfirmasi mengembalikan buku nomor:   ", value_no_pinjam)
        konfirmasi_ok = Label(frame5, image=logo_check, background=backgroundDasar)
        konfirmasi_ok.place(anchor='w', relx=0.35, rely=0.75)
        value_infobuku_judul.destroy()
        value_infobuku_pengarang.destroy()
        value_infobuku_isbn.destroy()
        value_infobuku_penerbit.destroy()
        value_infobuku_status.destroy()
        drop.destroy()

        print("client memilih ekspedisi", jenis_ekspedisi.get(), "dengan no resi: ", no_resi.get())
        
    button_pinjam = Button(frame5, text="Konfirmasi Pengembalian", command=konfirmasi_kembalikan_buku)
    button_pinjam.place(anchor='w', relx=0.2, rely=0.75)


#########################################################################

#Frame 6: Perpanjangan Buku
frame6 = Frame(notebook, width=1280, height=720, style='1.TFrame')
footer_logo = Label(frame6,image=lib_logo_app_kecil,background=backgroundDasar)
footer_logo.place(anchor='center',relx=0.1, rely=0.9)

kembali_buku_logo = Label(frame6,image=logo_perpanjang,background=backgroundDasar)
kembali_buku_logo.place(anchor='center',relx=0.1, rely=0.1)

return_text1 = Label(frame6, text="Perpanjangan Buku", font=('Muli', 20, 'bold underline'), background=backgroundDasar)
return_text1.place(anchor='w', relx=0.15, rely=0.1)

#Frame 4_0: Sisi kanan Judul
frame6_0 = Frame(frame6,width=640, height=180, style='1.TFrame')
frame6_0.pack(side = TOP, anchor = 'e')

borrow_text5 = Label(frame6_0, text="Buku yang sedang dipinjam", font=('Muli', 14, 'bold'), background=backgroundDasar)
borrow_text5.place(anchor='w', relx=0.03, rely=0.75)
#Frame 5_1: Sisi kanan, bagian Tabel 
frame6_1 = Frame(frame6, width=640, height=720, style='1.TFrame')
frame6_1.pack(side=RIGHT, anchor = 'center')

sortable5 = BooleanVar(frame6_1, False)
drag_row5 = BooleanVar(frame6_1, False)
drag_col5 = BooleanVar(frame6_1, False)

columns5 = ["No", "Judul Buku", "Penulis", "ISBN", "Tgl Pengembalian", "Status"]
table5 = Table(frame6_1, columns=columns5, sortable=sortable5.get(), drag_cols=drag_col5.get(),
              drag_rows=drag_row5.get(), height=20)
for col in columns5:
    table5.heading(col, text=col)
    table5.column(col, width=100, stretch=True, anchor = 'center')

# table5.column("No", width = 40, stretch=True, anchor = 'center')
# table5.column("Judul Buku", width = 160, stretch=True, anchor = 'w')
# table5.column("Penulis", width = 120, stretch=True, anchor = 'w')
# table5.column("Penerbit", width = 80, stretch=True, anchor = 'w')

# sort column A content as int instead of strings
table5.column('No', type=int)

#for i in range(50):
    #table.insert('', 'end', iid=i, values=(i, i) + tuple(i + 10 * j for j in range(2, 7)))

# for i in range(9):
#     if 'fisika' in judulbuku[i]:
#         table.insert('', 'end', iid=i, 
#                         values=(i+1,judulbuku[i],nama_pengarang[i],penerbit[i],no_isbn[i], 'tersedia'))

for i in range(9):
    table5.insert('', 'end', iid=i, 
                    values=(i+1,list[i].judul,list[i].pengarang,list[i].penerbit,list[i].isbn, list[i].status))


# add scrollbars
sx5 = Scrollbar(frame6_1, orient='horizontal', command=table.xview)
sy5 = Scrollbar(frame6_1, orient='vertical', command=table.yview)
table.configure(yscrollcommand=sy5.set, xscrollcommand=sx5.set)

table5.grid(sticky='ewns')
sx5.grid(row=1, column=0, sticky='ew')
sy5.grid(row=0, column=1, sticky='ns')
frame6_1.update_idletasks()

# toggle table properties
def toggle_sort5():
    table5.config(sortable=sortable.get())

def toggle_drag_col5():
    table5.config(drag_cols=drag_col.get())

def toggle_drag_row5():
    table5.config(drag_rows=drag_row.get())

sortable_t = Checkbutton(frame6_1, text='Enable Sorting', variable=sortable, command=toggle_sort5)#.pack(side='left')
sortable_t.place(anchor='center', relx=0.5, rely=0.987)

#Form Pengembalian Buku
def enter_no_return_buku():
    value_no_return = no_return.get()
    print("Client ingin mengembalikan buku nomor:        ", value_no_return)
    buku_terpilih_pengembalian()

form_pengembalian= Label(frame6, text="Form Perpanjangan Peminjaman Buku", font=('Muli', 14, 'bold'), background=backgroundDasar)
form_pengembalian.place(anchor='w', relx=0.08, rely=0.20)

return_text1 = Label(frame6, text="Masukkan nomor buku yang ingin diperpanjang:", font=('Muli', 13, 'bold'), background=backgroundDasar)
return_text1.place(anchor='w', relx=0.08, rely=0.25)

no_return = StringVar()
nomorEntry = Entry(frame6, textvariable=no_return, width = 50)
nomorEntry.place(anchor='w',relx=0.08, rely=0.30)

button_return = Button(frame6, text="Cek", command=enter_no_return_buku)
button_return.place(anchor='w', relx=0.34, rely=0.30)

status_pressed_return = 0

def buku_terpilih_pengembalian():
    global status_pressed_return

    def destroy_labels():
        value_infobuku_judul.destroy()
        value_infobuku_pengarang.destroy()
        value_infobuku_isbn.destroy()
        value_infobuku_penerbit.destroy()
        value_infobuku_status.destroy()
        drop.destroy()

    if (status_pressed_return == 1):
        #destroy_labels()
        print("not 1st try")
    else:
        print("1st try")
        status_pressed_return = 1
        
        
    #global status_pressed 
    #

    infobuku_judul= Label(frame6, text="Judul", font=('Muli', 12, 'bold'), background=backgroundDasar)
    infobuku_judul.place(anchor='w', relx=0.08, rely=0.35)

    infobuku_pengarang= Label(frame6, text="Pengarang", font=('Muli', 12, 'bold'), background=backgroundDasar)
    infobuku_pengarang.place(anchor='w', relx=0.08, rely=0.39)

    infobuku_isbn= Label(frame6, text="ISBN", font=('Muli', 12, 'bold'), background=backgroundDasar)
    infobuku_isbn.place(anchor='w', relx=0.08, rely=0.43)

    infobuku_penerbit= Label(frame6, text="Penerbit", font=('Muli', 12, 'bold'), background=backgroundDasar)
    infobuku_penerbit.place(anchor='w', relx=0.08, rely=0.47)

    infobuku_status= Label(frame6, text="Status", font=('Muli', 12, 'bold'), background=backgroundDasar)
    infobuku_status.place(anchor='w', relx=0.08, rely=0.51)

    value_infobuku_judul= Label(frame6, text="Buku ajar fisika radiasi", font=('Muli', 12), background='#dedad9')
    value_infobuku_judul.place(anchor='w', relx=0.2, rely=0.35)

    value_infobuku_pengarang= Label(frame6, text="Dr. Sarianoferni", font=('Muli', 12), background='#dedad9')
    value_infobuku_pengarang.place(anchor='w', relx=0.2, rely=0.39)
    
    value_infobuku_isbn= Label(frame6, text="978-623-329-815-5", font=('Muli', 12), background='#dedad9')
    value_infobuku_isbn.place(anchor='w', relx=0.2, rely=0.43)
    
    value_infobuku_penerbit= Label(frame6, text="CV. Literasi Nusantara Abadi", font=('Muli', 12), background='#dedad9')
    value_infobuku_penerbit.place(anchor='w', relx=0.2, rely=0.47)

    value_infobuku_status= Label(frame6, text="Dapat diperpanjang", font=('Muli', 12), background='#dedad9')
    value_infobuku_status.place(anchor='w', relx=0.2, rely=0.51)

    #Form Keperluan Peminjaman
    text_durasi= Label(frame6, text="Pilih durasi", font=('Muli', 12, 'bold'), background=backgroundDasar)
    text_durasi.place(anchor='w', relx=0.08, rely=0.55)

    def show_extend():
        Label.config( text = durasi_perpanjang.get() )

    options= ["pilih durasi","7 hari","14 hari"]
    # datatype of menu text
    durasi_perpanjang = StringVar()
    
    # initial menu text
    durasi_perpanjang.set("pilih durasi")

    drop = OptionMenu( frame6 , durasi_perpanjang , *options )
    drop.place(anchor='w', relx=0.2, rely=0.55)

    def konfirmasi_perpanjang_buku():
        value_no_pinjam = no_pinjam.get()
        print("Client konfirmasi ingin perpanjang buku nomor:   ", value_no_pinjam)
        konfirmasi_ok = Label(frame6, image=logo_check, background=backgroundDasar)
        konfirmasi_ok.place(anchor='w', relx=0.35, rely=0.75)
        value_infobuku_judul.destroy()
        value_infobuku_pengarang.destroy()
        value_infobuku_isbn.destroy()
        value_infobuku_penerbit.destroy()
        value_infobuku_status.destroy()
        drop.destroy()

        print("client memilih perpanjangan", durasi_perpanjang.get())
        
    button_pinjam = Button(frame6, text="Konfirmasi Perpanjangan", command=konfirmasi_perpanjang_buku)
    button_pinjam.place(anchor='w', relx=0.2, rely=0.75)


# add frames to notebook 

notebook.add(frame1, text='Login Page')
notebook.add(frame2, text='Dashboard')
notebook.add(frame3, text='Cari Buku')
notebook.add(frame4, text='Peminjaman Buku')
notebook.add(frame5, text='Pengembalian Buku')
notebook.add(frame6, text ='Perpanjangan')


root.mainloop()