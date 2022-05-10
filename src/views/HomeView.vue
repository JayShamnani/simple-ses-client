<template>
  <div class="home">
    <Header />
    <HelloWorld />
  </div>
</template>

<script>
// @ is an alias to /src
import Header from "@/components/HeaderComp.vue"
import HelloWorld from '@/components/IndexComp.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld,
    Header
  }
}
</script>

<style scoped>
</style>
