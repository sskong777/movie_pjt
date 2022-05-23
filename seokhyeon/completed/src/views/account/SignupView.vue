<template>
  <div>
    <h1>Signup</h1>

    <account-error-list v-if="authError"></account-error-list>

    <div class="container" align="left">
    <form @submit.prevent="signup(credentials)" >
      <div class="form-group">
        <label for="username">Username </label>
        <input class="form-control" v-model="credentials.username" type="text" id="username" required 
        placeholder="Username" data-validation-required-message="Please enter your username."/>

      </div>
      <div class="form-group my-4">
        <label for="password1">Password </label>
        <input class="form-control" v-model="credentials.password1" type="password" id="password1" required 
        placeholder="Password" data-validation-required-message="Please enter your password."/>
      </div>
      <div class="form-group">
        <label for="password2">Password Confirmation</label>
        <input class="form-control" v-model="credentials.password2" type="password" id="password2" required 
        placeholder="Password2" data-validation-required-message="Please enter your password."/>
      </div>
      <div>
      <button type="submit" class="btn btn-primary mt-4">SignUp</button>

      </div>
    </form>
    </div>
    
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'SignupView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup'])
    },
  }
</script>

<style></style>
