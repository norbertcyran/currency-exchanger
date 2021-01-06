import Vue from "vue";
export default {
  async getStocks() {
    return Vue.axios.get("/api/stocks/");
  },
  async stockTransaction(data) {
    return Vue.axiost.post("/api/stocktransfers/", data);
  }
};
