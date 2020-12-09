import Vue from "vue";

export default {
  async getTransfers() {
    return Vue.axios.get("/transfers/");
  },

  async sendTransfer(data) {
    return Vue.axios.post(/transfers/, data);
  }
};
