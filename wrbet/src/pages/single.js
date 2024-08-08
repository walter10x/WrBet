import React from 'react';
import { useParams } from 'react-router-dom';

export const Single = () => {
    const { theid } = useParams(); // Obtiene el parámetro de la URL

    return (
        <div>
            <h1>Single Page</h1>
            <p>This is the Single page.</p>
            <p>Item ID: {theid}</p>
        </div>
    );
};

