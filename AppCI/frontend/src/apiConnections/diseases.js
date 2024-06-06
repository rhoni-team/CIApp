import axios from "axios";

axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";


export async function getDiseasesList() {
    // get geopoints cases from REST API
    try {
      let response = await axios.get("api/diseases");
      let diseases = await response.data
      return diseases
    } catch(err) {
      if (err.response) {
        console.error('error: ', err.response.status);
      }
    }
  }
