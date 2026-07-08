import loadConfig from "./configLoader.js";
import validateConfig from "./configValidator.js";
import ExperimentRunner from "./ExperimentRunner.js";
import eventBus from "./eventBus.js";


const config = await loadConfig();
validateConfig(config);
const runner = new ExperimentRunner(config);
const results = await runner.run();
console.log(results);
console.log(config);

eventBus.on("experimnet:start", () => {
    console.log("Experiment Started");
});
eventBus.on("experiment:success", () => {
    console.log("Experiment Successful");
});

eventBus.on("experiment:error", (error) => {
    console.log("Experiment Failed");
    console.error(error.message);
});

eventBus.on("experiment:complete", () => {
    console.log("Experiment Completed");
});