<template>
  <div>
    <h1>Product</h1>
    <div v-if="item">
      <div class="card">
        <div class="card-image">
          <figure class="image is-4by3">
            <img :src="item.image" alt="image">
          </figure>
        </div>
        <div class="card-content">
          <div class="media">
            <div class="media-left">
              <figure class="image is-48x48">
                <img :src="item.image" alt="image">
              </figure>
            </div>
            <div class="media-content">
              <p class="title is-4">{{ item.name }}</p>
              <p class="subtitle is-6">${{ item.price }}</p>
            </div>
          </div>
          <div class="content">
            <div>{{ item.description }}</div>
            <time datetime="2016-1-1">{{ new Date() }}</time>
          </div>
          <footer class="buttons">
            <button class="button is-primary w-100" @click="handleAdd">Add to cart</button>
          </footer>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import store from '@/store'
import { ref, unref } from 'vue'
import { useRoute } from 'vue-router'

const { params } = useRoute()
const id = parseInt(params.id)
const item = ref(store.getters.getProduct(id))

const handleAdd = () => {
  store.commit('addItem', unref(item))
}

</script>
<style scoped>
.card{
  display: block;
  width: 90%;
  margin: 20px auto;
  @media (min-width: 768px) {
    width: 50%;
  }
  .buttons{
    .button.w-100{
      width: 100%;
    }
  }
}
</style>
