import React, { FC, createContext, useReducer } from "react";

enum ColorTheme {
  plasma = "plasma",
  bw = "bw",
  PiYG = "PiYG",
}

enum TypeConstr {
  plasma = "confidence",
  bw = "support",
  PiYG = "interestF",
}

export type TAppContextState = {
  session_id?: string;
  cluCut_default?: number;
  cluCut_max?: number;
  cluCut_min?: number;
  colorTheme?: ColorTheme[];
  colorTheme_default?: ColorTheme;
  driftAll?: boolean;
  noSort?: boolean;
  sliBy_default?: number;
  sliBy_max?: number;
  sliBy_min?: number;
  subL_default?: number;
  subL_max?: number;
  subL_min?: number;
  typeConstr?: TypeConstr[];
  typeConstr_default?: TypeConstr;
  defined?: {
    cluCut?: number;
    sliBy?: number;
    subL?: number;
    driftAll?: boolean;
    noSort?: boolean;
    colorTheme?: ColorTheme;
    typeConstr?: TypeConstr;
  };
  algorithmResult?: TAlgorithmResult;
  algorithmSliceIndex?: number;
  algorithmLoading?: boolean;
};

type TAlgorithmResult = {
  path_to_driftmap: string;
  erraticMeasureData: Array<Array<string>>;
  paths_to_drift_plots: Array<string>;
  spread_constraints: string;
  [key: string]: any;
};

type TStoreAction = { type: string; payload: { [key: string]: any } };
export type TDispatchType = React.Dispatch<TStoreAction>;

export const AppContext = createContext<{
  state: TAppContextState;
  dispatch: TDispatchType;
}>({
  state: {},
  dispatch: () => null,
});
AppContext.displayName = "AppContext";

export const SET_SESSION_ACTION = "SET_SESSION_ACTION";
export const UPDATE_SESSION_ACTION = "UPDATE_SESSION_ACTION";
export const UPDATE_DEFINED_PARAM_ACTION = "UPDATE_DEFINED_PARAM_ACTION";
export const SET_ALGORITHM_RESULT = "SET_ALGORITHM_RESULT";
export const SET_ALGORITHM_SLICE_INDEX = "SET_ALGORITHM_SLICE_INDEX";
export const SET_ALGORITHM_LOADING = 'SET_ALGORITHM_LOADING';

const reducer = (
  state: TAppContextState,
  action: TStoreAction
): TAppContextState => {
  switch (action.type) {
    case SET_SESSION_ACTION: {
      return {
        ...state,
        ...action.payload,
      };
    }

    case UPDATE_DEFINED_PARAM_ACTION: {
      return {
        ...state,
        defined: {
          ...state.defined,
          ...action.payload,
        },
      };
    }

    case SET_ALGORITHM_RESULT: {
      return {
        ...state,
        algorithmResult: action.payload as TAlgorithmResult,
        algorithmSliceIndex: 0,
      };
    }

    case SET_ALGORITHM_SLICE_INDEX: {
      return {
        ...state,
        algorithmSliceIndex: action.payload.index as number,
      }
    }

    case SET_ALGORITHM_LOADING: {
      return {
        ...state,
        algorithmLoading: action.payload.loading,
      }
    }

    default:
      return state;
  }
};

const wrappedDispatch = (dispatch: React.Dispatch<any>) => (
  action: TStoreAction
) => {
  console.log("DISPATCH:", action);
  dispatch(action);
};

export const AppContextProvider: FC = ({ children }) => {
  const [state, dispatch] = useReducer(reducer, {});

  console.log({ state });

  return (
    <AppContext.Provider value={{ state, dispatch: wrappedDispatch(dispatch) }}>
      {children}
    </AppContext.Provider>
  );
};
