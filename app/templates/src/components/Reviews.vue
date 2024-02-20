<template>
      <div class="container">
        <div class="d-flex justify-content-center mt-2">
          <h1>New PS5 Reviews</h1>
        </div>
        <div class="row row-cols-1 row-cols-md-3 g-4 flex align-items-center mt-5" style="height: 100vh;">
          <div class="col" v-for="item in catalog">
            <div class="card">
              <img :src="item['content']['feedImage']['url']" class="card-img-top" alt="...">
              <div class="card-body">
                <h5 class="card-title">{{ item['content']['title'] }}</h5>
                
                <RouterLink :to="{ name: 'review', params: { id: item['id'] }}" class="btn btn-primary">Go to review</RouterLink>
              </div>
            </div>
          </div>
      </div>
      </div>
</template>


<script>
import axios from 'axios';
import { RouterLink } from 'vue-router'
export default {
  data() {
    return {
      catalog: this.GetCatalog()
    }
    
  },
  methods: {
    GetCatalog(){
      axios.post(`review/catalog`)
                .then((res) => {
                        this.catalog = res.data
                })
                .catch((error) => {
                        console.error(error);
                });
    },
  }
}

</script>