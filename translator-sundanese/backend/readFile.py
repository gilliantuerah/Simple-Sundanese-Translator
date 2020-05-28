def readFile(path):
    # mengembalikan array of isi file tiap line
    # membagi isi file per line atau per kata
    with open(path) as f:
        line = f.read().splitlines()

    return line


def getHasilTerjemahan(idx, indoList):
    # mengembalikan terjemahan dalam bahasa sunda atau bahasa indonesia (bagian kanan)
    # membagi line dengan "="
    kataTerjemahan = indoList[idx].split("= ")
    # menambahkan imbuhan "teh" sebelum kata tanya siapa dan apa
    if(kataTerjemahan[1] == "saha")or((kataTerjemahan[1] == "naon")):
        kataTerjemahan[1] = "teh "+kataTerjemahan[1]
    return kataTerjemahan[1]
