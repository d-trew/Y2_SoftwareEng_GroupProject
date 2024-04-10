import { createApp } from 'vue';
import { createPinia } from 'pinia';
import App from './App.vue';
import router from './router';
import axios from 'axios';

import './assets/main.css';

// Set base URL for Axios
axios.defaults.baseURL = import.meta.env.VITE_API_URL;

// Create Vue app
const app = createApp(App);

// Use Pinia for state management
app.use(createPinia());

// Use Vue Router
app.use(router);

// Inject Axios instance into the Vue app
app.config.globalProperties.$axios = axios;

// Mount the app
app.mount('#app');
