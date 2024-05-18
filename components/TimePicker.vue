<template>
  <v-card elevation="8" class="my-2 rounded-lg" width="100%">
    <v-card-title>A quina hora?</v-card-title>
    <div class="pa-2">
      <v-chip-group column 
        selected-class="text-primary">
        <v-chip v-for="hour in hours" :key="hour">
          {{ hour }}
        </v-chip>
      </v-chip-group>
    </div>
  </v-card>
</template>

<script>
export default {
  data: () => ({
    hours: [
      "15:02",
      "15:02",
      "15:02",
      "15:02",
      "15:02",
      "15:02",
      "15:02",
      "15:02",
      "15:02",
    ],
  }),
};
</script>

<style>
</style>