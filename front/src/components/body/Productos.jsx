import React, { useState, useEffect } from 'react';
import '../styles/main.css';

function CardList() {
    const [productos, setProductos] = useState([]);

    useEffect(() => {
        fetch('/ubishop/productos/')
            .then(response => response.json())
            .then(data => setProductos(data))
            .catch(error => console.error('Error fetching productos:', error));
    }, []);

    const Card = ({ title, description, imagen, stock, precio}) => (
        <div className="card">
            <img src={imagen} className="w-full xs" alt={title} />
            <h2>{title}</h2>
            <p>{description}</p>
            <p>Stock - {stock}</p>
            <p>Precio - {precio}</p>
        </div>
    );

    const imagenes = [
        require('../../assets/memegato.png'),
        // Agregar más imágenes según sea necesario
    ];

    return (
        <div className="cards">
            <div className="row">
                {productos.slice(0, 3).map((producto, index) => (
                    <Card key={index} title={producto.nombre_producto} description={producto.descripcion} stock={producto.stock} precio={producto.precio} imagen={imagenes[index % imagenes.length]} />
                ))}
            </div>
            <div className="row">
                {productos.slice(3).map((producto, index) => (
                    <Card key={index + 3} title={producto.nombre_producto} description={producto.descripcion} stock={producto.stock} precio={producto.precio} imagen={imagenes[(index + 3) % imagenes.length]} />
                ))}
            </div>
        </div>
    );
}

function Imagen_Categoria() {
    const imagen = [
        require('../../assets/memegato.png'),
    ];
    return imagen.map((img, index) => (
        <div key={index}>
            <img src={img} alt={`Imagen de categoria ${index}`} />
        </div>
    ));
}

const Productos = () => {
    return (
        <div>
            <h2>Nueva Página</h2>
            <CardList />
            {/* Aquí puedes agregar más contenido si es necesario */}
        </div>
    );
};
export default Productos;
