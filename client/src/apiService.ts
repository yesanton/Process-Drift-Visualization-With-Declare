import { parse, ParseResult } from "papaparse";

export const API_URL = "https://processdrift.ai.wu.ac.at";
// const API_URL = 'http://127.0.0.1:5000';

const cleanUpParams = (params: { [key: string]: any }) =>
  Object.entries(params).reduce((acc: { [key: string]: any }, [key, value]) => {
    if (value) {
      acc[key] = value;
    }

    return acc;
  }, {});
export const uploadFile = (body: FormData) =>
  fetch(`${API_URL}/uploadFile`, {
    method: "POST",
    body,
  })
    .then((response) => response.json())
    .catch(console.error);

export const makeDriftMap = ({
  session_id,
  params,
}: {
  session_id: string;
  params?: { [key: string]: any };
}) => {
  let url = new URL(`${API_URL}/makeDriftMap`);
  url.search = new URLSearchParams({
    logName: session_id,
    ...(params ? cleanUpParams(params) : {}),
  }).toString();

  return fetch(url.toString()).then((response) => response.json());
};

export const parseErraticMeasureCsv = (path: string) =>
  fetch(`${API_URL}${path}`)
    .then((response) => response.text())
    .then((res: string) =>
      parse<string>(res, {
        skipEmptyLines: true,
      })
    )
    .then(({ data, errors }: ParseResult<string>) => {
      if (errors.length > 0) {
        throw errors;
      }
      console.log({ data });

      return data.slice(1);
    })
    .catch(console.error);
