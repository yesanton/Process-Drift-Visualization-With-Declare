import React from "react";
import { Typography, Select, Button } from "antd";

import {
  AppContext,
  SET_ALGORITHM_SLICE_INDEX,
  SET_ALGORITHM_RESULT,
} from "./context/appContext";
import { makeEDFG } from "./apiService";

export const AppHeader = () => (
  <header className="App-header">
    <Typography.Title level={1}>
      Visual drift detection for sequence data analysis system
    </Typography.Title>
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
                <Select.Option value={index}>Section {index}</Select.Option>
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
);
