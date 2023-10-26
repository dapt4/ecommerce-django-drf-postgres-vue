<template>
  <div class="columns">
    <div class="column">
      <h1 class="title title-cart">Cart</h1>
    </div>
  </div>
  <div class="card">
    <div class="cad-content">
      <table class="table">
        <thead>
          <tr>
            <td>&boxbox;</td>
            <th>Name</th>
            <th>Quantity</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in items" :key="index">
            <td>
              <div class="media-left">
                <figure class="image is-48x48">
                  <img :src="item.image" alt="image">
                </figure>
              </div>
            </td>
            <td>{{ item.name }}</td>
            <td>
              <div class="quantity">
                <button class="button is-light" @click="decrease(item.id)">-</button>
                <input class="myInput" type="number" v-model="quantities[item.id]">
                <button class="button is-success" @click="increase(item.id)">+</button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
      <div class="title amount">Amount: {{ amount.toFixed(2) }}</div>
      <div class="buttons">
        <button @click="orderHandler" class="button is-primary pay">
          Pay
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import router from '@/router'
import store from '@/store'
import { ref, watch } from 'vue'

const items = ref(store.getters.getCartItems)
const quantities = ref({})
const amount = ref(0)
const order = {
  username: 'user@mail.com',
  items: []
}
if (items.value.length > 0) {
  items.value.forEach(itm => {
    quantities.value[itm.id] = 1
    amount.value += itm.price
  })
}
const decrease = (id) => {
  quantities.value[id] -= 1
  if (quantities.value[id] < 0) {
    quantities.value[id] = 0
  }
}
const increase = (id) => {
  quantities.value[id] += 1
}
const buildOrder = () => {
  order.items = [] // for erase changes
  for (const key in quantities.value) {
    if (quantities.value[key] > 0) {
      order.items.push({ product: parseInt(key), quantity: quantities.value[key] })
    }
  }
}
const orderHandler = () => {
  buildOrder()
  sendOrder()
}
const sendOrder = async () => {
  const url = 'http://localhost:8000/order'
  const res = await fetch(url, {
    method: 'POST',
    body: JSON.stringify(order),
    headers: {
      'Content-type': 'application/json'
    }
  })
  const json = await res.json()
  store.commit('addInvoice', json)
  if (res.status > 300) {
    alert('There is an error')
  }
  router.push('/invoice')
}
watch(quantities.value, () => {
  amount.value = 0
  for (const key in quantities.value) {
    items.value.forEach(itm => {
      if (itm.id === parseInt(key)) {
        amount.value += itm.price * quantities.value[key]
      }
    })
  }
})
</script>

<style scoped>
.title-cart{
  text-align: center;
}
.card{
  display: block;
  width: fit-content;
  margin: 20px auto;
  padding: 40px;
  .quantity{
    display: flex;
    flex-wrap: nowrap;
    align-items: stretch;
    .myInput{
      width: 40px;
      max-width: fit-content;
    }
  }
  .amount{
    display: block;
    text-align: center;
  }
  .buttons{
    .button{
      display: block;
      margin: 20px auto;
      padding: 0px 20px;
    }
  }
}
</style>
