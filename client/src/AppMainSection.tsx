import React from "react";

import { Row, Col } from "antd";

import { AppContext } from "./context/appContext";

import { UploadComponent } from "./components/UploadComponent";
import { ToolsComponent } from "./components/ToolsComponent";
import { AlgorithmResultComponent } from "./components/AlgorithmResultComponent";

export const AppMainSection = () => (
  <main>
    <AppContext.Consumer>
      {({ state }) => {
        if (!state.session_id) {
          return <UploadComponent />;
        }
        return (
          <Row>
            <Col span={state.algorithmResult ? 1 : 24}>
              <ToolsComponent />
            </Col>
            <Col span={state.algorithmResult ? 23 : 0}>
              <AlgorithmResultComponent />
            </Col>
          </Row>
        );
      }}
    </AppContext.Consumer>
  </main>
);
