import tkinter as tk
from tkinter import ttk

def create_graphs():
    # Dosyayı oku ve verileri listelere ayır
    with open("notlar.txt", "r") as file:
        lines = file.readlines()
        data = [line.strip().split(",") for line in lines[1:]]  # Başlık satırını atlıyoruz
    
    # Harf notlarına göre verileri sırala
    data.sort(key=lambda x: x[4])
    
    # Grafiklerin çizilmesi
    # Her bir grafiği oluşturmak için tkinter'ın Canvas bileşenini kullanıyoruz
    root = tk.Toplevel()
    root.title("Grafikler")
    
    # Vize grafiği
    vize_frame = ttk.Frame(root)
    vize_frame.pack(pady=5)  # Yüksekliği azalttık
    vize_label = ttk.Label(vize_frame, text="Vize Notu Dağılımı")
    vize_label.pack()
    draw_histogram(vize_frame, data, 1)
    
    # Final grafiği
    final_frame = ttk.Frame(root)
    final_frame.pack(pady=5)  # Yüksekliği azalttık
    final_label = ttk.Label(final_frame, text="Final Notu Dağılımı")
    final_label.pack()
    draw_histogram(final_frame, data, 2)
    
    # Bütünleme grafiği (eğer bütünleme notu varsa)
    butunleme = [float(row[3]) for row in data if row[3] != '']  # Boş olmayan bütünleme notlarını al
    if butunleme:
        butunleme_frame = ttk.Frame(root)
        butunleme_frame.pack(pady=5)  # Yüksekliği azalttık
        butunleme_label = ttk.Label(butunleme_frame, text="Bütünleme Notu Dağılımı")
        butunleme_label.pack()
        draw_histogram(butunleme_frame, data, 3)
    
    root.mainloop()

def draw_histogram(frame, data, column_index):
    # Verileri ondalık sayıya dönüştürürken boş dize kontrolü yap
    notes = [(float(row[column_index]), row[0]) for row in data if row[column_index] != '']
    if not notes:
        return  # Veri yoksa fonksiyonu sonlandır
    
    # En yüksek notu bul
    max_note = max(note[0] for note in notes)
    
    # Histogram çizimi
    canvas = tk.Canvas(frame, width=600, height=200)  # Yüksekliği düşürdük
    canvas.pack()
    bar_width = 30  # Çubukların genişliğini artırdık
    x_offset = 50
    y_scale = 150 / max_note  # Çubukların en yüksek değerinin 150 olmasını istiyoruz
    for i, (note, name) in enumerate(notes):
        x0 = i * bar_width + x_offset
        y0 = 180  # Çubukların altına daha fazla boşluk bırakmak için yüksekliği ayarladık
        x1 = x0 + bar_width
        y1 = 180 - note * y_scale
        canvas.create_rectangle(x0, y0, x1, y1, fill="lightblue")
        # Notları çubukların altına yatay olarak yaz
        canvas.create_text(x0 + bar_width / 2, y0 + 10, text=name, font=("Arial", 7), anchor="n", angle=0)
        # Notları çubukların üstüne yaz
        canvas.create_text(x0 + bar_width / 2, y1 - 5, text=str(note), font=("Arial", 7), anchor="s")
    
    canvas.create_text(300, 10, text=frame.winfo_children()[0]['text'], font=("Arial", 14), anchor="n")

root = tk.Tk()
root.title("Python & R Programı")

# Tablo için başlık
table_header = ["İsim", "Vize", "Final", "Bütünleme", "Harf Notu"]

# notlar.txt dosyasından verileri oku
with open("notlar.txt", "r") as file:
    lines = file.readlines()
    data = [line.strip().split(",") for line in lines]

# Tablo oluşturma
table_frame = ttk.Frame(root)
table_frame.pack(padx=10, pady=10)
table = ttk.Treeview(table_frame, columns=table_header, show="headings")

for col in table_header:
    table.heading(col, text=col)

for row in data:
    table.insert("", "end", values=row)

table.pack()

# Buton ile grafik oluşturma
button_frame = ttk.Frame(root)
button_frame.pack(padx=10, pady=10)
create_graphs_button = ttk.Button(button_frame, text="Grafikleri Oluştur", command=create_graphs)
create_graphs_button.pack()

root.mainloop()
