import axios from "axios";
import { apiUrl, plannerId } from "./constants";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

let token = "";
let headers = "";

const getHeader = () => {
  if (typeof window !== "undefined" && localStorage.getItem("token")) {
    token = localStorage.getItem("token");
    // console.log("token",token)
    return (headers = {
      headers: {
        Authorization: `${token ? `Bearer ${token}` : ""}`,
        "Content-Type": "multipart/form-data",
      },
    });
  }
};

const notify = (message, status) => {
  if (status == "error") {
    toast.error(message);
  } else if (status == "success") {
    toast.success(message);
  } else if (status == "info") {
    toast.info(message);
  } else if (status == "warn") {
    toast.warn(message);
  } else {
    toast(message);
  }
};

const handleError = (err) => {
  console.log("erros", err);
  // return
  if (err) {
    notify("API error", "error");
  }
  return;

  if (err.response.status == 401) {
    //
    notify(JSON.stringify(err.response.data.detail), "error");
  }
  if (err.response.status == 400) {
    notify(JSON.stringify(err.response.data.detail), "error"); //bad request
  }
  if (err.response.status == 403) {
    notify(JSON.stringify(err.response.data.detail), "error"); //bad request
  }
  if (err.response.status == 404) {
    notify(JSON.stringify(err.response.data.detail), "error"); //page not found
  }
  if (err.response.status == 408) {
    //Request timeout -
    notify(JSON.stringify(err.response.data.detail), "error");
  }
  if (err.response.status == 500) {
    //internal sever
    notify(JSON.stringify(err.response.data.detail), "error");
  }
  if (err.response.status == 502) {
    //bad gateway - invalid response
    notify(JSON.stringify(err.response.data.detail), "error");
  }
};

const loginCall = (body) => {
  const url = `${apiUrl}/users/login`;
  return new Promise((resolve, reject) => {
    const header = getHeader();
    const url = `${apiUrl}/users/login`;
    console.log("url", url);
    const options = {
      method: "POST",
      body: body,
      headers: {
        "Content-Type": "application/json",
      },
    };
    axios
      .post(url, body, header)
      // fetch(url,options)
      .then((res) => {
        resolve(res.data);
      })
      .catch((err) => {
        reject(handleError(err));
      });
  });
};

const healthScoreCall = (materialId, healthDate) => {
  const url = `${apiUrl}/healthscore/${eval(plannerId)}/${materialId}?healthdate=${healthDate}`;
  console.log("url", url);
  // http://localhost:8000/exceptions/healthscore/115/?start_date=02/18/22&end_date=04/04/22
  return new Promise((resolve, reject) => {
    const header = getHeader();
    axios
      .get(url, header)
      .then((res) => {
        resolve(res.data);
      })
      .catch((err) => {
        reject(handleError(err));
      });
  });
};

const ExceptionManagerCall = (currentDate) => {
  const url = `${apiUrl}/exceptions/manager/${eval(plannerId)}?days=${currentDate}`;
  // http://localhost:8000/exceptions/manager/114/?days=60

  return new Promise((resolve, reject) => {
    const header = getHeader();
    axios
      .get(url, header)
      .then((res) => {
        resolve(res.data);
      })
      .catch((err) => {
        reject(handleError(err));
      });
  });
};

const ExceptionMatrixCall = (currentDate) => {
  const url = `${apiUrl}/exceptions/matrix/${eval(plannerId)}?days=${currentDate}`;
  // http://localhost:8000/exceptions/matrix/114/?days=60
  // http://localhost:8000/exceptions/manager/115/?start_date=02/18/22&end_date=04/04/22
  return new Promise((resolve, reject) => {
    const header = getHeader();
    axios
      .get(url, header)
      .then((res) => {
        resolve(res.data);
      })
      .catch((err) => {
        reject(handleError(err));
      });
  });
};

const plannerIdCall = () => {
  const url = `${apiUrl}/planners/planner-id/${eval(plannerId)}`;
  return new Promise((resolve, reject) => {
    const header = getHeader();
    axios
      .get(url, header)
      .then((res) => {
        resolve(res.data);
      })
      .catch((err) => {
        reject(handleError(err));
      });
  });
};

const matetrialCall = () => {
  const url = `${apiUrl}/materials/${eval(plannerId)}`;
  return new Promise((resolve, reject) => {
    const header = getHeader();
    axios
      .get(url, header)
      .then((res) => {
        resolve(res.data);
      })
      .catch((err) => {
        reject(handleError(err));
      });
  });
};

// const rankCall = () => {
//   const url = `${apiUrl}/ranking/${eval(plannerId)}/742065710`; // change material number
//   // http://localhost:8000/ranking/114/742065710
//   return new Promise((resolve, reject) => {
//     const header = getHeader();
//     axios
//       .get(url, header)
//       .then((res) => {
//         resolve(res.data);
//       })
//       .catch((err) => {
//         reject(handleError(err));
//        // localStorage.setItem('RunCallPass', false);   // ADDEDDDDD
//       });
//      // localStorage.setItem('RunCallPass', true);
//   });
// };

const rankCall = () => {
  var material = localStorage.getItem("materialID");
  console.log("MATERIAL: ", material);
  const url = `${apiUrl}/ranking/${eval(plannerId)}/${material}`; // change material number
  // http://localhost:8000/ranking/114/742065710
  return new Promise((resolve, reject) => {
    const header = getHeader();
    axios
      .get(url, header)
      .then((res) => {
        resolve(res.data);
      })
      .catch((err) => {
        reject(handleError(err));
      });
  });
};

export {
  loginCall,
  healthScoreCall,
  ExceptionManagerCall,
  ExceptionMatrixCall,
  plannerIdCall,
  matetrialCall,
  rankCall,
};
