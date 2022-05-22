<template>
  <form @submit.prevent="onSubmit" class="review-list-form">
    <label for="review">title: </label>
    <input type="text" id="review" v-model="title" required>
    <label for="review">content: </label>
    <input type="text" id="review" v-model="content" required>
    <!-- <label for="review">rank: </label>
    <input type="number" id="review" v-model="rank" required> -->
        <div class="text-center mt-12">
        <v-rating
          v-model="rank"
          color="yellow darken-3"
          background-color="grey darken-1"
          empty-icon="$ratingFull"
          dense
          half-increments
          hover
          large
        ></v-rating>
        </div>
    <button @submit.prevent="onSubmit">Review</button>
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ReviewListForm',
  data() {
    return {
      title: '',
      content: '',
      rank: null,
    }
  },
  computed: {
    ...mapGetters(['movie']),
  },
  methods: {
    ...mapActions(['createReview']),
    onSubmit() {
      this.createReview({ moviePk: this.movie.id, title: this.title, content: this.content, rank: this.rank})
      this.content = ''
      this.title = ''
      this.rank = null
    }
  }
}
</script>

<style>
.review-list-form {
  border: 1px solid black;
  margin: 1rem;
  padding: 1rem;
}
</style>