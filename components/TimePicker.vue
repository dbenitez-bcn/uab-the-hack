<template>
  <v-card elevation="8" class="my-2 rounded-lg" width="100%">
    <v-card-title>A quina hora?</v-card-title>
    <div class="pa-2">
      <v-chip-group column selected-class="text-primary">
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
    hoursxxx: [["16:00", "16:10", "16:20", "16:30", "16:40", "16:50"],
    ["12:00", "12:10", "12:20", "12:30", "12:40", "12:50"],
    ["09:00", "09:06", "09:12", "09:18", "09:24", "09:30"],],
  }),
};
</script>

<style>
</style>