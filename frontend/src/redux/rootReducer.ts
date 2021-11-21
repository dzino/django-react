import { Redux } from "declaration"
import { combineReducers } from "redux"
import { groupReducer } from "./groupReducer"

const reducers: Redux.Reducers = {
  groups: groupReducer,
}

export const rootReducer = combineReducers(reducers)
