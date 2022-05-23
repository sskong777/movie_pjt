<template>
  <nav class='navbar navbar-expand-xxl navbar-dark bg-dark sticky-top py-0'>
    <!-- <ul> -->
    <div class='container-fluid d-flex justify-content-between'>
        <router-link :to="{ name: 'movies' }" class="text-danger fw-bold">ACHCA</router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>        
        </button>
      <div class="collapse navbar-collapse flex-grow-0" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0 d-flex" >
          <li v-if="isLoggedIn" class='nav-item me-3'>
            <router-link :to="{ name: 'movieRecommend', params: { username } }">Recommend</router-link>
          </li>
            <li class='nav-item me-3'>
            <router-link :to="{ name: 'movieTheater' }">Theater</router-link>
          </li>
          <li class='nav-item me-3'>
            <router-link :to="{ name: 'articles' }">Community</router-link>
          </li>
          <li v-if="!isLoggedIn" class='nav-item me-3'>
            <router-link :to="{ name: 'login' }">Login</router-link>
          </li>
          <li v-if="!isLoggedIn" class='nav-item me-3'>
            <router-link :to="{ name: 'signup' }">Signup</router-link>
          </li>
          <li v-if="isLoggedIn" class='nav-item me-3'>
            <router-link :to="{ name: 'profile', params: { username } }">
              {{ currentUser.username }}'s page
            </router-link>
          </li>
          <li v-if="isLoggedIn">
            <router-link :to="{ name: 'logout' }">Logout</router-link>
          </li>
        </ul>
      </div>
    </div>
    <!-- </ul> -->
  </nav>
</template>

<script>
  import { mapGetters } from 'vuex'

  export default {
    name: 'NavBar',
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
  }
</script>

<style>
  nav {
    padding: 30px;
    background-color:rgba(185, 229, 247, 0.281);
  }

  nav a {
    font-weight: bold;
    color:whitesmoke;
    text-decoration-line: none;
  }

  nav a.router-link-exact-active {
    color:crimson;
  }
</style>
