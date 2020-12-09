import Vue from "vue";
import VueRouter from "vue-router";
import Login from "@/views/Login";
import Signup from "@/views/Signup";
import HomePage from "@/views/HomePage";
import StockPrices from "@/views/StockPrices";
import Wallet from "@/views/Wallet";
import Profile from "@/views/Profile";
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    component: HomePage,
    name: "Home"
  },
  {
    path: "/login",
    component: Login,
    name: "Login"
  },
  {
    path: "/signup",
    component: Signup,
    name: "Signup"
  },
  {
    path: "/stockprices",
    component: StockPrices,
    name: "StockPrices"
  },
  {
    path: "/wallet",
    component: Wallet,
    name: "Wallet"
  },
  {
    path: "/profile",
    component: Profile,
    name: "Profile"
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
