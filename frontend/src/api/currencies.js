import Vue from "vue";
export default {
  async getUserCurrencies() {
    return Vue.axios.get("/currencies/getUserCurrencies");
  },
  async getExchangeRate(code) {
    return Vue.axios.get("/currencies/", {
      params: {code: code}
    });
  }
};
