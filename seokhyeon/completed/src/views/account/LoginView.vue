<template>
  <div>
    <h1>Login</h1>

    <account-error-list v-if="authError"></account-error-list>

    <div class="container" align="left">
    <form @submit.prevent="login(credentials)">
      <div class="form-group">
        <label for="username">Username </label>
        <input class="form-control" v-model="credentials.username" type="text" id="username" required />
      </div>

      <div class="form-group my-4">
        <label for="password">Password </label>
        <input class="form-control" v-model="credentials.password" type="password" id="password" required />
      </div>

      <button class="btn btn-primary">Login</button>
    </form>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'LoginView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        }
      }
    },
  computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['login'])
    },
  }
</script>

<style></style>
