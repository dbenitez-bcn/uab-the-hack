<template>
  <v-card elevation="8" 
      width="100%"
      class="mb-4 rounded-lg"
      >
    <v-select
      :items="municipis"
      label="On vius?"
      color="primary"
      bg-color="white"
      width="100%"
      class="mb-0"
      @update:model-value="onLocationSelected"
    ></v-select>
  </v-card>
</template>

<script>
export default {
  props: ['municipis', 'onLocationSelected'],
  data: () => ({
    select: null,
    items: ["Item 1", "Item 2", "Item 3", "Item 4"],
    checkbox: false,
  }),
};
</script>

<style>
</style>