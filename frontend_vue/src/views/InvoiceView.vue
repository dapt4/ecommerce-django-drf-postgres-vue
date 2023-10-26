<template>
  <div class="card">
    <header class="card-header">
      <span class="card-header-title">
        <span>
          Invoice
        </span>
      </span>
    </header>
    <div class="card-content">
      <div class="content">
        <p class="title is-4 user">Client: {{ invoice.username }}</p>
        <table class="table">
          <thead>
            <tr>
              <th>Name</th>
              <th>Quantity</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in invoice.items" :key="index">
              <td>{{ item.name }}</td>
              <td class="quantity">{{ item.quantity }} units</td>
            </tr>
          </tbody>
        </table>
        <div class="title is-4 amount">Amount: ${{ invoice.amount }}</div>
      </div>
    </div>
    <footer class="card-footer">
      <a class="button" href="/">Home</a>
    </footer>
  </div>
</template>

<script>
import store from '@/store'
import { ref } from 'vue'
export default {
  name: 'InvoiceView',
  components: {},
  setup () {
    const invoice = ref(store.getters.getInvoice)
    return {
      invoice
    }
  }
}
</script>

<style scoped lang="scss">
.card{
  width: fit-content;
  margin: 40px auto;
  &-header{
    &-title{
      width: 100%;
      span{
        display: block;
        width: fit-content;
        margin: 0px auto;
      }
    }
  }
  &-content{
    padding: 40px;
    .content{
      .title{
        text-align: center;
      }
      table tbody tr .quantity {
        text-align: center;
      }
      .amount{
        margin-top: 40px;
        text-align: center;
      }
    }
  }
  &-footer{
    padding: 20px;
    .button{
      margin: 0px auto;
    }
  }
}
</style>
