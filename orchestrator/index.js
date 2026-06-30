import loadConfig from "./configLoader.js";
import validateConfig from "./configValidator.js";
const config = await loadConfig();

validateConfig(config);
console.log("Success");
console.log(config);