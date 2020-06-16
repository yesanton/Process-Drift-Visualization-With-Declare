import React, { useState, useContext } from "react";

import { uploadFile } from '../../apiService';
import { AppContext, SET_SESSION_ID_ACTION } from '../../context/appContext';
import './FormComponent.css';

export const FormComponent = () => {
  const {dispatch} = useContext(AppContext);
  const [file, setFile] = useState<{file: File, file_name: string}>();

  const handleChange = (event: React.SyntheticEvent<HTMLInputElement>) => {
    const target = event.target as HTMLInputElement;
    if (target.files && target.files.length) {
      const file = target.files[0];
      setFile({file, file_name: file.name});
    }
  }

  const handleSubmitForm = async () => {
    if (file) {
      const formData = new FormData();
      formData.append('file', file.file);
      try {
        const response = await uploadFile(formData);
        console.log({response})
        dispatch({type: SET_SESSION_ID_ACTION, payload: {sessionId: response.session_id}});
      } catch (error) {
        console.log(error);
      }
    }
  };

  return (
    <div className="FormComponent">
      <input
        type="file"
        accept=".xes"
        onChange={handleChange}
      />
      <input type="button" value="Submit!" onClick={handleSubmitForm} />
    </div>
  );
};
