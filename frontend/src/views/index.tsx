import Bar from "components/app-bar"
import List from "components/list"
import { useEffect } from "react"
import { useSelector, useDispatch } from "react-redux"
import { General, Redux, Actions } from "declaration"
import { useParams } from "react-router-dom"

export default function App() {
  const manufacturerCar = useGetManufacturerCar()
  const selectManufacturer = useSetSelectManufacturer()
  const params = useParams()
  const groups = useSelector((state: Redux.RootState) => state.groups.value)

  useEffect(manufacturerCar, [])
  useEffect(selectManufacturer, [params, groups])

  return (
    <Bar>
      <List />
    </Bar>
  )
}

function useGetManufacturerCar() {
  const dispatch: (v: Actions.All) => void = useDispatch()
  const dev = window.location.host === "localhost:3000"
  const url = dev
    ? "http://127.0.0.1:8000/api/manufacturer_car/"
    : "/api/manufacturer_car/"
  return () => {
    fetch(url, {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    })
      .then((response) => response.json())
      .then((commits: General.Manufacturer[]) =>
        dispatch({ type: "ADD_GROUPS", payload: commits })
      )
  }
}

function useSetSelectManufacturer() {
  const dispatch: (v: Actions.All) => void = useDispatch()
  const category = useParams()?.category
  const groups = useSelector((state: Redux.RootState) => state.groups.value)
  return () => {
    if (groups.length > 0) {
      dispatch({
        type: "SET_GROUPS_TARGET",
        payload: category ? +category : groups[0].id || 0,
      })
    }
  }
}
