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
import currenciesAPI from "../api/currencies";
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
        const response = await currenciesAPI.getUserCurrencies();
        this.arrCurrencies = response.data.currencies;
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
