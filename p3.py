#Kurung kurawal
#fungsi dict()

akun = {
    'admin' : '1234',
    'user1' : 'abcd',
    'user2' : 'pass123',
}

percobaan = 0

while percobaan < 3:
   
    input_username = input("Masukkan username Anda: ")
    input_password = input("Masukkan password Anda: ")
    percobaan += 1

    # alternatif: if input_username in akun and input_password == akun[input_username]
    if input_password == akun.get(input_username):
        print("Login Berhasil")
        break
    else:
            print("Login Gagal")
else:
    print("Akun Terkunci")