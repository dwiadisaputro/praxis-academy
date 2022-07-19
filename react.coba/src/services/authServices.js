// import axios from "axios";

// const BASE_PATH = "https://2286-36-72-213-10.ap.ngrok.io";

// export async function getUser() {
//     try {
//         const results = await axios.get('${BASE_PATH}/list');
//         console.log(result.data.data);

//     } catch (error) {
//         console.log(error);
//     }
// };



// import axios from "axios";

// const BASE_PATH = "https://899a-36-73-103-14.ap.ngrok.io/";

// export async function getUser(setUser) {
//     try {
//        const results = await axios.get(`${BASE_PATH}/list`);
//        setUser(results.data.data);
//        console.log(results.data.data); 
//     } catch (error) {
//         console.log("ERROR GET: ", error);
//     }
// };

// export async function editUser(dataUser, setIsEditing, setDataUser, setMessage) {
//     const payload = dataUser;

//     try {
//         const results = await axios.put(`${BASE_PATH}/update/${dataUser.id}`, payload);
//         if (results.status === 200) {
//             setIsEditing(false);
//             setDataUser({nama: "", nama_lengkap: "", tanggal_lahir: ""});
//             setMessage("User Edited Successfully!!");
//         }
//         // console.log(results);
//     } catch (error) {
//         console.log("ERROR EDIT: ", error);
//     }
//     // console.log("EDIT USER", payload);
// };

// export async function postUser(dataUser, setDataUser, setMessage) {
//     const payload = {
//         nama: dataUser.pengirim,
//         nama_lengkap: dataUser.produk,
//         tanggal_lahir: dataUser.asal
//     };

//     try {
//         const results = await axios.post(`${BASE_PATH}/create`, payload);
//         if (results.status === 200) {
//             setDataUser({nama: "", nama_lengkap: "", tanggal_lahir: ""});
//             setMessage("New User Added Successfully !!");
//         }
//         // console.log(results);
//     } catch (error) {
//         console.log("ERROR EDIT: ", error.response);
//     }
// };

// export async function deleteUser(dataUser, setMessage) {
//     try {
//         const results = await axios.delete(`${BASE_PATH}/delete/${dataUser.id}`);
//         if (results.status === 200) {
//             setMessage("User Deleted Successfully!!!")
//             // console.log("DELETE SUCCESSFULLY !!!");
//         }
//         // console.log(results);
//     } catch (error) {
//         console.log("ERROR EDIT: ", error.response);
//     }
// }