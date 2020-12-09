<template>
  <div class="mt-4"> 
    <StockCard
      v-for="el in userStocks"
      :key="el.label"
      :arrPrices="el.arrPrices"
      :amount="el.amount"
      :options="chartOptions"
      :label="el.label"
    ></StockCard>
  </div>
</template>
<script>
import StockCard from "../components/StockCard";
import stockAPI from "../api/stocks";
export default {
  data: () => ({
    userStocks: [
      {
        label: "cos",
        amount: 3,
        arrPrices: [
          {
            date: "13/12/2020",
            price: 18,
          },
          {
            date: "12/12/2020",
            price: 12,
          },
        ],
      },
      {
        label: "cos2",
        amount: 6,
        arrPrices: [
          {
            date: "13/12/2020",
            price: 18,
          },
          {
            date: "12/12/2020",
            price: 22,
          },
        ],
      },
    ],
    chartOptions: {
      responsive: true,
      maintainAspectRatio: false,
    },
  }),
  methods: {
    async getUserStocks() {
      try {
        const response = await stockAPI.getUserStocks();
        this.userStocks = response.data.Stocks;
      } catch (err) {
        console.log(err);
      }
    },
  },
  created() {
    this.getUserStocks();
  },
  components: {
    StockCard,
  },
};
</script>