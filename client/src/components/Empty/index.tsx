import React, { FC } from 'react';
import { Empty } from "antd";

import { AppLogo } from "../AppLogo";
import './Empty.css'

export const EmptyComponent: FC<{
  loading?: boolean,
  description: React.ReactNode,
}> = ({loading = false, children, description}) => {
  return <div className="Empty-area">
      <Empty
        description={description}
        image={<AppLogo size={{ width: "100px", height: "100px" }} spin={loading} />}
      >
        {children}
      </Empty>
    </div>
}