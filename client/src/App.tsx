import React from 'react';
import { Typography, Row, Col } from 'antd';
import 'antd/dist/antd.css';

import { UploadComponent } from './components/UploadComponent';
import { ToolsComponent } from './components/ToolsComponent';
import { AlgorithmResultComponent } from './components/AlgorithmResultComponent';
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
          <UploadComponent />
          <Row>
            <Col span={8}>
              <ToolsComponent />
            </Col>
            <Col span={16}>
              <AlgorithmResultComponent />
            </Col>
          </Row>
        </main>
      </div>
    </AppContextProvider>
  );
}

export default App;
