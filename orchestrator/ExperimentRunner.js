import sendRequest from "./httpService.js";
import eventBus from "./eventBus.js";

class ExperimentRunner {
    constructor(config) {
        this.config = config;

    }
    async run() {
     try {
        eventBus.emit("experiment:start");
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
            const results = await Promise.allSettled(promises);
            const successful = results.filter(
                result => result.status === "fulfilled"
            );

            const failed = results.filter(
                result => result.status === "rejected"
            );
            eventBus.emit("experiment:success");
            eventBus.emit("experiment:complete");
            return {
                successful, 
                failed
            };
        }

        catch(error) {
            eventBus.emit("experiment:error", error);
            console.error(error);
            throw error;
        }
        }
       
}

export default ExperimentRunner;