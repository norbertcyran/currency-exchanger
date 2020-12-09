<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <router-link to="/">
        <div class="d-flex align-center">
          <v-img
            alt="Vuetify Logo"
            class="shrink mr-2"
            contain
            src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
            transition="scale-transition"
            width="40"
          />

          <v-img
            alt="Vuetify Name"
            class="shrink mt-1 hidden-sm-and-down"
            contain
            min-width="100"
            src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
            width="100"
          />
        </div>
      </router-link>

      <v-spacer></v-spacer>
            <v-btn text to="/stockprices">
        <span class="mr-2">Stock prices</span>
      </v-btn>
      <v-btn text to="/wallet">
        <span class="mr-2">Wallet</span>
      </v-btn>
            <v-btn text to="/profile">
        <span class="mr-2">Profile</span>
      </v-btn>
      <v-btn v-if="isAuthenticated" @click="logout()" text>
        <span class="mr-2">Logout</span>
      </v-btn>
      <v-btn v-else to="/login" text>
        <span class="mr-2">Login</span>
      </v-btn>
    </v-app-bar>

    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>
<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "App",

  components: {},

  data: () => ({
    //
  }),

  computed: {
    ...mapGetters(["isAuthenticated"])
  },

  methods: {
    ...mapActions(["logout"])
  }
};
</script>
