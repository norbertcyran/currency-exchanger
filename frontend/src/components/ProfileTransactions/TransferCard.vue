<template >
  <v-card  display="block" class="mb-4">
    <v-card-title class="body-2"> Money transfer </v-card-title>
    <v-card-text
      >Title: {{ title }}
      <div v-if="isOutgoing">
        To: {{ this.otherUser }}
      <div class="float-right"> <strong class="red--text text--lighten-1">  -{{ this.amount.toFixed(2) }} {{this.shortcut}}</strong></div>
      </div>
      <div v-else>
        From: {{ this.otherUser }}
   <div class="float-right"> <strong class="green--text text--lighten-1">  {{ this.amount.toFixed(2) }} {{this.shortcut}}</strong></div>
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
    },
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
