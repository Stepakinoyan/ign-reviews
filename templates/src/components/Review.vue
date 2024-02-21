<template>
        <div class="container" v-for="item in review">
                <h1 class="d-flex justify-content-center">{{ item['content']['title'] }}</h1>
                <div class="">
                    <p>{{ item['text'] }}</p>
                </div>
                <div>
                    <span><b>Authors:</b></span> <span v-for="author in review[0]['content']['contributors']">{{ author['name'] }}</span>
                    <p><b>publishDate: {{ review[0]['content']['publishDate'] }}</b></p>
                    <p><b><a :href="'https://www.ign.com' + review[0]['content']['url']">Original source</a></b></p>
                </div>
        </div>
</template>

<script>
import axios from 'axios';

export default {
    data(){
        return {
            query: null,
            review: null,
        }
    },
    methods: {
        GetReview(id){
            axios.post(`review/${id}`)
                .then((res) => {
                        this.review = res.data
                })
                .catch((error) => {
                        console.error(error);
                })
        }
    },
    created() {
    this.query = this.$route.params.id;
    this.review = this.GetReview(this.query);
}
}

</script>