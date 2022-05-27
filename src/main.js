import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import { createVuestic } from 'vuestic-ui';
import 'vuestic-ui/dist/vuestic-ui.css'
const app = createApp(App)

app.use(store)
app.use(router)
app.use(createVuestic())

app.mount('#app')
