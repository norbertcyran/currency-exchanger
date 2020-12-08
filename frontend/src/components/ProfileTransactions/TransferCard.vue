
<template>
  <v-card display="block" class="mb-4">
    <v-card-title class="body-2"> Money transfer </v-card-title>
    <v-card-text
      >Title: {{ title }}
      <div v-if="isOutgoing">
        To: {{ this.otherUser }}

        <div class="float-right">
          <strong class="red--text text--lighten-1">
            -{{ this.amount.toFixed(2) }}</strong
          >
        </div>
      </div>
      <div v-else>
        From: {{ this.otherUser }}
        <div class="float-right">
          <strong class="green--text text--lighten-1">
            {{ this.amount.toFixed(2) }}</strong
          >
        </div>
      </div>
    </v-card-text>

    <v-divider />
  </v-card>
</template>


<script>
import { currenciesAndShortcuts } from '../../global constant variables/currencies and shortcuts'
export default {
  props: {
    title: {
      type: String,
    },
    isOutgoing: {
      type: Boolean,
    },https://github.com/norbertcyran/currency-exchanger/pull/43/conflict?name=frontend%252Fsrc%252Fcomponents%252FSellStocksModal.vue&base_oid=c3fe829858eb129e96f19c5c6c138b17792fb39d&head_oid=74ec66ebf2c41efcd3ca1f4b9d86a64f34fbc837
    otherUser: {
      type: String,
    },
    amount: {
      type: Number,
    },
    currency: {
      type: String,
    },
    time:{

    }
  },
  computed: {
    shortcut: function () {
      return this.getShortcut(this.currency);
    },
  },
    methods: {
      getShortcut(currency){
        console.log(currency)
        console.log(currenciesAndShortcuts)
        for(const elem in currenciesAndShortcuts){

          if(currenciesAndShortcuts[elem].currency==currency) return currenciesAndShortcuts[elem].shortcut
        }
      },
  },

};
</script>
