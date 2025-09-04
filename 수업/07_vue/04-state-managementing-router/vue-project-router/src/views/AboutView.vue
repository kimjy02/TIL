<template>
  <div>
    <h1>About View</h1>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
const router = useRouter()

const someFunction = function () {
  // 진짜 엄청 복잡하고 대단한 로직
}
router.push({ name: 'useProfile' })
</script>


<style scoped>

</style>