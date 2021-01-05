import Vue from "vue";
export default {
  async getUserCurrencies() {
    return Vue.axios.get("/api/currencies/getUserCurrencies");
  },
  async getExchangeRate(curr) {
    return Vue.axios.get("/api/currencies/"+curr+"/");
  },
  async getCurrencies(){
    return Vue.axios.get("/api/currencies/");
  },
  async makeExchange(data){
    return Vue.axios.post("/api/exchange/",data);
  }
};
