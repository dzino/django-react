import { Actions, Redux } from "declaration"

const initialState: Redux.RootState["groups"] = {
  target: 0,
  value: [],
}

export const groupReducer = (
  state = initialState,
  action: Actions.Groups
): Redux.RootState["groups"] => {
  switch (action.type) {
    case "ADD_GROUPS":
      return { ...state, value: [...state.value, ...action.payload] }
    case "SET_GROUPS_TARGET":
      return { ...state, target: action.payload }
    default:
      return state
  }
}
