import React, { FC, useContext, useState, useEffect } from "react";
import {
  Slider,
  Col,
  Checkbox,
  Radio,
  Button,
  Divider,
  Row,
  Tooltip,
  Layout,
} from "antd";
import { CheckboxChangeEvent } from "antd/lib/checkbox";
import { SliderValue } from "antd/lib/slider";
import { RadioChangeEvent } from "antd/lib/radio";
import { QuestionCircleOutlined, SettingTwoTone } from "@ant-design/icons";
import {
  AppContext,
  UPDATE_DEFINED_PARAM_ACTION,
  SET_ALGORITHM_RESULT,
  SET_ALGORITHM_LOADING,
  RESET_ALGORITHM_RESULT,
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
  const [collapsed, toggleSider] = useState<boolean>(false);

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
      dispatch({ type: SET_ALGORITHM_LOADING, payload: { loading: true } });
      dispatch({ type: RESET_ALGORITHM_RESULT });
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
        toggleSider(true);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
        dispatch({ type: SET_ALGORITHM_LOADING, payload: { loading: false } });
      }
    }
  };

  return (
    <Layout.Sider
      collapsible
      collapsed={collapsed}
      onCollapse={toggleSider}
      width={350}
      className="App-sider"
    >
      {collapsed && (
        <SettingTwoTone style={{ width: "50px", height: "50px" }} />
      )}
      <div
        style={{
          opacity: collapsed ? 0 : 1,
          pointerEvents: collapsed ? "none" : "inherit",
        }}
      >
        <Row>
          {/* <Tooltip title="Win size" color="pink"> */}
          <Col span={24}>
            <Tooltip
              title="the size of the sliding window for mining declare constraints"
              color={"green"}
            >
              <Divider>
                Win size{" "}
                <sup>
                  <QuestionCircleOutlined />
                </sup>
              </Divider>
            </Tooltip>
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
            <Tooltip
              title="this parameter sets the number of event sequences will be skipped with each new window. this number shouldn't be larger than the Win size"
              color={"pink"}
              key={"?"}
            >
              <Divider>
                Slide Size
                <sup>
                  <QuestionCircleOutlined />
                </sup>
              </Divider>
            </Tooltip>
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
            <Tooltip
              title="this parameter affects the hierarchical clustering algorithm to determine the number of clusters, 
                          and there fore number of changing behaviours. the larger the number the less clusters will be found "
              color={"orange"}
              key={"?"}
            >
              <Divider>
                Cut Threshold{" "}
                <sup>
                  <QuestionCircleOutlined />
                </sup>
              </Divider>
            </Tooltip>
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
            <Tooltip
              title="choose the color scheme for the Drift Map visualizatoin. All of the options should be colorblind friendly. Read more about color schemas at https://matplotlib.org/examples/color/colormaps_reference.html"
              color={"volcano"}
              key={"?"}
            >
              <Divider>
                Color scheme{" "}
                <sup>
                  <QuestionCircleOutlined />
                </sup>
              </Divider>
            </Tooltip>
          </Col>
          <Col span={24}>
            <Radio.Group
              defaultValue={
                state.defined?.colorTheme || state.colorTheme_default
              }
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
            <Tooltip
              title="Choose between three types of measures on Declare constraints"
              color={"lime"}
              key={"?"}
            >
              <Divider>
                Type of constraint{" "}
                <sup>
                  <QuestionCircleOutlined />
                </sup>
              </Divider>
            </Tooltip>
          </Col>
          <Col span={24}>
            <Radio.Group
              defaultValue={
                state.defined?.typeConstr || state.typeConstr_default
              }
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
            <Tooltip
              title="Click in driftAll if you want find sudden drifts in all separate clusters of behaviour. Leave it if you want to find sudden drifts on the whole dataset."
              color={"geekblue"}
              key={"?"}
            >
              <Checkbox
                checked={state.defined?.driftAll ?? state.driftAll}
                onChange={onCheckboxChange("driftAll")}
              >
                drift all{" "}
                <sup>
                  <QuestionCircleOutlined />
                </sup>
              </Checkbox>
            </Tooltip>
            <br />
            <Tooltip
              title="Click in noSort if you do not want to sort constrants in clusters by similarity for the drift map. This only influences the visul representation"
              color={"geekblue"}
              key={"?"}
            >
              <Checkbox
                checked={state.defined?.noSort ?? state.noSort}
                onChange={onCheckboxChange("noSort")}
              >
                no sort{" "}
                <sup>
                  <QuestionCircleOutlined />
                </sup>
              </Checkbox>
            </Tooltip>
          </Col>
        </Row>
        <Row>
          <Col span={24}>
            <Button
              type="primary"
              disabled={loading}
              loading={loading}
              onClick={onStartAlgorithm}
              style={{ margin: "20px 0" }}
            >
              Start algorithm
            </Button>
          </Col>
        </Row>
      </div>
    </Layout.Sider>
  );
};
