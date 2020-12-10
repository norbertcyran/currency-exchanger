<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="600px">
      <template v-slot:activator="{ on, attrs }">
        <v-btn color="primary" dark v-bind="attrs" v-on="on"> Sell </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">{{ this.label }} </span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  label="Currency"
                  v-model="defaultCurrency"
                  disabled
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6">
                <v-text-field
                  label="Ammount"
                  v-model="amount"
                  :rules="[rules.available]"
                  type="number"
                  required
                >
                </v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6">
                <v-text-field
                  label="Price"
                  v-model="cost"
                  disabled
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog = false">
            Close
          </v-btn>
          <v-btn color="blue darken-1" text @click="dialog = false">
            Sell
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>
<script>
export default {
  data: () => ({
    dialog: false,
    amount: 0,
    defaultCurrency: "Euro (26)",
    userStockAmmount2: 0,
    rules: {
      available: (value) => value < this.userStockAmmount2 || "Required",
    },
  }),
  props: {
    label: {
      type: String,
    },
    currentPrice: {
      type: Number,
    },
    userStockAmmount: {
      type: Number,
      default: 0,
    },
  },

  methods: {
    updateSth() {
      this.userStockAmmount2 = this.userStockAmmount;
    },
  },
  computed: {
    cost: function () {
      return this.amount * this.currentPrice;
    },
  },
  mounted() {
    this.updateSth();
  },
};
</script>
