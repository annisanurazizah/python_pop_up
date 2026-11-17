import tkinter as tk
from tkinter import ttk, messagebox

def simpan_data():
    nama = entry_nama.get()
    ttgl = entry_ttgl.get()
    email = entry_email.get()
    gender = var_gender.get()
    jurusan = combo_jurusan.get()

    # Validasi Sederhana
    if not nama or not ttgl or not email or jurusan == "-- Pilih Jurusan --":
       messagebox.showwarning("Peringatan", "Mohon isi semua data yang diperlukan!")
       return

    # Tampilkan Pesan Sukses
    info = (
    "Pendaftaran Berhasil!\n"
    "-------------------------------------------\n\n"
    f"Nama              :  {nama}\n"
    f"TTL               :  {ttgl}\n"
    f"Email             :  {email}\n"
    f"Jenis Kelamin     :  {gender}\n"
    f"Jurusan           :  {jurusan}\n"
    "-------------------------------------------\n"
    "Data telah tersimpan di sistem"
    )

    messagebox.showinfo("Sukses", info)
    
    #Reset Form
    reset_form()

def reset_form():
    entry_nama.delete(0, tk.END)
    entry_ttgl.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    var_gender.set("Laki-laki")
    combo_jurusan.current(0)

#1. Inisialisasi Window Utama
root =tk.Tk ()
root.title("Form Pendaftaran FK")
root.geometry("600x520")
root.resizable(True, True)
root.state('zoomed')

# Pembuatan Judul JENDELA
label_judul = tk.Label(root, text="FORM PENDAFTARAN MAHASISWA", bg="#aa0ab9", fg="#ffffff", font=("Helvetica", 14, "bold"))
label_judul.pack(fill="x", pady=15)
#------------------------------------------------------

#Buat frame berisi form
frame_form = tk.Frame(root, bg="#aa0ab9", padx=20, pady=10)
frame_form.pack(fill="both", expand=True) # both melebar (sumbu x) dan meninggi (sumbu y). 
#-------------------------------------------------------------

#Label Nama
lbl_nama = tk.Label(frame_form, bg="#f23dfb", text="Nama Lengkap:", font="bold", anchor="w")
lbl_nama.pack(fill="x", pady=(15, 0))

# Entry Nama
entry_nama = tk.Entry(frame_form, font=("Helvetica", 10))
entry_nama.pack(fill="x", pady=(0, 10))
#------------------------------------------------------------

# LABEL TTGL
lbl_ttgl = tk.Label(frame_form, bg="#f28dfb", text="Tempat/Tanggal Lahir:", font="bold", anchor="w")
lbl_ttgl.pack(fill="x", pady=(5, 0))

# ENTRY TTGL
entry_ttgl = tk.Entry(frame_form, font=("Helvetica", 10))
entry_ttgl.pack(fill="x", pady=(0, 10))
#------------------------------------------------------------

#LABEL EMAIL
lbl_email = tk.Label(frame_form, bg="#ffbadd", text="Email:", font="bold", anchor="w")
lbl_email.pack(fill="x", pady=(5, 0))

# ENTRY EMAIL
entry_email = tk.Entry(frame_form, font=("Helvetica", 10))
entry_email.pack(fill="x", pady=(0, 10))
#------------------------------------------------------------

#LABEL JENIS KELAMIN
lbl_gender = tk.Label(frame_form, bg="#fba8cf", text="Jenis Kelamin:", font="bold", anchor="w")
lbl_gender.pack(fill="x", pady=(5, 0))
#------------------------------------------------------------

var_gender = tk.StringVar(value="Laki-laki")
frame_gender = tk.Frame(frame_form, bg="#f8f2f9", highlightbackground="#cccccc", padx=20, pady=10)
frame_gender.pack(fill="x", pady=(0, 10))

rb_pria = tk.Radiobutton(frame_gender, text="Laki-laki", font="bold", variable=var_gender, value="Laki-laki")
rb_pria.pack(side="left", padx=(0,10))

rb_wanita = tk.Radiobutton(frame_gender, text="Perempuan", font="bold", variable=var_gender, value="Perempuan")
rb_wanita.pack(side="left", padx=(0,10))
#-----------------------------------------------------------------

#ComboBox Jurusan
lbl_jurusan = tk.Label(frame_form, bg="#f8aed8", text="Jurusan / Pilihan:", font="bold", anchor="w")
lbl_jurusan.pack(fill="x", pady=(5, 0))

root.option_add("*TCombobox*Listbox.font", ("Helvetica", 12))

daftar_jurusan = ["-- Pilih Jurusan --", "Pendidikan Dokter", "Farmasi", "Pendidikan Keperawatan", "Kebidanan"]
combo_jurusan = ttk.Combobox(frame_form, values=daftar_jurusan, state="readonly", font=("Helvetica", 12))
combo_jurusan.current(0)
combo_jurusan.pack(fill="x", pady=(0, 20))

# Tombol Submit
frame_tombol = tk.Frame(frame_form, bg="#d25d82")
frame_tombol.pack(fill="x")

btn_simpan = tk.Button(
    frame_tombol,
    text="Daftar",
    bg="#4caf50",
    fg="white",
    font=("Helvetica", 10, "bold"),
    command=simpan_data
)
btn_simpan.pack(side="left", fill="x", expand=True, padx=(0, 40))

btn_reset = tk.Button(
    frame_tombol,
    text="Reset",
    bg="#4caf50",
    fg="white",
    font=("Helvetica", 10, "bold"),
    command=reset_form
)
btn_reset.pack(side="right", fill="x", expand=True, padx=(0, 40))

root.mainloop()
