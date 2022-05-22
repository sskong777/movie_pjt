<template>
  <div>
    <h1>{{ '배우 프로필' }}</h1>

  <h2>출연한 영화</h2>
  <!-- {{ actor }} -->
  <ul>
    <li v-for="(movie, idx) in actor.movies" :key="idx">
      <router-link :to="{ name: 'movie', params: { moviePk: movie.pk } }">
        {{ movie.title }}
      </router-link>
    </li>
  </ul>
  </div>

</template>

<script>
import { mapActions, mapGetters } from 'vuex'


export default {
  name: 'ActorProfile',
  computed: {
    ...mapGetters(['actor'])
  },
  methods: {
    ...mapActions(['fetchActor'])
  },
  created() {
    this.fetchActor(this.$route.params.actorPk)
  },
}
</script>
