import React from 'react';
import { Typography } from 'antd';
import 'antd/dist/antd.css';

import { FormComponent } from './components/FormComponent';
import { ToolsComponent } from './components/ToolsComponent';
import { AppContextProvider } from './context/appContext';
import './App.css';

function App() {
  return (
    <AppContextProvider>
      <div className="App">
        <header className="App-header">
          <Typography.Title level={1}>PROJECT TITLE</Typography.Title>
        </header>
        <main>
          <FormComponent />
          <ToolsComponent />
        </main>
      </div>
    </AppContextProvider>
  );
}

export default App;
