import Vue from "vue";
import Vuex, { createLogger } from "vuex";
import auth from "./auth";
import wallet from "./wallet";

Vue.use(Vuex);

const debug = process.env.NODE_ENV !== "production";

export default new Vuex.Store({
  modules: {
    auth,
    wallet
  },
  strict: debug,
  plugins: debug ? [createLogger()] : []
});
