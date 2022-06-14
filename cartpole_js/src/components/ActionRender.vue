<template>
  <div>
    <div class="icon_container">
      <span v-if="action == 0" class="active"> left </span>
      <span v-else>left</span>
    </div>

    <div class="icon_container">
      <span v-if="action == 1" class="active"> right </span>
      <span v-else>right</span>
    </div>
  </div>
</template>

<script>
export default {
  props: ["action"],
};
</script>

<style>
span {
  display: inline;
  color: grey;
  font-weight: normal;
  font-size: 40px;
}

.active {
  color: black;
  font-weight: bold;
}

.icon_container {
  display: inline-block;
  margin: 10px;
}
</style>
