<template>
  <v-card display="block" class="mb-4">
    <v-card-title class="body-2"> Currency exchange </v-card-title>
    <v-card-text>
      <div>
        {{ this.currencyFrom }}:<strong class="red--text text--lighten-1">
          -{{ this.fromAmount.toFixed(2) }} {{ this.currency }}</strong
        >

        <div class="float-right">
          {{ this.currencyTo }}:<strong class="green--text text--lighten-1">
            {{ this.toAmount.toFixed(2) }} {{ this.currency }}</strong
          >
        </div>
      </div>
    </v-card-text>

    <v-divider />
  </v-card>
</template>

<script>
export default {
  props: {
    currencyFrom: {
      type: String
    },
    currencyTo: {
      type: String
    },
    fromAmount: {
      type: Number
    },
        toAmount: {
      type: Number
    },


    time: {}
  },
  computed: {
    shortcutFrom: function() {
      return this.getShortcut(this.currencyFrom);
    },
    shortcutTo: function() {
      return this.getShortcut(this.currencyTo);
    },

  },
  methods: {
    getShortcut(currency) {
      console.log(currency);
    }
  }
};
</script>
