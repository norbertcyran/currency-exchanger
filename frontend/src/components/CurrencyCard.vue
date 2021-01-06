<template>
  <v-card width="400px" display="block" class="mb-4">
    <v-card-title>
      {{ currency }}
    </v-card-title>
    <v-card-text v-if="owned"
      >Available funds: {{ amount }} {{ currency }}
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: {
    currency: {
      type: String
    },
    amount: {
      type: String
    },
    owned: {
      type: Boolean,
      default: true
    }
  },

  components: {},
  methods: {
    cashIn(addAmount) {
      this.amount += parseFloat(addAmount);
    }
  }
};
</script>
