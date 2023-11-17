class AnggotaKeluarga:
    def __init__(self, nama, hubungan):
        self.nama = nama
        self.hubungan = hubungan
        self.anak = []

    def tambah_anak(self, anak):
        self.anak.append(anak)

def tampilkan_keluarga(anggota, level=0):
    indentasi = "  " * level
    print(f"{indentasi}|- {anggota.nama} ({anggota.hubungan})")
    for anak in anggota.anak:
        tampilkan_keluarga(anak, level + 1)

# Membuat anggota keluarga
kakek = AnggotaKeluarga("Kakek", "Hadi")
nenek = AnggotaKeluarga("Nenek", "Retno")
ayah = AnggotaKeluarga("Ayah", "Nur")
ibu = AnggotaKeluarga("Ibu", "Nisa")
anak = AnggotaKeluarga("Anak", "Tari")
saudara = AnggotaKeluarga("Saudara", "Yanto")
saudari = AnggotaKeluarga("Saudari", "Nurul")
paman = AnggotaKeluarga("Paman" , "Wahyu, Ardi")
bibi = AnggotaKeluarga("Bibi" , "Rina, Ana")
Sepupu = AnggotaKeluarga("Sepupu" , "Hamzah, Bastian, Mira, Eka")
# Menentukan hubungan keluarga
kakek.tambah_anak(ayah)
kakek.tambah_anak(ibu)
kakek.tambah_anak(paman)
kakek.tambah_anak(bibi)
ayah.tambah_anak(anak)
ayah.tambah_anak(saudara)
ayah.tambah_anak(saudari)
ayah.tambah_anak(Sepupu)

# Menampilkan keluarga
tampilkan_keluarga(kakek)
tampilkan_keluarga(nenek)
print ("Jika Yanto saudara Nurul maka Yanto saudara Tari juga")
print ("jika Hamzah anak Rina maka Hamzah sepupu Yanto")
print ("Jika Nisa ibu Yanto maka Retno nenek Yanto")
print ("Jika Nur Ayah Yanto maka Hadi Kakek Yanto")