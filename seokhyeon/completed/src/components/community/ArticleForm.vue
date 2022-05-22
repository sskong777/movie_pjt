<template>
  <div class="container">
  <form @submit.prevent="onSubmit">
    <div class='form-group' align="left">
      <label for="title">Title </label>
      <input v-model="newArticle.title" type="text" id="title" class='form-control' />
    </div>
    <div class='form-group my-3' align="left">
      <label for="content">Content </label>
      <textarea v-model="newArticle.content" type="text" id="content" class='form-control' rows='5'></textarea>
    </div>

    <div align="right">
      <button class="btn btn-secondary">{{ action }}</button>
    </div>
  </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

  export default {
    name: 'ArticleForm',
    props: {
      article: Object,
      action: String,
    },
    data() {
      return {
        newArticle: {
          title: this.article.title,
          content: this.article.content,
        }
      }
    },

    methods: {
      ...mapActions(['createArticle', 'updateArticle']),
      onSubmit() {
        if (this.action === 'create') {
          this.createArticle(this.newArticle)
        } else if (this.action === 'update') {
          const payload = {
            pk: this.article.pk,
            ...this.newArticle,
          }
          this.updateArticle(payload)
        }
      },
    },
  }
</script>

<style></style>
