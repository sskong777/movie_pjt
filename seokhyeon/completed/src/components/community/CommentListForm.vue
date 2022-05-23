<template>
  <div >
    <!-- <form @submit.prevent="onSubmit" class="comment-list-form" >
      <div>
      <label for="comment" class="from-group"></label>
      <input type="text" id="comment" v-model="content" required >
      </div>
      <button @submit.prevent="onSubmit" class="btn btn-info">댓글 작성</button>
    </form> -->


    <form @submit.prevent="onSubmit" class="comment-list-form" >
    <div class="input-group mb-3">
      <input type="text" id="comment" v-model="content" required class="form-control" placeholder="댓글을 입력하세요.">
      <div class="input-group-append">
        <button @submit.prevent="onSubmit" class="btn btn-info">댓글 작성</button>
      </div>
    </div>
    </form>
    <!-- <vue-editor v-model="content"></vue-editor>
    <button @click="onSubmit" class="btn btn-secondary" align="right">댓글작성</button> -->

  </div>
</template>

<script>
// import { VueEditor } from "vue2-editor";

import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListForm',
  components:{
    // VueEditor,
  },
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['article']),
  },
  methods: {
    ...mapActions(['createComment']),
    onSubmit() {
      this.createComment({ articlePk: this.article.pk, content: this.content, })
      this.content = ''
    }
  }
}
</script>

<style>
.comment-list-form {
  /* border: 1px solid black; */
  margin: 1rem;
  padding: 1rem;
}
</style>