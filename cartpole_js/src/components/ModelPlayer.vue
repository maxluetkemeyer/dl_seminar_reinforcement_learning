<script setup>
import GymEnv from "./GymEnv.vue";
import ActionRender from "./ActionRender.vue";
</script>

<template>
  <div>
    <h1>Model Player</h1>
    <GymEnv
      :actionCallback="actionCallback"
      :step="step"
      canvasId="model0"
      key="model0"
    />
    <ActionRender :action="action" key="model_action" />
  </div>
</template>

<script>
export default {
  props: ["step"],
  data() {
    return {
      action: 0,
    };
  },
  methods: {
    actionCallback() {
      this.action = Math.random() > 0.5 ? 1 : 0;
      return this.action;
    },
  },
};
</script>
