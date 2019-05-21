import Vue from 'vue'
import Router from 'vue-router'
import Vuetify from 'vuetify'

import SignIn from '@/components/SignIn'
import SignUp from '@/components/SignUp'
import Mainpage from '@/components/Mainpage'
import NewChat from '@/components/NewChat'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'SignIn',
      component: SignIn
    },
    {
      path: '/signUp',
      name: 'SignUp',
      component: SignUp
    },
    {
      path: '/mainpage',
      name: 'Mainpage',
      component: Mainpage
    },
    {
      path: '/newChat',
      name: 'NewChat',
      component: NewChat
    }
  ]
})
