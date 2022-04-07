# Buat directory baru, dapat menggunakan :
mkdir Adi (namefile
# untuk masuk ke direktory, menggunakan :
cd Adi (namefile)

# Untuk membuat direktory dan mengosongkan direktory repo git, menggunakan:
git init 

# Membuat file README.txt kosong dengan first commit pada project.
# history. 
touch README.txt 
git add README.txt 
git commit -m 'First commit.' 

# Tambahkan beberapa penjelasan tentang project ke file README.
echo 'This repo is a collection of my favorite nursery rhymes.' >> README.txt

# Tinjau perubahan yang terjadi, kemudian commit semua.
git status
git diff
git add README.txt
git commit -m 'Added project overview to README.txt'
