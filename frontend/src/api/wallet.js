import Vue from "vue";

export default {
  getWallet: async () => Vue.axios.get("/wallet/")
};
