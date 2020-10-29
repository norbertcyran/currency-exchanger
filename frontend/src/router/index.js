import Vue from "vue";
import VueRouter from "vue-router";
import Login from "@/components/Auth/Login";
import Signup from "@/components/Auth/Signup";

Vue.use(VueRouter);

const routes = [
  {
    path: "/login",
    component: () => import(Login),
    name: "Login"
  },
  {
    path: "/signup",
    component: () => import(Signup),
    name: "Signup"
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
