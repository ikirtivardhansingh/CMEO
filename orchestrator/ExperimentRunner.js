import sendRequest from "./httpService.js";

class ExperimentRunner {
    constructor(config) {
        this.config = config;

    }
    async run() {
     
        const promises = [];
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
                    promises.push( 
                        sendRequest(
                            `${BASE_URL}/predict`, 
                            payload
                        )
                    );
            }
            const results = await Promise.all(promises);
            return results;
        }
       
}

export default ExperimentRunner;