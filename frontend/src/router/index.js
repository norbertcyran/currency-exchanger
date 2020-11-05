import Vue from "vue";
import VueRouter from "vue-router";
import Login from "@/views/Login";
import Signup from "@/views/Signup";
import HomePage from "@/views/HomePage";

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
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
