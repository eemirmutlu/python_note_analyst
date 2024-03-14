import tkinter as tk
from tkinter import ttk, messagebox
import os

def hesapla_notu(event=None):
    try:
        ad_soyad = ad_soyad_entry.get()
        vize_notu = float(vize_entry.get())
        final_notu = float(final_entry.get())
        butunleme_notu = butunleme_entry.get()

        if butunleme_notu and float(butunleme_notu) >= 50:
            not_ortalama = vize_notu * 0.4 + float(butunleme_notu) * 0.6
            harf_notu = harf_notunu_hesapla(not_ortalama)
            notu_goster(not_ortalama, harf_notu)
        else:
            if final_notu >= 50:
                not_ortalama = vize_notu * 0.4 + final_notu * 0.6
                harf_notu = harf_notunu_hesapla(not_ortalama)
                notu_goster(not_ortalama, harf_notu)
            else:
                sonuc_label.config(text="Final notu 50'den küçük olduğu için dersten kaldınız.", fg="red")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin.")

    # Verileri dosyaya kaydet
    verileri_dosyaya_kaydet(ad_soyad, vize_notu, final_notu, butunleme_notu, harf_notu)

    # R scriptini çalıştır
    os.system("Rscript grafik_olustur.R")


def notu_goster(not_ortalama, harf_notu):
    sonuc_label.config(text="Not ortalaması: {:.2f}, Harf notu: {}".format(not_ortalama, harf_notu), fg="green")


def harf_notunu_hesapla(not_ortalama):
    if not_ortalama >= 90:
        return "AA"
    elif not_ortalama >= 80:
        return "BA"
    elif not_ortalama >= 70:
        return "BB"
    elif not_ortalama >= 60:
        return "CB"
    elif not_ortalama >= 50:
        return "CC"
    elif not_ortalama >= 40:
        return "DC"
    elif not_ortalama >= 30:
        return "FD"
    else:
        return "FF"


def on_enter(event):
    hesapla_butonu.config(style="Hover.TButton")


def on_leave(event):
    hesapla_butonu.config(style="TButton")


def hover_animation(i):
    if i < 30:
        style.configure("Hover.TButton", background='lightblue')
    elif i < 60:
        style.configure("Hover.TButton", background='dodgerblue')
    else:
        return
    hesapla_butonu.after(10, lambda: hover_animation(i+1))


def verileri_dosyaya_kaydet(ad_soyad, vize_notu, final_notu, butunleme_notu, harf_notu):
    with open("notlar.txt", "a") as dosya:
        dosya.write(f"{ad_soyad},{vize_notu},{final_notu},{butunleme_notu},{harf_notu}\n")


# Ana uygulama penceresi
root = tk.Tk()
root.title("Not Hesaplama")
root.configure(bg="white")

# Font tanımlaması
font_stil = ("Nanum Gothic Coding", 12, "bold")

# Frame oluşturma
frame = tk.Frame(root, bg="white")
frame.pack(padx=10, pady=10)

# Giriş etiketleri ve alanları stillendirmeleri
ad_soyad_label = tk.Label(frame, text="Ad Soyad:", font=font_stil, bg="white", fg="black")
ad_soyad_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
ad_soyad_entry = tk.Entry(frame, font=font_stil, bg="white", fg="black", bd=3, relief="groove", highlightbackground="white", highlightcolor="white", highlightthickness=2)
ad_soyad_entry.grid(row=0, column=1, padx=5, pady=5)

vize_label = tk.Label(frame, text="Vize Notu:", font=font_stil, bg="white", fg="black")
vize_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
vize_entry = tk.Entry(frame, font=font_stil, bg="white", fg="black", bd=3, relief="groove", highlightbackground="white", highlightcolor="white", highlightthickness=2)
vize_entry.grid(row=1, column=1, padx=5, pady=5)
vize_entry.config(validate="key", validatecommand=(frame.register(lambda s: s.isdigit() or s == "."), "%S"))

final_label = tk.Label(frame, text="Final Notu:", font=font_stil, bg="white", fg="black")
final_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
final_entry = tk.Entry(frame, font=font_stil, bg="white", fg="black", bd=3, relief="groove", highlightbackground="white", highlightcolor="white", highlightthickness=2)
final_entry.grid(row=2, column=1, padx=5, pady=5)
final_entry.config(validate="key", validatecommand=(frame.register(lambda s: s.isdigit() or s == "."), "%S"))

butunleme_label = tk.Label(frame, text="Bütünleme Notu (boş bırakabilirsiniz):", font=font_stil, bg="white", fg="black")
butunleme_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
butunleme_entry = tk.Entry(frame, font=font_stil, bg="white", fg="black", bd=3, relief="groove", highlightbackground="white", highlightcolor="white", highlightthickness=2)
butunleme_entry.grid(row=3, column=1, padx=5, pady=5)
butunleme_entry.config(validate="key", validatecommand=(frame.register(lambda s: s.isdigit() or s == "."), "%S"))

# Buton
buton_font_stil = ("Nanum Gothic Coding", 12, "bold")
style = ttk.Style()
style.theme_use("default")
style.configure("TButton", font=buton_font_stil, relief="raised", borderwidth=3, foreground='black', background='lightblue')
style.map("TButton",
    foreground=[('active', 'white'), ('pressed', 'black')],
    background=[('active', 'lightblue'), ('pressed', 'lightblue')],
    highlightcolor=[('active', 'white'), ('pressed', 'black')],
    bordercolor=[('active', 'white'), ('pressed', 'black')],
    lightcolor=[('active', 'white'), ('pressed', 'black')],
    darkcolor=[('active', 'white'), ('pressed', 'black')]
)
style.configure("Hover.TButton", background='dodgerblue')

hesapla_butonu = ttk.Button(frame, text="Hesapla", command=hesapla_notu, style="TButton")
hesapla_butonu.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Hover efekti için fare olayların
hesapla_butonu.bind("<Enter>", on_enter)
hesapla_butonu.bind("<Leave>", on_leave)

# Hover
hover_animation(0)

# Sonuç etiketi
sonuc_label = tk.Label(root, text="", font=font_stil, bg="white", fg="black")
sonuc_label.pack(padx=10, pady=10)

# Analiz Butonu
def run_data_analysis():
    os.system("python data.py")

analiz_butonu = ttk.Button(root, text="Analiz Uygulaması", command=run_data_analysis, style="TButton")
analiz_butonu.pack(pady=10)

root.mainloop()
