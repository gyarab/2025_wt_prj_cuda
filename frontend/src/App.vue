<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
    <header>
        <RouterLink to="/">
            <h1>Trading Journal</h1>
        </RouterLink>
    </header>

    <main>
        <RouterView />
    </main>
</template>
