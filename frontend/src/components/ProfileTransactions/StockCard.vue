<template >
  <v-card display="block" class="mb-4">
    <v-card-title class="body-2"> Stock transaction </v-card-title>
    <v-card-text>
      <div v-if="0<currencyAmount">
        {{this.stockName}}:<strong class="red--text text--lighten-1">  {{ this.stockAmount.toFixed(2) }}</strong>

        <div class="float-right">
            Euro:<strong class="green--text text--lighten-1"> {{ this.currencyAmount.toFixed(2) }} €</strong> </div>
      </div>
            <div v-else>
        {{this.stockName}}:<strong class="green--text text--lighten-1"> {{ this.stockAmount.toFixed(2) }}</strong>

        <div class="float-right">
            Euro:<strong class="red--text text--lighten-1"> {{ this.currencyAmount.toFixed(2) }} €</strong> </div>
      </div>
    </v-card-text>

    <v-divider />
  </v-card>
</template>


<script>
// import { currenciesAndShortcuts } from "../../global constant variables/currencies and shortcuts";
export default {
  props: {
    stockName: {
      type: String,
    },
    stockAmount: {
      type: Number,
    },

    currencyAmount: {
      type: Number,
    },
    time:{

    }
  },
  // computed: {
  //   currencyShortcut: function () {
  //     return this.getShortcut("Euro");
  //   },
  // },
  // methods: {
  //   getShortcut(currency) {
  //     console.log(currency);
  //     console.log(currenciesAndShortcuts);
  //     return currenciesAndShortcuts.find(element => element.currency == currency).shortcut
  //   },
  // },
};
</script>
