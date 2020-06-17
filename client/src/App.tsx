import React from 'react';
import { FormComponent } from './components/FormComponent';
import { AppContextProvider } from './context/appContext';
import './App.css';

function App() {
  return (
    <AppContextProvider>
      <div className="App">
        <header className="App-header">
          <h1>PROJECT TITLE</h1>
        </header>
        <main>
          <FormComponent />
        </main>
      </div>
    </AppContextProvider>
  );
}

export default App;
