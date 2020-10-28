<template>
    <v-container fluid fill-height >
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
                            :rules="[rules.required]"
                            >
                            </v-text-field> 

                            <v-text-field
                            prepend-icon="mdi-email"
                            name="email"
                            label="Email"
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
                            
                            <v-divider light></v-divider>
                            
                            </v-form>
                        </v-card-text>

                        <v-card-actions>
                            <v-btn to="/login" round color="black" dark>Sign in</v-btn>
                            <v-spacer></v-spacer>
                            <v-btn roun color="success" dark>Register
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
    data:() =>({
        password:'',
        confirm_password:'',
        rules:{
            required: value=> !!value || "Required",
            email: value=>{
                  const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
                  return re.test(value) || "Invalid e-mail."
            }
        }
    }),
    methods:{
        valid(){
            return this.password===this.confirm_password;
            },
        valid_length(){
            return this.password.length<=8 && this.password.length!=0;
        }
    }
}
</script>