import React, {useState} from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import products from "./data/products.js";

import Nav from "./components/Nav.js";
import HomePage from "./pages/HomePage.js";
import GalleryPage from "./pages/GalleryPage.js";
import StaffPage from "./pages/StaffPage.js";
import OrderPage from "./pages/OrderPage.js";
import LogPage from "./pages/LogPage.js";
import CreatePage from "./pages/CreatePage.js";
import EditPage from "./pages/EditPage.js";
import TopicsPage from "./pages/TopicsPage.js";

// import logo from "./logo.svg";
import "./App.css";

function App() {
  const [event, setEvent] = useState([])
  return (
    <>

    <BrowserRouter>

    <header><h1>Mason Blanford | MERN Portfolio Page</h1></header>

    <Nav />

    <main>
    <section>

    <Routes>

      <Route path="/" element={<HomePage />} />

      <Route path="/log" element={<LogPage setEvent={setEvent} />} />
      <Route path="/add-event" element={<CreatePage />} />
      <Route path="/edit-event" element={<EditPage setEvent={event} />} />

      <Route path="/gallery" element={<GalleryPage />} />
      <Route path="/order" element={<OrderPage products={products} />}/>
      <Route path="/staff" element={<StaffPage />} />
      <Route path="/topics" element={<TopicsPage />}/>

    </Routes>
    
    </section>
    </main>
    <footer><p>&copy; Mason Blanford</p></footer>
    </BrowserRouter>
    </>
  );
}

export default App;
