import React, { FC, createContext, useReducer } from "react";

enum ColorTheme {
  plasma = "plasma",
  bw = "bw",
  PiYG = "PiYG",
};

enum TypeConstr {
  plasma = "confidence",
  bw = "support",
  PiYG = "InterestF",
};

type TAppContextState = {
  sessionId?: string;
  cluCut?: {
    default?: number;
    max?: number;
    min?: number;
  };
  colorTheme?: ColorTheme [];
  selectedTheme?: ColorTheme;
  driftAll?: boolean;
  noSort?: boolean;
  sliBy?: {
    default?: number;
    max?: number;
    min?: number;
  };
  subL?: {
    default?: number;
    max?: number;
    min?: number;
  };
  typeConstr?: TypeConstr [];
  selectedTypeConstr?: TypeConstr;
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

export const SET_SESSION_ID_ACTION = "SET_SESSION_ID_ACTION";

const reducer = (
  state: TAppContextState,
  action: TStoreAction,
): TAppContextState => {
  switch (action.type) {
    case SET_SESSION_ID_ACTION: {
      return {
        ...state,
        sessionId: action.payload?.sessionId,
      };
    }

    default:
      return state;
  }
};

const wrappedDispatch = (dispatch: React.Dispatch<any>) => (action: TStoreAction) => {
  console.log("DISPATCH ACTION", action);

  dispatch(action);
};

export const AppContextProvider: FC = ({ children }) => {
  const [state, dispatch] = useReducer(reducer, {});
  return (
    <AppContext.Provider value={{ state, dispatch: wrappedDispatch(dispatch) }}>
      {children}
    </AppContext.Provider>
  );
};
