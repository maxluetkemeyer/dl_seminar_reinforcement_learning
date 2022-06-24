<script setup>
import GymEnv from "./GymEnv.vue";
import ActionRender from "./ActionRender.vue";
</script>

<template>
  <div>
    <h1>Random Policy</h1>
    <GymEnv
      :actionCallback="actionCallback"
      :step="step"
      canvasId="model0"
      key="model0"
      :doneCallback="doneCallback"
    />
    <ActionRender :action="action" key="model_action" />
  </div>
</template>

<script>
export default {
  components: {
    GymEnv,
    ActionRender,
  },
  props: ["step", "doneCallback"],
  data() {
    return {
      action: 0,
    };
  },
  methods: {
    actionCallback() {
      this.action = Math.random() > 0.5 ? 1 : 0;
      //this.action = this.action == 0 ? 1 : 0;
      return this.action;
    },
  },
};
</script>
