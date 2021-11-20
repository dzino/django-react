// import { useDispatch, useSelector } from "react-redux"
// import * as Dec from "declaration"

// Material-UI
import {
  AppBar,
  Button,
  Container,
  IconButton,
  Toolbar,
  Typography,
  Box,
  Breadcrumbs,
  Link,
  Paper,
} from "@material-ui/core"
import { Menu } from "@material-ui/icons"
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
}))

interface Props {
  children: JSX.Element
}

export default function Bar({ children }: Props) {
  const classes = useStyles()

  return (
    <>
      <AppBar className={classes.appBar} position="fixed">
        <Container fixed>
          <Toolbar>
            <IconButton
              edge="start"
              color="inherit"
              aria-label="menu"
              className={classes.menuButton}
            >
              <Menu />
            </IconButton>
            <Typography variant="h6" component="h1" className={classes.title}>
              Django & React
            </Typography>
            <Box mr={3}>
              <Breadcrumbs
                aria-label="breadcrumb"
                className={classes.bottomNavigation}
              >
                <Link underline="hover" color="inherit" href="/">
                  MUI
                </Link>
                <Link
                  underline="hover"
                  color="inherit"
                  href="/getting-started/installation/"
                >
                  Core
                </Link>
              </Breadcrumbs>
            </Box>
            <Box mr={3}>
              <Button color="inherit" variant="outlined">
                Log In
              </Button>
            </Box>
            <Button color="secondary" variant="contained">
              Sign Up
            </Button>
          </Toolbar>
        </Container>
      </AppBar>
      <main className={classes.main}>{children}</main>
    </>
  )
}
