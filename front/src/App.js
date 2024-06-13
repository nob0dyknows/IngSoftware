
import React, { useState} from 'react';
import "./App.css";
import Header from "./components/comun/header.jsx";
import Footer from "./components/comun/Footer.jsx";
import { Carousel } from "./components/body/main.jsx";
import { Home_maps } from "./components/body/main.jsx";
import { CardList } from "./components/body/main.jsx";
import Productos from "./components/body/Productos.jsx"; 

function App() {
  const [showProductos, setShowProductos] = useState(false); // Estado para controlar si se muestra Productos

  const toggleProductos = () => {
    setShowProductos(true); // Establece showProductos a true para mostrar Productos
  };

  return (
    <div className="App">
      <Header toggleProductos={toggleProductos} /> {/* Pasa la función toggleProductos al Header */}
      <div className="main">
        {showProductos ? (
          <Productos /> // Muestra Productos si showProductos es true
        ) : (
          <React.Fragment>
            <Home_maps />
            <Carousel />
            <div className="porotos">
              <CardList />
            </div>
          </React.Fragment>
        )}
      </div>
      <br></br>
      <Footer />
    </div>
  );
}

export default App;