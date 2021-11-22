import { useSelector } from "react-redux"
import { Redux } from "declaration"

// Material-UI
import {
  Container,
  Typography,
  Grid,
  Card,
  CardContent,
} from "@material-ui/core"
import { makeStyles } from "@material-ui/core/styles"

const useStyles = makeStyles((theme) => ({
  card: {
    margin: theme.spacing(1),
  },
}))

export default function List() {
  const classes = useStyles()
  const target = useSelector((state: Redux.RootState) => state.groups.target)
  const manufacturer = useSelector(
    (state: Redux.RootState) =>
      state.groups.value.find((i) => i.id === target)?.name || []
  )
  const posts = useSelector(
    (state: Redux.RootState) =>
      state.groups.value.find((i) => i.id === target)?.posts || []
  )

  return (
    <Container fixed>
      <Grid container>
        {posts.map((post) => (
          <Grid key={`post${post.id}`} item md={6}>
            <Card className={classes.card}>
              <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                  {post.name}
                </Typography>
                <Typography variant="body2" color="textSecondary">
                  Manufacturer: {manufacturer}
                </Typography>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Container>
  )
}
