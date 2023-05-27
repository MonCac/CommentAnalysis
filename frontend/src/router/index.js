import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login.vue'
import UserRegister from '../components/UserRegister.vue'
import MerchantRegister from '../components/MerchantRegister.vue'
import Recommend from '../components/Recommend.vue'
import UserInformation from '../components/UserInformation.vue'
import MerchantInformationManagement from '../components/MerchantInformationManagement'
import MerchantDisplay from '../components/MerchantDisplay.vue'



Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    component: Login
  },
  {
    path: '/userregister',
    component: UserRegister
  },
  {
    path: '/merchantregister',
    component: MerchantRegister
  },
  {
    path: '/recommend',
    component: Recommend
  },
  {
    path: '/userinformation',
    component: UserInformation
  },
  {
    path:'/merchantdisplay',
    component: MerchantDisplay
  },
  {
    path: '/merchantinformationmanagement',
    component: MerchantInformationManagement
  }
]

const router = new VueRouter({
  routes
})

export default router

// router.beforeEach((to, from, next) => {
//   if (to.path === '/login') return next()
//   const tokenStr = window.sessionStorage.getItem('token')
//   if (!tokenStr) return next('/login')
//   next()
// })
