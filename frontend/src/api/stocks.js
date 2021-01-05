import Vue from "vue";
export default {
  async getStockNames() {
    return Vue.axios.get("/api/stocks/getNameList/");
  },
  async getStockPrices(stockName) {
    return Vue.axios.get("/api/stocks/getPrices/", {
      params: { stockName: stockName }
    });
  },
  async getUserStocks() {
    return Vue.axios.get("/api/stocks/getUserStocks/");
  },
  async buyStocks() {
    return Vue.axios.get("/stocks/buyStocks/");
  },
  async getStockTransfers() {
    return Vue.axios.get("/api/stocktransfer");

  }
};
