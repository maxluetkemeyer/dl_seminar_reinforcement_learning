<template>
  <div class="finished" :style="cssVars">
    <p class="my-color" :style="cssVars">
      Step: {{ maxStep }}, Done: {{ done }}
    </p>
    <canvas width="500" ref="canvas" :id="canvasId" :key="canvasId"></canvas>
  </div>
</template>

<script>
import { CartPole, renderCartPole } from "./cartpole";

export default {
  name: "GymEnv",
  props: ["step", "canvasId", "actionCallback", "doneCallback"],
  data() {
    return {
      env: new CartPole(),
      done: false,
      canvas: null,
      maxStep: 0,
    };
  },
  mounted() {
    this.canvas = document.getElementById(this.canvasId);
    renderCartPole(this.env, this.canvas);
  },
  watch: {
    step() {
      if (this.done) return;

      const action = this.actionCallback(this.env.getStateTensor());
      this.env.update(action);
      renderCartPole(this.env, this.canvas);
      this.maxStep++;

      if (this.env.isDone()) {
        this.done = true;
        this.doneCallback();
      }
    },
  },
  computed: {
    cssVars() {
      return {
        "--button-bg-color": this.maxStep > 200 ? "green" : "black",
        "--bg-color": this.done ? "lightgray" : "white",
      };
    },
  },
};
</script>

<style scoped>
canvas {
  border: 1px solid black;
}

p {
  font-size: 2rem;
}
</style>

<style lang="scss" scoped>
.my-color {
  color: var(--button-bg-color);
  font-weight: bold;
}

.finished {
  background-color: var(--bg-color);
}
</style>
