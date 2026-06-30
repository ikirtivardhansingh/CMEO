function validateConfig(config) {
    if(!config.dataset) { 
        throw new Error("Dataset is required");
    }

    if (!config.models) {
        throw new Error("Models are required.");
    }

    if (config.models.length === 0) {
        throw new Error("At least one model is required.");
    }

}

export default validateConfig;
