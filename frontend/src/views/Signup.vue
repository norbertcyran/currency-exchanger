<template>
  <v-container fluid fill-height>
    <v-layout align-center justify-center>
      <v-flex xs12 sm8 md6>
        <v-card class="elevation-12">
          <v-toolbar dark color="blue">
            <v-toolbar-title>
              Sign up
            </v-toolbar-title>
          </v-toolbar>
          <v-card-text>
            <v-form>
              <!-- <v-alert
                                :value="true"
                                color="error"
                                icon="mdi-alert"
                                >
                                This user already exist, try a diffrent one
                                </v-alert> -->

              <v-text-field
                prepend-icon="mdi-account"
                name="login"
                label="Login"
                v-model="nick"
                :rules="[rules.required]"
              >
              </v-text-field>

              <v-text-field
                prepend-icon="mdi-email"
                name="email"
                label="Email"
                v-model="email"
                :rules="[rules.required, rules.email]"
              >
              </v-text-field>

              <v-text-field
                prepend-icon="mdi-lock"
                name="password"
                label="Password"
                :rules="[rules.required]"
                type="password"
                :error="valid_length()"
                v-model="password"
              >
              </v-text-field>

              <v-text-field
                prepend-icon="mdi-lock-alert"
                name="password"
                label="Confirm Password"
                :rules="[rules.required]"
                type="password"
                :error="!valid()"
                v-model="confirm_password"
              >
              </v-text-field>

              <v-text-field
                name="first_name"
                label="First Name"
                :rules="[rules.required]"
                type="name"
                :error="!valid()"
                v-model="first_name"
              >
              </v-text-field>

              <v-text-field
                name="last_name"
                label="Lastname"
                :rules="[rules.required]"
                type="lastname"
                :error="!valid()"
                v-model="last_name"
              >
              </v-text-field>

              <v-text-field
                prepend-icon="mdi-phone"
                name="phone"
                label="Phone number"
                :rules="[rules.required]"
                type="phone"
                :error="!valid()"
                v-model="phone"
              >
              </v-text-field>

              <v-text-field
                name="billing_address"
                label="Billing address"
                :rules="[rules.required]"
                type="address"
                :error="!valid()"
                v-model="billing_address"
              >
              </v-text-field>


              <v-divider light></v-divider>
            </v-form>
          </v-card-text>

          <v-card-actions>
            <v-btn to="/login" color="black" dark>Sign in</v-btn>
            <v-spacer></v-spacer>
            <v-btn color="success" dark @click.native="register"
              >Register
              <v-icon>mdi-chevron-up</v-icon>
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
export default {
  data: () => ({
    password: "",
    confirm_password: "",
    nick: "",
    email: "",
    first_name: "",
    last_name: "",
    phone: "",
    billing_address: "",

    rules: {
      required: value => !!value || "Required",
      email: value => {
        const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(value) || "Invalid e-mail.";
      }
    }
  }),
  computed: {
    isFormValid: {
      get: () => ({})
    }
  },

  methods: {
    register() {
      let data = {
        username: this.nick,
        email: this.email,
        password1: this.password,
        password2: this.confirm_password,
        first_name: this.first_name,
        last_name: this.last_name,
        phone: this.phone,
        billing_address: this.billing_address

      };
      this.$store
        .dispatch("register", data)
        .then(() => this.$router.push("/"))
        .catch(err => console.log(err));


    },
    valid() {
      return this.password === this.confirm_password;
    },
    valid_length() {
      return this.password.length <= 8 && this.password.length != 0;
    }
  }
};
</script>
