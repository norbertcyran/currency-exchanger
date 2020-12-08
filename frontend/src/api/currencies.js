import Vue from "vue";

export default {
  async getUserCurrencies() {
    return Vue.axios.get("/currencies/getUserCurrencies");
  },
  async getExchangeRate(from, to) {
    return Vue.axios.get("/currencies/getExchangeRate", {
      params: { from: from, to: to }
    });
  }
};

