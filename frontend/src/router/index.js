import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import GoogleLineChartView from '../views/GoogleLineChartView.vue'

Vue.use(VueRouter)  // vue 에서 vue router 를 사용하기 위해 알려줘야합니다.

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/equity-eps',
    name: 'equity-eps',
    component: GoogleLineChartView
  }
]

const router = new VueRouter({
  mode: 'history',                // browser history mode 를 사용합니다.
  base: process.env.BASE_URL,
  routes,                         // path 별 component 를 추가합니다.
})

export default router
