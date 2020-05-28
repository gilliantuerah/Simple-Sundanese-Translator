import re


def kalimatToKata(kalimat):
    # mengembalikan tuple of array yang berisikan kata-kata tanpa character dan teh dari kalimat,
    # serta kata-kata dengan character dari kalimat
    # membagi kalimat dengan karakter selain [a-zA-Z0-9] dan "teh"
    kata = re.split('\W+|teh ', kalimat)
    kataWChar = re.split(' ', kalimat)
    for i in range(len(kata)):
        kata[i] = kata[i].lower()
    return kata, kataWChar
