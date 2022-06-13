import Head from "next/head";
import { Box, Container, Grid } from "@mui/material";
import { DashboardLayout } from "../components/common/dashboard-layout";

import { LongRunAndMarkov } from "src/components/rank/longRunAndMarkov";

const Dashboard = () => (
  <>
    <Head>
      <title>BMW Material Ranking</title>
      <link
        rel="icon"
        type="image/x-icon"
        href="https://pngimg.com/uploads/bmw_logo/bmw_logo_PNG19714.png"
      ></link>
    </Head>
    <Box
      component="main"
      sx={{
        flexGrow: 1,
        py: 8,
      }}
    >
      <Container maxWidth={false}>
        <Grid container spacing={3}>
          {/* <Grid
            item
            lg={3}
            sm={6}
            xl={3}
            xs={12}
          >
            <Budget />
          </Grid> */}
          {/* <Grid
            item
            xl={3}
            lg={3}
            sm={6}
            xs={12}
          >
            <TotalCustomers />
          </Grid> */}
          {/* <Grid
            item
            xl={3}
            lg={3}
            sm={6}
            xs={12}
          >
            <TasksProgress />
          </Grid> */}
          {/* <Grid
            item
            xl={3}
            lg={3}
            sm={6}
            xs={12}
          >
            <TotalProfit sx={{ height: '100%' }} />
          </Grid> */}

          <Grid item lg={12} md={12} xl={12} xs={12}>
            {/* <ExceptionManager /> */}

            <LongRunAndMarkov />
          </Grid>

          {/* <Grid
            item
      
            lg={12}
            md={12}
            xl={12}
            xs={12}
          >
            {/* <ExceptionMatrix /> */}
          {/* <Markov/>
          </Grid> */}

          {/* <Grid
            item
            lg={8}
            md={12}
            xl={9}
            xs={12}
          >
            <Sales />
          </Grid>
       
          <Grid
            item
            lg={4}
            md={6}
            xl={3}
            xs={12}
          >
            <LatestProducts sx={{ height: '100%' }} />
          </Grid> */}
        </Grid>
      </Container>
    </Box>
  </>
);

Dashboard.getLayout = (page) => <DashboardLayout>{page}</DashboardLayout>;

export default Dashboard;
