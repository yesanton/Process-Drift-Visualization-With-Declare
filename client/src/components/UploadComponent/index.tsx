import React, { useState, useContext } from "react";
import { Upload, Button, Empty, Typography } from "antd";
import { UploadOutlined } from "@ant-design/icons";

import { uploadFile } from "../../apiService";
import { AppContext, SET_SESSION_ACTION } from "../../context/appContext";
import "./Upload.css";

export const UploadComponent = () => {
  const { dispatch, state } = useContext(AppContext);
  const [loading, setLoading] = useState<boolean>(false);

  if (state.session_id) {
    return null;
  }

  const handleSubmitForm = async ({
    file,
    onSuccess,
    onError,
  }: {
    file: File;
    onSuccess: (response: object, file: File) => void;
    onError: (event: Error, body?: Object) => void;
  }) => {
    if (file) {
      setLoading(true);
      const formData = new FormData();
      formData.append("file", file);
      try {
        const response = await uploadFile(formData);
        dispatch({ type: SET_SESSION_ACTION, payload: response });
        onSuccess(response, file);
      } catch (error) {
        console.log(error);
        onError(error);
      }
      setLoading(false);
    }
  };

  return (
    <div className="Upload-area">
      <Empty
        description={
          <Typography.Title level={2}>The technique that supports the discovery of process drifts!</Typography.Title>
        }
        image={Empty.PRESENTED_IMAGE_SIMPLE}
      >
        <Upload accept=".xes" name="file" customRequest={handleSubmitForm}>
          <Button loading={loading} size="large">
            <UploadOutlined /> Click to upload a <b> .xes </b> file
          </Button>
        </Upload>
      </Empty>
    </div>
  );
};
