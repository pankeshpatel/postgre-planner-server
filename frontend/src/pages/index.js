import Head from "next/head";
import { Box, Container, Grid } from "@mui/material";
import { PartLookUp } from "../components/healthscore/part-lookup";
import { TrafficByDevice } from "../components/healthscore/traffic-by-device";
import { DashboardLayout } from "../components/common/dashboard-layout";
import React from "react";
import { useState } from "react";
import { useEffect } from "react";

const Dashboard = () => {
  const [healthguage, sethealthguage] = useState(10);

  return (
    <>
      <Head>
        <title>BMW Material Planner</title>
        <link rel="icon" type="image/png" href="bmw_logo_PNG19714.png"></link>
      </Head>
      <Box
        component="main"
        sx={{
          flexGrow: 1,
          py: 0,
          marginTop: "-4%",
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
            {/* <Grid
            item
            lg={4}
            md={6}
            xl={3}
            xs={12}
          >
            <TrafficByDevice healthGuage={healthGuage} setHealthGuage={setHealthGuage} sx={{ height: '100%' }}   />
          </Grid> */}

            <Grid item lg={12} md={12} xl={9} xs={12}>
              <PartLookUp healthguage={healthguage}  />
            </Grid>
            {/* <Grid
            item
            lg={12}
            md={12}
            xl={9}
            xs={12}
          >
            <LatestOrderDetail />
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
};

Dashboard.getLayout = (page) => <DashboardLayout>{page}</DashboardLayout>;

export default Dashboard;
