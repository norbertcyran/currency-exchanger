import Vue from "vue";

export default {
  getWallet: async () => Vue.axios.get("/api/wallet/"),
  cashIn: async (currency, amount) =>
    Vue.axios.post("/api/cashin/", { currency, amount })
};
