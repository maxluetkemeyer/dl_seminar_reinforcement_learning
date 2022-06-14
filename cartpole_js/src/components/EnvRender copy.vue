<template>
  <div class="greetings">
    <h1>Render</h1>
    <canvas id="game_render" width="600" height="300"></canvas>
  </div>
</template>

<script>
import { CartPole, renderCartPole } from "./cartpole";

export default {
  mounted: function () {
    console.log("hey");
    const cartpole = new CartPole();
    const canvas = document.getElementById("game_render");

    renderCartPole(cartpole, canvas);

    const interval = setInterval(() => {
      const action = Math.random() > 0.5 ? 1 : 0;
      cartpole.update(action);
      renderCartPole(cartpole, canvas);
      console.log(cartpole.getStateTensor().arraySync());
      if (cartpole.isDone()) {
        clearInterval(interval);
      }
    }, 100);
  },
};
</script>

<style scoped>
canvas {
  border: 1px solid black;
}
</style>
