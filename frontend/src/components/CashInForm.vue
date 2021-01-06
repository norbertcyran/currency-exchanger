<template>
  <v-form @submit.prevent="onSubmit(formData)">
    <v-row>
      <v-col :cols="4">
        <v-autocomplete
          v-model="formData.currency"
          :items="selectItems"
          item-value="code"
          item-text="code"
        ></v-autocomplete>
      </v-col>
      <v-col :cols="8">
        <v-text-field
          v-model="formData.amount"
          :rules="amountRules"
          label="Amount"
          required
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row justify="end">
      <v-col cols="auto">
        <v-btn color="primary" type="submit">Cash in</v-btn>
      </v-col>
    </v-row>
  </v-form>
</template>

<script>
export default {
  name: "CashInForm",
  props: {
    userCurrencies: Array,
    otherCurrencies: Array,
    onSubmit: Function
  },
  data: () => ({
    formData: {
      currency: "",
      amount: "0.00"
    },
    amountRules: [
      amount => !!amount || "Amount is required",
      amount =>
        !isNaN(Number(amount)) || "Amount needs to be a valid decimal number",
      amount => Number(amount) >= 0 || "Amount needs to be positive"
    ]
  }),
  computed: {
    selectItems() {
      return [
        { header: "Your currencies", divider: true },
        ...this.userCurrencies,
        { header: "Other currencies", divider: true },
        ...this.otherCurrencies
      ];
    }
  }
};
</script>

<style scoped></style>
