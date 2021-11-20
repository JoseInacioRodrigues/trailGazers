<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    
   <button @click="getImages">Images List</button>
   <div>
    <ul id="example-1">
        <li class="row" v-for="item in imageList" :key="item.id">
          <p>{{item.content}}</p>
          <p><img v-bind:src=[[item.image]] :alt="item.content"></p>
          
        </li>
   </ul>
   </div>
</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data () {
    return {
      imageList : [],
    }
  },
  methods: {
     async getImages() {
        try {
            const response = await axios.get('/api/images/');
            console.log(response.data);
            this.imageList = response.data;
        } catch (error) {
            console.error(error);
          }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
