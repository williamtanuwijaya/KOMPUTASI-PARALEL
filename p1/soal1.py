if __name__ == "__main__":
    try:
        # angka1 = input("Masukkan angka 1 = ")
        # angka2 = input("Masukkan angka 2 = ")
        angka1, angka2 = input("Masukkan angka 1 = "), input("Masukkan angka 2 =")
        print(f"Angka yang Anda masukkan = {angka1} {type(angka1)} {angka2}")
        print(f"{angka1} + {angka2} = {int(angka1) + int(angka2)}")
    except Exception as err:
        print(f"ERROR {err}")