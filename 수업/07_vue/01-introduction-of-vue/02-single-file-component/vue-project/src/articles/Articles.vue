<template>
    <h1>아무거나</h1>
    <p>{{  message }}</p>
</template>

<script setup>
import { ref } from 'vue'
const message = ref('hello, articles')
</script>

<style scoped>

</style>