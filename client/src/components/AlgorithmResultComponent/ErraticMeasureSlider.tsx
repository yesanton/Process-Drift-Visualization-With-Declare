import React, { FC, useMemo } from "react";
import { Slider } from "antd";

export const ErraticMeasureSlider: FC<{
  selected: number;
  data: Array<Array<string>>;
}> = ({ selected, data }) => {
  const [, min, cluster_em] = data[selected];
  const maxEm = useMemo<number>(() => {
    return +(Math.max(...data.map(([, , cluster_em]) => +cluster_em)) / +min).toFixed(3);
  }, [data, min]);
  const currentEm: number = +(+cluster_em / +min).toFixed(3);

  return (
    <Slider
      disabled
      marks={{
        1: 1,
        [maxEm]: maxEm,
      }}
      min={1}
      max={maxEm}
      step={0.001}
      tooltipVisible
      value={currentEm}
    />
  );
};
