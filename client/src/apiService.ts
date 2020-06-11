const API_URL = 'https://processdrift.ai.wu.ac.at';

export const uploadFile = (body: FormData) => fetch(`${API_URL}/uploadFile`, {
  method: 'POST',
  body,
  mode: 'no-cors',
}).catch(console.error);
