<template>
  <v-form ref="form" class="ma-3 d-flex flex-column align-center">
    <LocationList />
    <v-date-picker
      color="primary"
      header=""
      hide-header="true"
      class="mb-2 mt-0 rounded-lg"
      width="100%"
      elevation="8"
    ></v-date-picker>
    <TimePicker />
    <v-btn color="primary" rounded width="100%" class="my-2">Continuar</v-btn>
  </v-form>
</template>

<script>
export default {};
</script>

<style>
</style>