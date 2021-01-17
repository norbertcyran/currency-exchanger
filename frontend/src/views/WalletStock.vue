<template>
  <div class="ma-4">
    <v-snackbar
      v-model="snackbar"
      :timeout="2000"
      multi-line
      top
      outlined
      color="error"
    >
      {{ errorText }}
      <template v-slot:action="{ attrs }">
        <v-btn color="error" text v-bind="attrs" @click="snackbar = false"
          >Close
        </v-btn>
      </template>
    </v-snackbar>
    <v-row>
      <v-col>
        <h3>Your stocks</h3>
      </v-col>
    </v-row>
    <v-data-table :headers="userStocksHeaders" :items="wallet.stocks">
    </v-data-table>
    <v-row class="mt-3">
      <v-col>
        <h3>Stocks</h3>
      </v-col>
      <v-spacer></v-spacer>
      <v-col>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search"
          single-line
          hide-details
          class="pa-0 ma-0"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-data-table
      :headers="headers"
      :items="stocks"
      :loading="loading"
      :search="search"
      loading-text="Loading stocks..."
    >
      <template v-slot:item.actions="{ item }">
        <v-row justify="end">
          <v-col cols="2">
            <v-btn
              @click="tradeStock(item, true)"
              x-small
              fab
              block
              color="error"
              ><v-icon>mdi-minus</v-icon></v-btn
            >
          </v-col>
          <v-col cols="2" class="px-2">
            <v-text-field
              v-model.number="item.amount"
              type="number"
              single-line
              hide-details
              class="ma-0 pa-0 centered-input"
            ></v-text-field>
          </v-col>
          <v-col cols="2">
            <v-btn @click="tradeStock(item)" x-small fab block color="success"
              ><v-icon>mdi-plus</v-icon></v-btn
            >
          </v-col>
        </v-row>
      </template>
    </v-data-table>
  </div>
</template>
<script>
import { mapActions, mapGetters } from "vuex";
import stockAPI from "../api/stocks";
export default {
  data: () => ({
    search: "",
    loading: true,
    userStocksHeaders: [
      { text: "Stock code", value: "symbol" },
      { text: "Price (EUR)", value: "price" },
      { text: "Owned amount", value: "count" }
    ],
    headers: [
      { text: "Stock code", value: "symbol" },
      { text: "Price (EUR)", value: "price" },
      { text: "Actions", value: "actions", sortable: false, align: "end" }
    ],
    stocks: [],
    snackbar: false,
    errorText: ""
  }),
  computed: {
    ...mapGetters(["wallet"])
  },
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
    },

    async tradeStock(stock, sell = false) {
      const data = {
        stock: stock.symbol,
        amount: sell ? -stock.amount : stock.amount
      };
      try {
        await stockAPI.stockTransaction(data);
        await this.fetchWallet();
      } catch (error) {
        if (error.response && error.response.data) {
          const errorData = error.response.data;
          if (errorData.non_field_errors) {
            this.errorText = errorData.non_field_errors.join("\n");
            this.snackbar = true;
          }
        }
      }
    },

    ...mapActions(["fetchWallet"])
  },
  async created() {
    await this.getStocks();
  }
};
</script>
<style scoped lang="scss">
.centered-input::v-deep input {
  text-align: center;
  -moz-appearance: textfield;

  &::-webkit-outer-spin-button,
  &::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
  }
}
</style>
