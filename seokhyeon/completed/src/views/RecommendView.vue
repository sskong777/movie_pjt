<template>
  <div>
    <h1>Recommend</h1>
    <button @click="[recommendMovies(), topPick()]" class="btn btn-success">TOP 10</button>
    <button @click="[recommendMovies(), userPick()]" class="btn btn-success mx-5">User Recommend</button>
    <button @click="[recommendMovies(), likePick()]" class="btn btn-success">Atrraction</button>
    <!-- <div v-if="topCheck"> -->
    <!-- <movie-card v-for="movie in recoMovies[0]" :key="movie.pk" :movie="movie">
    </movie-card>
   </div>
       <div v-if="userCheck">
    <movie-card v-for="movie in recoMovies[1]" :key="movie.pk" :movie="movie">
    </movie-card>
   </div>
       <div v-if="likeCheck">
    <movie-card v-for="movie in recoMovies[2]" :key="movie.pk" :movie="movie">
    </movie-card>
  </div> -->
    
      <vue-glide v-if="topCheck"
      class="glide__track"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      :breakpoints="{3000: {perView: 7}, 1100: {perView: 5}, 600: {perView: 3}}"
    >
      <vue-glide-slide
        v-for="recomovie in recoMovies[0]"
        :key="recomovie.pk">
        <RecoMovieCard :recomovie="recomovie"
          />
      </vue-glide-slide>
    </vue-glide>

      <vue-glide v-if="userCheck"
      class="glide__track"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      :breakpoints="{3000: {perView: 7}, 1100: {perView: 5}, 600: {perView: 3}}"
    >
      <vue-glide-slide class="mx-2"
        v-for="recomovie in recoMovies[1]"
        :key="recomovie.pk">
        <RecoMovieCard :recomovie="recomovie"
          />
      </vue-glide-slide>
    </vue-glide>
 
      <vue-glide v-if="likeCheck"
      class="glide__track"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      :breakpoints="{3000: {perView: 7}, 1100: {perView: 5}, 600: {perView: 3}}"
    >
      <vue-glide-slide class="mx-2"
        v-for="recomovie in recoMovies[2]"
        :key="recomovie.pk">
        <RecoMovieCard :recomovie="recomovie"
          />
      </vue-glide-slide>
    </vue-glide>


  </div>
</template>

<script>
  import { Glide, GlideSlide } from 'vue-glide-js'
  import { mapActions, mapGetters } from 'vuex'
  // import MovieCard from '@/components/movie/MovieCard.vue'
  import RecoMovieCard from '@/components/movie/RecoMovieCard.vue'
  export default {
    name: 'MovieList',
    components: {
      RecoMovieCard,
      [Glide.name]: Glide,
      [GlideSlide.name]: GlideSlide,
    },
    data () {
      return {
        topCheck: false,
        userCheck: false,
        likeCheck: false,
      }
    },
    computed: {
      ...mapGetters(['recoMovies']),
      checkTop() {
        return this.topCheck
      },
      checkUser() {
        return this.userCheck
      },
      checkLike() {
        return this.likeCheck
      }
    },
    methods: {
      ...mapActions(['recommendMovies']),
      topPick: function () {
        this.topCheck = !this.topCheck
        this.userCheck = false
        this.likeCheck = false
      },
      userPick: function () {
        this.userCheck = !this.userCheck
        this.topCheck = false
        this.likeCheck = false
      },
      likePick: function () {
        this.likeCheck = !this.likeCheck
        this.userCheck = false
        this.topCheck = false
      }
    },
  }
</script>

<style>
  vue-glide-slide{
    padding :3em;
  }

</style>
