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
export default {
  props: {
    title: {
      type: String
    },
    isOutgoing: {
      type: Boolean
    },
    otherUser: {
      type: String
    },
    amount: {
      type: Number
    },
    currency: {
      type: String
    }
  },
  computed: {
    shortcut: function() {
      return this.generateShrotcut(this.currency);
    }
  },
  methods: {
    generateShrotcut(currency) {
      switch (currency) {
        case "zlotys":
          return "PLN";
        case "euro":
          return "€";
        case "dollar":
          return "$";
        case "Yen":
          return "¥";
        case "ruble":
          return "RUB";
        case "forint":
          return "HUF";
        case "krona":
          return "SEK";
        case "pound":
          return "£";
      }
    }
  }
};
</script>
