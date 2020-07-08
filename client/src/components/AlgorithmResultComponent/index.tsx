import React, { FC, useContext } from "react";

import { Select, Row, Col, Typography, Button } from "antd";
import { API_URL } from "../../apiService";
import {
  AppContext,
  TAppContextState,
  TDispatchType,
  SET_ALGORITHM_SLICE_INDEX,
  SET_ALGORITHM_RESULT,
} from "../../context/appContext";

import { makeEDFG } from "../../apiService";

import { ErraticMeasureSlider } from "./ErraticMeasureSlider";
import { SpreadConstraintsSlider } from "./SpreadConstraintsSlider";

export const AlgorithmResultComponent: FC = () => {
  const { state, dispatch } = useContext<{
    state: TAppContextState;
    dispatch: TDispatchType;
  }>(AppContext);
  if (!state.algorithmResult?.path_to_driftmap) {
    return <div>Start algorithm to see result here!</div>;
  }

  const selectAlgorithmSliceIndex = (index: number) =>
    dispatch({
      type: SET_ALGORITHM_SLICE_INDEX,
      payload: { index },
    });

  const getEdfgHandler = async () => {
    if (state.session_id) {
      const params = { logName: state.session_id, ...state.defined };
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

  const {
    algorithmResult: {
      path_to_driftmap,
      erraticMeasureData = [],
      paths_to_drift_plots = [],
      spread_constraints,
      stationarityTestResult,
      autocorrelationPlots,
      edfgs,
    },
    algorithmSliceIndex = 0,
  } = state;

  console.log({edfgs})

  const pValue: number = stationarityTestResult[algorithmSliceIndex]?.[2];
  const pValueText: string =
    pValue > 0.05
      ? `Incremental drift present, p = ${pValue}`
      : `No incremental drift, p = ${pValue}`;

  return (
    <div>
      <img src={`${API_URL}${path_to_driftmap}`} alt="Drift map" />
      <Select onChange={selectAlgorithmSliceIndex} defaultValue={0}>
        {erraticMeasureData.map((elem, index) => (
          <Select.Option value={index}>Section {index}</Select.Option>
        ))}
      </Select>
      {edfgs?.[algorithmSliceIndex] ? (
        <img
          src={`${API_URL}${edfgs[algorithmSliceIndex]}`}
          alt="EDGF"
        />
      ) : (
        <Button onClick={getEdfgHandler}>Get EDFG</Button>
      )}
      <Row>
        <Col span={10}>
          <Typography.Title level={3}>Erratic measure</Typography.Title>
          <ErraticMeasureSlider
            selected={algorithmSliceIndex}
            data={erraticMeasureData}
          />
          <Typography.Title level={3}>Spread of constraints</Typography.Title>
          <SpreadConstraintsSlider value={spread_constraints} />
          <Typography.Title level={3}>{pValueText}</Typography.Title>
        </Col>
        <Col span={12} offset={2}>
          <img
            src={`${API_URL}${paths_to_drift_plots[algorithmSliceIndex]}`}
            alt="drift plot"
          />
          <img
            src={`${API_URL}${autocorrelationPlots[algorithmSliceIndex]}`}
            alt="autocorrelation plots"
          />
        </Col>
      </Row>
    </div>
  );
};
