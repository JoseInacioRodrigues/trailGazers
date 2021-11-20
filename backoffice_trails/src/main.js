import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const myApp = createApp(App)
myApp.config.delimiters = ['[[', ']]']
myApp.use(router).mount('#app')
