<template>
  <span class="start-btn" @click="click">
    <slot></slot>
  </span>
</template>

<script lang="ts">
export default {
  emits: ["click"],
  setup(_, { emit }) {
    return {
      click(evt: MouseEvent) {
        return emit("click", evt);
      },
    };
  },
};
</script>

<style scoped>
.start-btn {
  text-align: center;
  display: inline-block;
  margin-top: 0.75em;
  padding: 0.5em 0.8em;

  cursor: pointer;

  background-color: var(--green-primary);
  box-shadow: 0 0.2em var(--green-secondary);
  color: white;
  border-radius: 0.4735em;

  font-weight: bold;
  font-size: 2em;
}

.start-btn:active {
  box-shadow: none;
  position: relative;
  top: 0.2em;
}
</style>
