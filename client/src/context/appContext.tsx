import React, { FC, createContext, useReducer } from "react";

enum ColorTheme {
  plasma = "plasma",
  bw = "bw",
  PiYG = "PiYG",
};

enum TypeConstr {
  plasma = "confidence",
  bw = "support",
  PiYG = "interestF",
};

type TAppContextState = {
  session_id?: string;
  cluCut_default?: number;
  cluCut_max?: number;
  cluCut_min?: number;
  colorTheme?: ColorTheme [];
  colorTheme_default?: ColorTheme;
  driftAll?: boolean;
  noSort?: boolean;
  sliBy_default?: number;
  sliBy_max?: number;
  sliBy_min?: number;
  subL_default?: number;
  subL_max?: number;
  subL_min?: number;
  typeConstr?: TypeConstr [];
  typeConstr_default?: TypeConstr;
  defined?: {
    cluCut?:number;
    sliBy?: number;
    subL?: number;
    driftAll?: boolean;
    noSort?: boolean;
    colorTheme?: ColorTheme;
    typeConstr?: TypeConstr;
  }
}

type TStoreAction = { type: string; payload: { [key: string]: any } };

export const AppContext = createContext<{
  state: TAppContextState;
  dispatch: React.Dispatch<TStoreAction>;
}>({
  state: {},
  dispatch: () => null,
});
AppContext.displayName = "AppContext";

export const SET_SESSION_ACTION = "SET_SESSION_ACTION";
export const UPDATE_SESSION_ACTION = "UPDATE_SESSION_ACTION";
export const UPDATE_DEFINED_PARAM_ACTION = "UPDATE_DEFINED_PARAM_ACTION";

const reducer = (
  state: TAppContextState,
  action: TStoreAction,
): TAppContextState => {
  switch (action.type) {
    case SET_SESSION_ACTION: {
      return {
        ...state,
        ...action.payload,
      }
    }

    case UPDATE_DEFINED_PARAM_ACTION: {
      return {
        ...state,
        defined: {
          ...state.defined,
          ...action.payload,
        }
      }
    }

    default:
      return state;
  }
};

const wrappedDispatch = (dispatch: React.Dispatch<any>) => (action: TStoreAction) => {
  console.log('DISPATCH:', action);
  dispatch(action);
};

export const AppContextProvider: FC = ({ children }) => {
  const [state, dispatch] = useReducer(reducer, {});

  console.log({state})
  
  return (
    <AppContext.Provider value={{ state, dispatch: wrappedDispatch(dispatch) }}>
      {children}
    </AppContext.Provider>
  );
};
