import React, { FC } from "react";
import { Slider } from "antd";

export const SpreadConstraintsSlider: FC<{
  value: string;
}> = ({ value }) => {
  return (
    <Slider
      disabled
      marks={{
        0: 0,
        1: 1,
      }}
      min={0}
      max={1}
      step={0.001}
      tooltipVisible
      value={+(+value / 100).toFixed(3)}
    />
  );
};
