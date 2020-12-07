import Vue from "vue";
import auth from "@/api/auth";

const state = () => ({
  status: "",
  token: localStorage.getItem("token") || "",
  user: {}
});

const getters = {
  isAuthenticated: state => state.token !== ""
};

const mutations = {
  AUTH_REQUEST(state) {
    state.status = "loading";
  },
  AUTH_SUCCESS(state, token, user) {
    state.status = "success";
    state.token = token;
    state.user = user;
  },
  AUTH_ERROR(state) {
    state.status = "error";
  },
  AUTH_LOGOUT(state) {
    state.status = "";
    state.token = "";
    state.user = {};
  },
  AUTH_SET_USER(state, user) {
    state.status = "";
    state.user = user;
  }
};

const actions = {
  async login({ commit, dispatch }, { username, password }) {
    commit("AUTH_REQUEST");
    try {
      const response = await auth.login(username, password);
      const token = response.data.key;
      const user = response.data.user;
      localStorage.setItem("token", token);
      Vue.axios.defaults.headers.common["Authorization"] = `Token ${token}`;
      commit("AUTH_SUCCESS", token, user);
      dispatch("fetchWallet");
    } catch (err) {
      commit("AUTH_ERROR");
      localStorage.removeItem("token");
    }
  },

  async logout({ commit }) {
    commit("AUTH_LOGOUT");
    try {
      await auth.logout();
    } finally {
      localStorage.removeItem("token");
      Vue.axios.defaults.headers.common["Authorization"] = "";
    }
  },

  async register({ commit }, data) {
    commit("AUTH_REQUEST");
    try {
      const response = await auth.register(data);
      const token = response.data.token;
      const user = response.data.user;
      localStorage.setItem("token", token);
      Vue.axios.defaults.headers.common["Authorization"] = `Token ${token}`;
      commit("AUTH_SUCCESS", token, user);
    } catch (err) {
      commit("AUTH_ERROR", err);
      localStorage.removeItem("token");
    }
  },

  async fetchUser({ commit }) {
    commit("AUTH_REQUEST");
    try {
      const response = await auth.fetchUser();
      const user = response.data;
      commit("AUTH_SET_USER", user);
    } catch (err) {
      commit("AUTH_ERROR", err);
    }
  }
};

export default {
  state,
  mutations,
  actions,
  getters
};
