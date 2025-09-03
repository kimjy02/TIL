<template>
  <div>
    <p>name: {{  myInfo.name  }}</p>
    <p>balance: {{  myInfo.balance }}</p>
    <button @click="$emit('balanceUpdate', myInfo.name)">+</button>
    <hr>
  </div>
</template>

<script setup>
const props = defineProps({myInfo: Object})
const balanceUpdate = function () {
    props.myInfo.balance += 1000
}
</script>

<style scoped>

</style>