import React from "react";

import { Layout } from "antd";

import { AppContext } from "./context/appContext";

import { UploadComponent } from "./components/UploadComponent";
import { ToolsComponent } from "./components/ToolsComponent";
import { AlgorithmResultComponent } from "./components/AlgorithmResultComponent";
import "./App.css";

export const AppMainSection = () => (
  <main>
    <AppContext.Consumer>
      {({ state }) => {
        if (!state.session_id) {
          return <UploadComponent />;
        }

        // if (!state.algorithmResult) {
        //   return <ToolsComponent />
        // }


        return (
          <Layout>
            <ToolsComponent />
            {state.algorithmResult && <Layout.Content>
              <AlgorithmResultComponent />
            </Layout.Content>}
          </Layout>
        );
      }}
    </AppContext.Consumer>
  </main>
);
