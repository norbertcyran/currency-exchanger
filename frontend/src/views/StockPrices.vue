<template>
  <v-container fill-height>
    <v-layout align-center justify-center>
      <v-flex xs12 sm11 md20>
        <v-form>
          <v-card class="elevation-12">
            <v-toolbar dark color="blue">
              <v-toolbar-title>
                Stock Prices
              </v-toolbar-title>
            </v-toolbar>
            <v-card-text>
              <v-row>
                <v-col cols="7">
                  <LineChart
                    v-if="loaded"
                    :chartData="arrPrices"
                    :options="chartOptions"
                    :label="stocklabel"
                  />
                </v-col>
                <v-col cols="5">
                  <v-combobox
                    label="Type stock name"
                    outlined
                    dense
                    v-on:change="onStockNameChange"
                  ></v-combobox>
                  <v-text-field
                    ref="amount"
                    v-model="amount"
                    label="amount"
                    placeholder="0"
                  ></v-text-field>
                  <v-text v-if="amount != 0">
                    Total cost: {{ totalPrice }}€
                    <BuyStocksModal
                      :currentPrice="this.arrPrices[arrPrices.length - 1].price"
                      :label="this.stocklabel"
                    />
                  </v-text>
                </v-col>
              </v-row>
            </v-card-text>
            <v-divider light></v-divider>
          </v-card>
        </v-form>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
import LineChart from "../components/LineChart";
import BuyStocksModal from "../components/BuyStocksModal";
import stocks from "../api/stocks";
export default {
  name: "stockprices",
  stockNames: [],
  ischartloading: false,
  components: {
    LineChart,
    BuyStocksModal
  },
  data: () => ({
    loaded: true,
    amount: 0,
    arrPrices: [
      {
        date: "13/12/2020",
        price: 18
      },
      {
        date: "12/12/2020",
        price: 12
      }
    ],
    stocklabel: "Stock prices",
    chartOptions: {
      responsive: true,
      maintainAspectRatio: false
    }
  }),

  created() {
    this.getStockNames();
  },
  methods: {
    onStockNameChange: function() {
      this.amount = 0;
      this.getStockPrices();
    },
    async getStockPrices() {
      try {
        const response = await stocks.getStockPrices();
        this.arrPrices = response.data.prices;
      } catch (err) {
        console.log(err);
      }
    },
    async getStockNames() {
      try {
        const response = await stocks.getStockNames();
        const stockNames = response.data.stockNames;
        this.stockNames = stockNames;
      } catch (err) {
        console.log(err);
      }
    }
  },
  computed: {
    totalPrice: function() {
      return this.amount * this.arrPrices[0].price;
    }
  }
};
</script>
