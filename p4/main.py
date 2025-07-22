def cek_login(input_username, input_password):
    if input_password == akun.get(input_username):
        return "login berhasil"
    else:
        return "login gagal"

def input_akun():
    
    username = input("Masukkan username Anda: ")
    password = input("Masukkan password Anda: ")
    return username, password

akun = {
    'admin' : '1234',
    'user1' : 'abcd',
    'user2' : 'pass123',
}

percobaan = 0

if __name__ == "__main__":
    while percobaan < 3:
        username, password = input_akun()
        hasil = cek_login(username, password)
        
        if hasil == "login berhasil":
            print(hasil)
            break
        else:
            print(hasil)
        
        percobaan += 1
    else:
        print("Akun Terkunci")