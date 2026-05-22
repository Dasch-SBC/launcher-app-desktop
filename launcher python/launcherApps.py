# library untuk program ini
import os
import time
import subprocess

# inputan untuk memulai program di fase terminal
print("masukkan kata 'gas coding' untuk mulai")
pilih = input("ketik di sini: ")

# logika proses saat kata kunci di masukkan
if pilih == "gas coding":
    print("lagi otw broooo.....")# animasi loading
    time.sleep(2) # untuk jeda selama 2 detik untuk proses membuka 
    
    os.startfile(r"D:\\Users\\User\\AppData\Local\Programs\Microsoft VS Code\Code.exe")# untuk membuka vs code dengan alamat file tujuan
    os.startfile("explorer.exe")# untuk membuka file explorer
    subprocess.Popen([r"D:\Users\\User\AppData\Local\Google\Chrome\Application\chrome.exe",'--profile-directory=Default'])# untuk membuka chrome dengan membuka profile default desktop user
else:
    print("Pilihan tidak tersedia")# jika inputan false