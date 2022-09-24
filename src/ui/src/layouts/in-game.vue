<template>
  <div class="base">
    <header>
      <h1 class="heading-title" @click="goHome">my little maze solver</h1>
    </header>
    <slot />
  </div>
</template>

<script lang="ts" setup>
async function goHome() {
  await navigateTo("/");
}
</script>

<style scoped>
.base {
  display: flex;
  flex-direction: column;

  width: 100vw;
  min-height: 100vh;
}

.base header {
  display: flex;
  justify-content: center;

  background-color: var(--green-primary);
  padding: 0.5em 0;
}

.heading-title {
  font-size: 2.4em;
  cursor: pointer;
}
</style>
