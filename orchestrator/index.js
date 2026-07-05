import loadConfig from "./configLoader.js";
import validateConfig from "./configValidator.js";
import sendRequest from "./httpService.js";
import ExperimentRunner from "./ExperimentRunner.js";


const config = await loadConfig();


validateConfig(config);
console.log("Success");
console.log(config);
const payload = {
    model: "LogisticRegressionModel",
    features: [
        24,
        65.5,
        1572.0,
        0,
        "Yes",
        "No",
        "Yes",
        "Month-to-month"
    ]
};
const BASE_URL = "http://127.0.0.1:5000";
const result = await sendRequest(
    `${BASE_URL}/predict`,
    payload
);

console.log(result);