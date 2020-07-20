import React, { FC, useContext, useState } from "react";
import { Slider, Col, Checkbox, Radio, Button, Divider, Row } from "antd";
import { CheckboxChangeEvent } from "antd/lib/checkbox";
import { SliderValue } from "antd/lib/slider";
import { RadioChangeEvent } from "antd/lib/radio";

import {
  AppContext,
  UPDATE_DEFINED_PARAM_ACTION,
  SET_ALGORITHM_RESULT,
} from "../../context/appContext";

import {
  makeDriftMap,
  parseErraticMeasureCsv,
  makeSpreadOfConstraints,
  makeStationarityTest,
  makeAutocorrelationPlots,
} from "../../apiService";

const getDefaultMark = (defaultValue: number = 0) => ({
  [defaultValue]: defaultValue,
});

export const ToolsComponent: FC = () => {
  const { state, dispatch } = useContext(AppContext);
  const [loading, setLoading] = useState<boolean>(false);

  if (!state.session_id) {
    return null;
  }

  const onAfterChangeSlider = (key: string) => (value: SliderValue) => {
    dispatch({ type: UPDATE_DEFINED_PARAM_ACTION, payload: { [key]: value } });
  };

  const onCheckboxChange = (key: string) => (event: CheckboxChangeEvent) => {
    dispatch({
      type: UPDATE_DEFINED_PARAM_ACTION,
      payload: { [key]: event.target.checked },
    });
  };

  const onRadioChange = (key: string) => (event: RadioChangeEvent) => {
    dispatch({
      type: UPDATE_DEFINED_PARAM_ACTION,
      payload: { [key]: event.target.value },
    });
  };

  const onStartAlgorithm = async () => {
    if (state.session_id) {
      setLoading(true);
      try {
        const params = { logName: state.session_id, ...state.defined };
        const algorithmResult = await makeDriftMap(params);
        const { spread_constraints } = await makeSpreadOfConstraints(params);
        const stationarityTestResult = await makeStationarityTest(params);
        const erraticMeasureData = await parseErraticMeasureCsv(
          algorithmResult.path_to_erratic_measure
        );
        const {
          paths_to_autocorrelation: autocorrelationPlots,
        } = await makeAutocorrelationPlots(params);


        dispatch({
          type: SET_ALGORITHM_RESULT,
          payload: {
            ...algorithmResult,
            erraticMeasureData,
            spread_constraints,
            stationarityTestResult,
            autocorrelationPlots,
          },
        });
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    }
  };

  return (
    <div>
      <Row>
        {/* <Tooltip title="Win size" color="pink"> */}
            <Col span={24}>
              <Divider>Win size</Divider>
            </Col>
            <Col span={24}>
              <Slider
                min={state.subL_min}
                max={state.subL_max}
                defaultValue={state.subL_default}
                marks={getDefaultMark(state.subL_default)}
                onAfterChange={onAfterChangeSlider("subL")}
              />
            </Col>
        {/* </Tooltip> */}
      </Row>
      <Row>
        <Col span={24}>
          <Divider>Slide Size</Divider>
        </Col>
        <Col span={24}>
          <Slider
            min={state.sliBy_min}
            max={state.sliBy_max}
            defaultValue={state.sliBy_default}
            marks={getDefaultMark(state.sliBy_default)}
            onAfterChange={onAfterChangeSlider("sliBy")}
          />
        </Col>
      </Row>
      <Row>
        <Col span={24}>
          <Divider>Cut Threshold</Divider>
        </Col>
        <Col span={24}>
          <Slider
            min={state.cluCut_min}
            max={state.cluCut_max}
            defaultValue={state.cluCut_default}
            marks={getDefaultMark(state.cluCut_default)}
            onAfterChange={onAfterChangeSlider("cluCut")}
          />
        </Col>
      </Row>
      <Row>
        <Col span={24}>
        <Divider>Color scheme</Divider>
        </Col>
        <Col span={24}>
          <Radio.Group
            defaultValue={state.defined?.colorTheme || state.colorTheme_default}
            onChange={onRadioChange("colorTheme")}
          >
            {state.colorTheme?.map((theme) => (
              <Radio value={theme} key={theme}>
                {theme}
              </Radio>
            ))}
          </Radio.Group>
        </Col>
      </Row>
      <Row>
        <Col span={24}>
          <Divider>Type of constraint</Divider>
        </Col>
        <Col span={24}>
        <Radio.Group
          defaultValue={state.defined?.typeConstr || state.typeConstr_default}
          onChange={onRadioChange("typeConstr")}
        >
          {state.typeConstr?.map((type) => (
            <Radio value={type} key={type}>
              {type}
            </Radio>
          ))}
        </Radio.Group>
        </Col>
      </Row>
      <Row>
        <Col span={24}>
          <Divider>Additional parameters</Divider>
        </Col>
        <Col span={24}>
          <Checkbox
            checked={state.defined?.driftAll ?? state.driftAll}
            onChange={onCheckboxChange("driftAll")}
          >
            drift all
          </Checkbox>
          <br />
          <Checkbox
            checked={state.defined?.noSort ?? state.noSort}
            onChange={onCheckboxChange("noSort")}
          >
            no sort
          </Checkbox>
        </Col>
      </Row>
      <Row>
        <Col span={24}>
          <Button loading={loading} onClick={onStartAlgorithm} style={{margin: "20px 0"}}>
            Start algorithm
          </Button>
        </Col>
      </Row>
    </div>
  );
};
