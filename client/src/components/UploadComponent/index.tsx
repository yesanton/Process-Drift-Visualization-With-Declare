import React, { useState, useContext } from "react";
import { Upload, Button, Typography } from "antd";
import { UploadOutlined } from "@ant-design/icons";

import { uploadFile } from "../../apiService";
import { AppContext, SET_SESSION_ACTION } from "../../context/appContext";
import { EmptyComponent } from "../Empty";

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
    <EmptyComponent
      loading={loading}
      description={
        <Typography.Title level={2}>
          The technique that supports the discovery of process drifts!
        </Typography.Title>
      }
    >
      <Upload accept=".xes" name="file" customRequest={handleSubmitForm}>
        <Button
          loading={loading}
          size="large"
          type="primary"
          disabled={loading}
        >
          <UploadOutlined /> Click to upload a <b> .xes </b> file
        </Button>
      </Upload>
    </EmptyComponent>
  );
};
