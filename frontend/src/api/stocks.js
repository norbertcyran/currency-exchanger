import Vue from "vue";

export default {
  async getStocks(params = {}) {
    return Vue.axios.get("/api/stocks/", { params });
  },
  async stockTransaction(data) {
    return Vue.axios.post("/api/stocktransfers/", data);
  }
};
