<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="600px">
      <template v-slot:activator="{ on, attrs }">
        <v-btn color="primary" dark v-bind="attrs" v-on="on" class="m-12">
           Cash-in
            </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">{{this.currency}} </span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6" md="12">
                <v-text-field label="Amount" v-model="amount" required></v-text-field>
              </v-col>

            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog = false">
            Close
          </v-btn>
          <v-btn color="blue darken-1" text @click="addMoney();dialog = false">
            Add
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>
<script>
import Vue from "vue";

export default {
  data: () => ({
    dialog: false,
    amount:0,
  }),
  props: {
    currency: {
      type: String,
    },
  },
  methods:{
      async addMoney(){
          let data ={
            currency: this.currency,
            amount: this.amount,
          }
          return await Vue.axios.post("/api/cashin/", data);
      }
  }

};
</script>