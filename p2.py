valid_username = "admin"
valid_password = "1234"
percobaan = 0

while percobaan < 3:
   
    input_username = input("Masukkan username Anda: ")
    input_password = input("Masukkan password Anda: ")
    percobaan += 1

    if input_username == valid_username and input_password == valid_password:
        print("Login Berhasil")
        break
    else:
            print("Login Gagal")
else:
    print("Akun Terkunci")