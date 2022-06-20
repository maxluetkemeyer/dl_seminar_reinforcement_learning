<template>
  <div>
    <div class="icon_container">
      <i v-if="action == 0" class="fa-solid fa-left-long active"></i>
      <i v-else class="fa-solid fa-left-long"></i>
    </div>

    <div class="icon_container">
      <i v-if="action == 1" class="fa-solid fa-right-long active"></i>
      <i v-else class="fa-solid fa-right-long"></i>
    </div>
  </div>
</template>

<script>
export default {
  props: ["action"],
};
</script>

<style scoped>
div {
  display: flex;
  justify-content: space-between;
}

span {
  display: inline;
  color: grey;
  font-weight: normal;
  font-size: 40px;
}

.active {
  font-size: 5rem;
  color: black;
}

i {
  font-size: 4rem;
  color: grey;
}

.icon_container {
  display: inline-block;
  margin: 10px;
}
</style>
