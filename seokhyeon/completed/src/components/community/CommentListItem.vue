<template>
  <div class="comment-list-item">
    <router-link :to="{ name: 'profile', params: { username: comment.user.username } }" class="fw-bold text-decoration-none text-white">
        {{ comment.user.username }}
    </router-link>
    <p class="text-muted" v-html="payload.content" v-if="!isEditing"></p>
    
     <!-- 생성: {{ comment.created_at }} / 수정: {{ comment.updated_at }} -->
    <span v-if="isEditing">
      <input class="bg-secondary" type="text" v-model="payload.content">
      <button @click="onUpdate">Update</button> |
      <button @click="switchIsEditing">Cancle</button>
    </span>

    <p v-if="currentUser.username === comment.user.username && !isEditing" align='right'>
      <v-btn 
      text
      color = "white"
      @click="switchIsEditing">Edit</v-btn>
      <v-btn 
      text
      color = "white"
      @click="deleteComment(payload)">Delete</v-btn>
    </p>
    <hr>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListItem',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        articlePk: this.comment.article,
        commentPk: this.comment.pk,
        content: this.comment.content
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style>
/* .comment-list-item {
  border: 1px solid green;

} */
</style>