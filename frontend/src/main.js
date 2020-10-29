import Vue from 'vue'
import "./plugins/vuetify.js"
import VueRouter from 'vue-router'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import Login from './components/Auth/Login.vue'
import Signup from './components/Auth/Signup.vue'
 import store from './store'
import Axios from 'axios'
import Vuex from 'vuex'

// import VueAxios from 'vue-axios'
Vue.use(VueRouter)
Vue.use(Vuex)
Vue.prototype.$http = Axios;
const token = localStorage.getItem('token')
if (token) {
  Vue.prototype.$http.defaults.headers.common['Authorization'] = token
}
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
  store,
  render: h => h(App)
}).$mount('#app')
