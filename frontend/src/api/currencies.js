import Vue from "vue";
export default {
  async getUserCurrencies() {
    return Vue.axios.get("/api/currencies/getUserCurrencies");
  },
  async getExchangeRate(from, to) {
    return Vue.axios.get("/api/currencies/getExchangeRate", {
      params: { from: from, to: to }
    });
  }
};
