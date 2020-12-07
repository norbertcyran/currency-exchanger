<template>
  <div>
    <v-card width="400px" class="mt-4">
      <v-snackbar absolute top v-model="snackbar">
        You have exceeded your payment resources

        <template v-slot:action="{ attrs }">
          <v-btn color="red" text v-bind="attrs" @click="snackbar = false">
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
            :rules="[rules.required, rules.email]"
          >
          </v-text-field>

          <v-select
            :items="userCurrenciesAndAmmount"
            label="Currency"
            v-model="value"
          ></v-select>
          <v-text-field
            name="amount"
            type="number"
            label="Ammount "
            v-model="amount"
            :rules="[rules.required]"
          >
          </v-text-field>
          <v-text-field name="title" label="Title " v-model="title">
          </v-text-field>
          <v-divider light></v-divider>
        </v-form>
      </v-card-text>

      <v-card-actions>
        <v-btn color="success" dark @click="checkAmmount"
          >Commit transfer
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>
<script>
import currenciesAPI from "../api/currencies";
export default {
  data: () => ({
    value: "",
    recipient: "",
    snackbar: false,
    text: `I'm a multi-line snackbar.`,
    currenciesAndAmmount: [
      {
        currency: "zloty",
        amount: 24
      },
      {
        currency: "dollar",
        amount: 30
      }
    ],
    title: "",
    amount: 0,
    rules: {
      required: value => !!value || "Required",
      email: value => {
        const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(value) || "Invalid e-mail.";
      }
    }
  }),

  components: {},
  methods: {
    async getUserCurrencies() {
      try {
        const response = await currenciesAPI.getUserCurrencies();
        this.arrCurrencies = response.data.currencies;
      } catch (err) {
        console.log(err);
      }
    },
    checkAmmount() {
      var amomountAvailable = this.value.split(" ")[1];
      amomountAvailable = amomountAvailable.substring(1);
      amomountAvailable = amomountAvailable.slice(0, -1);

      if (this.amount > amomountAvailable) {
        this.snackbar = true;
      }
    }
  },
  computed: {
    userCurrenciesAndAmmount: function() {
      var res = this.currenciesAndAmmount.map(
        cur => cur.currency + " (" + cur.amount + ")"
      );
      return res;
    }
  },
  created() {
    this.getUserCurrencies();
  }
};
</script>
