// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;


// import './App.css';
// import Home from './Home';


// function App() {
//   return (
//   <div>
// <Home/>
//   </div>
//   );
// }

// export default App;


// import logo from '.logo.svg';


// import logo from './logo.svg';
import './App.css';
import Login from './Component/Login';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
// import Registrasion from './Component/Registrasion';
import Lupasandi from './Component/Lupasandi';
// import Home from './Component/Home';

// import { Home } from './pages/Home';

// import Registrasion from './pages/Registrasion';

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path='/' element={<Login/>} />
          {/* <Route path='/registrasion' element={<Registrasion/>} /> */}
          <Route path='/lupasandi' element={<Lupasandi/>} />
          {/* <Route path='/home' element={<Home/>} /> */}
        </Routes>
      </Router>
      
    </div>
  );
}

export default App;