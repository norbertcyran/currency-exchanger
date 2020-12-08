<template>

  <v-card width="400px" class="mt-4" display="block">
    <v-toolbar-title>
      <!-- <h4>rate: {{this.exchangeRate}}</h4> -->
    </v-toolbar-title>
    <v-container>
      <v-row>
        <v-col cols="12" sm="6" md="6">
          <v-combobox
            v-model="fromCurrency"
            label="From"
            @change="getExchaneRate"
            :items="userCurrencies"
            outlined
            dense
          ></v-combobox>
        </v-col>

        <v-col cols="12" sm="6" md="6">
          <v-text-field
            v-model="fromCurrencyAmmount"
            label="Solo"
            placeholder="Ammount"
            solo
            :rules="[rules.required]"
          ></v-text-field>
        </v-col>
        <v-col cols="12" sm="6" md="6">
          <v-combobox
            v-model="toCurrency"
            label="To"
            :items="allCurrencies"
            outlined
            dense
            @change="updateNewCurrencyAmmount"
          ></v-combobox>
        </v-col>

        <v-col cols="12" sm="6" md="6">
          <v-text-field
            label=""
            solo
            disabled
            v-model="toCurrencyAmmount"
          ></v-text-field>
        </v-col>
      </v-row>
    </v-container>
    <v-card-actions>
      <v-layout align-center justify-center
        ><v-btn color="indigo" dark a>Change currency</v-btn>
      </v-layout>
    </v-card-actions>
  </v-card>
</template>
<script>
import currenciesAPI from "../api/currencies";
export default {
  data: () => ({
    currenciesAndAmmount: [
      {
        currency: "zloty",
        amount: 24,
      },
      {
        currency: "dollar",
        amount: 30,
      },

    ],
    allCurrencies: ["dollar", "zloty", "euro", "yen"],
    exchangeRate: 3.65,
    fromCurrency: "",
    toCurrency: "",
    fromCurrencyAmmount: 0,
    toCurrencyAmmount: 0,

    rules: {
      //   limitAmmount:  value => value <= this.maxAmmount || "you cannot exceed your limit",
      required: (value) => !!value || "Required.",
    },
  }),
  computed: {
    userCurrencies: function () {
      var res = this.currenciesAndAmmount.map((cur) => cur.currency);
      return res;
    },
    maxAmmount: function () {

      for (var i = 0; i < this.currenciesAndAmmount.length; i++) {
        if (this.currenciesAndAmmount[i].currency === this.fromCurrency) {
          return this.currenciesAndAmmount[i].amount;
        }
      }
      return 0;
    },

  },
  methods: {
    updateNewCurrencyAmmount() {
      this.toCurrencyAmmount = this.fromCurrencyAmmount * this.exchangeRate;
    },
    async getUserCurrrencies() {
      try {
        const response = await currenciesAPI.getUserCurrencies();
        this.currenciesAndAmmount = response.data.currenciesAndAmmount;
      } catch (err) {
        console.log(err);
      }
    },
    async getExchaneRate() {
      if (this.fromCurrency && this.toCurrency)
        try {
          const response = await currenciesAPI.getExchangeRate(
            this.fromCurrency,
            this.toCurrency
          );
          this.exchangeRate = response.data.exchangeRate;
        } catch (err) {
          console.log(err);
        }
    },
  },
};
</script>

