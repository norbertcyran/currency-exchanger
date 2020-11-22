<template>
  <v-container fluid class="text-center pa-0">
    <v-img
      src="@/assets/nicholas-capello-stock-market.jpg"
      :height="300"
      class="app-banner"
    >
    </v-img>
    <v-row align="center" justify="center" class="my-3">
      <v-col cols="12" class="app-heading">
        <h3 class="text-h2 my-8">Currency Exchanger</h3>
        <h5 class="text-h5 font-weight-light my-5">
          Online banking, currency exchange, stock trading. All in one place.
        </h5>
        <v-btn to="/signup" x-large color="primary" class="my-3">
          Register now
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "HomePage"
};
</script>

<style scoped lang="scss">
.app-banner {
  opacity: 0.6;
  position: absolute;
  top: 0;
}

.app-heading {
  z-index: 1;
}
</style>
