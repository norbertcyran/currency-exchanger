<template>
  <div class="ma-4">
    <!--    <StockCard-->
    <!--      v-for="el in userStocks"-->
    <!--      :key="el.label"-->
    <!--      :arrPrices="el.arrPrices"-->
    <!--      :amount="el.amount"-->
    <!--      :options="chartOptions"-->
    <!--      :label="el.label"-->
    <!--    ></StockCard>-->
    <v-row>
      <v-col cols="12">
        <h3>Your stocks</h3>
      </v-col>
    </v-row>
    <v-data-table> </v-data-table>
    <v-row>
      <v-col cols="12">
        <h3>Stocks</h3>
      </v-col>
    </v-row>
    <v-data-table
      :headers="headers"
      :items="stocks"
      :loading="loading"
      loading-text="Loading stocks..."
    >
    </v-data-table>
  </div>
</template>
<script>
import stockAPI from "../api/stocks";
export default {
  data: () => ({
    loading: true,
    headers: [
      { text: "Stock code", value: "symbol" },
      { text: "Price (EUR)", value: "price" }
    ],
    stocks: []
  }),
  methods: {
    async getStocks() {
      try {
        const response = await stockAPI.getStocks();
        this.stocks = response.data;
      } catch (err) {
        console.log(err);
      } finally {
        this.loading = false;
      }
    }
  },
  async created() {
    await this.getStocks();
  }
};
</script>
