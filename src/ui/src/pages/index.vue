<template>
  <div class="base">
    <header>
      <h1 class="header-title">my little maze solver</h1>
      <img class="header-img" :src="mazeLogo" alt="" />
    </header>
    <main>
      <Button @click="start">START</Button>
    </main>
  </div>
</template>

<script lang="ts">
import mazeLogo from "@/assets/images/maze.png";

export default {
  transition: {
    name: "home",
    mode: "out-in",
  },
  setup() {
    return {
      mazeLogo,
    };
  },
  methods: {
    async start() {
      await navigateTo('/maze/game');
    }
  }
};
</script>

<style scoped>
.base {
  display: flex;
  flex-direction: column;
  justify-content: center;

  width: 100vw;
  min-height: 100vh;
}

.base > header,
.base main {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.header-title {
  font-size: 3.5em;
}

.header-img {
  width: 40%;
}
</style>
