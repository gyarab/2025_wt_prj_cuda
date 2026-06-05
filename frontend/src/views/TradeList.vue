<script setup>
import { ref } from 'vue'

const trades = ref([])

async function loadTrades() {
    const response = await fetch('/api/trades')
    trades.value = await response.json()
}

onMounted(loadTrades)

</script>

<template>
    <h2>Trade List</h2>
</template>
