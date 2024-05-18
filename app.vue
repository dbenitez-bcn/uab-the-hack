<template>
  <div>
    <v-app class="bg-grey-lighten-3 px-4">
      <p class="text-h5">Procés de reserva</p>
    <BookingForm :transition="{
        name: 'bounce',
        mode: 'out-in'
      }"/>
    </v-app>
  </div>
</template>
