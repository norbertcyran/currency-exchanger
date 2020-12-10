import Vue from "vue";

export default {
  async login(username, password) {
    return Vue.axios.post("/api/auth/login/", { username, password });
  },

  async logout() {
    return Vue.axios.post("/api/auth/logout/");
  },

  async register(data) {
    return Vue.axios.post("/api/auth/register/", data);
  },

  fetchUser: async () => Vue.axios.get("auth/user/")
};
