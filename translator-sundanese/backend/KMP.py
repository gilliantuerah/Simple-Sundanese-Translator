def KMPmatching(text, pattern):
    # Menggunakan algoritma string matching Knuth Morris Pratt (KMP)
    # Mengembalikan indeks pertama dimana pattern ditemukan di teks
    panjangText = len(text)
    panjangPattern = len(pattern)

    lpst = LPStable(pattern)

    i = 0  # text
    j = 0  # pattern
    found = -1
    while found == -1 and i < panjangText:
        if text[i] == pattern[j]:
            if j == panjangPattern-1:
                found = i-panjangPattern+1
            else:
                i += 1
                j += 1
        else:
            if j != 0:
                j = lpst[j-1]
            else:
                i += 1

    return found


def LPStable(pattern):
    lps = [0 for i in range(len(pattern))]
    a = 0
    b = 1
    for j in range(1, len(pattern)):
        done = False
        while not done:
            if pattern[a] == pattern[b]:
                lps[j] = a+1
                a += 1
                b += 1
                done = True
            else:
                if(a != 0):
                    a = lps[a-1]
                else:
                    b += 1
                    done = True

    return lps
