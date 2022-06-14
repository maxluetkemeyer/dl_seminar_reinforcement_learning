<script setup>
import Gym from "./Gym.vue";
import ActionRender from "./ActionRender.vue";
</script>

<template>
    <div>
        <h1>Model Player</h1>
        <Gym :actionCallback="actionCallback" :start="start" canvasId="model0" key="model0"/>
        <ActionRender :action="action" />
    </div>
</template>

<script>
export default {
  props: ["start"],
  data(){
    return {
        action: "",
    }
  },
  methods: {
    actionCallback(){
        this.action = Math.random() > 0.5 ? 1 : 0;
        return this.action;
    }
  }
}
</script>