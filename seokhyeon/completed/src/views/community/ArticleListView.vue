<template v-slot:default>
  <div>
    <h1>Community</h1>

   <div class="container">
      <p v-if="isLoggedIn">
        <router-link class='btn btn-info btn-lg text-decoration-none text-white'
          :to="{ name: 'articleNew' }">
          New
        </router-link>
      </p>
    <v-simple-table fixed-header>
      <thead>
        <tr>
          <th scope="col">번호</th>
          <th scope="col">제목</th>
          <th scope="col">작성자</th>
          <th scope="col">댓글 / 좋아요</th>
        </tr>
      </thead>

      <tbody align="left">      
        <tr v-for="(article,idx) in articles" :key="idx">
        <!-- 게시글 번호 -->
        <td>{{ idx+1 }}</td>

        <!-- 글 이동 링크 (제목) -->
        <td>
          <router-link class='text-decoration-none'
            :to="{ name: 'article', params: {articlePk: article.pk} }">
            {{ article.title }}
         </router-link>
        </td>
        
        <!-- 작성자 -->
        <td>{{ article.user.username }}</td> 
        
        <!-- 댓글 개수/좋아요 개수 --> 
        <td>{{ article.comment_count }} / {{ article.like_count }}</td>

       </tr>
      </tbody>

    </v-simple-table>
   </div>
  
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'ArticleList',
    computed: {
      ...mapGetters(['articles', 'isLoggedIn'])
    },
    methods: {
      ...mapActions(['fetchArticles'])
    },
    created() {
      this.fetchArticles()
    },
  }
</script>

<style></style>
