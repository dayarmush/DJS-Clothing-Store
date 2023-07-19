import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter} from 'react-router-dom';
import './index.css';
import App from './App';
import ProductList from './components/homeScreen';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <ProductList />
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
);


