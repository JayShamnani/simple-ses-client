<template>
  <div class="createUser">
    <HelloWorld />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/CreateUserComp'

export default {
  name: 'CreateUser',
  components: {
    HelloWorld
  }
}
</script>

<style scoped>
.login {
    background-color: #252525;
}
</style>