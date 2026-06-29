import fs from "fs/promises";
import path from "path";

async function loadConfig() {
    const coonfigPath = path.join(
        process.cwd(),
        "config",
        "experiment.json"
    );
}