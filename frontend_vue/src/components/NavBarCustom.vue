<template>
  <nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <router-link class="navbar-item" to="/">
        <img
          src="/logo.png"
          width="112"
          height="28"
        />
      </router-link>
    </div>
    <div id="navbarBasicExample" class="navbar-menu">
      <div class="navbar-start">
        <router-link class="navbar-item" to="/">Products</router-link>
      </div>
      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <router-link class="button is-primary" to="/cart">
              cart
              <span class="badge" v-if="numberOfProducts !== 0">{{ numberOfProducts }}</span>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import store from '@/store'
import { ref, watch } from 'vue'
const numberOfProducts = ref(store.getters.getNumberOfProducts)
watch(() => store.getters.getNumberOfProducts, () => {
  numberOfProducts.value = store.getters.getNumberOfProducts
})
</script>

<style scoped>
.badge {
  background-color: #ef2e55;
  display: inline-block;
  padding: 2px 5px;
  font-weight: bold;
  line-height: 1;
  color: white;
  text-align: center;
  vertical-align: baseline;
  border-radius: 5px;
  margin-left: 5px;
}
</style>
