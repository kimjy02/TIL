<template>
  <div>
    <h1>User</h1>
    <p>{{  route.params.username }}</p>
    <button @click='goHome'>홈으로!</button>
  </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router';

const router = useRouter()


const goHome = function() {
    router.push({ name: 'home' })
}

</script>

<style scoped>

</style>