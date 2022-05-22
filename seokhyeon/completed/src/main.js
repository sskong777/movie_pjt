// import Vue from 'vue'
// import VueCookies from 'vue-cookies'

// import App from './App.vue'
// import router from './router'
// import store from './store'

// Vue.config.productionTip = false

// Vue.use(VueCookies)

// new Vue({
//   router,
//   store,
//   render: h => h(App)
// }).$mount('#app')


import Vue from "vue";
// import VueCookies from 'vue-cookies'
import Vuetify from "vuetify";
import "vuetify/dist/vuetify.min.css";

import VueGlide from "vue-glide-js"
import 'vue-glide-js/dist/vue-glide.css'

import App from "./App.vue";
import router from "./router";
import store from "./store";

Vue.config.productionTip = false;
Vue.use(VueGlide)
Vue.use(Vuetify);

new Vue({
  router,
  store,
  vuetify: new Vuetify(),
  render: (h) => h(App),
}).$mount("#app");