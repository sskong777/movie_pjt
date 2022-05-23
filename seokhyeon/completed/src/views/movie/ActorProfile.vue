<template>
  <div>
    <!-- <h1>{{ '배우 프로필' }}</h1> -->
    <h1>{{ actor.actor_name }} 배우 프로필</h1>
  <hr>
  <h2>출연한 영화</h2>
  <hr>
  <!-- {{ actor }} -->

<!-- 
  <ul>
    <li v-for="(movie, idx) in actor.movies" :key="idx">
      <router-link :to="{ name: 'movie', params: { moviePk: movie.pk } }">
        {{ movie.title }}
      </router-link>
    </li>
  </ul> -->

   <!-- carousel-3d -->
   <carousel-3d :inverse-scaling="1500" :space="800" :width="600" :height="850" :controls-visible="true">
      <slide v-for="(movie,idx) in Object.keys(actor.movies).length"
        :key="idx" :index="idx">
        <figure>
          <router-link 
            :to="{ name: 'movie', params: {moviePk: actor.movies[idx].pk} }" class='movie_link'>
          <img :src="`https://image.tmdb.org/t/p/original/${actor.movies[idx].poster_path}`" alt="...">
          </router-link>        
      </figure>

      </slide>
    </carousel-3d>



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
