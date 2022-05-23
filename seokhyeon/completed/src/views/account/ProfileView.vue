<template>
  <div class="container">
    <h1 align="left">{{ profile.username }}'s Page</h1>
  <hr>
  <h2>내가 좋아하는 영화</h2>
  
   <!-- carousel-3d -->
   <carousel-3d :controls-visible="true" :clickable="false" :width="400" :height="580">
      <slide v-for="(favomovie,idx) in Object.keys(profile.favorite_movies).length"
        :key="idx" :index="idx">
        <figure>
          <router-link 
            :to="{ name: 'movie', params: {moviePk: profile.favorite_movies[idx].id} }" class='movie_link'>
          <img :src="`https://image.tmdb.org/t/p/original/${profile.favorite_movies[idx].poster_path}`" alt="...">
          </router-link>        
          <!-- <figcaption class="bg-danger text-center">
            {{ profile.favorite_movies[idx].title }}
          </figcaption> -->
      </figure>

      </slide>
    </carousel-3d>


      <!-- vue glide -->
      <!-- <vue-glide
      class="glide__track"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      :breakpoints="{3000: {perView: 7}, 1100: {perView: 5}, 600: {perView: 3}}"
    >
      <vue-glide-slide
        v-for="favomovie in profile.favorite_movies"
        :key="favomovie.pk">
        <FavoriteMovieCard :favomovie="favomovie"
          />
      </vue-glide-slide>
    </vue-glide> -->

    <hr>
    

    <h2>내가 작성한 글</h2>
      <vue-glide
        class="glide__track mh-40"
        data-glide-el="track"
        ref="slider"
        type="carousel"
        :breakpoints="{3000: {perView: 7}, 1100: {perView: 5}, 600: {perView: 3}}"
        >
        <vue-glide-slide
          class="mh-50"
          v-for="favoarticle in profile.articles"
          :key="favoarticle.pk">
          <!-- {{ favoarticle }} -->
          <FavoriteArticle :favoarticle="favoarticle"
            />
        </vue-glide-slide>
      </vue-glide>

    <hr>
    <h2>내가 좋아요 한 글</h2>
    <!-- <ul>
      <p v-for="article in profile.like_articles" :key="article.pk">
        <router-link :to="{ name: 'article', params: { articlePk: article.pk } }" class='movie_link text-white'>
          {{ article.title }}
        </router-link>
      </p>
    </ul> -->
      <vue-glide
        class="glide__track mh-40"
        data-glide-el="track"
        ref="slider"
        type="carousel"
        :breakpoints="{3000: {perView: 7}, 1100: {perView: 5}, 600: {perView: 3}}"
        >
        <vue-glide-slide
          class="mh-50"
          v-for="article in profile.like_articles"
          :key="article.pk">
          <!-- {{ favoarticle }} -->
          <FavoriteArticle :favoarticle="article"
            />
        </vue-glide-slide>
      </vue-glide>



<hr>


    <h2>내가 남긴 리뷰 </h2>
    <ul>
      <p v-for="review in profile.reviews" :key="review.pk">
        <router-link :to="{ name: 'movie', params: { moviePk: review.movie } }" class='movie_link text-white'>
          {{ review.title }}  ({{review.rank}}점)
        </router-link>
      </p>
    </ul>

  </div>
</template>

<script>
import { Glide, GlideSlide } from 'vue-glide-js'
import { Carousel3d, Slide } from 'vue-carousel-3d';


import { mapGetters, mapActions } from 'vuex'
// import FavoriteMovieCard from '@/components/movie/FavoriteMovieCard.vue'
import FavoriteArticle from '@/views/community/FavoriteArticle.vue'

export default {
  name: 'ProfileView',
  components:{
    // FavoriteMovieCard,
    FavoriteArticle,
    [Glide.name]: Glide,
    [GlideSlide.name]: GlideSlide,
    Carousel3d,
    Slide
  },
  computed: {
    ...mapGetters(['profile']),
    // posterUrl () {
    //   return `https://image.tmdb.org/t/p/original/${this.favomovie.poster_path}`
    // },
  },
  methods: {
    ...mapActions(['fetchProfile'])
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
  
}
</script>
