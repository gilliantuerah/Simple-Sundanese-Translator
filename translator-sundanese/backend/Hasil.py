from KMP import KMPmatching
from readFile import readFile, getHasilTerjemahan
from Regex import kalimatToKata


def hasil(menu, kalimat):
    # fungsi yang mengembalikan kalimat terjemahan untuk
    # kalimatSunda dalam bahasa Indonesia atau
    # kalimatIndo dalam bahasa Sunda
    # algoritma string matching yang digunakan adalah algoritma KMP (Knuth-Morris-Pratt)

    # list yang menampung kata-kata hasil terjemahan
    kalimatHasil = []
    # kalimat hasil
    hasilTerjemahan = ''
    # mengubah kalimat menjadi list of kata
    kata, kataPure = kalimatToKata(kalimat)
    # kata : array of kata tanpa character dan "teh"
    # kataPure : array of kata dengan chacacter dan "teh"

    dir = 'D:\\kuliahh\\aslab\\ca-irk\\Simple-Sundanese-Translator\\translator-sundanese\\backend\\doc\\'
    # read file sunda.txt untuk menu "STI"
    if(menu == "STI"):
        kamus = readFile(dir+'sunda.txt')
    # read file indo.txt untuk menu "ITS"
    else:
        kamus = readFile(dir+'indonesia.txt')

    # mengecek seluruh isi kamus menemukan kata yang sama
    for j in range(len(kata)):
        idx = -1  # idx adalah indeks pattern ditemukan di kamus[i]
        i = 0  # i adalah indeks yang digunakan untuk iterasi kamus

        # jika kataPure[j] bukan merupakan character atau teh
        if(kata[j] != ''):
            # hasil indeks dengan algoritma yang digunakan adalah KMP
            while(i < len(kamus))and(idx != 0):
                idx = KMPmatching(kamus[i], kata[j])
                i += 1

            # jika kata ditemukan dalam kamus
            if(idx != -1):
                kalimatHasil.append(getHasilTerjemahan(i-1, kamus, j)+' ')
            # jika kata tidak ditemukan dalam kamus
            else:
                kalimatHasil.append(kataPure[j])

        else:
            # ignore teh di hasil terjemahan
            if(kataPure[j] != "teh "):
                kalimatHasil.append(kataPure[j])
    for k in kalimatHasil:
        hasilTerjemahan += k

    return hasilTerjemahan
