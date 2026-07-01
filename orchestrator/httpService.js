import axios from "axios";


async function sendRequest(url, data) {
    const response = await axios.post(url, data);

    return response.data;
}

export default sendRequest;
