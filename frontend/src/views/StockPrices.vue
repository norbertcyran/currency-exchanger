
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
                    ref="ammount"
                    v-model="ammount"
                    label="ammount"
                    placeholder="0"
                  ></v-text-field>
                  <v-text v-if="ammount != 0">
                    Total cost: {{ totalPrice }}€
                    <v-btn
                      class="float-right"
                      color="success"
                      dark
                      @click.native="register"
                    >
                      Buy stocks
                      <v-icon>mdi-cash-usd-outline</v-icon>
                    </v-btn>
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
import stocks from "../api/stocks";
export default {
  name: "stockprices",
  stockNames: [],
  ischartloading: false,
  components: {
    LineChart
  },
  data: () => ({
    loaded: true,
    ammount: 0,
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
    stocklabel: "Srock prices", //nie wyswietla sie v model z comboboxa
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
      this.ammount = 0;
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
      return this.ammount * this.arrPrices[0].price;
    }
  }
};
</script>
