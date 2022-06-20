<script setup>
import GymEnv from "./GymEnv.vue";
import ActionRender from "./ActionRender.vue";
</script>

<template>
  <div>
    <h1>Human Player</h1>
    <GymEnv
      :actionCallback="actionCallback"
      :step="step"
      canvasId="human"
      key="human"
    />
    <ActionRender :action="action" key="human_action" />
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
  mounted() {
    document
      .getElementsByTagName("body")[0]
      .addEventListener("keypress", (e) => {
        this.action = e.key === "a" ? 0 : 1;
      });
  },
  methods: {
    actionCallback() {
      return this.action;
    },
  },
};
</script>
