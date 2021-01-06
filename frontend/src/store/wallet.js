import wallet from "@/api/wallet";

const state = () => ({
  wallet: {
    currencies: [],
    stocks: []
  },
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
    state.wallet = {
      currencies: [],
      stocks: []
    };
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
  },

  async cashIn({ commit, dispatch }, { currency, amount }) {
    commit("WALLET_REQUEST");
    await wallet.cashIn(currency, amount);
    dispatch("fetchWallet");
  }
};

export default { state, getters, mutations, actions };
