import tkinter as tk

def hitung_total():
    harga_barang = float(entry_harga.get())
    jumlah_barang = int(entry_jumlah.get())
    total = harga_barang * jumlah_barang
    label_total.config(text=f"Total: {total} Rupiah")

root = tk.Tk()
root.title("Program Kasir")

# harga
label_harga = tk.Label(root, text="Harga Barang :")
label_harga.pack()
entry_harga = tk.Entry(root)
entry_harga.pack()

# jumlah
label_jumlah = tk.Label(root, text="Jumlah Barang:")
label_jumlah.pack()
entry_jumlah = tk.Entry(root)
entry_jumlah.pack()

# tombol total
button_hitung = tk.Button(root, text="Hitung Total", command=hitung_total)
button_hitung.pack()

# total
label_total = tk.Label(root, text="Total: 0")
label_total.pack()

root.mainloop()