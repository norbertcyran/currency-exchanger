<template >
  <v-card width="400px" display="block" class="mb-4">
    <v-card-title>
      {{ this.currency }}
    </v-card-title>
    <v-card-text
      >Dostępne środki: {{ this.amount }} {{ shortcut }}
      <div class="float-right">
        <CashInModal :currency="this.currency" :method="cashIn" />
      </div>
    </v-card-text>

    <v-divider />
  </v-card>
</template>


<script>
import CashInModal from "./CashInModal";
import { currenciesAndShortcuts } from "../global constant variables/currencies and shortcuts";
export default {
  props: {
    currency: {
      type: String,
    },
    amount: {
      type: Float64Array,
    },
  },

  components: {
    CashInModal,
  },
  computed: {
    shortcut: function () {
      return this.getShortcut(this.currency);
    },
  },
  methods: {
    getShortcut(currency) {
      console.log(currency);
      console.log(currenciesAndShortcuts);
      for (const elem in currenciesAndShortcuts) {
        if (currenciesAndShortcuts[elem].currency == currency)
          return currenciesAndShortcuts[elem].shortcut;
      }
    },
  
    cashIn(addAmount){
      this.amount+=parseFloat(addAmount)
      console.log(typeof addAmount)
    }
  }
};
</script>