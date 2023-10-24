<template>
  <div class="columns">
    <div class="column">
      <h1 class="title is-1 title-products">Products</h1>
    </div>
  </div>
  <div class="products_list">
    <div class="card products_list--item" v-for="(product, index) of products" :key="index">
      <div class="card-image">
        <figure class="image is-4by3">
          <img :src="product.image" alt="image">
        </figure>
      </div>
      <div class="card-content">
        <div class="media">
          <div class="media-left">
            <figure class="image is-48x48">
              <img :src="product.image" alt="image">
            </figure>
          </div>
          <div class="media-content">
            <p class="title is-4">{{ product.name }}</p>
            <p class="subtitle is-6">${{ product.price }}</p>
          </div>
        </div>
        <div class="content">
          {{ product.description }}
          <div class="content_buttons">
            <button class="button is-link" @click="handleDetail(product.id)">Detail</button>
            <button class="button is-primary" @click="handleAdd(product)">Add to cart</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import store from '@/store'
import router from '@/router'
import { ref } from 'vue'

const products = ref([])

export default {
  name: 'HomeView',
  components: {},
  setup () {
    const handleDetail = (id) => {
      router.push('/detail/' + id)
    }
    const handleAdd = (item) => {
      store.commit('addItem', item)
    }
    return {
      products,
      handleDetail,
      handleAdd
    }
  },
  mounted () {
    const getData = async () => {
      const url = 'http://localhost:8000/product'
      const res = await fetch(url)
      const json = await res.json()
      console.log(json)
      store.commit('setProducts', json)
      products.value = store.getters.getProducts
    }
    getData()
  }
}
</script>
<style lang="scss" scoped>
.title-products{
  text-align: center;
}
.products_list{
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  gap: 20px;
  &--item{
    display: block;
    width: 18rem;
    .content{
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      gap: 20px;
      &_buttons{
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 10px;
      }
    }
  }
}
</style>
