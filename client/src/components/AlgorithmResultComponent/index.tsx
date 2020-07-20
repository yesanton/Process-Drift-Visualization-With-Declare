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
import './styles.css';

export const AlgorithmResultComponent: FC = () => {
  const { state, dispatch } = useContext<{
    state: TAppContextState;
    dispatch: TDispatchType;
  }>(AppContext);
  if (!state.algorithmResult?.path_to_driftmap) {
    return null;
  }

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

  console.log({ edfgs });

  const pValue: number = stationarityTestResult[algorithmSliceIndex]?.[2];
  const pValueText: string =
    pValue > 0.05
      ? `Incremental drift present, p = ${pValue}`
      : `No incremental drift, p = ${pValue}`;

  return (
    <div>
      <Row>
        <Col span={14}>
          <img src={`${API_URL}${path_to_driftmap}`} alt="Drift map" className="image"/>
        </Col>
        <Col span={10}>
          <img
            className="image"
            src={`${API_URL}${paths_to_drift_plots[algorithmSliceIndex]}`}
            alt="drift plot"
          />
        </Col>
      </Row>
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
            src={`${API_URL}${autocorrelationPlots[algorithmSliceIndex]}`}
            alt="autocorrelation plots"
            className="image"
          />
        </Col>
      </Row>
      {edfgs?.[algorithmSliceIndex] && (
        <Row>
          <Col span={24}>
            <img src={`${API_URL}${edfgs[algorithmSliceIndex]}`} alt="EDGF" className="image"/>
          </Col>
        </Row>
      )}
    </div>
  );
};
