<template>
  <li class="review-list-item">
    <router-link :to="{ name: 'profile', params: { username: review.user.username } }">
      {{ review.user.username }}
    </router-link>: 
    <span v-if="!isEditing"><strong>{{ payload.title }}</strong></span>
    <br>
    <span v-if="!isEditing">{{ payload.content }}</span>
    <br>
    <span v-if="!isEditing">평점: {{ payload.rank }}</span>
    <br>
     생성: {{ review.created_at }} / 수정: {{ review.updated_at }}


    <span v-if="isEditing">
      <input type="text" v-model="payload.title">
      <input type="text" v-model="payload.content">
      <input type="number" v-model="payload.rank">
      <button @click="onUpdate">Update</button> |
      <button @click="switchIsEditing">Cancle</button>
    </span>
    <span v-if="currentUser.username === review.user.username && !isEditing">
      <button @click="switchIsEditing">Edit</button> |
      <button @click="deleteReview(payload)">Delete</button>
    </span>
  </li>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ReviewListItem',
  props: { review: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        moviePk: this.review.movie,
        reviewPk: this.review.pk,
        title: this.review.title,
        content: this.review.content,
        rank: this.review.rank
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateReview', 'deleteReview']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateReview(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style>
.review-list-item {
  border: 1px solid green;

}
</style>