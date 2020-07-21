import React from "react";
import { Typography, Row, Col, Select, Button } from "antd";
import "antd/dist/antd.css";

import { UploadComponent } from "./components/UploadComponent";
import { ToolsComponent } from "./components/ToolsComponent";
import { AlgorithmResultComponent } from "./components/AlgorithmResultComponent";
import {
  AppContextProvider,
  AppContext,
  SET_ALGORITHM_SLICE_INDEX,
  SET_ALGORITHM_RESULT,
} from "./context/appContext";
import { makeEDFG } from "./apiService";
import "./App.css";

function App() {
  return (
    <AppContextProvider>
      <div className="App">
        <header className="App-header">
          <Typography.Title level={1}>Visual drift detection for sequence data analysis system</Typography.Title>
          <AppContext.Consumer>
            {({ state, dispatch }) => {
              const selectAlgorithmSliceIndex = (index: number) =>
                dispatch({
                  type: SET_ALGORITHM_SLICE_INDEX,
                  payload: { index },
                });
              const getEdfgHandler = async () => {
                if (state.session_id) {
                  const params = {
                    logName: state.session_id,
                    ...state.defined,
                  };
                  const { paths_to_edfgs: edfgs } = await makeEDFG(params);

                  dispatch({
                    type: SET_ALGORITHM_RESULT,
                    payload: {
                      ...state.algorithmResult,
                      edfgs,
                    },
                  });
                }
              };
              if (!state.algorithmResult) {
                return null;
              }

              const {
                algorithmResult: { edfgs, erraticMeasureData },
                algorithmSliceIndex = 0,
              } = state;

              return (
                <div>
                  <Select onChange={selectAlgorithmSliceIndex} defaultValue={0}>
                    {erraticMeasureData.map((elem, index) => (
                      <Select.Option value={index}>
                        Section {index}
                      </Select.Option>
                    ))}
                  </Select>

                  {!edfgs?.[algorithmSliceIndex] && (
                    <Button onClick={getEdfgHandler}>Get EDFG</Button>
                  )}
                </div>
              );
            }}
          </AppContext.Consumer>
        </header>
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
      </div>
    </AppContextProvider>
  );
}

export default App;
