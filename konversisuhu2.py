import time
jeda1 = 1

while True:

    #pembuka
    print("\n====KONVERSI SUHU====\n")

    time.sleep(jeda1)
    print("\nsilahkan pilih suhu apa yang ingin di konversi:")
    print("-celcius\n-fahrenheit\n-reamur\n-kelvin\n")

    suhu_awal = str(input("Silahkan masukkan suhu yang mau anda konversikan (celcius/fahrenheit/reamur/kelvin):"))
    if suhu_awal == "celcius":
        print("kamu mau konversi celcius ke suhu apa?")
        celcius = (str(input(("fahrenheit/reamur/kelvin:"))))
        if celcius == "fahrenheit":
            celcius2 = float(input("silahkan masukkan angka:"))
            fahrenheit_celcius = (celcius2 * 9/5) + 32
            print("suhu dalam fahrenheit: ", fahrenheit_celcius, "°F")
        elif celcius == "reamur":
            celcius3 = float(input("silahkan masukkan angka:"))
            reamur_celcius = celcius3 * 4/5
            print("suhu dalam reamur: ", reamur_celcius, "°R")
        elif celcius == "kelvin":
            celcius4 = float(input("silahkan masukkan angka:"))
            kelvin_celcius = celcius4 + 273
            print("suhu dalam kelvin: ", kelvin_celcius, "°K")
        elif celcius == "tidak":
            print("program selesai")
        else:
            print("maaf data tidak dapat dibaca, silahkan diulang")
    elif suhu_awal == "fahrenheit":
        print("kamu mau konversi fahrenheit ke suhu apa?")
        fahrenheit = (str(input(("celcius/reamur/kelvin:"))))
        if fahrenheit == "celcius":
            fahrenheit2 = float(input("silahkan masukkan angka:"))
            celcius_fahrenheit = (fahrenheit2 - 32) * 5/9
            print("suhu dalam celcius: ", celcius_fahrenheit, "°C")
        elif fahrenheit == "reamur":
            fahrenheit3 = float(input("silahkan masukkan angka:"))
            reamur_fahrenheit = (fahrenheit3 - 32) * 4/9
            print("suhu dalam reamur: ", reamur_fahrenheit, "°R")
        elif fahrenheit == "kelvin":
            fahrenheit4 = float(input("silahkan masukkan angka:"))
            kelvin_fahrenheit = (fahrenheit4 - 32) * 5/9 + 273
            print("suhu dalam kelvin: ", kelvin_fahrenheit, "°K")
        elif fahrenheit == "tidak":
            print("program selesai")
        else:
            print("maaf data tidak dapat dibaca, silahkan diulang")
    elif suhu_awal == "reamur":
        print("kamu mau konversi reamur ke suhu apa?")
        reamur = (str(input(("celcius/fahrenheit/kelvin:"))))
        if reamur == "celcius":
            reamur2 = float(input("silahkan masukkan angka:"))
            reamur_celcius = reamur2 *5/4
            print("suhu dalam celcius: ", reamur_celcius, "°C")
        elif reamur == "fahrenheit":
            reamur3 = float(input("silahkan masukkan angka:"))
            fahrenheit_reamur = reamur3 * 9/4 + 32
            print("suhu dalam fahrenheit: ", fahrenheit_reamur, "°F")
        elif reamur == "kelvin":
            reamur4 = float(input("silahkan masukkan angka:"))
            kelvin_reamur = reamur4 * 5/4 + 273
            print("suhu dalam kelvin: ", kelvin_reamur, "°K")
        elif reamur == "tidak":
            print("program selesai")
        else:
            print("maaf data tidak dapat dibaca, program selesai")
    elif suhu_awal == "kelvin":
        print("kamu mau konversi kelvin ke suhu apa?")
        kelvin = (str(input(("celcius/fahrenheit/reamur:"))))
        if kelvin == "celcius":
            kelvin2 = float(input("silahkan masukkan angka:"))
            celcius_kelvin = kelvin2 - 273
            print("suhu dalam celcius: ", celcius_kelvin, "°C")
        elif kelvin == "fahrenheit":
            kelvin3 = float(input("silahkan masukkan angka:"))
            fahrenheit_kelvin = (kelvin3 - 273) * 9/5 + 32
            print("suhu dalam fahrenheit: ", fahrenheit_kelvin, "°F")
        elif kelvin == "reamur":
            kelvin4 = float(input("silahkan masukkan angka:"))
            reamur_kelvin = (kelvin4 - 273) * 4/5
            print("suhu dalam reamur: ", reamur_kelvin, "°R")
        elif kelvin == "tidak":
            print("program selesai")
        else:
            print("maaf data tidak dapat dibaca, silahkan diulang")
    elif suhu_awal == "tidak":
        print("program selesai")
    else:
        print("maaf data tidak dapat dibaca, silahkan diulang")

    print()
    print("apakah kamu ingin mengulang")
    ulang = (input("ya/tidak?:"))
    if ulang == "tidak":
        print("program selesai terima kasih telah menggunakan program ini")
        break 