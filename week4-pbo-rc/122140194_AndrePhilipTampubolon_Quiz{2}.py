import random

kata_kunci = [
    'algoritma', 'biner', 'boolean', 'byte', 'cache', 'compiler', 'debugger',
    'enkripsi', 'kerangka', 'fungsi', 'sampah', 'hash', 'indeks', 'iterator',
    'javascript', 'json', 'pustaka', 'perulangan', 'ruangnama', 'objek', 'operator',
    'overload', 'polimorfisme', 'antrian', 'rekursi', 'serialisasi', 'tumpukan',
    'template', 'variabel', 'virtual', 'web', 'xml', 'yaml', 'zip'
]

tahapan = [
    """
    ------
    |    |
    |
    |
    |
    |
    |
    ------------
    """,
    """
    ------
    |    |
    |    O
    |
    |
    |
    |
    ------------
    """,
    """
    ------
    |    |
    |    O
    |    |
    |    |
    |
    |
    ------------
    """,
    """
    ------
    |    |
    |    O
    |    |
    |    |
    |   /
    |
    ------------
    """,
    """
    ------
    |    |
    |    O
    |    |
    |    |
    |   / \\
    |
    ------------
    """,
    """
    ------
    |    |
    |    O
    |  --|
    |    |
    |   / \\
    |
    ------------
    """,
    """
    ------
    |    |
    |    O
    |  --|--
    |    |
    |   / \\
    |
    ------------
    """
]

def pilih_kata():
    return random.choice(kata_kunci)

def tampilkan_kata(kata, huruf_tebakan):
    tampilan = ""
    for huruf in kata:
        if huruf in huruf_tebakan:
            tampilan += huruf
        else:
            tampilan += "_"
    return tampilan

def main_hangman():
    kata = pilih_kata()
    huruf_tebakan = []
    sisa_percobaan = len(tahapan) - 1
    poin = 0

    print("Selamat datang di Hangman!")
    print("Tebak kata:")

    while sisa_percobaan > 0:
        tebakan = input("Masukkan huruf: ").lower()

        if tebakan in huruf_tebakan:
            print("Anda sudah menebak huruf tersebut sebelumnya.")
        elif tebakan in kata:
            huruf_tebakan.append(tebakan)
            print(tampilkan_kata(kata, huruf_tebakan))
            poin += 1  # Menambah poin jika tebakan benar
        else:
            huruf_tebakan.append(tebakan)
            sisa_percobaan -= 1
            print(tahapan[len(tahapan) - sisa_percobaan - 1])
            print(f"Sisa percobaan: {sisa_percobaan}")

        if "_" not in tampilkan_kata(kata, huruf_tebakan):
            print("Selamat! Anda berhasil menebak kata tersebut:", kata)
            print("Poin:", poin)  # Menampilkan poin
            break

    if sisa_percobaan == 0:
        print(f"Maaf, Anda kehabisan percobaan. Kata tersebut adalah '{kata}'.")
        print("Poin:", poin)  # Menampilkan poin

main_hangman()
