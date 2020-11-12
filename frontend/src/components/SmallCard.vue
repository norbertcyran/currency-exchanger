<template >
  <v-card width="400px" display="block" class="mb-4">
    <v-card-title>
      {{ this.currency }}
    </v-card-title>
    <v-card-text>Dostępne środki: {{ this.ammount }} {{shortcut}}
                    <v-btn color="success" dark class="float-right" small>Cash-in
              <v-icon>mdi-chevron-up</v-icon>
            </v-btn>
    </v-card-text>

          <v-divider/>
  </v-card>

</template>


<script>
export default {
  props: {
    currency: {
      type: String
    },
    ammount: {
      type: Float64Array
    }
    
  },
    computed: {
      shortcut: function() {
        return this.generateShrotcut(this.currency);
      }
    },
  methods: {
    generateShrotcut(currency) {
        console.log("ja")
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
