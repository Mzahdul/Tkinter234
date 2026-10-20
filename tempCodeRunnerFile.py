import tkinter as tk

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x480")

# Label judul
judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 14, "bold")
)
judul.grid(row=0, column=0, columnspan=2, pady=15)

# 10 input nilai mata pelajaran yang berbeda
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

# Membuat label dan input nilai
for i, nama_mapel in enumerate(mapel, start=1):
    label = tk.Label(root, text=nama_mapel)
    label.grid(row=i, column=0, padx=15, pady=4, sticky="w")

    entry = tk.Entry(root, width=20)
    entry.grid(row=i, column=1, padx=10, pady=4)

# Fungsi hasil prediksi
def hasil_prediksi():
    hasil.config(text="Teknologi Informasi")

# Button Hasil Prediksi
button = tk.Button(
    root,
    text="Hasil Prediksi",
    command=hasil_prediksi
)
button.grid(row=11, column=0, columnspan=2, pady=15)

# Label luaran hasil prediksi
hasil = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold"),
    fg="blue"
)
hasil.grid(row=12, column=0, columnspan=2, pady=5)

root.mainloop()
