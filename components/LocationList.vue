<template>
  <v-select
        :items="items"
        label="On vius?"
        color="primary"
        bg-color="white"
        width="100%"
        class="mb-0"
      ></v-select>
</template>

<script>
export default {
    data: () => ({
      select: null,
      items: [
        'Item 1',
        'Item 2',
        'Item 3',
        'Item 4',
      ],
      checkbox: false,
    }),
}
</script>

<style>
</style>