import Vue from "vue";
export default {
  async getUserCurrencies() {
    return Vue.axios.get("/api/currencies/getUserCurrencies");
  },
  async getExchangeRate(from) {
    return Vue.axios.get("/api/currency/", {
      params: { code: from }
    });
  },
  async getCurrencies(){
    return Vue.axios.get("/api/currencies/");
  },
  async makeExchange(data){
    return Vue.axios.post("/api/exchange/",data);
  }
};
