<script setup>
import HumanPlayer from "./components/HumanPlayer.vue";
import ModelPlayer from "./components/ModelPlayer.vue";
</script>

<template>
  <div id="menu">
    <p @click="start">Start</p>
  </div>
  <div id="games">
    <HumanPlayer :step="step" key="k1" :doneCallback="humanDoneCb" />
    <ModelPlayer :step="step" key="k2" :doneCallback="modelDoneCb" />
  </div>
  <div id="custom_console"></div>
</template>

<script>
export default {
  data() {
    return {
      step: 0,
      humanDone: false,
      modelDone: false,
    };
  },
  methods: {
    async start() {
      addToConsole("3");
      await delay(1000);
      addToConsole("2");
      await delay(1000);
      addToConsole("1");
      await delay(1000);
      addToConsole("Go!");

      const loop = setInterval(() => {
        this.step++;

        if (this.humanDone && this.modelDone) {
          clearInterval(loop);
        }
      }, 80);
    },
    humanDoneCb() {
      this.humanDone = true;
      addToConsole("Human Done");
    },
    modelDoneCb() {
      this.modelDone = true;
      addToConsole("Model Done");
    },
  },
};

function delay(time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}

function addToConsole(text) {
  const output = document.getElementById("custom_console");
  const p = document.createElement("p");
  p.appendChild(document.createTextNode(text));

  output.appendChild(p);
}
</script>

<style>
html,
body {
  margin: 0;
  padding: 0;
}
</style>

<style scoped>
#games {
  display: flex;
  justify-content: space-evenly;
}

#menu {
  width: 100%;
  background-color: aliceblue;
}

#menu p {
  margin: 0;
  padding: 1rem 2rem 1rem 2rem;
  height: 100%;
  width: min-content;
  border-right: 1px solid #111111;
  cursor: pointer;
}

#custom_console {
  font-size: 2rem;
  margin: 0;
}

#custom_console p {
  padding: 0;
  margin: 0;
}
</style>
