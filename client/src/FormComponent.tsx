import React, { useState } from "react";

import { uploadFile } from './apiService';

export const FormComponent = () => {
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
      // formData.append('file', file.file);
      formData.append('file_name', file.file);
      try {
        const response = await uploadFile(formData);
        console.log({ response })
      } catch (error) {
        console.log(error);
      }
    }
  };

  return (
    <div>
      <input
        type="file"
        // accept=".xes"
        onChange={handleChange}
      />
      <input type="button" value="Submit!" onClick={handleSubmitForm} />
    </div>
  );
};
