import React, { useState, useEffect } from 'react';
import LeafletMap from './map.jsx'; // Ruta corregida
import '../styles/main.css';
import image1 from '../../assets/Unimarc/queso.jpg';
import image2 from '../../assets/mastikar/chileno.jpg';
import image3 from '../../assets/jumbo/jumbo.png';


function Home_maps() {
    const [mapCenter, setMapCenter] = useState(null); // Inicializamos con null
    const zoom = 15; // Nivel de zoom inicial

    useEffect(() => {
        const getUserLocation = () => {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    (pos) => {
                        const { latitude, longitude } = pos.coords;
                        setMapCenter([latitude, longitude]);
                    },
                    (err) => {
                        console.error(err);
                        // Si hay un error al obtener la ubicación, podemos establecer un centro por defecto
                        setMapCenter([51.505, -0.09]); // Ejemplo de centro por defecto (Londres)
                    }
                );
            } else {
                console.error("Geolocation is not supported by this browser.");
                // Si la geolocalización no es soportada, establecer un centro por defecto
                setMapCenter([51.505, -0.09]); // Ejemplo de centro por defecto (Londres)
            }
        };

        getUserLocation();
    }, []);

    return (
        <div className="Home_maps">
            {mapCenter && ( // Mostrar el mapa solo cuando tengamos una ubicación válida
                <div className="leaflet-map-container">
                    <LeafletMap center={mapCenter} zoom={zoom} userLocation={mapCenter} />
                </div>
            )}
        </div>
    );
}

function Carousel() {
    const images = [
        require('../../PUBLICIDAD1.png'),
        require('../../PUBLICIDAD2.png'),
        require('../../PUBLICIDAD3.png')
    ];
    const [currentIndex, setCurrentIndex] = useState(0);

    const handlePrev = () => {
        setCurrentIndex((prevIndex) =>
            prevIndex === 0 ? images.length - 1 : prevIndex - 1
        );
    };

    const handleNext = () => {
        setCurrentIndex((prevIndex) =>
            prevIndex === images.length - 1 ? 0 : prevIndex + 1
        );
    };

    useEffect(() => {
        const intervalId = setInterval(handleNext, 3000); // Cambiar imagen cada 3 segundos

        return () => {
            clearInterval(intervalId); // Limpia el intervalo cuando el componente se desmonta
        };
    }, []);

    return (
        <div className="Carusel">
                <img class='pato' src={images[currentIndex]}/>
        </div>
    );
}

function CardList() {
    const [stores, setStores] = useState([]);

    useEffect(() => {
        fetch('/ubishop/tiendas/')
            .then(response => {
                return response.json();
            })
            .then(data => {
                setStores(data);
            })
            .catch(error => {
                console.error("Error al obtener informacion", error);
            });
    }, []);

    const Card = ({ title, description, image}) => {
        return (
            <div className="card">
                <img src={image} className="img" alt={title} />
                <h2>{title}</h2>
                <p>{description}</p>
            </div>
        );
    };

    return (
        <div className="cards">
            <div className="row">
                {stores.length > 0 ? (
                    stores.map((store, index) => (
                        <Card 
                            key={index} 
                            title={store.nombre} 
                            description={store.descripcion} 
                            image={index === 0 ? image1 : index === 1 ? image2 : image3}
                        />
                    ))
                ) : (
                    <p>No se encontraron tiendas.</p>
                )}
            </div>
        </div>
    );
}


// Exportaciones corregidas
export { Home_maps, Carousel,CardList };
