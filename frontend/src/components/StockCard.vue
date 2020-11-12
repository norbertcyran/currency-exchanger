<template>
  <v-card width="400px" class="mb-4">
    <v-card-title>
      <!-- {{ this.currency }} -->
      {{this.label}} : {{this.ammount}}
      <v-spacer></v-spacer>

      <v-btn icon @click="show = !show">
        <v-icon>{{ show ? "mdi-chevron-up" : "mdi-chevron-down" }}</v-icon>
      </v-btn>
    </v-card-title>
    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>
        <div height="150px">
          <LineChart
            :chartData="this.arrPrices"
            :options="this.chartOptions"
            :label="this.stocklabel"
          />
        </div>
        <v-card-actions>
          <v-btn color="green" dark>Buy
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn color="light-green" dark type="submit"
            >Sell
          </v-btn>
        </v-card-actions>
      </div>
    </v-expand-transition>
  </v-card>
</template>

<script>
import LineChart from "../components/LineChart";
export default {
  data: () => ({
     show: false,

  }),
  props: {
    label: {
      type: String
    },
    arrPrices: {
      type: Float64Array
    },
    ammount:{
      type: Number
    }

  },
  computed: {
    shortcut: function() {
      return this.generateShrotcut(this.currency);
    }
  },
  components: {
    LineChart
  }
};
</script>
