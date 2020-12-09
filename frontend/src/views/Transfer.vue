<template>
  <div>
    <v-card width="400px" class="mt-4">
      <v-snackbar
        :timeout="3000"
        v-model="snackbar.visible"
        :color="snackbar.success ? 'success' : 'error'"
        outlined
        top
      >
        {{ snackbar.text }}

        <template v-slot:action="{ attrs }">
          <v-btn
            :color="snackbar.success ? 'success' : 'error'"
            text
            v-bind="attrs"
            @click="snackbar.visible = false"
          >
            Close
          </v-btn>
        </template>
      </v-snackbar>
      <v-card-text>
        <v-form>
          <v-text-field
            name="recipient"
            label="Transfer recipient "
            v-model="recipient"
            :rules="[rules.required]"
          >
          </v-text-field>

          <v-select
            v-model="selectedCurrency"
            :items="wallet.currencies"
            :item-value="item => item"
            :item-text="item => `${item.currency} (${item.amount})`"
            label="Currency"
          ></v-select>
          <v-text-field
            v-model.number="amount"
            name="amount"
            label="Amount"
            :rules="[rules.required, checkAmount]"
          >
          </v-text-field>
          <v-text-field name="title" label="Title " v-model="title">
          </v-text-field>
          <v-divider light></v-divider>
        </v-form>
      </v-card-text>

      <v-card-actions>
        <v-btn color="success" small dark @click="sendTransfer"
          >Commit transfer
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>
<script>
import { mapGetters, mapActions } from "vuex";
import transfers from "@/api/transfers";

export default {
  data: () => ({
    selectedCurrency: null,
    recipient: "",
    snackbar: {
      visible: false,
      success: false,
      text: ""
    },
    snackbarText: "",
    title: "",
    amount: 0,
    rules: {
      required: value => !!value || "Required"
    }
  }),

  components: {},

  methods: {
    checkAmount() {
      if (this.selectedCurrency === null) return true;
      const availableFunds = parseFloat(this.selectedCurrency.amount);
      if (this.amount > availableFunds) {
        return "You have exceeded your payment resources.";
      }
      return true;
    },

    async sendTransfer() {
      try {
        await transfers.sendTransfer(this.formData);
        await this.fetchWallet();
        this.snackbar.text = "Transfer sent successfully";
        this.snackbar.success = true;
        this.snackbar.visible = true;
      } catch (e) {
        if (e.response.data.user_to) {
          this.snackbar.text = "User with such name does not exist.";
          this.snackbar.visible = true;
          this.snackbar.success = false;
        }
        console.log(e);
      }
    },

    ...mapActions(["fetchWallet"])
  },

  computed: {
    ...mapGetters(["wallet"]),

    formData() {
      return {
        user_to: this.recipient,
        currency: this.selectedCurrency.currency,
        title: this.title,
        amount: this.amount
      };
    }
  }
};
</script>
