import re


def kalimatToKata(kalimat):
    # mengembalikan tuple of array yang berisikan kata-kata tanpa character dan teh dari kalimat,
    # serta kata-kata dengan character dari kalimat
    # membagi kalimat dengan karakter selain [a-zA-Z0-9] dan "teh"
    kata = re.split(' teh|\W+', kalimat)
    kataWChar = re.split(' ', kalimat)
    for i in range(len(kata)):
        # menyesuaikan dengan kamus / lower case
        kata[i] = kata[i].lower()
        # menambahkan spasi setiap akhir kata
        if(kata[i] != ''):
            kata[i] += " "
    for i in range(len(kataWChar)):
        # menambahkan spasi di akhir kata
        if(kataWChar[i] != ''):
            kataWChar[i] += " "
    return kata, kataWChar
