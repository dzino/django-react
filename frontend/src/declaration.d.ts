export declare namespace General {}

export declare namespace Redux {
  interface RootState {}

  type Reducers = { [key in keyof RootState]: any }
}

export declare namespace Actions {
  interface List {}

  type All = List[keyof List]
  type Type = List[keyof List]["type"]
}
