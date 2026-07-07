import sendRequest from "./httpService.js";

class ExperimentRunner {
    constructor(config) {
        this.config = config;

    }
    async run() {
        const results = [];
        for ( const model of this.config.models) {
            const payload = {
                model: model,
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
            const result = 
                await sendRequest(
                    `${BASE_URL} /predict`, 
                    payload);
            }
            results.push({model, result});
            return result;
        }
}

export default ExperimentRunner;