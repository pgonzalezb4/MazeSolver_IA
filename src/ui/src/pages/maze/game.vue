<template>
  <main>
    <div class="in-maze" v-if="mazeFile">
      <Maze class="maze" :file="mazeFile" />
      <Button @click="mazeFile = undefined">NEW MAZE</Button>
    </div>
    <span v-else>
      <FileDropZone class="drop-zone" @file-dropped="onFileDropped">
        insert files here or click to find a file
      </FileDropZone>
    </span>
  </main>
</template>

<script lang="ts" setup>
const mazeFile = ref<File>();

definePageMeta({
  layout: "in-game",
});

function onFileDropped(inputFile: File) {
  mazeFile.value = inputFile;
}
</script>

<style scoped>
main {
  display: flex;
  flex-direction: column;
  align-items: center;

  padding: 3em 1.5em;
  color: var(--green-secondary);

  max-width: 100vw;
}

.drop-zone {
  padding: 5em;
  font-size: 2.5em;
  text-align: center;

  width: 60%;
}

.in-maze {
  display: flex;
  flex-direction: column;
  align-items: center;
  
  width: 100%;
}

.maze {
  width: 100%;
}

</style>
