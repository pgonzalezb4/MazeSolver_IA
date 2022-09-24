<template>
  <div
    class="drop-zone"
    :class="dragging ? 'drag' : ''"
    @dragenter="onDrag"
    @dragleave="onLeave"
    @drop.prevent="onDrop"
    @click.prevent="openFile"
  >
    <slot></slot>
  </div>
</template>

<script lang="ts">
const events = ["dragcenter", "dragover", "dragleave", "drop"];
function preventDefault(e: DragEvent) {
  e.preventDefault();
}

export default {
  data() {
    return {
      dragging: false,
    };
  },
  emits: ["file-dropped"],
  setup(_props, { emit }) {
    return {
      emitFileDropped(file: File) {
        emit("file-dropped", file);
      },
    };
  },
  methods: {
    onDrag(_: DragEvent) {
      this.dragging = true;
    },
    onLeave(_: DragEvent) {
      this.dragging = false;
    },
    onDrop(event: DragEvent) {
      this.onLeave(event);

      const [file] = [...(event.dataTransfer?.files ?? [])].filter(
        ({ type }) => type === "text/csv"
      );
      this.emitFileDropped(file);
    },
    openFile(_: MouseEvent) {
      const input = document.createElement("input");
      input.type = "file";
      input.multiple = false;
      input.accept = "text/csv";

      input.onchange = (_) => {
        const [file] = [...(input.files ?? [])];
        this.emitFileDropped(file);
      };

      input.click();
    },
  },
  mounted() {
    events.forEach((eventName) => {
      document.body.addEventListener(eventName, preventDefault);
    });
  },
  unmounted() {
    events.forEach((eventName) => {
      document.body.removeEventListener(eventName, preventDefault);
    });
  },
};
</script>

<style scoped>
.drop-zone {
  border-radius: 0.5em;
  border-width: 2.8px;
  border-style: dotted;
  border-color: rgba(var(--green-secondary), 0.2);

  cursor: pointer;
}

.drag {
  border-style: dashed;
  opacity: 0.5;
}
</style>
