<template>

  <div class="container" style="width: 13rem;">
    <hr>
  <v-card
    class="mx-3"
    color="#26c6da"
    dark
    max-width="500"
  >
    <v-card-title>
      <v-icon
        large
        left
      >
        mdi-twitter
      </v-icon>
      <span class="text-h6 font-weight-light">ACHCA</span>
    </v-card-title>

    <v-card-text class="text-h5 font-weight-bold">
      <h1>
        <router-link class='text-decoration-none text-white'
            :to="{ name: 'article', params: {articlePk: favoarticle.pk} }">
            {{ favoarticle.title }}
         </router-link>
       </h1>    
    </v-card-text>

      <v-list-item class="grow">
        <v-list-item-avatar color="grey darken-3">
        <v-icon
          color="grey lighten-1"
          large
        >
          mdi-account
        </v-icon>        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title>{{favoarticle.username }}</v-list-item-title>
        </v-list-item-content>
        <!-- {{ favoarticle}} -->
        <!-- <v-row 
          class="my-3"
          align="center"
          justify="end"
        >
          <v-icon class="mr-1">
            mdi-heart
          </v-icon>
          <span class="subheading mr-2">256</span>
          <span class="mr-1">·</span>
          <v-icon class="mr-1">
            mdi-share-variant
          </v-icon>
          <span class="subheading">45</span>
        </v-row> -->
      </v-list-item>
  </v-card>



  </div>
</template>

<script>
  // import { mapGetters, mapActions } from 'vuex'



  export default {
    name: 'FavoriteArticle',
    props:{
      favoarticle:Object,
    },
    // data() {
    //   return {
    //     articlePk: this.favoarticle.pk,
    //   }
    // },
    // computed: {
    //   ...mapGetters(['isAuthor', 'article']),
    //   likeCount() {
    //     return this.article.like_users?.length
    //   }
    // },
    // methods: {
    //   ...mapActions([
    //     'fetchArticle',
    //     'likeArticle',
    //     'deleteArticle',
    //   ])
    // },
    // created() {
    //   this.fetchArticle(this.articlePk)
    // },
  }
</script>

<style></style>
