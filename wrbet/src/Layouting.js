import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { ScrollToTop } from "./components/ScrollToTop "
import { BackendURL } from "./components/BackendURL"; // Verifica la ruta de importación
import { Home } from "./pages/Home"; // Verifica la ruta de importación
import { Demo } from "./pages/demo"; // Verifica la ruta de importación
import { Single } from "./pages/single"; // Verifica la ruta de importación
import { Footer } from "./components/Footer"; // Verifica la ruta de importación
import injectContext from "./store/appContext"; // Verifica la ruta de importación
import { UsersComponent } from "./components/UsersComponent";
const Layouting = () => {
  const basename = process.env.BASENAME || "";

  if (!process.env.BACKEND_URL || process.env.BACKEND_URL === "") {
    return <BackendURL />;
  }

  return (
    <BrowserRouter basename={basename}>
      <ScrollToTop>
        <UsersComponent />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/demo" element={<Demo />} />
          <Route path="/single/:theid" element={<Single />} />
          <Route path="*" element={<h1>Not found!</h1>} />
        </Routes>
        <Footer />
      </ScrollToTop>
    </BrowserRouter>
  );
};

export default injectContext(Layouting);
