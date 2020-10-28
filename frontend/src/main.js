import Vue from 'vue'
import "./plugins/vuetify.js"
import VueRouter from 'vue-router'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import Login from './components/Auth/Login.vue'
import Signup from './components/Auth/Signup.vue'

Vue.use(VueRouter)

const routes=[{
  path:'/login',
  component: Login,
  name:"Login"

},
{
path:'/signup',
component: Signup,
name:"Signup"

}];

const router = new VueRouter({
  mode:'history',
  routes,
  base:'/'

})
Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
