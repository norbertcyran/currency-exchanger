import Vue from "vue";
import VueRouter from "vue-router";
import Login from "@/views/Login";
import Signup from "@/views/Signup";
import Wallet from "@/views/Wallet";
import Profile from "@/views/Profile";
import HomePage from "@/views/HomePage";
import store from "@/store";

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
    path: "/wallet",
    component: Wallet,
    name: "Wallet",
    meta: { requiresAuth: true }
  },
  {
    path: "/profile",
    component: Profile,
    name: "Profile",
    meta: { requiresAuth: true }
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.getters.isAuthenticated) {
      next({
        path: "/login",
        query: { redirect: to.fullPath }
      });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
