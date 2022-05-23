<template>
 <div class="card col d-flex justify-content-center align-items-center" style=" border: 1px solid rgb(78, 51, 62); background-color: rgba(0, 0, 0, 0.3);">
     <!-- <input @keyup="getMovies" type="text" v-model="keyword" placeholder="검색어를 입력하세요"> -->
     <div class="input-group mb-3">
     <input :value="keyword" @input="changeKeyword" type="text" class="form-control" placeholder="검색어를 입력하세요">
        <!-- <div class="input-group-append">
          <button class="btn btn-primary" type="button">Button</button>
        </div> -->
    </div>
     <!-- 자료가 없을 때-->
    <div v-if="result.length === 0">
    <h3 class='text-secondary'>해당 영화에 대한 정보가 없습니다.</h3>
    <!-- {{ movies[2] }} -->
    </div>
    <div v-else>
      <div class="card m-5 d-flex justify-content-center align-items-center" style=" width:1000px; border: 1px solid rgb(78, 51, 62); background-color: rgba(0, 0, 0, 0.6);">
      <div>
        <!-- <h2 style="font-weight: bold;">{{ result[0].title }} </h2>
        <hr> -->
        <div v-for="(re, idx) in result" :key='idx'>
          <router-link class='text-decoration-none text-white'
    :to="{ name: 'movie', params: {moviePk: re.id} }">
        <h3 class="fw-bold">{{ re.title }}</h3>
    </router-link>
      </div>
        <div class="mt-4 d-flex align-items-center">
        <br>
       
        </div>
        </div>
        
      </div>
      </div>
       
    

 </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'


export default {
  name: 'SearchBar',
  components: {
  },
  data: function () {
    return {
      keyword: '',
      result: [],     
    }
  },
    computed:{
        ...mapGetters(['movies'])
  },
    methods: {
      ...mapActions(['fetchMovies']),
      getMovies: function () {
        // console.log(this.movies)
        this.result = []
            for(let i=0; i<this.movies.length; i++) {
              if (this.movies[i].title.includes(this.keyword) & !!this.keyword) {
                // console.log(this.movies[i])
                this.result.push(this.movies[i])
                }
              }
          },
      changeKeyword: function(event) {
        this.keyword = event.target.value
        this.getMovies(event)
      }
        },
    created () {
      // this.keyword = this.$route.query.keyword //검색창에서 받아옴
      this.fetchMovies()
    }
  }
</script>

<style>

  nav a {
    font-weight: bold;
    color:whitesmoke;
    text-decoration-line: none;
  }


</style>