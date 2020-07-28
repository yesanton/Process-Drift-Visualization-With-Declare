import React from "react";
import "antd/dist/antd.css";

import { AppHeader } from "./AppHeader";
import { AppMainSection } from "./AppMainSection";

import {
  AppContextProvider,
} from "./context/appContext";
import "./App.css";

function App() {
  return (
    <AppContextProvider>
      <div className="App">
        <AppHeader />
        <AppMainSection />
      </div>
    </AppContextProvider>
  );
}

export default App;
