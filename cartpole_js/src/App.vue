<script setup>
import HumanPlayer from "./components/HumanPlayer.vue";
import ModelPlayer from "./components/ModelPlayer.vue";
</script>

<template>
  <div>
    <HumanPlayer :startCallback="startCallback" key="k1" />
    <div style="width: 20px"></div>
    <ModelPlayer :start="startModels" key="k2" />
  </div>
</template>

<script>
export default {
  data() {
    return {
      startModels: false,
    };
  },
  methods: {
    startCallback() {
      this.startModels = true;
    },
  },
};
</script>

<style scoped>
div {
  display: inline-block;
}
</style>
