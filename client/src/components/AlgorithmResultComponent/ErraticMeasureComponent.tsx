import React, { FC, useMemo } from "react";
import { Slider } from "antd";

export const ErraticMeasureComponent: FC<{
  selected: number;
  data: Array<Array<string>>;
}> = ({ selected, data }) => {
  const [, min, cluster_em] = data[selected];
  const maxEm = useMemo(() => {
    return Math.round(Math.max(...data.map(([, , cluster_em]) => +cluster_em)) / +min);
  }, [data, min]);
  const currentEm = Math.round(+cluster_em / +min);

  return (
    <Slider
      disabled
      marks={{
        1: 1,
        [currentEm]: currentEm,
        [maxEm]: maxEm,
      }}
      min={1}
      max={maxEm}
      value={Math.round(+cluster_em / +min)}
    />
  );
};
