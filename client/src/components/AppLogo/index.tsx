import React from "react";

import logo from "./logo.jpeg";
import "./AppLogo.css";

export const AppLogo = ({
  spin = false,
  size = { width: "40px", height: "40px" },
}) => {
  return (
    <img
      src={logo}
      alt="Logo"
      className={`App-logo ${spin ? "spin" : ""}`}
      style={{ ...size }}
    />
  );
};
