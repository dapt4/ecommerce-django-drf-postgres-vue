import { createStore } from 'vuex'

export default createStore({
  state: {
    products: [],
    cartItems: []
  },
  getters: {
    getProducts (state) {
      return state.products
    },
    getProduct: (state) => (id) => {
      return state.products.find(prod => prod.id === id)
    },
    getCartItems (state) {
      return state.cartItems
    },
    getCartItem: (state) => (id) => {
      return state.cartItems.find(prod => prod.id === id)
    },
    getNumberOfProducts: (state) => state.cartItems.length
  },
  mutations: {
    setProducts (state, products) {
      state.products = products
    },
    addProduct (state, product) {
      state.products.push(product)
    },
    editProduct (state, id, product) {
      state.products.forEach(prod => {
        if (prod.id === id) {
          prod.name = product.name
          prod.description = product.description
          prod.price = product.price
          prod.image = product.image
        }
      })
    },
    deleteProduct (state, id) {
      state.products.filter(prod => prod.id !== id)
    },
    addItem (state, item) {
      const previous = state.cartItems.find((Item) => Item.id === item.id)
      if (!previous) {
        state.cartItems.push(item)
      }
    },
    deleteItem (state, id) {
      state.cartItems.reduce(item => item.id !== id)
    }
  },
  actions: {
  },
  modules: {
  }
})
