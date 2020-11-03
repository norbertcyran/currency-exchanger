<template>
  <v-container fill-height>
    <v-layout align-center justify-center>
      <v-flex xs12 sm8 md6>
        <v-form @submit="onSubmit">
          <v-card class="elevation-12">
            <v-toolbar dark color="blue">
              <v-toolbar-title>
                Login
              </v-toolbar-title>
            </v-toolbar>
            <v-card-text>
              <v-text-field
                prepend-icon="mdi-account"
                name="login"
                label="Login"
                type="text"
                v-model="email"
              >
              </v-text-field>
              <v-text-field
                prepend-icon="mdi-lock"
                name="password"
                label="Password"
                type="password"
                v-model="password"
              >
              </v-text-field>
            </v-card-text>
            <v-divider light></v-divider>
            <v-card-actions>
              <v-btn to="/signup" color="indigo" dark>Sign up</v-btn>
              <v-spacer></v-spacer>
              <v-btn color="indigo" dark type="submit"
                >Login
                <v-icon>mdi-arrow-right</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-form>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
export default {
  name: "login",
  data: () => ({
    email: "",
    password: ""
  }),
  methods: {
    async onSubmit(event) {
      event.preventDefault();
      await this.$store.dispatch("login", {
        username: this.email,
        password: this.password
      });
      await this.$router.push("/");
    }
  }
};
</script>
