# -*- coding: utf-8 -*-
"""Soal_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12ZBEOXzjNBtq4DNAoOrqJ7iOTf7_6Eci
"""

def identifikasi_hama(gejala):
    daun_menguning = "daun menguning" in gejala
    bercak_hitam = "bercak hitam" in gejala
    daun_berlubang = "daun berlubang" in gejala
    tanaman_kayu = "tanaman kayu" in gejala

    if daun_menguning and bercak_hitam:
        return "Hama A"
    elif daun_berlubang:
        return "Hama B"
    elif tanaman_kayu and bercak_hitam:
        return "Hama C"
    elif daun_menguning and daun_berlubang:
        return "Hama D"
    else:
        return "Hama tidak diketahui"

# Contoh penggunaan
gejala_input = ["daun menguning", "bercak hitam"]
hasil = identifikasi_hama(gejala_input)
print(f"Tanaman terkena {hasil}")