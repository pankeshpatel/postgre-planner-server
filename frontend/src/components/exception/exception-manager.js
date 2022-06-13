import { useEffect, useState } from "react";
import { Bar } from "react-chartjs-2";
import { Box, Button, Card, CardContent, CardHeader, Divider, useTheme } from "@mui/material";
import { setDate } from "date-fns";
import axios from "axios";
import { ExceptionManagerCall } from "src/utils/apihelper";
import ChartDataLabels from "chartjs-plugin-datalabels";
import { makeStyles } from "@mui/styles";

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

export const ExceptionManager = (props) => {
  // ChartJS.register(ChartDataLabels);
  const theme = useTheme();
  const classStyle = useStyles();


  const [resultBool, setResultBool] = useState(false);
  const [GraphValues, setGraphValues] = useState([]);
  const [GraphLabels, setGraphLabels] = useState([]);

  ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

  let array2 = [];
  let array2_Exceptions = [];
  let arrayLabels = [];

  useEffect(async () => {
    if (resultBool === false) {
      let data = await ExceptionManagerCall("60");
      // data = data.data;
      console.log("data", data);
      for (let i = 0; i < data.result.length; i++) {
        array2.push(parseFloat(data.result[i].percentage));
        array2_Exceptions.push(parseInt(data.result[i].exception));
      }

      for (let i = 0; i < data.exceptions.length; i++) {
        if (array2_Exceptions[i] === data.exceptions[i].exceptionID) {
          arrayLabels.push(data.exceptions[i].exceptionMsg);
        }
      }

      array2.push(100);
      setGraphValues(array2);
      setGraphLabels(arrayLabels);
      setResultBool(true);
    }
  });

  let token = "";
  let headers = "";

  // const ExceptionManagerCall = (plannerId,startDate,EndDate) => {
  //   const apiUrl = `http://18.208.171.25`;
  //   const url = `${apiUrl}/exceptions/manager/${plannerId}?start_date=${startDate}&end_date=${EndDate}`

  //   return new Promise((resolve,reject)=>{
  //   const header = getHeader();
  //           axios
  //               .get(url,header)
  //               .then((res)=>{
  //                   resolve(res)
  //               })
  //               .catch((err) => {
  //                   reject((err))
  //               })
  //           })
  // }

  const data = {
    // getEPDataAPI();
    plugins: {
      datalabels: {
        display: true,
        color: "white",
      },
    },
    datasets: [
      {
        barPercentage: 0.5,
        barThickness: 40,
        borderRadius: 4,
        categoryPercentage: 0.5,
        backgroundColor: ["#232323", "#28587b", "#253021", "#4C3B4D"],
        data: GraphValues,
        label: "",
        maxBarThickness: 100,
      },
    ],
    labels: GraphLabels,
  };

  const options = {
    animation: false,
    cornerRadius: 20,
    // color=['red','blue'],
    layout: { padding: 0 },
    // legend: { display: true },
    maintainAspectRatio: false,
    responsive: true,
    indexAxis: "y",
    plugins: {
      tooltip: false,
      legend: {
        display: false,
      },
      datalabels: {
        formatter: function (value, context) {
          return value.toString().slice(0, 5);
        },

        color: "black",
        align: 0,
        anchor: "end",
        offset: 5,

        clip: true,
        font: {
          size: "18",
          weight: "bold",
        },
      },
    },
    scales: {
      y: {
        ticks: { color: "black", beginAtZero: true },
      },

      x: {
        ticks: { color: "black", beginAtZero: true },

        title: {
          display: true,
          text: "Percantages",
          color: "black",
        },
      },
    },
    yAxes: [
      {
        ticks: {
          fontColor: theme.palette.text.secondary,
        },
        gridLines: {
          display: false,
          drawBorder: false,
        },
      },
    ],
    xAxes: [
      {
        ticks: {
          fontColor: theme.palette.text.secondary,
          beginAtZero: true,
          min: 0,
        },
        gridLines: {
          borderDash: [2],
          borderDashOffset: [2],
          color: theme.palette.divider,
          drawBorder: false,
          zeroLineBorderDash: [2],
          zeroLineBorderDashOffset: [2],
          zeroLineColor: theme.palette.divider,
        },
      },
    ],
  };

  return (
    <Card {...props} className={classStyle.card}>
      <CardHeader
        action={
          <Button
            // endIcon={<ArrowDropDownIcon fontSize="small" />}
            size="small"
          >
            <select>
              <option value="" key="">
                last 60 days
              </option>
            </select>
          </Button>
        }
        title="Part Exception Manager"
      />
      <Divider />
      <CardContent>
        <Box
          sx={{
            height: 400,
            position: "relative",
          }}
        >
          <Bar data={data} options={options} plugins={[ChartDataLabels]} />
        </Box>
      </CardContent>
      <Divider />
      <Box
        sx={{
          display: "flex",
          justifyContent: "flex-end",
          p: 2,
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

const useStyles = makeStyles({
  card: {
    border: "2px solid",
    borderColor: "#3a86ff",
    boxShadow: "0 19px 38px rgba(1,0.75,1,0.75), 0 15px 12px rgba(0,0,0,0.22)",
   // boxShadow: "9px 18px #3a86ff",   // AABDFF   ---   F1EFFE --- 6F6F6F --- 0166B1
    // borderColor: '#C4C4C4',
    marginTop:25,
    marginBottom:35
  }
});
