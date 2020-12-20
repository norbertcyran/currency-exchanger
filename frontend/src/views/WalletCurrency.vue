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
import { mapGetters} from "vuex";



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
         this.currencies = this.wallet.currencies;


      } catch (err) {
        console.log(err);
      }
    }
  },
  computed: {
    ...mapGetters(["wallet"]),
  },


  created() {
    this.getUserCurrencies();
  },
  components: {
    SmallCard
  }
};
</script>
