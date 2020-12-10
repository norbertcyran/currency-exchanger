<template>
  <div class="mt-4">
    <SmallCard
      v-for="el in currencies"
      :key="el.currency"
      :currency="el.currency"
      :amount="el.amount"
    ></SmallCard>
  </div>
</template>
<script>
import SmallCard from "../components/SmallCard";
import walletAPI from "../api/wallet";
export default {
  data: () => ({
    currencies: [
      { currency: "dollar", amount: 300.23 },
      { currency: "zlotys", amount: 20.2 }
    ]
  }),
  methods: {
    async getUserCurrencies() {
      try {
        const response = await walletAPI.getWallet();
        this.currencies = response.data.currencies;


      } catch (err) {
        console.log(err);
      }
    }
  },
  created() {
    this.getUserCurrencies();
  },
  components: {
    SmallCard
  }
};
</script>
