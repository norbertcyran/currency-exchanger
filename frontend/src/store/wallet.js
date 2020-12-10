import wallet from "@/api/wallet";

const state = () => ({
  wallet: {},
  status: ""
});

const getters = {
  wallet: state => state.wallet
};

const mutations = {
  WALLET_REQUEST(state) {
    state.status = "loading";
  },

  SET_WALLET(state, wallet) {
    state.wallet = wallet;
    state.status = "success";
  },

  WALLET_ERROR(state) {
    state.wallet = {};
    state.status = "error";
  }
};

const actions = {
  async fetchWallet({ commit }) {
    commit("WALLET_REQUEST");
    try {
      const response = await wallet.getWallet();
      commit("SET_WALLET", response.data);
    } catch (err) {
      commit("WALLET_ERROR");
    }
  }
};

export default { state, getters, mutations, actions };
