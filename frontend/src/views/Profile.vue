<template>
  <v-container>
    <v-layout align-center justify-center>
      <v-flex xs8 sm8 md6>
        <v-form>
          <v-card class="elevation-12">
            <v-toolbar dark color="blue">
              <v-toolbar-title> Profile </v-toolbar-title>
            </v-toolbar>
            <v-card-text>
              Recent Transactions
              <TransferCard
                v-for="(el, index) in userTransfers"
                :key="index"
                :currency="el.currency"
                :amount="el.amount"
                :isOutgoing="el.isOutgoing"
                :otherUser="el.otherUser"
                :title="el.title"
              ></TransferCard>
            </v-card-text>
            <v-divider light></v-divider>
          </v-card>
        </v-form>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
import TransferCard from "../components/ProfileTransactions/TransferCard";
export default {
  data: () => ({
    recentTransactions: [],
    userTransfers: [
      {
        title: "money transfer1",
        isOutgoing: true,
        amount: 41,
        otherUser: "gaws@gmail.com",
        currency: "zlotys"
      },
      {
        title: "money transfer2",
        isOutgoing: false,
        amount: 41,
        otherUser: "gaws@gmail.com",
        currency: "zlotys"
      }
    ]
  }),
  components: {
    TransferCard
  }
};
</script>
