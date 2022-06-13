import { Doughnut } from 'react-chartjs-2';
import { Box, Card, CardContent, CardHeader, Divider, Typography, useTheme } from '@mui/material';

import GaugeChart from 'react-gauge-chart'
import { useEffect, useState } from 'react';

export const TrafficByDevice = (props) => {

  const [arcs, setArcs] = useState([0.2, 0.3, 0.5])
  const theme = useTheme();

  // const data = {
  //   datasets: [
  //     {
  //       data: [45,100],
  //       backgroundColor: ['red', 'green', '#FB8C00'],
  //       borderWidth: 8,
  //       borderColor: '#FFFFFF',
  //       hoverBorderColor: '#FFFFFF'
  //     }
  //   ],
  //   // labels: ['Desktop', 'Tablet', 'Mobile']
  // };

  // const options = { 
  //   animation: false,
  //   cutoutPercentage: 80,
  //   layout: { padding: 0 },
  //   legend: {
  //     display: false
  //   },
  //   maintainAspectRatio: false,
  //   responsive: true,
  //   tooltips: {
  //     backgroundColor: theme.palette.background.paper,
  //     bodyFontColor: theme.palette.text.secondary,
  //     borderColor: theme.palette.divider,
  //     borderWidth: 1,
  //     enabled: true,
  //     footerFontColor: theme.palette.text.secondary,
  //     intersect: false,
  //     mode: 'index',
  //     titleFontColor: theme.palette.text.primary
  //   }
  // };



  const devices = [
    {
      title: 'Health Status',
      value: props.healthGuage,
      // icon: LaptopMacIcon,
      color: '#3F51B5'
    },
    
  ];

  return (
    <>
    <GaugeChart
    id="gauge-chart9"
    // style={{width:"90%"}}
    nrOfLevels={420}
    arcsLength={arcs}
    colors={[ '#EA4228','#F5CD19','#5BE12C', ]}
    percent={props.healthGuage/100}
    arcPadding={0.02}
    hideText={true}
    animateDuration={10000}
    // animDelay={1000}
  />
    <Typography style={{ color:"black" }} variant="h4" > { props.healthGuage} %</Typography>
  </>
    // <Card {...props}>
    //   <CardHeader title="Part Health Status" />
    //   <Divider />
    //   <CardContent>
    //     <Box
    //       sx={{
    //         height: 200,
    //         position: 'relative'
    //       }}
    //     >
    //      <GaugeChart
    //           id="gauge-chart9"
		// 					// style={chartStyle}
    //           nrOfLevels={420}
    //           arcsLength={arcs}
    //           colors={[ '#EA4228','#F5CD19','#5BE12C', ]}
    //           percent={props.healthGuage/100}
    //           arcPadding={0.02}
    //           hideText={true}
    //           animateDuration={10000}
    //           // animDelay={1000}
    //         />
    //     </Box>
    //     <Box
    //       sx={{
    //         display: 'flex',
    //         justifyContent: 'center',
    //         pt: 2
    //       }}
    //     >
    //       {devices.map(({
    //         color,
    //         icon: Icon,
    //         title,
    //         value
    //       }) => (
    //         <Box
    //           key={title}
    //           sx={{
    //             p: 1,
    //             textAlign: 'center'
    //           }}
    //         >
    //           {/* <Icon color="action" /> */}
    //           <Typography
    //             color="textPrimary"
    //             variant="body1"
    //           >
    //             {title}
    //           </Typography>
    //           <Typography
    //             style={{ color }}
    //             variant="h4"
    //           >
    //             {value}
    //             %
    //           </Typography>
    //         </Box>
    //       ))}
    //     </Box>
    //   </CardContent>
    // </Card>
  );
};