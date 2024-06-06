import axios from "axios";

axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";


export async function getDiseasesList() {
    // get list of diseases's names and labels REST API
    try {
      let response = await axios.get("api/diseases");
      let diseases = await response.data
      console.log(diseases);
      return diseases
    } catch(err) {
      if (err.response) {
        console.error('error: ', err.response.status);
      }
    }
  }

export async function getDetailedDisease(disease_id) {
  // get data for a given disease from REST API
  let disease_data = null;
  let response_status = null;
  let error_message = null;

  try {
    let response = await axios.get("api/diseases/" + disease_id);
    disease_data = await response.data
    response_status = response.status;
    console.log(disease_data);
    console.log(response_status);
    return disease_data

  } catch(err) {
      if (err.response) {
        response_status = err.response.status
        error_message = "No existe una enfermedad para el ID ingresado"
        console.log(error_message);
        return error_message
      }
    }
}
