import Head from 'next/head';
import { Box, Container, Grid } from '@mui/material';
import { TotalMaterial } from '../components/dashboard/totalmaterial';
import { MaterialRedScore } from '../components/dashboard/material-red-score';
import { MaterialGreenScore } from '../components/dashboard/material-green-score';
import { MaterialYellowScore } from '../components/dashboard/material-yellow-score';
import { DashboardLayout } from '../components/common/dashboard-layout';
import { useEffect } from 'react';


const Dashboard = () => (


  
  

  

  <>
    <Head>
      {/* <title>
        Dashboard | Material Kit
      </title> */}
    </Head>
    <Box
      component="main"
      sx={{
        flexGrow: 1,
        py: 8
      }}
    >
      <Container maxWidth={false}>
        <Grid
          container
          spacing={3}
        >
          <Grid
            item
            lg={3}
            sm={6}
            xl={3}
            xs={12}
          >
            <TotalMaterial />
          </Grid>
          <Grid
            item
            xl={3}
            lg={3}
            sm={6}
            xs={12}
          >
            <MaterialGreenScore />
          </Grid>
          <Grid
            item
            xl={3}
            lg={3}
            sm={6}
            xs={12}
          >
            <MaterialRedScore />
          </Grid>
          <Grid
            item
            xl={3}
            lg={3}
            sm={6}
            xs={12}
          >
            <MaterialYellowScore sx={{ height: '100%' }} />
          </Grid>
          <Grid
            item
            lg={8}
            md={12}
            xl={9}
            xs={12}
          >
            {/* <Sales /> */}
          </Grid>
          <Grid
            item
            lg={4}
            md={6}
            xl={3}
            xs={12}
          >
            {/* <TrafficByDevice sx={{ height: '100%' }} /> */}
          </Grid>
          <Grid
            item
            lg={4}
            md={6}
            xl={3}
            xs={12}
          >
            {/* <LatestProducts sx={{ height: '100%' }} /> */}
          </Grid>
          <Grid
            item
            lg={8}
            md={12}
            xl={9}
            xs={12}
          >
            {/* <LatestOrders /> */}
          </Grid>
        </Grid>
      </Container>
    </Box>
  </>
);


Dashboard.getLayout = (page) => (

  <DashboardLayout>
    {page}
  </DashboardLayout>
);

export default Dashboard;
