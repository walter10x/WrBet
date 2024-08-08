import React from 'react';
//import './Footer.css';  // Si decides agregar estilos personalizados en un archivo CSS

export const Footer = () => {
    return (
        <footer className="footer">
            <div className="footer-content">
                <p>&copy; {new Date().getFullYear()} My Application. All rights reserved.</p>
                <p>
                    <a href="/privacy-policy">Privacy Policy</a> | 
                    <a href="/terms-of-service"> Terms of Service</a>
                </p>
            </div>
        </footer>
    );
};


