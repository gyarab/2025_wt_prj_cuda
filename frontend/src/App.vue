<template>
  <header>
    <router-link to="/">Homepage</router-link>
  </header>
  <main>
    <router-view />
  </main>
</template>

<script setup>
  import { RouterLink, RouterView } from 'vue-router'
</script>

