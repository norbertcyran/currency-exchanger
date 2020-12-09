import Vue from "vue";

export default {
  async getTransfers() {
    return Vue.axios.get("/api/transfers/");
  },

  async sendTransfer(data) {
    return Vue.axios.post("/api/transfers/", data);
  }
};
