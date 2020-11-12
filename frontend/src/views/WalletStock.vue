<template>
  <div>
    <StockCard
      v-for="el in userStocks"
      :key="el.label"
      :arrPrices="el.arrPrices"
      :ammount="el.ammount"
      :options="chartOptions"
      :label="el.label"
    ></StockCard>
  </div>
</template>
<script>
import StockCard from "../components/StockCard";
export default {
  data: () => ({
    userStocks: [
      {
        label: "cos",
        ammount:3,
        arrPrices: [
          {
            date: "13/12/2020",
            price: 18
          },
          {
            date: "12/12/2020",
            price: 12
          }
        ]
      },
      {
        label: "cos2",
        ammount:3,
        arrPrices: [
          {
            date: "13/12/2020",
            price: 18
          },
          {
            date: "12/12/2020",
            price: 22
          }
        ]
      }
    ],
    chartOptions: {
      responsive: true,
      maintainAspectRatio: false
    }
  }),
  components: {
    StockCard
  }
};
</script>