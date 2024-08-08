import api from "../api";

const getState = ({ getStore, getActions, setStore }) => {
    return {
        store: {
            // Aquí define tu estado inicial
            user: []
        },
        actions: {
            // Acción para obtener datos de usuarios
            getUsers: () => {
                api.get('/users') // Usa axios para hacer la petición GET
                    .then(response => {
                        // Actualiza el store con los datos recibidos
                        setStore({ user: response.data });
                    })
                    .catch(error => console.error("Error fetching data:", error));
            },
            // Más acciones que necesites
        }
    };
};

export default getState;
