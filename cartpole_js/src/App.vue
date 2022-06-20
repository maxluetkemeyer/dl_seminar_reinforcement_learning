<script setup>
import HumanPlayer from "./components/HumanPlayer.vue";
import ModelPlayer from "./components/ModelPlayer.vue";
</script>

<template>
  <div>
    <HumanPlayer :step="step" key="k1" />
    <div style="width: 40px"></div>
    <ModelPlayer :step="step" key="k2" />
  </div>
  <br />
  <div @click="start">Start</div>
</template>

<script>
export default {
  data() {
    return {
      step: 0,
    };
  },
  methods: {
    start() {
      //const loop =
      setInterval(() => {
        this.step++;
      }, 200);
    },
  },
};
</script>

<style scoped>
div {
  display: inline-block;
}
</style>
