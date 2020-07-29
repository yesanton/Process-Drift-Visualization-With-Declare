import React from "react";
import { Spin } from "antd";

import { AppLogo } from '../AppLogo';
import './Loader.css';


export const LoaderComponent = () => {
  return (
    <div className="Overlay">
      <Spin
        className="Loader"
        tip="Loading..."
        indicator={<AppLogo spin/>}
      />
    </div>
  );
};
