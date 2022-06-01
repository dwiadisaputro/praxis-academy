from dotenv import find_dotenv, load_dotenv
from pymongo import MongoClient
import os
import pprint

##koneksi database
from distutils.log import info
from platformdirs import user_cache_dir


public function __construct() {
    try {
        //Connect to mongo
        $this -> mongo = new Mongo('127.0.0.1:27017');
        $this -> db = $this -> mongo -> selectDB('kampus');
        
        $tableName = 'mahasiswa';
        $this -> table = $this -> db -> $tableName;
    } catch(Exception $e) {
        echo "Something Went Wrong.";
        exit();
    }
}
##tampil data
//Get All Users
    function getListMahasiswa() {
        $users = $this -> table -> find() -> limit($limit);
        
        return $users;
    }

##tambah data
public function creatMahasiswa() {
        $nim = $_POST['nim'];
        $nama = $_POST['nama'];
        
        $insert = array("nim" => $nim, "nama" => $nama);
        $this -> table -> insert($insert);
    }

##edit data
public function updateMahasiswa($nim) {
    $query = array('nim' => $nim);
    
    //Get the existing info of the user
    $amahasiswaInfo = $this -> table -> findOne($query);
    
    //Assign New Value
    $amahasiswaInfo['nim'] = $_POST['nim'];
    $amahasiswaInfo['nama'] = $_POST['nama'];
    
    //update the user info
    $this -> table -> save($amahasiswaInfo);
}

##delete data
function deleteMahasiswa($nim) {
    $this -> table -> remove(array('nim' => $nim));
}