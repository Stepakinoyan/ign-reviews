import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios';


const app = createApp(App)

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://127.0.0.1:4444/';
app.use(router)

app.mount('#app')
