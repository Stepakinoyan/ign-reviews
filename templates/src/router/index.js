import { createRouter, createWebHistory } from 'vue-router'
import Reviews from "../components/Reviews.vue"
import Review from "../components/Review.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Reviews
    },
    {
      path: '/review/:id',
      name: 'review',
      component: Review
    },

  ]
})

export default router
