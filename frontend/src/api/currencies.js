import Vue from "vue";
export default {
  async getExchangeRate(curr) {
    return Vue.axios.get("/api/currencies/" + curr + "/");
  },
  async getCurrencies() {
    return Vue.axios.get("/api/currencies/");
  },
  async makeExchange(data) {
    return Vue.axios.post("/api/exchange/", data);
  },
  async getCurrencyExchanges() {
    return Vue.axios.get("/api/exchange");
  }
};
