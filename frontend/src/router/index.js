import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login.vue'
import UserRegister from '../components/UserRegister.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    component: Login
  },
  {
    path: '/userregister',
    component: UserRegister
  }
]

const router = new VueRouter({
  routes
})

export default router
