import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x520")

judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 14, "bold")
)
judul.grid(row=0, column=0, columnspan=2, pady=15)

mapel = [
    "Matematika",
    "Bahasa Indonesia",
    "Bahasa Inggris",
    "Fisika",
    "Kimia",
    "Biologi",
    "Sejarah",
    "Geografi",
    "Ekonomi",
    "Informatika"
]

entries = {}

for i, nama_mapel in enumerate(mapel, start=1):
    label = tk.Label(root, text=nama_mapel)
    label.grid(row=i, column=0, padx=15, pady=4, sticky="w")

    entry = tk.Entry(root, width=20)
    entry.grid(row=i, column=1, padx=10, pady=4)

    entries[nama_mapel] = entry

hasil = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold"),
    fg="blue"
)
hasil.grid(row=12, column=0, columnspan=2, pady=5)

def hasil_prediksi():
    try:
        nilai = {m: float(e.get()) for m, e in entries.items()}
    except ValueError:
        messagebox.showerror("Error", "Semua nilai harus diisi dengan angka!")
        return

    skor = {
        "Teknologi Informasi": (nilai["Matematika"] + nilai["Informatika"] + nilai["Bahasa Inggris"]) / 3,
        "Teknik": (nilai["Matematika"] + nilai["Fisika"] + nilai["Kimia"]) / 3,
        "Kedokteran / Kesehatan": (nilai["Biologi"] + nilai["Kimia"] + nilai["Fisika"]) / 3,
        "Ekonomi / Manajemen": (nilai["Ekonomi"] + nilai["Matematika"] + nilai["Bahasa Indonesia"]) / 3,
        "Ilmu Sosial / Sejarah": (nilai["Sejarah"] + nilai["Geografi"] + nilai["Bahasa Indonesia"]) / 3,
    }

    prodi_terbaik = max(skor, key=skor.get)
    hasil.config(text=prodi_terbaik)

button = tk.Button(
    root,
    text="Hasil Prediksi",
    command=hasil_prediksi
)
button.grid(row=11, column=0, columnspan=2, pady=15)

root.mainloop()