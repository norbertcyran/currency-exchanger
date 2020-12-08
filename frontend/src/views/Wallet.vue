<template>
  <v-card class="mx-auto" width="700" height="600">
    <v-navigation-drawer permanent width="100%">
      <v-row class="fill-height" no-gutters>
        <v-navigation-drawer dark permanent>
          <v-list dense>
            <v-subheader>Wallet</v-subheader>
            <v-list-item-group v-model="selectedItem" color="primary">
              <v-list-item v-for="([icon, text], i) in items" :key="i">
                <v-list-item-icon>
                  <v-icon>{{ icon }}</v-icon>
                </v-list-item-icon>

                <v-list-item-content>
                  <v-list-item-title>{{ text }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-navigation-drawer>

        <div v-if="this.selectedItem == 0"><WalletCurrency /></div>
        <div v-if="this.selectedItem == 1"><WalletStock /></div>
        <div v-if="this.selectedItem == 2"><WalletCurrencyConversion /></div>
        <div v-if="this.selectedItem == 3"><Transfer /></div>
      </v-row>
    </v-navigation-drawer>
  </v-card>
</template>

<script>
import WalletCurrency from "./WalletCurrency";
import WalletStock from "./WalletStock";
import WalletCurrencyConversion from "./WalletCurrencyConversion";
import Transfer from "./Transfer";
export default {
  data: () => ({
    items: [
      ["mdi-wallet", "Your currencies"],
      ["mdi-chart-line", "Your stocks"],
      ["mdi-currency-usd", "Currency conversion"],
      ["mdi-cash-multiple", "Transfer"]
    ],
    selectedItem: 0
  }),

  components: {
    WalletCurrency,
    WalletStock,
    WalletCurrencyConversion,
    Transfer
  }
};
</script>
