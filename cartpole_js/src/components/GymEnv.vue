<script setup>
import { CartPole, renderCartPole } from "./cartpole";
</script>

<template>
  <div>
    <p>Step: {{ step }}, Done: {{ done }}</p>
    <canvas width="500" ref="canvas" :id="canvasId" :key="canvasId"></canvas>
  </div>
</template>

<script>
export default {
  props: ["step", "canvasId", "actionCallback"],
  data() {
    return {
      env: new CartPole(),
      done: false,
      canvas: null,
    };
  },
  mounted() {
    this.canvas = document.getElementById(this.canvasId);
    console.log(this.canvas);
    renderCartPole(this.env, this.canvas);
  },
  watch: {
    step() {
      console.log("Step update " + this.step);
      if (this.done) return;

      const action = this.actionCallback(this.env.getStateTensor());
      this.env.update(action);
      renderCartPole(this.env, this.canvas);

      if (this.env.isDone()) {
        this.done = true;
      }
    },
  },
};
</script>

<style scoped>
canvas {
  border: 1px solid black;
}
</style>
