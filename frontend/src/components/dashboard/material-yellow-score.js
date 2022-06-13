import { Avatar, Card, CardContent, Grid, Typography } from '@mui/material';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faRankingStar } from '@fortawesome/free-solid-svg-icons';


export const MaterialYellowScore = (props) => (
  <Card {...props}>
    <CardContent>
      <Grid
        container
        spacing={3}
        sx={{ justifyContent: 'space-between' }}
      >
        <Grid item>
          <Typography
            color="textSecondary"
            gutterBottom
            variant="overline"
          >
            Material With Yellow <br/>
            Score
          </Typography>
          <Typography
            color="textPrimary"
            variant="h4"
          >
            4
          </Typography>
        </Grid>
        <Grid item>
          <Avatar
            sx={{
              backgroundColor: 'warning.main',
              height: 56,
              width: 56
            }}
          >
            {/* <AttachMoneyIcon /> */}
            <FontAwesomeIcon icon={faRankingStar} />
          </Avatar>
        </Grid>
      </Grid>
    </CardContent>
  </Card>
);
