import React, { FC, useContext } from "react";

import { Row, Col, Typography } from "antd";
import { API_URL } from "../../apiService";
import {
  AppContext,
  TAppContextState,
  TDispatchType,
} from "../../context/appContext";

import { ErraticMeasureSlider } from "./ErraticMeasureSlider";
import { SpreadConstraintsSlider } from "./SpreadConstraintsSlider";
import "./styles.css";

export const AlgorithmResultComponent: FC = () => {
  const { state } = useContext<{
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
        <Col span={10}>
          <img
            src={`${API_URL}${path_to_driftmap}`}
            alt="Drift map"
            className="image"
          />
        </Col>
        <Col span={8}>
          <img
            className="image"
            src={`${API_URL}${paths_to_drift_plots[algorithmSliceIndex]}`}
            alt="drift plot"
          />
        </Col>
        <Col span={5} offset={1}>
          <img
            src={`${API_URL}${autocorrelationPlots[algorithmSliceIndex]}`}
            alt="autocorrelation plots"
            className="image"
          />
          <Typography.Text>Erratic measure</Typography.Text>
          <ErraticMeasureSlider
            selected={algorithmSliceIndex}
            data={erraticMeasureData}
          />
          <Typography.Text>Spread of constraints</Typography.Text>
          <SpreadConstraintsSlider value={spread_constraints} />
          <Typography.Paragraph>{pValueText}</Typography.Paragraph>
        </Col>
      </Row>
      <Row>
        {edfgs?.[algorithmSliceIndex] && (
          <Col span={24}>
            <img
              src={`${API_URL}${edfgs[algorithmSliceIndex]}`}
              alt="EDGF"
              className="image"
            />
          </Col>
        )}
      </Row>
    </div>
  );
};
