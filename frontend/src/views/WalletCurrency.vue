<template>
  <div class="ma-4">
    <v-row>
      <v-col>
        <h3>Your currencies</h3>
      </v-col>
    </v-row>
    <CurrencyCard
      v-for="walletCurrency in wallet.currencies"
      :key="walletCurrency.currency"
      :currency="walletCurrency.currency"
      :amount="walletCurrency.amount"
    ></CurrencyCard>
    <v-row>
      <v-col>
        <h3>Cash in</h3>
      </v-col>
    </v-row>
    <CashInForm
      :user-currencies="userCurrencies"
      :other-currencies="otherCurrencies"
      :on-submit="cashIn"
    />
  </div>
</template>
<script>
import CurrencyCard from "@/components/CurrencyCard";
import currenciesApi from "@/api/currencies";
import { mapActions, mapGetters } from "vuex";
import CashInForm from "@/components/CashInForm";

export default {
  data: () => ({
    currencies: []
  }),
  methods: {
    ...mapActions(["fetchWallet", "cashIn"]),

    async fetchCurrencies() {
      const response = await currenciesApi.getCurrencies();
      this.currencies = response.data;
    }
  },
  computed: {
    ...mapGetters(["wallet"]),
    userCurrencies() {
      return this.wallet.currencies.map(currency => ({
        code: currency.currency,
        amount: currency.amount
      }));
    },
    otherCurrencies() {
      const userCodes = this.wallet.currencies.map(
        currency => currency.currency
      );
      return this.currencies.filter(
        currency => !userCodes.includes(currency.code)
      );
    }
  },

  async created() {
    await Promise.all([this.fetchWallet(), this.fetchCurrencies()]);
  },
  components: {
    CashInForm,
    CurrencyCard
  }
};
</script>
