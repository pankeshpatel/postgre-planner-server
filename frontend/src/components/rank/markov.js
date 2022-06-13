import { useEffect, useState } from 'react';
import { Bar } from 'react-chartjs-2';
import { Box, Button, Card, CardContent, CardHeader, Divider, useTheme } from '@mui/material';
import { setDate } from 'date-fns';
import axios from 'axios';
import {  ExceptionManagerCall } from 'src/utils/apihelper';
import ChartDataLabels from 'chartjs-plugin-datalabels';
import {  rankCall } from 'src/utils/apihelper';

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';



export const Markov = (props) => {
  // ChartJS.register(ChartDataLabels);
  const theme = useTheme();

  const [resultBool, setResultBool] = useState(false);
  const [GraphValues, setGraphValues] = useState([]);
  const [GraphLabels, setGraphLabels] = useState([]);

  ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend
  );

 

  let array2 = [];
  let array2_Exceptions = [];
  let arrayLabels = [];

  const [earlyPercentage, setEarlyPercentage] = useState();
  const [onTimePercentage, setOnTimePercentage] = useState();
  const [latePercentage, setLatePercentage] = useState();

  const [negThree, setNegThree] = useState();
  const [negTwo, setNegTwo] = useState();
  const [negOne, setNegOne] = useState();
  const [zero, setZero] = useState();
  const [one, setOne] = useState();
  const [two, setTwo] = useState();
  const [three, setThree] = useState();



  useEffect( async () => {


    if (resultBool == false){

        let data = await rankCall();
       // data = data.data;

        console.log("DATA Markov: ", data.markov);
        // console.log("DATA Markov -3: ", data.markov[0]["-3"]);
        // console.log("DATA Markov -2: ", data.markov[1]["-2"]);
        // console.log("DATA Markov -1: ", data.markov[2]["-1"]);
        // console.log("DATA Markov 0: ", data.markov[3]["0"]);
        // console.log("DATA Markov 1: ", data.markov[4]["1"]);
        // console.log("DATA Markov 2: ", data.markov[5]["2"]);
        // console.log("DATA Markov 3: ", data.markov[6]["3"]);

        setNegThree(parseFloat(data.markov[0]["-3"]));
        setNegTwo(parseFloat(data.markov[1]["-2"]));
        setNegOne(parseFloat(data.markov[2]["-1"]));
        setZero(parseFloat(data.markov[3]["0"]));
        setOne(parseFloat(data.markov[4]["1"]));
        setTwo(parseFloat(data.markov[5]["2"]));
        setThree(parseFloat(data.markov[6]["3"]));


        // let resultErr = localStorage.getItem('RunCallPass');

        // if (resultErr == false){
        //     setResultBool(false);
        // } else {
        //     setResultBool(true);
        // }
    }
  });

  let negThreeValue = negThree*100;
  let negTwoValue = negTwo*100;
  let negOneValue = negOne*100;
  let zeroValue = zero*100;
  let oneValue = one*100;
  let twoValue = two*100;
  let threeValue = three*100;

//   let negThreeValue = 4.2;
//   let negTwoValue = 29.1;
//   let negOneValue = 8.3;
//   let zeroValue = 16.7;
//   let oneValue = 8.3;
//   let twoValue = 12.5;
//   let threeValue = 20.8;



  let e = earlyPercentage*100;
  let ot = onTimePercentage*100;
  let l = latePercentage*100;
    

  let data ={ 
    datasets:[{
      label: '-3',
        data: [negThreeValue],
        stack:"",
        backgroundColor: "#FFC100"
      },
      {
        label: '-2',
        data:  [negTwoValue],
        stack:"",
        backgroundColor: "#FED862"
      },
      {
        label: '-1',
        data:  [negOneValue],
        stack:"",
        backgroundColor: "#FCE290"
      },

      {
        label: '0',
        data:  [zeroValue],
        stack:"",
        backgroundColor: "#00FF00"
      },
      {
        label: '1',
        data:  [oneValue],
        stack:"",
        backgroundColor: "#FAA2A2"
      },
      {
        label: '2',
        data:  [twoValue],
        stack:"",
        backgroundColor: "#FC6A6A"
      },
      {
        label: '3',
        data:  [threeValue],
        stack:"",
        backgroundColor: "#FF0000"
      },
  ],
    labels:['Arrival Probabilities']
  }


  const options = {
    animation: true,
    cornerRadius: 20, 
    // color=['red','blue'],
    layout: { padding: 0 },
    // legend: { display: true },
    maintainAspectRatio: false,
    responsive: true,
    indexAxis: 'y',
    plugins: {
      tooltip:true,
      legend:{
        display:true,
        position: 'bottom',
        align: 'center'
      },
      datalabels: {
        formatter: function(value, context) {
          return value.toString().slice(0,5)
        },

        color:'black',
        align: 0,
        anchor: "end",
        offset:5,
     
        clip: true,
        font: {
          size: "18",
          weight: "bold"
        }
      }
    },
    scales: {
        y: {
            ticks: { color: 'black', beginAtZero: true },
            },
        
        x: {
            ticks: { color: 'black', beginAtZero: true },
            title: {display: true, text: 'Percantages', color:"black"},
            },
        xAxes: [{
            stacked: true,
            // ticks: {
            //     fontColor: theme.palette.text.secondary,
            //     beginAtZero: true,
            //     min: 0
            //   },
            // gridLines: {
            //     borderDash: [2],
            //     borderDashOffset: [2],
            //     color: theme.palette.divider,
            //     drawBorder: false,
            //     zeroLineBorderDash: [2],
            //     zeroLineBorderDashOffset: [2],
            //     zeroLineColor: theme.palette.divider
            // }
        }],
        yAxes: [{
            stacked: true,
          //  ticks: {fontColor: theme.palette.text.secondary},
          //  gridLines: {display:false,drawBorder: false}
        }]
    },
    // scales: {
    //   y: {
    //     ticks: { color: 'black', beginAtZero: true },
    //     //stacked: true,
    //   },
    
    //     x: {
    //     ticks: { color: 'black', beginAtZero: true },
        
    //     title: {
    //         display: true,
    //         text: 'Percantages',
    //         color:"black" 
    //     },
    //     // stacked: true
        
    //     }
    // },
    // yAxes: [
    //   {
    //     ticks: {fontColor: theme.palette.text.secondary},
    //     gridLines: {display:false,drawBorder: false}
    //   }
    // ],
    // xAxes: [
    //   {
    //     ticks: {
    //       fontColor: theme.palette.text.secondary,
    //       beginAtZero: true,
    //       min: 0
    //     },
    //     gridLines: {
    //       borderDash: [2],
    //       borderDashOffset: [2],
    //       color: theme.palette.divider,
    //       drawBorder: false,
    //       zeroLineBorderDash: [2],
    //       zeroLineBorderDashOffset: [2],
    //       zeroLineColor: theme.palette.divider
    //     }
    //   }
    // ],

  
 
  };

  return (
    <Card {...props}>
      <CardHeader
        action={(
          <Button
            // endIcon={<ArrowDropDownIcon fontSize="small" />}
            size="small"
          >
            <select>
            
              <option value="" key="">last 45 days</option>
       

            </select>
          </Button>
        )}
        title="Markov"
      />
      <Divider />
      <CardContent>
        <Box
          sx={{
            height: 350,
            position: 'relative'
          }}
        >
          <Bar style={{backgroundColor: "#ccc"}}
            data={data}
            options={options}
            //plugins={[ChartDataLabels]}
            
          />
        </Box>
      </CardContent>
      <Divider />
      <Box
        sx={{
          display: 'flex',
          justifyContent: 'flex-end',
          p: 2
        }}
      >
        {/* <Button
          color="primary"
          endIcon={<ArrowRightIcon fontSize="small" />}
          size="small"
        >
          Overview
        </Button> */}
      </Box>
    </Card>
  );
};
