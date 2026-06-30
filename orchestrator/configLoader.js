import fs from "fs/promises";
import path from "path";

async function loadConfig() {
    const configPath = path.join(
        process.cwd(),
        "config",
        "experiment.json"
    );

    const fileContent = await fs.readFile(configPath, "utf-8");
    const config = JSON.parse(fileContent);
    return config;
}

export default loadConfig;