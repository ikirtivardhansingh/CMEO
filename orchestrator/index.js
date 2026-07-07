import loadConfig from "./configLoader.js";
import validateConfig from "./configValidator.js";
import ExperimentRunner from "./ExperimentRunner.js";


const config = await loadConfig();
validateConfig(config);
const runner = new ExperimentRunner(config);
const results = await runner.run();
console.log(results);
console.log(config);
