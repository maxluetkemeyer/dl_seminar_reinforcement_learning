<template>
  <div id="game">
    <h1>Render</h1>
    <canvas id="game_render" width="600" height="300"></canvas>
  </div>
</template>

<script>
import { renderCartPole } from "./cartpole";

export default {
  props: ["cartpole"],
  mounted() {
    const canvas = document.getElementById("game_render");
    const env = this.cartpole;

    renderCartPole(env, canvas);
  },
};
</script>

<style scoped>
canvas {
  border: 1px solid black;
}
</style>
