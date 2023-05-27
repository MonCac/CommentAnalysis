import axios from "axios";

const BaseURL = '/api'
const service = axios.create({
  baseURL: BaseURL,
  timeout: 90000
});

service.interceptors.request.use(
  config => {
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

service.interceptors.response.use(
  response => {
    return response;
  },
);

export default service;
