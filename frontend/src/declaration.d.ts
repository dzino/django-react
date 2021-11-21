export declare namespace General {
  interface Car {
    id: number
    name: string
    manufacturer: number
  }

  interface Manufacturer {
    id: number
    name: string
    posts: Car[]
  }
}

export declare namespace Redux {
  interface RootState {
    groups: {
      target: General.Manufacturer.id
      value: General.Manufacturer[]
    }
  }

  type Reducers = { [key in keyof RootState]: any }
}

export declare namespace Actions {
  interface List {
    addGroups: {
      type: "ADD_GROUPS"
      payload: General.Manufacturer[]
    }
    setGroupsTarget: {
      type: "SET_GROUPS_TARGET"
      payload: General.Manufacturer.id
    }
  }

  type All = List[keyof List]
  type Type = List[keyof List]["type"]
  type Groups = List["addGroups" | "setGroupsTarget"]
}
