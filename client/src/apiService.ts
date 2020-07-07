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

const generateGetURLWithParams = (
  path: string,
  params?: { [key: string]: any }
): string => {
  let url = new URL(`${API_URL}${path}`);
  url.search = new URLSearchParams({
    ...(params ? cleanUpParams(params) : {}),
  }).toString();

  return url.toString();
};

export const uploadFile = (body: FormData) =>
  fetch(`${API_URL}/uploadFile`, {
    method: "POST",
    body,
  })
    .then((response) => response.json())
    .catch(console.error);

export const makeDriftMap = (params: {
  logName: string;
  [key: string]: any;
}) => {
  return fetch(
    generateGetURLWithParams("/makeDriftMap", params)
  ).then((response) => response.json());
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

export const makeStationarityTest = (params: {
  logName: string;
  [key: string]: any;
}) =>
  fetch(generateGetURLWithParams("/makeStationarityTest", params))
    .then((response) => response.json())
    .then(({ path_to_stationarity }) =>
      fetch(`${API_URL}${path_to_stationarity}`)
    )
    .then((res) => res.text())
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

export const makeSpreadOfConstraints = (params: {
  logName: string;
  [key: string]: any;
}) => {
  return fetch(
    generateGetURLWithParams("/makeSpreadOfConstraints", params)
  ).then((response) => response.json());
};

export const makeAutocorrelationPlots = (params: {
  logName: string;
  [key: string]: any;
}) =>
  fetch(
    generateGetURLWithParams("/makeAutocorrelationPlots", params)
  ).then((response) => response.json());

export const makeEDFG = (params: { logName: string; [key: string]: any }) =>
  fetch(
    generateGetURLWithParams("/makeEDFG", params)
  ).then((response) => response.json());
