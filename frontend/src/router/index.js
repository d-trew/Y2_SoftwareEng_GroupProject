import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import SignupView from '../views/SignupView.vue'
import LoginView from '../views/LoginView.vue'
import FeedView from '../views/FeedView.vue'
import ChatView from '../views/ChatView.vue'
import SearchView from '../views/SearchView.vue'
import NotificationsView from '../views/NotificationsView.vue'
import ProfileView from '../views/ProfileView.vue'
import PostView from '@/views/PostView.vue'
import ConnectionsView from '../views/ConnectionsView.vue'
import EditProfileView from '../views/EditProfileView.vue'
import EditPasswordView from '../views/EditPasswordView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/feed',
      name: 'feed',
      component: FeedView
    },
    {
      path: '/messages',
      name: 'messages',
      component: ChatView
    },
    {
      path: '/search',
      name: 'search',
      component: SearchView
    },
    {
      path: '/notifications',
      name: 'notifications',
      component: NotificationsView
    },
    {
      path: '/:id',
      name: 'postview',
      component: PostView
    },
    {
      path: '/profile/:id',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/profile/:id/connections',
      name: 'connections',
      component: ConnectionsView
    },
    {
      path: '/profile/edit',
      name: 'editprofile',
      component: EditProfileView
    },
    {
      path: '/profile/edit/password',
      name: 'editpassword',
      component: EditPasswordView
    }
  ]
})

export default router
