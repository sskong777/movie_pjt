<template>

  <div class="container">
    <v-card color="pink accent-2" dark>
      <v-card-title>
      <h1>{{ article.title }}</h1>
      </v-card-title>
      <v-card-text class='text-h5'>
        <p>
        {{ article.content }}
        </p>
      </v-card-text>
      <v-card-text class='py-0'>
        <p align="right" class='py-0'>
          작성: {{ article.created_at }}
          <br>
          수정: {{ article.updated_at }}
        </p>
      </v-card-text>

      <!-- Article Edit/Delete UI -->
      <v-card-actions>

        <div v-if="isAuthor">
          <router-link :to="{ name: 'articleEdit', params: { articlePk } }" class="text-decoration-none">
            <v-btn
            color = 'teal accent-4'
            >
            Edit
            </v-btn>
          </router-link>
        
          <v-btn 
          color = 'red accent-4'
          class="mx-3" 
          @click="deleteArticle(articlePk)"
          >Delete</v-btn>
        </div>
        <!-- Article Like UI -->
        <v-spacer></v-spacer>
        <div>
          <v-btn icon
            color ='white'
            @click="likeArticle(articlePk)"
          >
            <v-icon>mdi-heart</v-icon>
          </v-btn>
          {{ likeCount }}명이 이 글을 좋아합니다.
        </div>
      </v-card-actions>
    </v-card>

    <hr />
    <!-- Comment UI -->
    <comment-list :comments="article.comments"></comment-list>

  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/community/CommentList.vue'



  export default {
    name: 'ArticleDetail',
    components: { CommentList },
    data() {
      return {
        articlePk: this.$route.params.articlePk,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'article']),
      likeCount() {
        return this.article.like_users?.length
      }
    },
    methods: {
      ...mapActions([
        'fetchArticle',
        'likeArticle',
        'deleteArticle',
      ])
    },
    created() {
      this.fetchArticle(this.articlePk)
    },
  }
</script>

<style></style>
