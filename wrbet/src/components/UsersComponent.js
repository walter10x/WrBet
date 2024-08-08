import React, { useEffect, useContext } from 'react';
import { Context } from '../store/appContext';
 export const UsersComponent = () => {
  const { store, actions } = useContext(Context); // Destructura el store y las acciones del contexto

  useEffect(() => {
    actions.getUsers(); // Llama a la acción para obtener los usuarios
  }, [actions]);

  return (
    <div>
      <h1>Users</h1>
      {store.user.length > 0 ? (
        <ul>
          {store.user.map(user => (
            <li key={user.email}>{user.first_name}</li>
          ))
          }
        </ul>
      ) : (
        <p>No users found.</p>
      )}
    </div>
  );
};


