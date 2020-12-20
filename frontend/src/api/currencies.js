import Vue from "vue";
export default {
  async getUserCurrencies() {
    return Vue.axios.get("/api/currencies/getUserCurrencies");
  },
  async getExchangeRate(code) {
    return Vue.axios.get("/api/currencies/", {
      params: {code: code}
    });
  },
  async getCurrencies(){
    return Vue.axios.get("/api/currencies/");
  }

};
