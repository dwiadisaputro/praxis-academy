from random import randint

##---membuat list pilihan untuk dimankan--##
G = ["Guntung", "Batu", "Kertas"]

##---membuat pilihan secara random memakai fungsi randit--##
komputer = G[randint(0, 2)]

##--pemain--
pemain = False

while pemain == False:
    ##set pemain ke true
    pemain = input("Gunnting, Batu, Kertas ? : ")
    if pemain == komputer:
        print("Seri!")
    elif pemain == "Batu":
        if komputer == "Kertas":
            print("Kamu Kalah!", komputer, "membungkus", pemain)
        else:
            print("Kamu Menang!", pemain, "membungkus", komputer)
            
    elif pemain == "Kertas":
        if komputer == "Gunting":
            print("Kamu Kalah!", komputer, "memotong", pemain)
        else:
            print("Kamu Menang!", pemain, "membungkus", komputer)
            
    elif pemain == "Gunting":
        if komputer == "Batu":
            print("Kamu Kalah!", komputer, "menghancurkan", pemain)
        else:
            print("Kamu Menang!", pemain, "memotong", komputer)
    
    else:
        print("Pilihan yang kamu masukkan salah...")
        
    ##-- set pemain ke ke False lagi, supaya terjadi looping yang berulang
    
    pemain = False   
komputer = G[randint(0, 2)]