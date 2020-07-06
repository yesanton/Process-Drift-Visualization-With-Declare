import React, { FC, useContext } from "react";

import { Select, Row, Col, Typography } from "antd";
import { API_URL } from "../../apiService";
import {
  AppContext,
  TAppContextState,
  TDispatchType,
  SET_ALGORITHM_SLICE_INDEX,
} from "../../context/appContext";

import { ErraticMeasureComponent } from "./ErraticMeasureComponent";

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

  const {
    algorithmResult: { path_to_driftmap, erraticMeasureData = [], paths_to_drift_plots = [] },
    algorithmSliceIndex = 0,
  } = state;

  return (
    <div>
      <img src={`${API_URL}${path_to_driftmap}`} alt="Drift map"/>
      <Select onChange={selectAlgorithmSliceIndex} defaultValue={0}>
        {erraticMeasureData.map((elem, index) => (
          <Select.Option value={index}>Section {index}</Select.Option>
        ))}
      </Select>
      <Row>
        <Col span={10}>
          <Typography.Title level={3}>Erratic measure</Typography.Title>
          <ErraticMeasureComponent
            selected={algorithmSliceIndex}
            data={erraticMeasureData}
          />
        </Col>
        <Col span={12} offset={2}>
          <img src={`${API_URL}${paths_to_drift_plots[algorithmSliceIndex]}`} alt="drift plot"/>
        </Col>
      </Row>
    </div>
  );
};
