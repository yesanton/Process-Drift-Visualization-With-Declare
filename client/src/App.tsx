import React from 'react';
import logo from './logo.svg';
import { FormComponent } from './FormComponent';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      </header>
      <main>
        <FormComponent />
      </main>
    </div>
  );
}

export default App;
