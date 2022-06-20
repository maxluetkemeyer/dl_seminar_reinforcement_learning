<script setup>
import GymEnv from "./GymEnv.vue";
import ActionRender from "./ActionRender.vue";
</script>

<template>
  <div>
    <h1>Human Player</h1>
    <GymEnv
      :actionCallback="actionCallback"
      :start="start"
      canvasId="human"
      key="human"
    />
    <ActionRender :action="action" key="human_action" />
  </div>
</template>

<script>
export default {
  props: ["startCallback"],
  data() {
    return {
      action: "",
      start: false,
    };
  },
  mounted() {
    document
      .getElementsByTagName("body")[0]
      .addEventListener("keypress", (e) => {
        this.action = e.key === "a" ? 0 : 1;

        if (!this.start) {
          this.start = true;
          this.startCallback();
        }
      });
  },
  methods: {
    actionCallback() {
      return this.action;
    },
  },
};
</script>
