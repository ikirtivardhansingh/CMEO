import {v4 as uuidv4 } from "uuid";

class ExperimentRunner {
    constructor(config) {
        this.config = config;
        this.experimentId = uuidv4(); 
    }
}

export default ExperimentRunner;