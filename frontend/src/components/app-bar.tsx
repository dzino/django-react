import { useSelector } from "react-redux"
import { Redux } from "declaration"
import { Link } from "react-router-dom"

// Material-UI
import {
  AppBar,
  Container,
  Toolbar,
  Typography,
  Box,
  Breadcrumbs,
} from "@material-ui/core"
import { makeStyles } from "@material-ui/core/styles"

const useStyles = makeStyles((theme) => ({
  appBar: {
    backgroundColor: "#0f3c2d",
  },
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(1),
  },
  bottomNavigation: {
    color: "#fff",
  },
  title: {
    flexGrow: 1,
  },
  main: {
    paddingTop: theme.spacing(9),
  },
  link: {
    color: "#ccc",
  },
}))

interface Props {
  children: JSX.Element
}

export default function Bar({ children }: Props) {
  const classes = useStyles()
  const groups = useSelector((state: Redux.RootState) => state.groups.value)

  return (
    <>
      <AppBar className={classes.appBar} position="fixed">
        <Container fixed>
          <Toolbar>
            <Typography variant="h6" component="h1" className={classes.title}>
              Django & React
            </Typography>
            <Box mr={3}>
              <Breadcrumbs
                aria-label="breadcrumb"
                className={classes.bottomNavigation}
              >
                {groups.map((group) => (
                  <Link
                    className={classes.link}
                    key={`group${group.id}`}
                    to={`/category/${group.id}`}
                  >
                    <Typography>{group.name}</Typography>
                  </Link>
                ))}
              </Breadcrumbs>
            </Box>
          </Toolbar>
        </Container>
      </AppBar>
      <main className={classes.main}>{children}</main>
    </>
  )
}
