import Vue from "vue";

export default {
  async login(username, password) {
    return Vue.axios.post("/auth/login/", { username, password });
  },
  async logout() {
    return Vue.axios.post("/auth/logout/");
  },
  async register(data) {
    return Vue.axios.post("auth/register/", data);
  }
};
