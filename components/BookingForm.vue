<template>
  <Transition>
    <v-form
      v-if="stage == 0"
      ref="form"
      class="ma-3 d-flex flex-column align-center"
    >
      <v-card elevation="8" width="100%" class="mb-4 rounded-lg">
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
      <v-date-picker
        color="primary"
        header=""
        :hide-header="true"
        class="mb-2 mt-0 rounded-lg"
        width="100%"
        elevation="8"
        @update:model-value="onDateChanged"
      ></v-date-picker>
      <v-card elevation="8" class="my-2 rounded-lg" width="100%">
        <v-card-title>A quina hora?</v-card-title>
        <div class="pa-2">
          <v-chip-group
            column
            selected-class="text-primary"
            @update:model-value="onHourSelected"
          >
            <v-chip v-for="hour in selectedHours" :key="hour">
              {{ hour }}
            </v-chip>
          </v-chip-group>
        </div>
      </v-card>
      <v-btn color="primary" rounded width="100%" class="my-2" @click="book"
        >Continuar</v-btn
      >
    </v-form>
  </Transition>
  <Transition>
    <div class="d-flex justify-center py-2"
        v-if="stage == 1">
      <v-progress-circular
        color="primary"
        indeterminate
      ></v-progress-circular>
    </div>
  </Transition>
  <Transition>
    <div v-if="stage == 2">
      <v-alert
        :text='"Acabes de reservar per el dia " + selectedDate.getDate() + "/" + selectedDate.getMonth() + " a les " + selectedHour'
        title="Reserva exitosa"
        type="success"
        density="compact"
      ></v-alert>
    </div>
  </Transition>
</template>

<script>
export default {
  data: () => ({
    routesList: [
      {
        itinerari1: [
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Anoia",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Prats de Rei",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Anoia",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Bruc",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Anoia",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Vallbona d'Anoia",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Anoia",
              hores: [
                {
                  end: "11:03:00",
                  start: "11:00:00",
                },
                {
                  end: "11:06:00",
                  start: "11:03:00",
                },
                {
                  end: "11:09:00",
                  start: "11:06:00",
                },
                {
                  end: "11:12:00",
                  start: "11:09:00",
                },
                {
                  end: "11:15:00",
                  start: "11:12:00",
                },
                {
                  end: "11:18:00",
                  start: "11:15:00",
                },
                {
                  end: "11:21:00",
                  start: "11:18:00",
                },
                {
                  end: "11:24:00",
                  start: "11:21:00",
                },
                {
                  end: "11:27:00",
                  start: "11:24:00",
                },
                {
                  end: "11:30:00",
                  start: "11:27:00",
                },
              ],
              municipi: "Castellfollit de Riubreg�s",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Anoia",
              hores: [
                {
                  end: "11:33:00",
                  start: "11:30:00",
                },
                {
                  end: "11:36:00",
                  start: "11:33:00",
                },
                {
                  end: "11:39:00",
                  start: "11:36:00",
                },
                {
                  end: "11:42:00",
                  start: "11:39:00",
                },
                {
                  end: "11:45:00",
                  start: "11:42:00",
                },
                {
                  end: "11:48:00",
                  start: "11:45:00",
                },
                {
                  end: "11:51:00",
                  start: "11:48:00",
                },
                {
                  end: "11:54:00",
                  start: "11:51:00",
                },
                {
                  end: "11:57:00",
                  start: "11:54:00",
                },
                {
                  end: "12:00:00",
                  start: "11:57:00",
                },
              ],
              municipi: "Montmaneu",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Anoia",
              hores: [
                {
                  end: "12:03:00",
                  start: "12:00:00",
                },
                {
                  end: "12:06:00",
                  start: "12:03:00",
                },
                {
                  end: "12:09:00",
                  start: "12:06:00",
                },
                {
                  end: "12:12:00",
                  start: "12:09:00",
                },
                {
                  end: "12:15:00",
                  start: "12:12:00",
                },
                {
                  end: "12:18:00",
                  start: "12:15:00",
                },
                {
                  end: "12:21:00",
                  start: "12:18:00",
                },
                {
                  end: "12:24:00",
                  start: "12:21:00",
                },
                {
                  end: "12:27:00",
                  start: "12:24:00",
                },
                {
                  end: "12:30:00",
                  start: "12:27:00",
                },
              ],
              municipi: "Orp�",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Conca Barb.",
              hores: [
                {
                  end: "12:33:00",
                  start: "12:30:00",
                },
                {
                  end: "12:36:00",
                  start: "12:33:00",
                },
                {
                  end: "12:39:00",
                  start: "12:36:00",
                },
                {
                  end: "12:42:00",
                  start: "12:39:00",
                },
                {
                  end: "12:45:00",
                  start: "12:42:00",
                },
                {
                  end: "12:48:00",
                  start: "12:45:00",
                },
                {
                  end: "12:51:00",
                  start: "12:48:00",
                },
                {
                  end: "12:54:00",
                  start: "12:51:00",
                },
                {
                  end: "12:57:00",
                  start: "12:54:00",
                },
                {
                  end: "13:00:00",
                  start: "12:57:00",
                },
              ],
              municipi: "Passanant i Belltall",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Conca Barb.",
              hores: [
                {
                  end: "13:03:00",
                  start: "13:00:00",
                },
                {
                  end: "13:06:00",
                  start: "13:03:00",
                },
                {
                  end: "13:09:00",
                  start: "13:06:00",
                },
                {
                  end: "13:12:00",
                  start: "13:09:00",
                },
                {
                  end: "13:15:00",
                  start: "13:12:00",
                },
                {
                  end: "13:18:00",
                  start: "13:15:00",
                },
                {
                  end: "13:21:00",
                  start: "13:18:00",
                },
                {
                  end: "13:24:00",
                  start: "13:21:00",
                },
                {
                  end: "13:27:00",
                  start: "13:24:00",
                },
                {
                  end: "13:30:00",
                  start: "13:27:00",
                },
              ],
              municipi: "For�s",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-07 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Torroella de Fluvi�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-07 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Far d'Empord�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-07 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Cabanes",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-07 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
                {
                  end: "12:36:00",
                  start: "12:30:00",
                },
                {
                  end: "12:42:00",
                  start: "12:36:00",
                },
                {
                  end: "12:48:00",
                  start: "12:42:00",
                },
                {
                  end: "12:54:00",
                  start: "12:48:00",
                },
                {
                  end: "13:00:00",
                  start: "12:54:00",
                },
              ],
              municipi: "Espolla",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-10 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Vilamalla",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-10 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "09:03:00",
                  start: "09:00:00",
                },
                {
                  end: "09:06:00",
                  start: "09:03:00",
                },
                {
                  end: "09:09:00",
                  start: "09:06:00",
                },
                {
                  end: "09:12:00",
                  start: "09:09:00",
                },
                {
                  end: "09:15:00",
                  start: "09:12:00",
                },
                {
                  end: "09:18:00",
                  start: "09:15:00",
                },
                {
                  end: "09:21:00",
                  start: "09:18:00",
                },
                {
                  end: "09:24:00",
                  start: "09:21:00",
                },
                {
                  end: "09:27:00",
                  start: "09:24:00",
                },
                {
                  end: "09:30:00",
                  start: "09:27:00",
                },
              ],
              municipi: "Pedret i Marz�",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-10 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "09:33:00",
                  start: "09:30:00",
                },
                {
                  end: "09:36:00",
                  start: "09:33:00",
                },
                {
                  end: "09:39:00",
                  start: "09:36:00",
                },
                {
                  end: "09:42:00",
                  start: "09:39:00",
                },
                {
                  end: "09:45:00",
                  start: "09:42:00",
                },
                {
                  end: "09:48:00",
                  start: "09:45:00",
                },
                {
                  end: "09:51:00",
                  start: "09:48:00",
                },
                {
                  end: "09:54:00",
                  start: "09:51:00",
                },
                {
                  end: "09:57:00",
                  start: "09:54:00",
                },
                {
                  end: "10:00:00",
                  start: "09:57:00",
                },
              ],
              municipi: "Vilamaniscle",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-13 08:00:00",
            pd: {
              comarca: "Bages",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Castellfollit del Boix",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-14 08:00:00",
            pd: {
              comarca: "Baix Llobreg.",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Collbat�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-14 08:00:00",
            pd: {
              comarca: "Vall�s Occ.",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Ullastrell",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-14 08:00:00",
            pd: {
              comarca: "Vall�s Ori.",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Vallgorguina",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-14 08:00:00",
            pd: {
              comarca: "Vall�s Ori.",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Fogars de Montcl�s",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-14 08:00:00",
            pd: {
              comarca: "Vall�s Ori.",
              hores: [
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
                {
                  end: "12:36:00",
                  start: "12:30:00",
                },
                {
                  end: "12:42:00",
                  start: "12:36:00",
                },
                {
                  end: "12:48:00",
                  start: "12:42:00",
                },
                {
                  end: "12:54:00",
                  start: "12:48:00",
                },
                {
                  end: "13:00:00",
                  start: "12:54:00",
                },
              ],
              municipi: "Figar�-Montmany",
              temps_estimat: 60,
            },
          },
        ],
        itinerari2: [
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Anoia",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Sant Mart� Sesgueioles",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Anoia",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Castellol�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Anoia",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Llacuna",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Anoia",
              hores: [
                {
                  end: "11:03:00",
                  start: "11:00:00",
                },
                {
                  end: "11:06:00",
                  start: "11:03:00",
                },
                {
                  end: "11:09:00",
                  start: "11:06:00",
                },
                {
                  end: "11:12:00",
                  start: "11:09:00",
                },
                {
                  end: "11:15:00",
                  start: "11:12:00",
                },
                {
                  end: "11:18:00",
                  start: "11:15:00",
                },
                {
                  end: "11:21:00",
                  start: "11:18:00",
                },
                {
                  end: "11:24:00",
                  start: "11:21:00",
                },
                {
                  end: "11:27:00",
                  start: "11:24:00",
                },
                {
                  end: "11:30:00",
                  start: "11:27:00",
                },
              ],
              municipi: "Pujalt",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Anoia",
              hores: [
                {
                  end: "11:33:00",
                  start: "11:30:00",
                },
                {
                  end: "11:36:00",
                  start: "11:33:00",
                },
                {
                  end: "11:39:00",
                  start: "11:36:00",
                },
                {
                  end: "11:42:00",
                  start: "11:39:00",
                },
                {
                  end: "11:45:00",
                  start: "11:42:00",
                },
                {
                  end: "11:48:00",
                  start: "11:45:00",
                },
                {
                  end: "11:51:00",
                  start: "11:48:00",
                },
                {
                  end: "11:54:00",
                  start: "11:51:00",
                },
                {
                  end: "11:57:00",
                  start: "11:54:00",
                },
                {
                  end: "12:00:00",
                  start: "11:57:00",
                },
              ],
              municipi: "Rubi�",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Anoia",
              hores: [
                {
                  end: "12:03:00",
                  start: "12:00:00",
                },
                {
                  end: "12:06:00",
                  start: "12:03:00",
                },
                {
                  end: "12:09:00",
                  start: "12:06:00",
                },
                {
                  end: "12:12:00",
                  start: "12:09:00",
                },
                {
                  end: "12:15:00",
                  start: "12:12:00",
                },
                {
                  end: "12:18:00",
                  start: "12:15:00",
                },
                {
                  end: "12:21:00",
                  start: "12:18:00",
                },
                {
                  end: "12:24:00",
                  start: "12:21:00",
                },
                {
                  end: "12:27:00",
                  start: "12:24:00",
                },
                {
                  end: "12:30:00",
                  start: "12:27:00",
                },
              ],
              municipi: "Santa Maria de Miralles",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Conca Barb.",
              hores: [
                {
                  end: "12:33:00",
                  start: "12:30:00",
                },
                {
                  end: "12:36:00",
                  start: "12:33:00",
                },
                {
                  end: "12:39:00",
                  start: "12:36:00",
                },
                {
                  end: "12:42:00",
                  start: "12:39:00",
                },
                {
                  end: "12:45:00",
                  start: "12:42:00",
                },
                {
                  end: "12:48:00",
                  start: "12:45:00",
                },
                {
                  end: "12:51:00",
                  start: "12:48:00",
                },
                {
                  end: "12:54:00",
                  start: "12:51:00",
                },
                {
                  end: "12:57:00",
                  start: "12:54:00",
                },
                {
                  end: "13:00:00",
                  start: "12:57:00",
                },
              ],
              municipi: "Piles",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-04 08:00:00",
            pd: {
              comarca: "Conca Barb.",
              hores: [
                {
                  end: "08:03:00",
                  start: "08:00:00",
                },
                {
                  end: "08:06:00",
                  start: "08:03:00",
                },
                {
                  end: "08:09:00",
                  start: "08:06:00",
                },
                {
                  end: "08:12:00",
                  start: "08:09:00",
                },
                {
                  end: "08:15:00",
                  start: "08:12:00",
                },
                {
                  end: "08:18:00",
                  start: "08:15:00",
                },
                {
                  end: "08:21:00",
                  start: "08:18:00",
                },
                {
                  end: "08:24:00",
                  start: "08:21:00",
                },
                {
                  end: "08:27:00",
                  start: "08:24:00",
                },
                {
                  end: "08:30:00",
                  start: "08:27:00",
                },
              ],
              municipi: "Rocafort de Queralt",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-07 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Vilamacolum",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-07 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Forti�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-07 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
                {
                  end: "12:36:00",
                  start: "12:30:00",
                },
                {
                  end: "12:42:00",
                  start: "12:36:00",
                },
                {
                  end: "12:48:00",
                  start: "12:42:00",
                },
                {
                  end: "12:54:00",
                  start: "12:48:00",
                },
                {
                  end: "13:00:00",
                  start: "12:54:00",
                },
              ],
              municipi: "Pau",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-07 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "13:06:00",
                  start: "13:00:00",
                },
                {
                  end: "13:12:00",
                  start: "13:06:00",
                },
                {
                  end: "13:18:00",
                  start: "13:12:00",
                },
                {
                  end: "13:24:00",
                  start: "13:18:00",
                },
                {
                  end: "13:30:00",
                  start: "13:24:00",
                },
                {
                  end: "13:36:00",
                  start: "13:30:00",
                },
                {
                  end: "13:42:00",
                  start: "13:36:00",
                },
                {
                  end: "13:48:00",
                  start: "13:42:00",
                },
                {
                  end: "13:54:00",
                  start: "13:48:00",
                },
                {
                  end: "14:00:00",
                  start: "13:54:00",
                },
              ],
              municipi: "Ordis",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-10 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "08:03:00",
                  start: "08:00:00",
                },
                {
                  end: "08:06:00",
                  start: "08:03:00",
                },
                {
                  end: "08:09:00",
                  start: "08:06:00",
                },
                {
                  end: "08:12:00",
                  start: "08:09:00",
                },
                {
                  end: "08:15:00",
                  start: "08:12:00",
                },
                {
                  end: "08:18:00",
                  start: "08:15:00",
                },
                {
                  end: "08:21:00",
                  start: "08:18:00",
                },
                {
                  end: "08:24:00",
                  start: "08:21:00",
                },
                {
                  end: "08:27:00",
                  start: "08:24:00",
                },
                {
                  end: "08:30:00",
                  start: "08:27:00",
                },
              ],
              municipi: "Vila�r",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-10 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "08:33:00",
                  start: "08:30:00",
                },
                {
                  end: "08:36:00",
                  start: "08:33:00",
                },
                {
                  end: "08:39:00",
                  start: "08:36:00",
                },
                {
                  end: "08:42:00",
                  start: "08:39:00",
                },
                {
                  end: "08:45:00",
                  start: "08:42:00",
                },
                {
                  end: "08:48:00",
                  start: "08:45:00",
                },
                {
                  end: "08:51:00",
                  start: "08:48:00",
                },
                {
                  end: "08:54:00",
                  start: "08:51:00",
                },
                {
                  end: "08:57:00",
                  start: "08:54:00",
                },
                {
                  end: "09:00:00",
                  start: "08:57:00",
                },
              ],
              municipi: "Selva de Mar",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-10 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "09:03:00",
                  start: "09:00:00",
                },
                {
                  end: "09:06:00",
                  start: "09:03:00",
                },
                {
                  end: "09:09:00",
                  start: "09:06:00",
                },
                {
                  end: "09:12:00",
                  start: "09:09:00",
                },
                {
                  end: "09:15:00",
                  start: "09:12:00",
                },
                {
                  end: "09:18:00",
                  start: "09:15:00",
                },
                {
                  end: "09:21:00",
                  start: "09:18:00",
                },
                {
                  end: "09:24:00",
                  start: "09:21:00",
                },
                {
                  end: "09:27:00",
                  start: "09:24:00",
                },
                {
                  end: "09:30:00",
                  start: "09:27:00",
                },
              ],
              municipi: "Palau de Santa Eul�lia",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-13 08:00:00",
            pd: {
              comarca: "Bages",
              hores: [
                {
                  end: "12:36:00",
                  start: "12:30:00",
                },
                {
                  end: "12:42:00",
                  start: "12:36:00",
                },
                {
                  end: "12:48:00",
                  start: "12:42:00",
                },
                {
                  end: "12:54:00",
                  start: "12:48:00",
                },
                {
                  end: "13:00:00",
                  start: "12:54:00",
                },
                {
                  end: "13:06:00",
                  start: "13:00:00",
                },
                {
                  end: "13:12:00",
                  start: "13:06:00",
                },
                {
                  end: "13:18:00",
                  start: "13:12:00",
                },
                {
                  end: "13:24:00",
                  start: "13:18:00",
                },
                {
                  end: "13:30:00",
                  start: "13:24:00",
                },
              ],
              municipi: "Castellgal�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-14 08:00:00",
            pd: {
              comarca: "Baix Llobreg.t",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Castellv� de Rosanes",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-14 08:00:00",
            pd: {
              comarca: "Vall�s Occ.",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Sant Lloren� Savall",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-14 08:00:00",
            pd: {
              comarca: "Vall�s Ori.",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Vilalba Sasserra",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-14 08:00:00",
            pd: {
              comarca: "Vall�s Ori.",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Gualba",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-14 08:00:00",
            pd: {
              comarca: "Vall�s Ori.",
              hores: [
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
                {
                  end: "12:36:00",
                  start: "12:30:00",
                },
                {
                  end: "12:42:00",
                  start: "12:36:00",
                },
                {
                  end: "12:48:00",
                  start: "12:42:00",
                },
                {
                  end: "12:54:00",
                  start: "12:48:00",
                },
                {
                  end: "13:00:00",
                  start: "12:54:00",
                },
              ],
              municipi: "Montseny",
              temps_estimat: 60,
            },
          },
        ],
        itinerari3: [
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Anoia",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Copons",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Anoia",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Cabrera d'Anoia",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Anoia",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Carme",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Anoia",
              hores: [
                {
                  end: "11:03:00",
                  start: "11:00:00",
                },
                {
                  end: "11:06:00",
                  start: "11:03:00",
                },
                {
                  end: "11:09:00",
                  start: "11:06:00",
                },
                {
                  end: "11:12:00",
                  start: "11:09:00",
                },
                {
                  end: "11:15:00",
                  start: "11:12:00",
                },
                {
                  end: "11:18:00",
                  start: "11:15:00",
                },
                {
                  end: "11:21:00",
                  start: "11:18:00",
                },
                {
                  end: "11:24:00",
                  start: "11:21:00",
                },
                {
                  end: "11:27:00",
                  start: "11:24:00",
                },
                {
                  end: "11:30:00",
                  start: "11:27:00",
                },
              ],
              municipi: "Sant Pere Sallavinera",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Anoia",
              hores: [
                {
                  end: "11:33:00",
                  start: "11:30:00",
                },
                {
                  end: "11:36:00",
                  start: "11:33:00",
                },
                {
                  end: "11:39:00",
                  start: "11:36:00",
                },
                {
                  end: "11:42:00",
                  start: "11:39:00",
                },
                {
                  end: "11:45:00",
                  start: "11:42:00",
                },
                {
                  end: "11:48:00",
                  start: "11:45:00",
                },
                {
                  end: "11:51:00",
                  start: "11:48:00",
                },
                {
                  end: "11:54:00",
                  start: "11:51:00",
                },
                {
                  end: "11:57:00",
                  start: "11:54:00",
                },
                {
                  end: "12:00:00",
                  start: "11:57:00",
                },
              ],
              municipi: "Veciana",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Conca Barb.",
              hores: [
                {
                  end: "12:03:00",
                  start: "12:00:00",
                },
                {
                  end: "12:06:00",
                  start: "12:03:00",
                },
                {
                  end: "12:09:00",
                  start: "12:06:00",
                },
                {
                  end: "12:12:00",
                  start: "12:09:00",
                },
                {
                  end: "12:15:00",
                  start: "12:12:00",
                },
                {
                  end: "12:18:00",
                  start: "12:15:00",
                },
                {
                  end: "12:21:00",
                  start: "12:18:00",
                },
                {
                  end: "12:24:00",
                  start: "12:21:00",
                },
                {
                  end: "12:27:00",
                  start: "12:24:00",
                },
                {
                  end: "12:30:00",
                  start: "12:27:00",
                },
              ],
              municipi: "Conesa",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Conca Barb.",
              hores: [
                {
                  end: "12:33:00",
                  start: "12:30:00",
                },
                {
                  end: "12:36:00",
                  start: "12:33:00",
                },
                {
                  end: "12:39:00",
                  start: "12:36:00",
                },
                {
                  end: "12:42:00",
                  start: "12:39:00",
                },
                {
                  end: "12:45:00",
                  start: "12:42:00",
                },
                {
                  end: "12:48:00",
                  start: "12:45:00",
                },
                {
                  end: "12:51:00",
                  start: "12:48:00",
                },
                {
                  end: "12:54:00",
                  start: "12:51:00",
                },
                {
                  end: "12:57:00",
                  start: "12:54:00",
                },
                {
                  end: "13:00:00",
                  start: "12:57:00",
                },
              ],
              municipi: "Savall� del Comtat",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-07 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
              ],
              municipi: "Borrass�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-07 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
              ],
              municipi: "Santa Llogaia d'�lguema",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-07 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
              ],
              municipi: "Avinyonet de Puigvent�s",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-10 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Pont�s",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-10 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "09:03:00",
                  start: "09:00:00",
                },
                {
                  end: "09:06:00",
                  start: "09:03:00",
                },
                {
                  end: "09:09:00",
                  start: "09:06:00",
                },
                {
                  end: "09:12:00",
                  start: "09:09:00",
                },
                {
                  end: "09:15:00",
                  start: "09:12:00",
                },
                {
                  end: "09:18:00",
                  start: "09:15:00",
                },
                {
                  end: "09:21:00",
                  start: "09:18:00",
                },
                {
                  end: "09:24:00",
                  start: "09:21:00",
                },
                {
                  end: "09:27:00",
                  start: "09:24:00",
                },
                {
                  end: "09:30:00",
                  start: "09:27:00",
                },
              ],
              municipi: "Siurana",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-10 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "09:33:00",
                  start: "09:30:00",
                },
                {
                  end: "09:36:00",
                  start: "09:33:00",
                },
                {
                  end: "09:39:00",
                  start: "09:36:00",
                },
                {
                  end: "09:42:00",
                  start: "09:39:00",
                },
                {
                  end: "09:45:00",
                  start: "09:42:00",
                },
                {
                  end: "09:48:00",
                  start: "09:45:00",
                },
                {
                  end: "09:51:00",
                  start: "09:48:00",
                },
                {
                  end: "09:54:00",
                  start: "09:51:00",
                },
                {
                  end: "09:57:00",
                  start: "09:54:00",
                },
                {
                  end: "10:00:00",
                  start: "09:57:00",
                },
              ],
              municipi: "Mollet de Peralada",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-13 08:00:00",
            pd: {
              comarca: "Bages",
              hores: [
                {
                  end: "12:33:00",
                  start: "12:30:00",
                },
                {
                  end: "12:36:00",
                  start: "12:33:00",
                },
                {
                  end: "12:39:00",
                  start: "12:36:00",
                },
                {
                  end: "12:42:00",
                  start: "12:39:00",
                },
                {
                  end: "12:45:00",
                  start: "12:42:00",
                },
                {
                  end: "12:48:00",
                  start: "12:45:00",
                },
                {
                  end: "12:51:00",
                  start: "12:48:00",
                },
                {
                  end: "12:54:00",
                  start: "12:51:00",
                },
                {
                  end: "12:57:00",
                  start: "12:54:00",
                },
                {
                  end: "13:00:00",
                  start: "12:57:00",
                },
              ],
              municipi: "Mura",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-14 08:00:00",
            pd: {
              comarca: "Maresme",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "�rrius",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-14 08:00:00",
            pd: {
              comarca: "Vall�s Occ.",
              hores: [
                {
                  end: "09:03:00",
                  start: "09:00:00",
                },
                {
                  end: "09:06:00",
                  start: "09:03:00",
                },
                {
                  end: "09:09:00",
                  start: "09:06:00",
                },
                {
                  end: "09:12:00",
                  start: "09:09:00",
                },
                {
                  end: "09:15:00",
                  start: "09:12:00",
                },
                {
                  end: "09:18:00",
                  start: "09:15:00",
                },
                {
                  end: "09:21:00",
                  start: "09:18:00",
                },
                {
                  end: "09:24:00",
                  start: "09:21:00",
                },
                {
                  end: "09:27:00",
                  start: "09:24:00",
                },
                {
                  end: "09:30:00",
                  start: "09:27:00",
                },
              ],
              municipi: "Gallifa",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-14 08:00:00",
            pd: {
              comarca: "Vall�s Ori.",
              hores: [
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
              ],
              municipi: "Campins",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-14 08:00:00",
            pd: {
              comarca: "Vall�s Ori.",
              hores: [
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
              ],
              municipi: "Sant Pere de Vilamajor",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-14 08:00:00",
            pd: {
              comarca: "Vall�s Ori.",
              hores: [
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
              ],
              municipi: "Sant Esteve de Palautordera",
              temps_estimat: 60,
            },
          },
        ],
        itinerari4: [
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Anoia",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Jorba",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Anoia",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Torre de Claramunt",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Anoia",
              hores: [
                {
                  end: "10:03:00",
                  start: "10:00:00",
                },
                {
                  end: "10:06:00",
                  start: "10:03:00",
                },
                {
                  end: "10:09:00",
                  start: "10:06:00",
                },
                {
                  end: "10:12:00",
                  start: "10:09:00",
                },
                {
                  end: "10:15:00",
                  start: "10:12:00",
                },
                {
                  end: "10:18:00",
                  start: "10:15:00",
                },
                {
                  end: "10:21:00",
                  start: "10:18:00",
                },
                {
                  end: "10:24:00",
                  start: "10:21:00",
                },
                {
                  end: "10:27:00",
                  start: "10:24:00",
                },
                {
                  end: "10:30:00",
                  start: "10:27:00",
                },
              ],
              municipi: "Calonge de Segarra",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Anoia",
              hores: [
                {
                  end: "10:33:00",
                  start: "10:30:00",
                },
                {
                  end: "10:36:00",
                  start: "10:33:00",
                },
                {
                  end: "10:39:00",
                  start: "10:36:00",
                },
                {
                  end: "10:42:00",
                  start: "10:39:00",
                },
                {
                  end: "10:45:00",
                  start: "10:42:00",
                },
                {
                  end: "10:48:00",
                  start: "10:45:00",
                },
                {
                  end: "10:51:00",
                  start: "10:48:00",
                },
                {
                  end: "10:54:00",
                  start: "10:51:00",
                },
                {
                  end: "10:57:00",
                  start: "10:54:00",
                },
                {
                  end: "11:00:00",
                  start: "10:57:00",
                },
              ],
              municipi: "Argen�ola",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Anoia",
              hores: [
                {
                  end: "11:03:00",
                  start: "11:00:00",
                },
                {
                  end: "11:06:00",
                  start: "11:03:00",
                },
                {
                  end: "11:09:00",
                  start: "11:06:00",
                },
                {
                  end: "11:12:00",
                  start: "11:09:00",
                },
                {
                  end: "11:15:00",
                  start: "11:12:00",
                },
                {
                  end: "11:18:00",
                  start: "11:15:00",
                },
                {
                  end: "11:21:00",
                  start: "11:18:00",
                },
                {
                  end: "11:24:00",
                  start: "11:21:00",
                },
                {
                  end: "11:27:00",
                  start: "11:24:00",
                },
                {
                  end: "11:30:00",
                  start: "11:27:00",
                },
              ],
              municipi: "Bellprat",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Conca Barb.",
              hores: [
                {
                  end: "11:33:00",
                  start: "11:30:00",
                },
                {
                  end: "11:36:00",
                  start: "11:33:00",
                },
                {
                  end: "11:39:00",
                  start: "11:36:00",
                },
                {
                  end: "11:42:00",
                  start: "11:39:00",
                },
                {
                  end: "11:45:00",
                  start: "11:42:00",
                },
                {
                  end: "11:48:00",
                  start: "11:45:00",
                },
                {
                  end: "11:51:00",
                  start: "11:48:00",
                },
                {
                  end: "11:54:00",
                  start: "11:51:00",
                },
                {
                  end: "11:57:00",
                  start: "11:54:00",
                },
                {
                  end: "12:00:00",
                  start: "11:57:00",
                },
              ],
              municipi: "Llorac",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-03 08:00:00",
            pd: {
              comarca: "Conca Barb.",
              hores: [
                {
                  end: "12:03:00",
                  start: "12:00:00",
                },
                {
                  end: "12:06:00",
                  start: "12:03:00",
                },
                {
                  end: "12:09:00",
                  start: "12:06:00",
                },
                {
                  end: "12:12:00",
                  start: "12:09:00",
                },
                {
                  end: "12:15:00",
                  start: "12:12:00",
                },
                {
                  end: "12:18:00",
                  start: "12:15:00",
                },
                {
                  end: "12:21:00",
                  start: "12:18:00",
                },
                {
                  end: "12:24:00",
                  start: "12:21:00",
                },
                {
                  end: "12:27:00",
                  start: "12:24:00",
                },
                {
                  end: "12:30:00",
                  start: "12:27:00",
                },
              ],
              municipi: "Vallfogona de Riucorb",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-07 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Sant Miquel de Fluvi�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-07 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Garrig�s",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-07 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Vila-sacra",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-07 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
                {
                  end: "12:36:00",
                  start: "12:30:00",
                },
                {
                  end: "12:42:00",
                  start: "12:36:00",
                },
                {
                  end: "12:48:00",
                  start: "12:42:00",
                },
                {
                  end: "12:54:00",
                  start: "12:48:00",
                },
                {
                  end: "13:00:00",
                  start: "12:54:00",
                },
              ],
              municipi: "Masarac",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-10 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Vilafant",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-10 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "09:03:00",
                  start: "09:00:00",
                },
                {
                  end: "09:06:00",
                  start: "09:03:00",
                },
                {
                  end: "09:09:00",
                  start: "09:06:00",
                },
                {
                  end: "09:12:00",
                  start: "09:09:00",
                },
                {
                  end: "09:15:00",
                  start: "09:12:00",
                },
                {
                  end: "09:18:00",
                  start: "09:15:00",
                },
                {
                  end: "09:21:00",
                  start: "09:18:00",
                },
                {
                  end: "09:24:00",
                  start: "09:21:00",
                },
                {
                  end: "09:27:00",
                  start: "09:24:00",
                },
                {
                  end: "09:30:00",
                  start: "09:27:00",
                },
              ],
              municipi: "Riumors",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-10 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "09:33:00",
                  start: "09:30:00",
                },
                {
                  end: "09:36:00",
                  start: "09:33:00",
                },
                {
                  end: "09:39:00",
                  start: "09:36:00",
                },
                {
                  end: "09:42:00",
                  start: "09:39:00",
                },
                {
                  end: "09:45:00",
                  start: "09:42:00",
                },
                {
                  end: "09:48:00",
                  start: "09:45:00",
                },
                {
                  end: "09:51:00",
                  start: "09:48:00",
                },
                {
                  end: "09:54:00",
                  start: "09:51:00",
                },
                {
                  end: "09:57:00",
                  start: "09:54:00",
                },
                {
                  end: "10:00:00",
                  start: "09:57:00",
                },
              ],
              municipi: "Rab�s",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-13 08:00:00",
            pd: {
              comarca: "Bages",
              hores: [
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
                {
                  end: "12:36:00",
                  start: "12:30:00",
                },
                {
                  end: "12:42:00",
                  start: "12:36:00",
                },
                {
                  end: "12:48:00",
                  start: "12:42:00",
                },
                {
                  end: "12:54:00",
                  start: "12:48:00",
                },
                {
                  end: "13:00:00",
                  start: "12:54:00",
                },
              ],
              municipi: "Marganell",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-13 08:00:00",
            pd: {
              comarca: "Bages",
              hores: [
                {
                  end: "13:03:00",
                  start: "13:00:00",
                },
                {
                  end: "13:06:00",
                  start: "13:03:00",
                },
                {
                  end: "13:09:00",
                  start: "13:06:00",
                },
                {
                  end: "13:12:00",
                  start: "13:09:00",
                },
                {
                  end: "13:15:00",
                  start: "13:12:00",
                },
                {
                  end: "13:18:00",
                  start: "13:15:00",
                },
                {
                  end: "13:21:00",
                  start: "13:18:00",
                },
                {
                  end: "13:24:00",
                  start: "13:21:00",
                },
                {
                  end: "13:27:00",
                  start: "13:24:00",
                },
                {
                  end: "13:30:00",
                  start: "13:27:00",
                },
              ],
              municipi: "Talamanca",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-14 08:00:00",
            pd: {
              comarca: "Vall�s Occ.",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Rellinars",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-14 08:00:00",
            pd: {
              comarca: "Vall�s Ori.",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Santa Maria de Martorelles",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-14 08:00:00",
            pd: {
              comarca: "Vall�s Ori.",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "C�noves i Samal�s",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-14 08:00:00",
            pd: {
              comarca: "Vall�s Ori.",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Tagamanent",
              temps_estimat: 60,
            },
          },
        ],
      },
      {
        itinerari1: [
          {
            data: "2024-06-04 08:00:00",
            pd: {
              comarca: "Alt Pened�s",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Pontons",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-04 08:00:00",
            pd: {
              comarca: "Alt Pened�s",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Sant Cugat Sesgarrigues",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-04 08:00:00",
            pd: {
              comarca: "Alt Pened�s",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Olesa de Bonesvalls",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-04 08:00:00",
            pd: {
              comarca: "Alt Pened�s",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Torrelavit",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-04 08:00:00",
            pd: {
              comarca: "Baix Pened�s",
              hores: [
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
                {
                  end: "12:36:00",
                  start: "12:30:00",
                },
                {
                  end: "12:42:00",
                  start: "12:36:00",
                },
                {
                  end: "12:48:00",
                  start: "12:42:00",
                },
                {
                  end: "12:54:00",
                  start: "12:48:00",
                },
                {
                  end: "13:00:00",
                  start: "12:54:00",
                },
              ],
              municipi: "Maslloren�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-05 08:00:00",
            pd: {
              comarca: "Tarragon�s",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Vespella de Gai�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-10 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Llad�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-10 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Sant Lloren� de la Muga",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-10 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
                {
                  end: "12:36:00",
                  start: "12:30:00",
                },
                {
                  end: "12:42:00",
                  start: "12:36:00",
                },
                {
                  end: "12:48:00",
                  start: "12:42:00",
                },
                {
                  end: "12:54:00",
                  start: "12:48:00",
                },
                {
                  end: "13:00:00",
                  start: "12:54:00",
                },
              ],
              municipi: "Cantallops",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-11 08:00:00",
            pd: {
              comarca: "Garrotxa",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Mieres",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-11 08:00:00",
            pd: {
              comarca: "Garrotxa",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Argelaguer",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-11 08:00:00",
            pd: {
              comarca: "Garrotxa",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Montagut i Oix",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-14 08:00:00",
            pd: {
              comarca: "Bages",
              hores: [
                {
                  end: "13:06:00",
                  start: "13:00:00",
                },
                {
                  end: "13:12:00",
                  start: "13:06:00",
                },
                {
                  end: "13:18:00",
                  start: "13:12:00",
                },
                {
                  end: "13:24:00",
                  start: "13:18:00",
                },
                {
                  end: "13:30:00",
                  start: "13:24:00",
                },
                {
                  end: "13:36:00",
                  start: "13:30:00",
                },
                {
                  end: "13:42:00",
                  start: "13:36:00",
                },
                {
                  end: "13:48:00",
                  start: "13:42:00",
                },
                {
                  end: "13:54:00",
                  start: "13:48:00",
                },
                {
                  end: "14:00:00",
                  start: "13:54:00",
                },
              ],
              municipi: "Fonollosa",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-17 08:00:00",
            pd: {
              comarca: "Bages",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Sant Feliu Sasserra",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-17 08:00:00",
            pd: {
              comarca: "Bergued�",
              hores: [
                {
                  end: "09:03:00",
                  start: "09:00:00",
                },
                {
                  end: "09:06:00",
                  start: "09:03:00",
                },
                {
                  end: "09:09:00",
                  start: "09:06:00",
                },
                {
                  end: "09:12:00",
                  start: "09:09:00",
                },
                {
                  end: "09:15:00",
                  start: "09:12:00",
                },
                {
                  end: "09:18:00",
                  start: "09:15:00",
                },
                {
                  end: "09:21:00",
                  start: "09:18:00",
                },
                {
                  end: "09:24:00",
                  start: "09:21:00",
                },
                {
                  end: "09:27:00",
                  start: "09:24:00",
                },
                {
                  end: "09:30:00",
                  start: "09:27:00",
                },
              ],
              municipi: "Santa Maria de Merl�s",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-17 08:00:00",
            pd: {
              comarca: "Llu�an�s",
              hores: [
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
              ],
              municipi: "Perafita",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-17 08:00:00",
            pd: {
              comarca: "Moian�s",
              hores: [
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
              ],
              municipi: "Monistrol de Calders",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-17 08:00:00",
            pd: {
              comarca: "Moian�s",
              hores: [
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
              ],
              municipi: "Collsuspina",
              temps_estimat: 60,
            },
          },
        ],
        itinerari2: [
          {
            data: "2024-06-04 08:00:00",
            pd: {
              comarca: "Alt Pened�s",
              hores: [
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
              ],
              municipi: "Torrelles de Foix",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-04 08:00:00",
            pd: {
              comarca: "Alt Pened�s",
              hores: [
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
              ],
              municipi: "Santa Fe del Pened�s",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-04 08:00:00",
            pd: {
              comarca: "Alt Pened�s",
              hores: [
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
              ],
              municipi: "Puigd�lber",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-04 08:00:00",
            pd: {
              comarca: "Baix Pened�s",
              hores: [
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
              ],
              municipi: "Albinyana",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-04 08:00:00",
            pd: {
              comarca: "Baix Pened�s",
              hores: [
                {
                  end: "12:36:00",
                  start: "12:30:00",
                },
                {
                  end: "12:42:00",
                  start: "12:36:00",
                },
                {
                  end: "12:48:00",
                  start: "12:42:00",
                },
                {
                  end: "12:54:00",
                  start: "12:48:00",
                },
                {
                  end: "13:00:00",
                  start: "12:54:00",
                },
                {
                  end: "13:06:00",
                  start: "13:00:00",
                },
                {
                  end: "13:12:00",
                  start: "13:06:00",
                },
                {
                  end: "13:18:00",
                  start: "13:12:00",
                },
                {
                  end: "13:24:00",
                  start: "13:18:00",
                },
                {
                  end: "13:30:00",
                  start: "13:24:00",
                },
              ],
              municipi: "Montmell",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-10 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
              ],
              municipi: "Vilanant",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-10 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
              ],
              municipi: "Terrades",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-10 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "11:33:00",
                  start: "11:30:00",
                },
                {
                  end: "11:36:00",
                  start: "11:33:00",
                },
                {
                  end: "11:39:00",
                  start: "11:36:00",
                },
                {
                  end: "11:42:00",
                  start: "11:39:00",
                },
                {
                  end: "11:45:00",
                  start: "11:42:00",
                },
                {
                  end: "11:48:00",
                  start: "11:45:00",
                },
                {
                  end: "11:51:00",
                  start: "11:48:00",
                },
                {
                  end: "11:54:00",
                  start: "11:51:00",
                },
                {
                  end: "11:57:00",
                  start: "11:54:00",
                },
                {
                  end: "12:00:00",
                  start: "11:57:00",
                },
              ],
              municipi: "Albany�",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-11 08:00:00",
            pd: {
              comarca: "Garrotxa",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Sant Aniol de Finestres",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-11 08:00:00",
            pd: {
              comarca: "Garrotxa",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Riudaura",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-11 08:00:00",
            pd: {
              comarca: "Garrotxa",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Tortell�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-17 08:00:00",
            pd: {
              comarca: "Bages",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Rajadell",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-17 08:00:00",
            pd: {
              comarca: "Bergued�",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Olvan",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-17 08:00:00",
            pd: {
              comarca: "Llu�an�s",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Olost",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-17 08:00:00",
            pd: {
              comarca: "Llu�an�s",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Alpens",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-17 08:00:00",
            pd: {
              comarca: "Moian�s",
              hores: [
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
                {
                  end: "12:36:00",
                  start: "12:30:00",
                },
                {
                  end: "12:42:00",
                  start: "12:36:00",
                },
                {
                  end: "12:48:00",
                  start: "12:42:00",
                },
                {
                  end: "12:54:00",
                  start: "12:48:00",
                },
                {
                  end: "13:00:00",
                  start: "12:54:00",
                },
              ],
              municipi: "Sant Quirze Safaja",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-17 08:00:00",
            pd: {
              comarca: "Moian�s",
              hores: [
                {
                  end: "13:06:00",
                  start: "13:00:00",
                },
                {
                  end: "13:12:00",
                  start: "13:06:00",
                },
                {
                  end: "13:18:00",
                  start: "13:12:00",
                },
                {
                  end: "13:24:00",
                  start: "13:18:00",
                },
                {
                  end: "13:30:00",
                  start: "13:24:00",
                },
                {
                  end: "13:36:00",
                  start: "13:30:00",
                },
                {
                  end: "13:42:00",
                  start: "13:36:00",
                },
                {
                  end: "13:48:00",
                  start: "13:42:00",
                },
                {
                  end: "13:54:00",
                  start: "13:48:00",
                },
                {
                  end: "14:00:00",
                  start: "13:54:00",
                },
              ],
              municipi: "Estany",
              temps_estimat: 60,
            },
          },
        ],
        itinerari3: [
          {
            data: "2024-06-04 08:00:00",
            pd: {
              comarca: "Alt Pened�s",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Mediona",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-04 08:00:00",
            pd: {
              comarca: "Alt Pened�s",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Cabanyes",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-04 08:00:00",
            pd: {
              comarca: "Alt Pened�s",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Vilob� del Pened�s",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-04 08:00:00",
            pd: {
              comarca: "Alt Pened�s",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Sant Lloren� d'Hortons",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-04 08:00:00",
            pd: {
              comarca: "Baix Pened�s",
              hores: [
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
                {
                  end: "12:36:00",
                  start: "12:30:00",
                },
                {
                  end: "12:42:00",
                  start: "12:36:00",
                },
                {
                  end: "12:48:00",
                  start: "12:42:00",
                },
                {
                  end: "12:54:00",
                  start: "12:48:00",
                },
                {
                  end: "13:00:00",
                  start: "12:54:00",
                },
              ],
              municipi: "Bonastre",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-05 08:00:00",
            pd: {
              comarca: "Garraf",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Olivella",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-10 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Navata",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-10 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Boadella i les Escaules",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-10 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
                {
                  end: "12:36:00",
                  start: "12:30:00",
                },
                {
                  end: "12:42:00",
                  start: "12:36:00",
                },
                {
                  end: "12:48:00",
                  start: "12:42:00",
                },
                {
                  end: "12:54:00",
                  start: "12:48:00",
                },
                {
                  end: "13:00:00",
                  start: "12:54:00",
                },
              ],
              municipi: "Capmany",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-10 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "13:03:00",
                  start: "13:00:00",
                },
                {
                  end: "13:06:00",
                  start: "13:03:00",
                },
                {
                  end: "13:09:00",
                  start: "13:06:00",
                },
                {
                  end: "13:12:00",
                  start: "13:09:00",
                },
                {
                  end: "13:15:00",
                  start: "13:12:00",
                },
                {
                  end: "13:18:00",
                  start: "13:15:00",
                },
                {
                  end: "13:21:00",
                  start: "13:18:00",
                },
                {
                  end: "13:24:00",
                  start: "13:21:00",
                },
                {
                  end: "13:27:00",
                  start: "13:24:00",
                },
                {
                  end: "13:30:00",
                  start: "13:27:00",
                },
              ],
              municipi: "Vajol",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-11 08:00:00",
            pd: {
              comarca: "Garrotxa",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Mai� de Montcal",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-11 08:00:00",
            pd: {
              comarca: "Garrotxa",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Sant Jaume de Llierca",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-11 08:00:00",
            pd: {
              comarca: "Garrotxa",
              hores: [
                {
                  end: "10:03:00",
                  start: "10:00:00",
                },
                {
                  end: "10:06:00",
                  start: "10:03:00",
                },
                {
                  end: "10:09:00",
                  start: "10:06:00",
                },
                {
                  end: "10:12:00",
                  start: "10:09:00",
                },
                {
                  end: "10:15:00",
                  start: "10:12:00",
                },
                {
                  end: "10:18:00",
                  start: "10:15:00",
                },
                {
                  end: "10:21:00",
                  start: "10:18:00",
                },
                {
                  end: "10:24:00",
                  start: "10:21:00",
                },
                {
                  end: "10:27:00",
                  start: "10:24:00",
                },
                {
                  end: "10:30:00",
                  start: "10:27:00",
                },
              ],
              municipi: "Sales de Llierca",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-17 08:00:00",
            pd: {
              comarca: "Bages",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Castellnou de Bages",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-17 08:00:00",
            pd: {
              comarca: "Bergued�",
              hores: [
                {
                  end: "09:03:00",
                  start: "09:00:00",
                },
                {
                  end: "09:06:00",
                  start: "09:03:00",
                },
                {
                  end: "09:09:00",
                  start: "09:06:00",
                },
                {
                  end: "09:12:00",
                  start: "09:09:00",
                },
                {
                  end: "09:15:00",
                  start: "09:12:00",
                },
                {
                  end: "09:18:00",
                  start: "09:15:00",
                },
                {
                  end: "09:21:00",
                  start: "09:18:00",
                },
                {
                  end: "09:24:00",
                  start: "09:21:00",
                },
                {
                  end: "09:27:00",
                  start: "09:24:00",
                },
                {
                  end: "09:30:00",
                  start: "09:27:00",
                },
              ],
              municipi: "Viver i Serrateix",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-17 08:00:00",
            pd: {
              comarca: "Llu�an�s",
              hores: [
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
              ],
              municipi: "Orist�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-17 08:00:00",
            pd: {
              comarca: "Llu�an�s",
              hores: [
                {
                  end: "10:33:00",
                  start: "10:30:00",
                },
                {
                  end: "10:36:00",
                  start: "10:33:00",
                },
                {
                  end: "10:39:00",
                  start: "10:36:00",
                },
                {
                  end: "10:42:00",
                  start: "10:39:00",
                },
                {
                  end: "10:45:00",
                  start: "10:42:00",
                },
                {
                  end: "10:48:00",
                  start: "10:45:00",
                },
                {
                  end: "10:51:00",
                  start: "10:48:00",
                },
                {
                  end: "10:54:00",
                  start: "10:51:00",
                },
                {
                  end: "10:57:00",
                  start: "10:54:00",
                },
                {
                  end: "11:00:00",
                  start: "10:57:00",
                },
              ],
              municipi: "Sant Mart� d'Albars",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-17 08:00:00",
            pd: {
              comarca: "Moian�s",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Calders",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-17 08:00:00",
            pd: {
              comarca: "Moian�s",
              hores: [
                {
                  end: "12:03:00",
                  start: "12:00:00",
                },
                {
                  end: "12:06:00",
                  start: "12:03:00",
                },
                {
                  end: "12:09:00",
                  start: "12:06:00",
                },
                {
                  end: "12:12:00",
                  start: "12:09:00",
                },
                {
                  end: "12:15:00",
                  start: "12:12:00",
                },
                {
                  end: "12:18:00",
                  start: "12:15:00",
                },
                {
                  end: "12:21:00",
                  start: "12:18:00",
                },
                {
                  end: "12:24:00",
                  start: "12:21:00",
                },
                {
                  end: "12:27:00",
                  start: "12:24:00",
                },
                {
                  end: "12:30:00",
                  start: "12:27:00",
                },
              ],
              municipi: "Granera",
              temps_estimat: 30,
            },
          },
        ],
        itinerari4: [
          {
            data: "2024-06-04 08:00:00",
            pd: {
              comarca: "Alt Pened�s",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Font-rub�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-04 08:00:00",
            pd: {
              comarca: "Alt Pened�s",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Pacs del Pened�s",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-04 08:00:00",
            pd: {
              comarca: "Alt Pened�s",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Castellet i la Gornal",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-04 08:00:00",
            pd: {
              comarca: "Alt Pened�s",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Subirats",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-04 08:00:00",
            pd: {
              comarca: "Baix Pened�s",
              hores: [
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
                {
                  end: "12:36:00",
                  start: "12:30:00",
                },
                {
                  end: "12:42:00",
                  start: "12:36:00",
                },
                {
                  end: "12:48:00",
                  start: "12:42:00",
                },
                {
                  end: "12:54:00",
                  start: "12:48:00",
                },
                {
                  end: "13:00:00",
                  start: "12:54:00",
                },
              ],
              municipi: "Santa Oliva",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-05 08:00:00",
            pd: {
              comarca: "Tarragon�s",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Salom�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-10 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Cabanelles",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-10 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Cistella",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-10 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
                {
                  end: "12:36:00",
                  start: "12:30:00",
                },
                {
                  end: "12:42:00",
                  start: "12:36:00",
                },
                {
                  end: "12:48:00",
                  start: "12:42:00",
                },
                {
                  end: "12:54:00",
                  start: "12:48:00",
                },
                {
                  end: "13:00:00",
                  start: "12:54:00",
                },
              ],
              municipi: "Pont de Molins",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-10 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "13:03:00",
                  start: "13:00:00",
                },
                {
                  end: "13:06:00",
                  start: "13:03:00",
                },
                {
                  end: "13:09:00",
                  start: "13:06:00",
                },
                {
                  end: "13:12:00",
                  start: "13:09:00",
                },
                {
                  end: "13:15:00",
                  start: "13:12:00",
                },
                {
                  end: "13:18:00",
                  start: "13:15:00",
                },
                {
                  end: "13:21:00",
                  start: "13:18:00",
                },
                {
                  end: "13:24:00",
                  start: "13:21:00",
                },
                {
                  end: "13:27:00",
                  start: "13:24:00",
                },
                {
                  end: "13:30:00",
                  start: "13:27:00",
                },
              ],
              municipi: "Biure",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-11 08:00:00",
            pd: {
              comarca: "Garrotxa",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Sant Ferriol",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-11 08:00:00",
            pd: {
              comarca: "Garrotxa",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Vall de Bianya",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-11 08:00:00",
            pd: {
              comarca: "Garrotxa",
              hores: [
                {
                  end: "10:03:00",
                  start: "10:00:00",
                },
                {
                  end: "10:06:00",
                  start: "10:03:00",
                },
                {
                  end: "10:09:00",
                  start: "10:06:00",
                },
                {
                  end: "10:12:00",
                  start: "10:09:00",
                },
                {
                  end: "10:15:00",
                  start: "10:12:00",
                },
                {
                  end: "10:18:00",
                  start: "10:15:00",
                },
                {
                  end: "10:21:00",
                  start: "10:18:00",
                },
                {
                  end: "10:24:00",
                  start: "10:21:00",
                },
                {
                  end: "10:27:00",
                  start: "10:24:00",
                },
                {
                  end: "10:30:00",
                  start: "10:27:00",
                },
              ],
              municipi: "Beuda",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-14 08:00:00",
            pd: {
              comarca: "Bages",
              hores: [
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
                {
                  end: "12:36:00",
                  start: "12:30:00",
                },
                {
                  end: "12:42:00",
                  start: "12:36:00",
                },
                {
                  end: "12:48:00",
                  start: "12:42:00",
                },
                {
                  end: "12:54:00",
                  start: "12:48:00",
                },
                {
                  end: "13:00:00",
                  start: "12:54:00",
                },
              ],
              municipi: "Aguilar de Segarra",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-17 08:00:00",
            pd: {
              comarca: "Bages",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Sant Mateu de Bages",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-17 08:00:00",
            pd: {
              comarca: "Bergued�",
              hores: [
                {
                  end: "09:03:00",
                  start: "09:00:00",
                },
                {
                  end: "09:06:00",
                  start: "09:03:00",
                },
                {
                  end: "09:09:00",
                  start: "09:06:00",
                },
                {
                  end: "09:12:00",
                  start: "09:09:00",
                },
                {
                  end: "09:15:00",
                  start: "09:12:00",
                },
                {
                  end: "09:18:00",
                  start: "09:15:00",
                },
                {
                  end: "09:21:00",
                  start: "09:18:00",
                },
                {
                  end: "09:24:00",
                  start: "09:21:00",
                },
                {
                  end: "09:27:00",
                  start: "09:24:00",
                },
                {
                  end: "09:30:00",
                  start: "09:27:00",
                },
              ],
              municipi: "Sag�s",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-17 08:00:00",
            pd: {
              comarca: "Llu�an�s",
              hores: [
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
              ],
              municipi: "Llu��",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-17 08:00:00",
            pd: {
              comarca: "Llu�an�s",
              hores: [
                {
                  end: "10:33:00",
                  start: "10:30:00",
                },
                {
                  end: "10:36:00",
                  start: "10:33:00",
                },
                {
                  end: "10:39:00",
                  start: "10:36:00",
                },
                {
                  end: "10:42:00",
                  start: "10:39:00",
                },
                {
                  end: "10:45:00",
                  start: "10:42:00",
                },
                {
                  end: "10:48:00",
                  start: "10:45:00",
                },
                {
                  end: "10:51:00",
                  start: "10:48:00",
                },
                {
                  end: "10:54:00",
                  start: "10:51:00",
                },
                {
                  end: "10:57:00",
                  start: "10:54:00",
                },
                {
                  end: "11:00:00",
                  start: "10:57:00",
                },
              ],
              municipi: "Sobremunt",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-17 08:00:00",
            pd: {
              comarca: "Moian�s",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Castellcir",
              temps_estimat: 60,
            },
          },
        ],
      },
      {
        itinerari1: [
          {
            data: "2024-06-05 08:00:00",
            pd: {
              comarca: "Alt Camp",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Figuerola del Camp",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-05 08:00:00",
            pd: {
              comarca: "Alt Camp",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Mas�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-05 08:00:00",
            pd: {
              comarca: "Alt Camp",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Puigpelat",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-05 08:00:00",
            pd: {
              comarca: "Alt Camp",
              hores: [
                {
                  end: "12:03:00",
                  start: "12:00:00",
                },
                {
                  end: "12:06:00",
                  start: "12:03:00",
                },
                {
                  end: "12:09:00",
                  start: "12:06:00",
                },
                {
                  end: "12:12:00",
                  start: "12:09:00",
                },
                {
                  end: "12:15:00",
                  start: "12:12:00",
                },
                {
                  end: "12:18:00",
                  start: "12:15:00",
                },
                {
                  end: "12:21:00",
                  start: "12:18:00",
                },
                {
                  end: "12:24:00",
                  start: "12:21:00",
                },
                {
                  end: "12:27:00",
                  start: "12:24:00",
                },
                {
                  end: "12:30:00",
                  start: "12:27:00",
                },
              ],
              municipi: "Mont-ral",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-06 08:00:00",
            pd: {
              comarca: "Conca Barb.",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Pira",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-06 08:00:00",
            pd: {
              comarca: "Conca Barb.",
              hores: [
                {
                  end: "09:03:00",
                  start: "09:00:00",
                },
                {
                  end: "09:06:00",
                  start: "09:03:00",
                },
                {
                  end: "09:09:00",
                  start: "09:06:00",
                },
                {
                  end: "09:12:00",
                  start: "09:09:00",
                },
                {
                  end: "09:15:00",
                  start: "09:12:00",
                },
                {
                  end: "09:18:00",
                  start: "09:15:00",
                },
                {
                  end: "09:21:00",
                  start: "09:18:00",
                },
                {
                  end: "09:24:00",
                  start: "09:21:00",
                },
                {
                  end: "09:27:00",
                  start: "09:24:00",
                },
                {
                  end: "09:30:00",
                  start: "09:27:00",
                },
              ],
              municipi: "Vallclara",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-11 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Ventall�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-11 08:00:00",
            pd: {
              comarca: "Baix Empord�",
              hores: [
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
                {
                  end: "12:36:00",
                  start: "12:30:00",
                },
                {
                  end: "12:42:00",
                  start: "12:36:00",
                },
                {
                  end: "12:48:00",
                  start: "12:42:00",
                },
                {
                  end: "12:54:00",
                  start: "12:48:00",
                },
                {
                  end: "13:00:00",
                  start: "12:54:00",
                },
              ],
              municipi: "Vall-llobrega",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-11 08:00:00",
            pd: {
              comarca: "Baix Empord�",
              hores: [
                {
                  end: "13:06:00",
                  start: "13:00:00",
                },
                {
                  end: "13:12:00",
                  start: "13:06:00",
                },
                {
                  end: "13:18:00",
                  start: "13:12:00",
                },
                {
                  end: "13:24:00",
                  start: "13:18:00",
                },
                {
                  end: "13:30:00",
                  start: "13:24:00",
                },
                {
                  end: "13:36:00",
                  start: "13:30:00",
                },
                {
                  end: "13:42:00",
                  start: "13:36:00",
                },
                {
                  end: "13:48:00",
                  start: "13:42:00",
                },
                {
                  end: "13:54:00",
                  start: "13:48:00",
                },
                {
                  end: "14:00:00",
                  start: "13:54:00",
                },
              ],
              municipi: "Pera",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-12 08:00:00",
            pd: {
              comarca: "Baix Empord�",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Gualta",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-12 08:00:00",
            pd: {
              comarca: "Baix Empord�",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Bellcaire d'Empord�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-12 08:00:00",
            pd: {
              comarca: "Baix Empord�",
              hores: [
                {
                  end: "10:03:00",
                  start: "10:00:00",
                },
                {
                  end: "10:06:00",
                  start: "10:03:00",
                },
                {
                  end: "10:09:00",
                  start: "10:06:00",
                },
                {
                  end: "10:12:00",
                  start: "10:09:00",
                },
                {
                  end: "10:15:00",
                  start: "10:12:00",
                },
                {
                  end: "10:18:00",
                  start: "10:15:00",
                },
                {
                  end: "10:21:00",
                  start: "10:18:00",
                },
                {
                  end: "10:24:00",
                  start: "10:21:00",
                },
                {
                  end: "10:27:00",
                  start: "10:24:00",
                },
                {
                  end: "10:30:00",
                  start: "10:27:00",
                },
              ],
              municipi: "Serra de Dar�",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-12 08:00:00",
            pd: {
              comarca: "Baix Empord�",
              hores: [
                {
                  end: "10:33:00",
                  start: "10:30:00",
                },
                {
                  end: "10:36:00",
                  start: "10:33:00",
                },
                {
                  end: "10:39:00",
                  start: "10:36:00",
                },
                {
                  end: "10:42:00",
                  start: "10:39:00",
                },
                {
                  end: "10:45:00",
                  start: "10:42:00",
                },
                {
                  end: "10:48:00",
                  start: "10:45:00",
                },
                {
                  end: "10:51:00",
                  start: "10:48:00",
                },
                {
                  end: "10:54:00",
                  start: "10:51:00",
                },
                {
                  end: "10:57:00",
                  start: "10:54:00",
                },
                {
                  end: "11:00:00",
                  start: "10:57:00",
                },
              ],
              municipi: "Torrent",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-18 08:00:00",
            pd: {
              comarca: "Osona",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Muntanyola",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-18 08:00:00",
            pd: {
              comarca: "Osona",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Vilanova de Sau",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-18 08:00:00",
            pd: {
              comarca: "Osona",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Rupit i Pruit",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-18 08:00:00",
            pd: {
              comarca: "Osona",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Sant Boi de Llu�an�s",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-18 08:00:00",
            pd: {
              comarca: "Osona",
              hores: [
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
                {
                  end: "12:36:00",
                  start: "12:30:00",
                },
                {
                  end: "12:42:00",
                  start: "12:36:00",
                },
                {
                  end: "12:48:00",
                  start: "12:42:00",
                },
                {
                  end: "12:54:00",
                  start: "12:48:00",
                },
                {
                  end: "13:00:00",
                  start: "12:54:00",
                },
              ],
              municipi: "Brull",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-18 08:00:00",
            pd: {
              comarca: "Osona",
              hores: [
                {
                  end: "13:03:00",
                  start: "13:00:00",
                },
                {
                  end: "13:06:00",
                  start: "13:03:00",
                },
                {
                  end: "13:09:00",
                  start: "13:06:00",
                },
                {
                  end: "13:12:00",
                  start: "13:09:00",
                },
                {
                  end: "13:15:00",
                  start: "13:12:00",
                },
                {
                  end: "13:18:00",
                  start: "13:15:00",
                },
                {
                  end: "13:21:00",
                  start: "13:18:00",
                },
                {
                  end: "13:24:00",
                  start: "13:21:00",
                },
                {
                  end: "13:27:00",
                  start: "13:24:00",
                },
                {
                  end: "13:30:00",
                  start: "13:27:00",
                },
              ],
              municipi: "Sora",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Osona",
              hores: [
                {
                  end: "08:03:00",
                  start: "08:00:00",
                },
                {
                  end: "08:06:00",
                  start: "08:03:00",
                },
                {
                  end: "08:09:00",
                  start: "08:06:00",
                },
                {
                  end: "08:12:00",
                  start: "08:09:00",
                },
                {
                  end: "08:15:00",
                  start: "08:12:00",
                },
                {
                  end: "08:18:00",
                  start: "08:15:00",
                },
                {
                  end: "08:21:00",
                  start: "08:18:00",
                },
                {
                  end: "08:24:00",
                  start: "08:21:00",
                },
                {
                  end: "08:27:00",
                  start: "08:24:00",
                },
                {
                  end: "08:30:00",
                  start: "08:27:00",
                },
              ],
              municipi: "Espinelves",
              temps_estimat: 30,
            },
          },
        ],
        itinerari2: [
          {
            data: "2024-06-05 08:00:00",
            pd: {
              comarca: "Alt Camp",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Aiguam�rcia",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-05 08:00:00",
            pd: {
              comarca: "Alt Camp",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Montferri",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-05 08:00:00",
            pd: {
              comarca: "Alt Camp",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Vallmoll",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-05 08:00:00",
            pd: {
              comarca: "Alt Camp",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Vilabella",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-05 08:00:00",
            pd: {
              comarca: "Alt Camp",
              hores: [
                {
                  end: "12:03:00",
                  start: "12:00:00",
                },
                {
                  end: "12:06:00",
                  start: "12:03:00",
                },
                {
                  end: "12:09:00",
                  start: "12:06:00",
                },
                {
                  end: "12:12:00",
                  start: "12:09:00",
                },
                {
                  end: "12:15:00",
                  start: "12:12:00",
                },
                {
                  end: "12:18:00",
                  start: "12:15:00",
                },
                {
                  end: "12:21:00",
                  start: "12:18:00",
                },
                {
                  end: "12:24:00",
                  start: "12:21:00",
                },
                {
                  end: "12:27:00",
                  start: "12:24:00",
                },
                {
                  end: "12:30:00",
                  start: "12:27:00",
                },
              ],
              municipi: "Garidells",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-06 08:00:00",
            pd: {
              comarca: "Conca Barb.",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Vilaverd",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-06 08:00:00",
            pd: {
              comarca: "Conca Barb.",
              hores: [
                {
                  end: "09:03:00",
                  start: "09:00:00",
                },
                {
                  end: "09:06:00",
                  start: "09:03:00",
                },
                {
                  end: "09:09:00",
                  start: "09:06:00",
                },
                {
                  end: "09:12:00",
                  start: "09:09:00",
                },
                {
                  end: "09:15:00",
                  start: "09:12:00",
                },
                {
                  end: "09:18:00",
                  start: "09:15:00",
                },
                {
                  end: "09:21:00",
                  start: "09:18:00",
                },
                {
                  end: "09:24:00",
                  start: "09:21:00",
                },
                {
                  end: "09:27:00",
                  start: "09:24:00",
                },
                {
                  end: "09:30:00",
                  start: "09:27:00",
                },
              ],
              municipi: "Vilanova de Prades",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-11 08:00:00",
            pd: {
              comarca: "Alt Empord�",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Viladamat",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-11 08:00:00",
            pd: {
              comarca: "Baix Empord�",
              hores: [
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
                {
                  end: "12:36:00",
                  start: "12:30:00",
                },
                {
                  end: "12:42:00",
                  start: "12:36:00",
                },
                {
                  end: "12:48:00",
                  start: "12:42:00",
                },
                {
                  end: "12:54:00",
                  start: "12:48:00",
                },
                {
                  end: "13:00:00",
                  start: "12:54:00",
                },
              ],
              municipi: "Cru�lles, Monells i Sant\nSadurn� de l'Heura",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-12 08:00:00",
            pd: {
              comarca: "Baix Empord�",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Rupi�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-12 08:00:00",
            pd: {
              comarca: "Baix Empord�",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Ull�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-12 08:00:00",
            pd: {
              comarca: "Baix Empord�",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Jafre",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-12 08:00:00",
            pd: {
              comarca: "Baix Empord�",
              hores: [
                {
                  end: "11:03:00",
                  start: "11:00:00",
                },
                {
                  end: "11:06:00",
                  start: "11:03:00",
                },
                {
                  end: "11:09:00",
                  start: "11:06:00",
                },
                {
                  end: "11:12:00",
                  start: "11:09:00",
                },
                {
                  end: "11:15:00",
                  start: "11:12:00",
                },
                {
                  end: "11:18:00",
                  start: "11:15:00",
                },
                {
                  end: "11:21:00",
                  start: "11:18:00",
                },
                {
                  end: "11:24:00",
                  start: "11:21:00",
                },
                {
                  end: "11:27:00",
                  start: "11:24:00",
                },
                {
                  end: "11:30:00",
                  start: "11:27:00",
                },
              ],
              municipi: "Colomers",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-12 08:00:00",
            pd: {
              comarca: "Baix Empord�",
              hores: [
                {
                  end: "11:33:00",
                  start: "11:30:00",
                },
                {
                  end: "11:36:00",
                  start: "11:33:00",
                },
                {
                  end: "11:39:00",
                  start: "11:36:00",
                },
                {
                  end: "11:42:00",
                  start: "11:39:00",
                },
                {
                  end: "11:45:00",
                  start: "11:42:00",
                },
                {
                  end: "11:48:00",
                  start: "11:45:00",
                },
                {
                  end: "11:51:00",
                  start: "11:48:00",
                },
                {
                  end: "11:54:00",
                  start: "11:51:00",
                },
                {
                  end: "11:57:00",
                  start: "11:54:00",
                },
                {
                  end: "12:00:00",
                  start: "11:57:00",
                },
              ],
              municipi: "Ultramort",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-18 08:00:00",
            pd: {
              comarca: "Osona",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Folgueroles",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-18 08:00:00",
            pd: {
              comarca: "Osona",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Sant Mart� de Centelles",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-18 08:00:00",
            pd: {
              comarca: "Osona",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Sant Bartomeu del Grau",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-18 08:00:00",
            pd: {
              comarca: "Osona",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Sant Vicen� de Torell�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-18 08:00:00",
            pd: {
              comarca: "Osona",
              hores: [
                {
                  end: "12:03:00",
                  start: "12:00:00",
                },
                {
                  end: "12:06:00",
                  start: "12:03:00",
                },
                {
                  end: "12:09:00",
                  start: "12:06:00",
                },
                {
                  end: "12:12:00",
                  start: "12:09:00",
                },
                {
                  end: "12:15:00",
                  start: "12:12:00",
                },
                {
                  end: "12:18:00",
                  start: "12:15:00",
                },
                {
                  end: "12:21:00",
                  start: "12:18:00",
                },
                {
                  end: "12:24:00",
                  start: "12:21:00",
                },
                {
                  end: "12:27:00",
                  start: "12:24:00",
                },
                {
                  end: "12:30:00",
                  start: "12:27:00",
                },
              ],
              municipi: "Santa Cec�lia de Voltreg�",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-18 08:00:00",
            pd: {
              comarca: "Osona",
              hores: [
                {
                  end: "12:33:00",
                  start: "12:30:00",
                },
                {
                  end: "12:36:00",
                  start: "12:33:00",
                },
                {
                  end: "12:39:00",
                  start: "12:36:00",
                },
                {
                  end: "12:42:00",
                  start: "12:39:00",
                },
                {
                  end: "12:45:00",
                  start: "12:42:00",
                },
                {
                  end: "12:48:00",
                  start: "12:45:00",
                },
                {
                  end: "12:51:00",
                  start: "12:48:00",
                },
                {
                  end: "12:54:00",
                  start: "12:51:00",
                },
                {
                  end: "12:57:00",
                  start: "12:54:00",
                },
                {
                  end: "13:00:00",
                  start: "12:57:00",
                },
              ],
              municipi: "Vidr�",
              temps_estimat: 30,
            },
          },
        ],
        itinerari3: [
          {
            data: "2024-06-05 08:00:00",
            pd: {
              comarca: "Alt Camp",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Cabra del Camp",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-05 08:00:00",
            pd: {
              comarca: "Alt Camp",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Rodony�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-05 08:00:00",
            pd: {
              comarca: "Alt Camp",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Ali�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-05 08:00:00",
            pd: {
              comarca: "Alt Camp",
              hores: [
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
                {
                  end: "12:36:00",
                  start: "12:30:00",
                },
                {
                  end: "12:42:00",
                  start: "12:36:00",
                },
                {
                  end: "12:48:00",
                  start: "12:42:00",
                },
                {
                  end: "12:54:00",
                  start: "12:48:00",
                },
                {
                  end: "13:00:00",
                  start: "12:54:00",
                },
              ],
              municipi: "Nulles",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-05 08:00:00",
            pd: {
              comarca: "Alt Camp",
              hores: [
                {
                  end: "13:03:00",
                  start: "13:00:00",
                },
                {
                  end: "13:06:00",
                  start: "13:03:00",
                },
                {
                  end: "13:09:00",
                  start: "13:06:00",
                },
                {
                  end: "13:12:00",
                  start: "13:09:00",
                },
                {
                  end: "13:15:00",
                  start: "13:12:00",
                },
                {
                  end: "13:18:00",
                  start: "13:15:00",
                },
                {
                  end: "13:21:00",
                  start: "13:18:00",
                },
                {
                  end: "13:24:00",
                  start: "13:21:00",
                },
                {
                  end: "13:27:00",
                  start: "13:24:00",
                },
                {
                  end: "13:30:00",
                  start: "13:27:00",
                },
              ],
              municipi: "Mil�",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-06 08:00:00",
            pd: {
              comarca: "Conca Barb.",
              hores: [
                {
                  end: "08:03:00",
                  start: "08:00:00",
                },
                {
                  end: "08:06:00",
                  start: "08:03:00",
                },
                {
                  end: "08:09:00",
                  start: "08:06:00",
                },
                {
                  end: "08:12:00",
                  start: "08:09:00",
                },
                {
                  end: "08:15:00",
                  start: "08:12:00",
                },
                {
                  end: "08:18:00",
                  start: "08:15:00",
                },
                {
                  end: "08:21:00",
                  start: "08:18:00",
                },
                {
                  end: "08:24:00",
                  start: "08:21:00",
                },
                {
                  end: "08:27:00",
                  start: "08:24:00",
                },
                {
                  end: "08:30:00",
                  start: "08:27:00",
                },
              ],
              municipi: "Senan",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-11 08:00:00",
            pd: {
              comarca: "Baix Empord�",
              hores: [
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
              ],
              municipi: "Palau-sator",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-11 08:00:00",
            pd: {
              comarca: "Baix Empord�",
              hores: [
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
              ],
              municipi: "Forallac",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-12 08:00:00",
            pd: {
              comarca: "Baix Empord�",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Cor��",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-12 08:00:00",
            pd: {
              comarca: "Baix Empord�",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Tallada d'Empord�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-12 08:00:00",
            pd: {
              comarca: "Baix Empord�",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Ullastret",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-12 08:00:00",
            pd: {
              comarca: "Baix Empord�",
              hores: [
                {
                  end: "11:03:00",
                  start: "11:00:00",
                },
                {
                  end: "11:06:00",
                  start: "11:03:00",
                },
                {
                  end: "11:09:00",
                  start: "11:06:00",
                },
                {
                  end: "11:12:00",
                  start: "11:09:00",
                },
                {
                  end: "11:15:00",
                  start: "11:12:00",
                },
                {
                  end: "11:18:00",
                  start: "11:15:00",
                },
                {
                  end: "11:21:00",
                  start: "11:18:00",
                },
                {
                  end: "11:24:00",
                  start: "11:21:00",
                },
                {
                  end: "11:27:00",
                  start: "11:24:00",
                },
                {
                  end: "11:30:00",
                  start: "11:27:00",
                },
              ],
              municipi: "Garrigoles",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-18 08:00:00",
            pd: {
              comarca: "Osona",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Santa Eug�nia de Berga",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-18 08:00:00",
            pd: {
              comarca: "Osona",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Gurb",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-18 08:00:00",
            pd: {
              comarca: "Osona",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Masies de Voltreg�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-18 08:00:00",
            pd: {
              comarca: "Osona",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Montesquiu",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-18 08:00:00",
            pd: {
              comarca: "Osona",
              hores: [
                {
                  end: "12:03:00",
                  start: "12:00:00",
                },
                {
                  end: "12:06:00",
                  start: "12:03:00",
                },
                {
                  end: "12:09:00",
                  start: "12:06:00",
                },
                {
                  end: "12:12:00",
                  start: "12:09:00",
                },
                {
                  end: "12:15:00",
                  start: "12:12:00",
                },
                {
                  end: "12:18:00",
                  start: "12:15:00",
                },
                {
                  end: "12:21:00",
                  start: "12:18:00",
                },
                {
                  end: "12:24:00",
                  start: "12:21:00",
                },
                {
                  end: "12:27:00",
                  start: "12:24:00",
                },
                {
                  end: "12:30:00",
                  start: "12:27:00",
                },
              ],
              municipi: "Tavertet",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-18 08:00:00",
            pd: {
              comarca: "Osona",
              hores: [
                {
                  end: "12:33:00",
                  start: "12:30:00",
                },
                {
                  end: "12:36:00",
                  start: "12:33:00",
                },
                {
                  end: "12:39:00",
                  start: "12:36:00",
                },
                {
                  end: "12:42:00",
                  start: "12:39:00",
                },
                {
                  end: "12:45:00",
                  start: "12:42:00",
                },
                {
                  end: "12:48:00",
                  start: "12:45:00",
                },
                {
                  end: "12:51:00",
                  start: "12:48:00",
                },
                {
                  end: "12:54:00",
                  start: "12:51:00",
                },
                {
                  end: "12:57:00",
                  start: "12:54:00",
                },
                {
                  end: "13:00:00",
                  start: "12:57:00",
                },
              ],
              municipi: "Sant Agust� de Llu�an�s",
              temps_estimat: 30,
            },
          },
        ],
        itinerari4: [
          {
            data: "2024-06-05 08:00:00",
            pd: {
              comarca: "Alt Camp",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Querol",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-05 08:00:00",
            pd: {
              comarca: "Alt Camp",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Riba",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-05 08:00:00",
            pd: {
              comarca: "Alt Camp",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Br�fim",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-05 08:00:00",
            pd: {
              comarca: "Alt Camp",
              hores: [
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
                {
                  end: "12:36:00",
                  start: "12:30:00",
                },
                {
                  end: "12:42:00",
                  start: "12:36:00",
                },
                {
                  end: "12:48:00",
                  start: "12:42:00",
                },
                {
                  end: "12:54:00",
                  start: "12:48:00",
                },
                {
                  end: "13:00:00",
                  start: "12:54:00",
                },
              ],
              municipi: "Rourell",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-05 08:00:00",
            pd: {
              comarca: "Conca Barb.",
              hores: [
                {
                  end: "13:06:00",
                  start: "13:00:00",
                },
                {
                  end: "13:12:00",
                  start: "13:06:00",
                },
                {
                  end: "13:18:00",
                  start: "13:12:00",
                },
                {
                  end: "13:24:00",
                  start: "13:18:00",
                },
                {
                  end: "13:30:00",
                  start: "13:24:00",
                },
                {
                  end: "13:36:00",
                  start: "13:30:00",
                },
                {
                  end: "13:42:00",
                  start: "13:36:00",
                },
                {
                  end: "13:48:00",
                  start: "13:42:00",
                },
                {
                  end: "13:54:00",
                  start: "13:48:00",
                },
                {
                  end: "14:00:00",
                  start: "13:54:00",
                },
              ],
              municipi: "Blancafort",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-06 08:00:00",
            pd: {
              comarca: "Conca Barb.",
              hores: [
                {
                  end: "08:03:00",
                  start: "08:00:00",
                },
                {
                  end: "08:06:00",
                  start: "08:03:00",
                },
                {
                  end: "08:09:00",
                  start: "08:06:00",
                },
                {
                  end: "08:12:00",
                  start: "08:09:00",
                },
                {
                  end: "08:15:00",
                  start: "08:12:00",
                },
                {
                  end: "08:18:00",
                  start: "08:15:00",
                },
                {
                  end: "08:21:00",
                  start: "08:18:00",
                },
                {
                  end: "08:24:00",
                  start: "08:21:00",
                },
                {
                  end: "08:27:00",
                  start: "08:24:00",
                },
                {
                  end: "08:30:00",
                  start: "08:27:00",
                },
              ],
              municipi: "Pontils",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-11 08:00:00",
            pd: {
              comarca: "Baix Empord�",
              hores: [
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
              ],
              municipi: "Regenc�s",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-11 08:00:00",
            pd: {
              comarca: "Baix Empord�",
              hores: [
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
              ],
              municipi: "Parlav�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-12 08:00:00",
            pd: {
              comarca: "Baix Empord�",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Foix�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-12 08:00:00",
            pd: {
              comarca: "Baix Empord�",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Albons",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-12 08:00:00",
            pd: {
              comarca: "Baix Empord�",
              hores: [
                {
                  end: "10:03:00",
                  start: "10:00:00",
                },
                {
                  end: "10:06:00",
                  start: "10:03:00",
                },
                {
                  end: "10:09:00",
                  start: "10:06:00",
                },
                {
                  end: "10:12:00",
                  start: "10:09:00",
                },
                {
                  end: "10:15:00",
                  start: "10:12:00",
                },
                {
                  end: "10:18:00",
                  start: "10:15:00",
                },
                {
                  end: "10:21:00",
                  start: "10:18:00",
                },
                {
                  end: "10:24:00",
                  start: "10:21:00",
                },
                {
                  end: "10:27:00",
                  start: "10:24:00",
                },
                {
                  end: "10:30:00",
                  start: "10:27:00",
                },
              ],
              municipi: "Fontanilles",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-12 08:00:00",
            pd: {
              comarca: "Baix Empord�",
              hores: [
                {
                  end: "10:33:00",
                  start: "10:30:00",
                },
                {
                  end: "10:36:00",
                  start: "10:33:00",
                },
                {
                  end: "10:39:00",
                  start: "10:36:00",
                },
                {
                  end: "10:42:00",
                  start: "10:39:00",
                },
                {
                  end: "10:45:00",
                  start: "10:42:00",
                },
                {
                  end: "10:48:00",
                  start: "10:45:00",
                },
                {
                  end: "10:51:00",
                  start: "10:48:00",
                },
                {
                  end: "10:54:00",
                  start: "10:51:00",
                },
                {
                  end: "10:57:00",
                  start: "10:54:00",
                },
                {
                  end: "11:00:00",
                  start: "10:57:00",
                },
              ],
              municipi: "Vilopriu",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-17 08:00:00",
            pd: {
              comarca: "Osona",
              hores: [
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
                {
                  end: "12:36:00",
                  start: "12:30:00",
                },
                {
                  end: "12:42:00",
                  start: "12:36:00",
                },
                {
                  end: "12:48:00",
                  start: "12:42:00",
                },
                {
                  end: "12:54:00",
                  start: "12:48:00",
                },
                {
                  end: "13:00:00",
                  start: "12:54:00",
                },
              ],
              municipi: "Malla",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-18 08:00:00",
            pd: {
              comarca: "Osona",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Santa Eul�lia de Riuprimer",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-18 08:00:00",
            pd: {
              comarca: "Osona",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Masies de Roda",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-18 08:00:00",
            pd: {
              comarca: "Osona",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Or�s",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-18 08:00:00",
            pd: {
              comarca: "Osona",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Tav�rnoles",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-18 08:00:00",
            pd: {
              comarca: "Osona",
              hores: [
                {
                  end: "12:03:00",
                  start: "12:00:00",
                },
                {
                  end: "12:06:00",
                  start: "12:03:00",
                },
                {
                  end: "12:09:00",
                  start: "12:06:00",
                },
                {
                  end: "12:12:00",
                  start: "12:09:00",
                },
                {
                  end: "12:15:00",
                  start: "12:12:00",
                },
                {
                  end: "12:18:00",
                  start: "12:15:00",
                },
                {
                  end: "12:21:00",
                  start: "12:18:00",
                },
                {
                  end: "12:24:00",
                  start: "12:21:00",
                },
                {
                  end: "12:27:00",
                  start: "12:24:00",
                },
                {
                  end: "12:30:00",
                  start: "12:27:00",
                },
              ],
              municipi: "Santa Maria de Besora",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Osona",
              hores: [
                {
                  end: "08:03:00",
                  start: "08:00:00",
                },
                {
                  end: "08:06:00",
                  start: "08:03:00",
                },
                {
                  end: "08:09:00",
                  start: "08:06:00",
                },
                {
                  end: "08:12:00",
                  start: "08:09:00",
                },
                {
                  end: "08:15:00",
                  start: "08:12:00",
                },
                {
                  end: "08:18:00",
                  start: "08:15:00",
                },
                {
                  end: "08:21:00",
                  start: "08:18:00",
                },
                {
                  end: "08:24:00",
                  start: "08:21:00",
                },
                {
                  end: "08:27:00",
                  start: "08:24:00",
                },
                {
                  end: "08:30:00",
                  start: "08:27:00",
                },
              ],
              municipi: "Sant Sadurn� d'Osormort",
              temps_estimat: 30,
            },
          },
        ],
      },
      {
        itinerari1: [
          {
            data: "2024-06-06 08:00:00",
            pd: {
              comarca: "Baix Camp",
              hores: [
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
              ],
              municipi: "Riudecanyes",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-06 08:00:00",
            pd: {
              comarca: "Baix Camp",
              hores: [
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
              ],
              municipi: "Maspujols",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-06 08:00:00",
            pd: {
              comarca: "Baix Camp",
              hores: [
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
              ],
              municipi: "Almoster",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-06 08:00:00",
            pd: {
              comarca: "Baix Camp",
              hores: [
                {
                  end: "12:33:00",
                  start: "12:30:00",
                },
                {
                  end: "12:36:00",
                  start: "12:33:00",
                },
                {
                  end: "12:39:00",
                  start: "12:36:00",
                },
                {
                  end: "12:42:00",
                  start: "12:39:00",
                },
                {
                  end: "12:45:00",
                  start: "12:42:00",
                },
                {
                  end: "12:48:00",
                  start: "12:45:00",
                },
                {
                  end: "12:51:00",
                  start: "12:48:00",
                },
                {
                  end: "12:54:00",
                  start: "12:51:00",
                },
                {
                  end: "12:57:00",
                  start: "12:54:00",
                },
                {
                  end: "13:00:00",
                  start: "12:57:00",
                },
              ],
              municipi: "Arbol�",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-06 08:00:00",
            pd: {
              comarca: "Tarragon�s",
              hores: [
                {
                  end: "13:06:00",
                  start: "13:00:00",
                },
                {
                  end: "13:12:00",
                  start: "13:06:00",
                },
                {
                  end: "13:18:00",
                  start: "13:12:00",
                },
                {
                  end: "13:24:00",
                  start: "13:18:00",
                },
                {
                  end: "13:30:00",
                  start: "13:24:00",
                },
                {
                  end: "13:36:00",
                  start: "13:30:00",
                },
                {
                  end: "13:42:00",
                  start: "13:36:00",
                },
                {
                  end: "13:48:00",
                  start: "13:42:00",
                },
                {
                  end: "13:54:00",
                  start: "13:48:00",
                },
                {
                  end: "14:00:00",
                  start: "13:54:00",
                },
              ],
              municipi: "Pobla de Mafumet",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-07 08:00:00",
            pd: {
              comarca: "Tarragon�s",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Catllar",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-12 08:00:00",
            pd: {
              comarca: "Giron�s",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Aiguaviva",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-12 08:00:00",
            pd: {
              comarca: "Giron�s",
              hores: [
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
                {
                  end: "12:36:00",
                  start: "12:30:00",
                },
                {
                  end: "12:42:00",
                  start: "12:36:00",
                },
                {
                  end: "12:48:00",
                  start: "12:42:00",
                },
                {
                  end: "12:54:00",
                  start: "12:48:00",
                },
                {
                  end: "13:00:00",
                  start: "12:54:00",
                },
              ],
              municipi: "Madremanya",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-13 08:00:00",
            pd: {
              comarca: "Giron�s",
              hores: [
                {
                  end: "08:03:00",
                  start: "08:00:00",
                },
                {
                  end: "08:06:00",
                  start: "08:03:00",
                },
                {
                  end: "08:09:00",
                  start: "08:06:00",
                },
                {
                  end: "08:12:00",
                  start: "08:09:00",
                },
                {
                  end: "08:15:00",
                  start: "08:12:00",
                },
                {
                  end: "08:18:00",
                  start: "08:15:00",
                },
                {
                  end: "08:21:00",
                  start: "08:18:00",
                },
                {
                  end: "08:24:00",
                  start: "08:21:00",
                },
                {
                  end: "08:27:00",
                  start: "08:24:00",
                },
                {
                  end: "08:30:00",
                  start: "08:27:00",
                },
              ],
              municipi: "Sant Andreu Salou",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-13 08:00:00",
            pd: {
              comarca: "Pla Estany",
              hores: [
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
              ],
              municipi: "Vilademuls",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-13 08:00:00",
            pd: {
              comarca: "Pla Estany",
              hores: [
                {
                  end: "09:33:00",
                  start: "09:30:00",
                },
                {
                  end: "09:36:00",
                  start: "09:33:00",
                },
                {
                  end: "09:39:00",
                  start: "09:36:00",
                },
                {
                  end: "09:42:00",
                  start: "09:39:00",
                },
                {
                  end: "09:45:00",
                  start: "09:42:00",
                },
                {
                  end: "09:48:00",
                  start: "09:45:00",
                },
                {
                  end: "09:51:00",
                  start: "09:48:00",
                },
                {
                  end: "09:54:00",
                  start: "09:51:00",
                },
                {
                  end: "09:57:00",
                  start: "09:54:00",
                },
                {
                  end: "10:00:00",
                  start: "09:57:00",
                },
              ],
              municipi: "Sant Miquel de\nCampmajor",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-13 08:00:00",
            pd: {
              comarca: "Selva",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Osor",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Bergued�",
              hores: [
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
              ],
              municipi: "Vallcebre",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Bergued�",
              hores: [
                {
                  end: "09:33:00",
                  start: "09:30:00",
                },
                {
                  end: "09:36:00",
                  start: "09:33:00",
                },
                {
                  end: "09:39:00",
                  start: "09:36:00",
                },
                {
                  end: "09:42:00",
                  start: "09:39:00",
                },
                {
                  end: "09:45:00",
                  start: "09:42:00",
                },
                {
                  end: "09:48:00",
                  start: "09:45:00",
                },
                {
                  end: "09:51:00",
                  start: "09:48:00",
                },
                {
                  end: "09:54:00",
                  start: "09:51:00",
                },
                {
                  end: "09:57:00",
                  start: "09:54:00",
                },
                {
                  end: "10:00:00",
                  start: "09:57:00",
                },
              ],
              municipi: "Castellar del Riu",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Bergued�",
              hores: [
                {
                  end: "10:03:00",
                  start: "10:00:00",
                },
                {
                  end: "10:06:00",
                  start: "10:03:00",
                },
                {
                  end: "10:09:00",
                  start: "10:06:00",
                },
                {
                  end: "10:12:00",
                  start: "10:09:00",
                },
                {
                  end: "10:15:00",
                  start: "10:12:00",
                },
                {
                  end: "10:18:00",
                  start: "10:15:00",
                },
                {
                  end: "10:21:00",
                  start: "10:18:00",
                },
                {
                  end: "10:24:00",
                  start: "10:21:00",
                },
                {
                  end: "10:27:00",
                  start: "10:24:00",
                },
                {
                  end: "10:30:00",
                  start: "10:27:00",
                },
              ],
              municipi: "Castell de l'Areny",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Bergued�",
              hores: [
                {
                  end: "10:33:00",
                  start: "10:30:00",
                },
                {
                  end: "10:36:00",
                  start: "10:33:00",
                },
                {
                  end: "10:39:00",
                  start: "10:36:00",
                },
                {
                  end: "10:42:00",
                  start: "10:39:00",
                },
                {
                  end: "10:45:00",
                  start: "10:42:00",
                },
                {
                  end: "10:48:00",
                  start: "10:45:00",
                },
                {
                  end: "10:51:00",
                  start: "10:48:00",
                },
                {
                  end: "10:54:00",
                  start: "10:51:00",
                },
                {
                  end: "10:57:00",
                  start: "10:54:00",
                },
                {
                  end: "11:00:00",
                  start: "10:57:00",
                },
              ],
              municipi: "G�sol",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Ripoll�s",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Moll�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Ripoll�s",
              hores: [
                {
                  end: "12:03:00",
                  start: "12:00:00",
                },
                {
                  end: "12:06:00",
                  start: "12:03:00",
                },
                {
                  end: "12:09:00",
                  start: "12:06:00",
                },
                {
                  end: "12:12:00",
                  start: "12:09:00",
                },
                {
                  end: "12:15:00",
                  start: "12:12:00",
                },
                {
                  end: "12:18:00",
                  start: "12:15:00",
                },
                {
                  end: "12:21:00",
                  start: "12:18:00",
                },
                {
                  end: "12:24:00",
                  start: "12:21:00",
                },
                {
                  end: "12:27:00",
                  start: "12:24:00",
                },
                {
                  end: "12:30:00",
                  start: "12:27:00",
                },
              ],
              municipi: "Campelles",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Ripoll�s",
              hores: [
                {
                  end: "12:33:00",
                  start: "12:30:00",
                },
                {
                  end: "12:36:00",
                  start: "12:33:00",
                },
                {
                  end: "12:39:00",
                  start: "12:36:00",
                },
                {
                  end: "12:42:00",
                  start: "12:39:00",
                },
                {
                  end: "12:45:00",
                  start: "12:42:00",
                },
                {
                  end: "12:48:00",
                  start: "12:45:00",
                },
                {
                  end: "12:51:00",
                  start: "12:48:00",
                },
                {
                  end: "12:54:00",
                  start: "12:51:00",
                },
                {
                  end: "12:57:00",
                  start: "12:54:00",
                },
                {
                  end: "13:00:00",
                  start: "12:57:00",
                },
              ],
              municipi: "Ogassa",
              temps_estimat: 30,
            },
          },
        ],
        itinerari2: [
          {
            data: "2024-06-06 08:00:00",
            pd: {
              comarca: "Baix Camp",
              hores: [
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
              ],
              municipi: "Vilanova d'Escornalbou",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-06 08:00:00",
            pd: {
              comarca: "Baix Camp",
              hores: [
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
              ],
              municipi: "Riudecols",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-06 08:00:00",
            pd: {
              comarca: "Baix Camp",
              hores: [
                {
                  end: "11:33:00",
                  start: "11:30:00",
                },
                {
                  end: "11:36:00",
                  start: "11:33:00",
                },
                {
                  end: "11:39:00",
                  start: "11:36:00",
                },
                {
                  end: "11:42:00",
                  start: "11:39:00",
                },
                {
                  end: "11:45:00",
                  start: "11:42:00",
                },
                {
                  end: "11:48:00",
                  start: "11:45:00",
                },
                {
                  end: "11:51:00",
                  start: "11:48:00",
                },
                {
                  end: "11:54:00",
                  start: "11:51:00",
                },
                {
                  end: "11:57:00",
                  start: "11:54:00",
                },
                {
                  end: "12:00:00",
                  start: "11:57:00",
                },
              ],
              municipi: "Argentera",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-06 08:00:00",
            pd: {
              comarca: "Baix Camp",
              hores: [
                {
                  end: "12:03:00",
                  start: "12:00:00",
                },
                {
                  end: "12:06:00",
                  start: "12:03:00",
                },
                {
                  end: "12:09:00",
                  start: "12:06:00",
                },
                {
                  end: "12:12:00",
                  start: "12:09:00",
                },
                {
                  end: "12:15:00",
                  start: "12:12:00",
                },
                {
                  end: "12:18:00",
                  start: "12:15:00",
                },
                {
                  end: "12:21:00",
                  start: "12:18:00",
                },
                {
                  end: "12:24:00",
                  start: "12:21:00",
                },
                {
                  end: "12:27:00",
                  start: "12:24:00",
                },
                {
                  end: "12:30:00",
                  start: "12:27:00",
                },
              ],
              municipi: "Capafonts",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-07 08:00:00",
            pd: {
              comarca: "Tarragon�s",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Vilallonga del Camp",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-07 08:00:00",
            pd: {
              comarca: "Tarragon�s",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Secuita",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-12 08:00:00",
            pd: {
              comarca: "Giron�s",
              hores: [
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
                {
                  end: "12:36:00",
                  start: "12:30:00",
                },
                {
                  end: "12:42:00",
                  start: "12:36:00",
                },
                {
                  end: "12:48:00",
                  start: "12:42:00",
                },
                {
                  end: "12:54:00",
                  start: "12:48:00",
                },
                {
                  end: "13:00:00",
                  start: "12:54:00",
                },
              ],
              municipi: "Sant Mart� de Ll�mena",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-13 08:00:00",
            pd: {
              comarca: "Giron�s",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Sant Mart� Vell",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-13 08:00:00",
            pd: {
              comarca: "Giron�s",
              hores: [
                {
                  end: "09:03:00",
                  start: "09:00:00",
                },
                {
                  end: "09:06:00",
                  start: "09:03:00",
                },
                {
                  end: "09:09:00",
                  start: "09:06:00",
                },
                {
                  end: "09:12:00",
                  start: "09:09:00",
                },
                {
                  end: "09:15:00",
                  start: "09:12:00",
                },
                {
                  end: "09:18:00",
                  start: "09:15:00",
                },
                {
                  end: "09:21:00",
                  start: "09:18:00",
                },
                {
                  end: "09:24:00",
                  start: "09:21:00",
                },
                {
                  end: "09:27:00",
                  start: "09:24:00",
                },
                {
                  end: "09:30:00",
                  start: "09:27:00",
                },
              ],
              municipi: "Viladasens",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-13 08:00:00",
            pd: {
              comarca: "Pla Estany",
              hores: [
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
              ],
              municipi: "Crespi�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-13 08:00:00",
            pd: {
              comarca: "Selva",
              hores: [
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
              ],
              municipi: "Massanes",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-13 08:00:00",
            pd: {
              comarca: "Selva",
              hores: [
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
              ],
              municipi: "Fogars de la Selva",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Bergued�",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Espunyola",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Bergued�",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Saldes",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Bergued�",
              hores: [
                {
                  end: "10:03:00",
                  start: "10:00:00",
                },
                {
                  end: "10:06:00",
                  start: "10:03:00",
                },
                {
                  end: "10:09:00",
                  start: "10:06:00",
                },
                {
                  end: "10:12:00",
                  start: "10:09:00",
                },
                {
                  end: "10:15:00",
                  start: "10:12:00",
                },
                {
                  end: "10:18:00",
                  start: "10:15:00",
                },
                {
                  end: "10:21:00",
                  start: "10:18:00",
                },
                {
                  end: "10:24:00",
                  start: "10:21:00",
                },
                {
                  end: "10:27:00",
                  start: "10:24:00",
                },
                {
                  end: "10:30:00",
                  start: "10:27:00",
                },
              ],
              municipi: "F�gols",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Bergued�",
              hores: [
                {
                  end: "10:33:00",
                  start: "10:30:00",
                },
                {
                  end: "10:36:00",
                  start: "10:33:00",
                },
                {
                  end: "10:39:00",
                  start: "10:36:00",
                },
                {
                  end: "10:42:00",
                  start: "10:39:00",
                },
                {
                  end: "10:45:00",
                  start: "10:42:00",
                },
                {
                  end: "10:48:00",
                  start: "10:45:00",
                },
                {
                  end: "10:51:00",
                  start: "10:48:00",
                },
                {
                  end: "10:54:00",
                  start: "10:51:00",
                },
                {
                  end: "10:57:00",
                  start: "10:54:00",
                },
                {
                  end: "11:00:00",
                  start: "10:57:00",
                },
              ],
              municipi: "Sant Jaume de Frontany�",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Bergued�",
              hores: [
                {
                  end: "11:03:00",
                  start: "11:00:00",
                },
                {
                  end: "11:06:00",
                  start: "11:03:00",
                },
                {
                  end: "11:09:00",
                  start: "11:06:00",
                },
                {
                  end: "11:12:00",
                  start: "11:09:00",
                },
                {
                  end: "11:15:00",
                  start: "11:12:00",
                },
                {
                  end: "11:18:00",
                  start: "11:15:00",
                },
                {
                  end: "11:21:00",
                  start: "11:18:00",
                },
                {
                  end: "11:24:00",
                  start: "11:21:00",
                },
                {
                  end: "11:27:00",
                  start: "11:24:00",
                },
                {
                  end: "11:30:00",
                  start: "11:27:00",
                },
              ],
              municipi: "Castellar de n'Hug",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Ripoll�s",
              hores: [
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
              ],
              municipi: "Vilallonga de Ter",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Ripoll�s",
              hores: [
                {
                  end: "12:33:00",
                  start: "12:30:00",
                },
                {
                  end: "12:36:00",
                  start: "12:33:00",
                },
                {
                  end: "12:39:00",
                  start: "12:36:00",
                },
                {
                  end: "12:42:00",
                  start: "12:39:00",
                },
                {
                  end: "12:45:00",
                  start: "12:42:00",
                },
                {
                  end: "12:48:00",
                  start: "12:45:00",
                },
                {
                  end: "12:51:00",
                  start: "12:48:00",
                },
                {
                  end: "12:54:00",
                  start: "12:51:00",
                },
                {
                  end: "12:57:00",
                  start: "12:54:00",
                },
                {
                  end: "13:00:00",
                  start: "12:57:00",
                },
              ],
              municipi: "Gombr�n",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Ripoll�s",
              hores: [
                {
                  end: "13:03:00",
                  start: "13:00:00",
                },
                {
                  end: "13:06:00",
                  start: "13:03:00",
                },
                {
                  end: "13:09:00",
                  start: "13:06:00",
                },
                {
                  end: "13:12:00",
                  start: "13:09:00",
                },
                {
                  end: "13:15:00",
                  start: "13:12:00",
                },
                {
                  end: "13:18:00",
                  start: "13:15:00",
                },
                {
                  end: "13:21:00",
                  start: "13:18:00",
                },
                {
                  end: "13:24:00",
                  start: "13:21:00",
                },
                {
                  end: "13:27:00",
                  start: "13:24:00",
                },
                {
                  end: "13:30:00",
                  start: "13:27:00",
                },
              ],
              municipi: "Pardines",
              temps_estimat: 30,
            },
          },
        ],
        itinerari3: [
          {
            data: "2024-06-06 08:00:00",
            pd: {
              comarca: "Baix Camp",
              hores: [
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
              ],
              municipi: "Botarell",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-06 08:00:00",
            pd: {
              comarca: "Baix Camp",
              hores: [
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
              ],
              municipi: "Aleixar",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-06 08:00:00",
            pd: {
              comarca: "Baix Camp",
              hores: [
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
              ],
              municipi: "Vilaplana",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-06 08:00:00",
            pd: {
              comarca: "Baix Camp",
              hores: [
                {
                  end: "11:33:00",
                  start: "11:30:00",
                },
                {
                  end: "11:36:00",
                  start: "11:33:00",
                },
                {
                  end: "11:39:00",
                  start: "11:36:00",
                },
                {
                  end: "11:42:00",
                  start: "11:39:00",
                },
                {
                  end: "11:45:00",
                  start: "11:42:00",
                },
                {
                  end: "11:48:00",
                  start: "11:45:00",
                },
                {
                  end: "11:51:00",
                  start: "11:48:00",
                },
                {
                  end: "11:54:00",
                  start: "11:51:00",
                },
                {
                  end: "11:57:00",
                  start: "11:54:00",
                },
                {
                  end: "12:00:00",
                  start: "11:57:00",
                },
              ],
              municipi: "Colldejou",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-06 08:00:00",
            pd: {
              comarca: "Baix Camp",
              hores: [
                {
                  end: "12:03:00",
                  start: "12:00:00",
                },
                {
                  end: "12:06:00",
                  start: "12:03:00",
                },
                {
                  end: "12:09:00",
                  start: "12:06:00",
                },
                {
                  end: "12:12:00",
                  start: "12:09:00",
                },
                {
                  end: "12:15:00",
                  start: "12:12:00",
                },
                {
                  end: "12:18:00",
                  start: "12:15:00",
                },
                {
                  end: "12:21:00",
                  start: "12:18:00",
                },
                {
                  end: "12:24:00",
                  start: "12:21:00",
                },
                {
                  end: "12:27:00",
                  start: "12:24:00",
                },
                {
                  end: "12:30:00",
                  start: "12:27:00",
                },
              ],
              municipi: "Febr�",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-07 08:00:00",
            pd: {
              comarca: "Tarragon�s",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Nou de Gai�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-07 08:00:00",
            pd: {
              comarca: "Tarragon�s",
              hores: [
                {
                  end: "09:03:00",
                  start: "09:00:00",
                },
                {
                  end: "09:06:00",
                  start: "09:03:00",
                },
                {
                  end: "09:09:00",
                  start: "09:06:00",
                },
                {
                  end: "09:12:00",
                  start: "09:09:00",
                },
                {
                  end: "09:15:00",
                  start: "09:12:00",
                },
                {
                  end: "09:18:00",
                  start: "09:15:00",
                },
                {
                  end: "09:21:00",
                  start: "09:18:00",
                },
                {
                  end: "09:24:00",
                  start: "09:21:00",
                },
                {
                  end: "09:27:00",
                  start: "09:24:00",
                },
                {
                  end: "09:30:00",
                  start: "09:27:00",
                },
              ],
              municipi: "Renau",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-12 08:00:00",
            pd: {
              comarca: "Giron�s",
              hores: [
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
              ],
              municipi: "Campllong",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-12 08:00:00",
            pd: {
              comarca: "Giron�s",
              hores: [
                {
                  end: "12:36:00",
                  start: "12:30:00",
                },
                {
                  end: "12:42:00",
                  start: "12:36:00",
                },
                {
                  end: "12:48:00",
                  start: "12:42:00",
                },
                {
                  end: "12:54:00",
                  start: "12:48:00",
                },
                {
                  end: "13:00:00",
                  start: "12:54:00",
                },
                {
                  end: "13:06:00",
                  start: "13:00:00",
                },
                {
                  end: "13:12:00",
                  start: "13:06:00",
                },
                {
                  end: "13:18:00",
                  start: "13:12:00",
                },
                {
                  end: "13:24:00",
                  start: "13:18:00",
                },
                {
                  end: "13:30:00",
                  start: "13:24:00",
                },
              ],
              municipi: "Canet d'Adri",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-13 08:00:00",
            pd: {
              comarca: "Giron�s",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Cervi� de Ter",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-13 08:00:00",
            pd: {
              comarca: "Pla Estany",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Cam�s",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-13 08:00:00",
            pd: {
              comarca: "Pla Estany",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Esponell�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-13 08:00:00",
            pd: {
              comarca: "Selva",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Sant Feliu de Buixalleu",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-13 08:00:00",
            pd: {
              comarca: "Selva",
              hores: [
                {
                  end: "12:03:00",
                  start: "12:00:00",
                },
                {
                  end: "12:06:00",
                  start: "12:03:00",
                },
                {
                  end: "12:09:00",
                  start: "12:06:00",
                },
                {
                  end: "12:12:00",
                  start: "12:09:00",
                },
                {
                  end: "12:15:00",
                  start: "12:12:00",
                },
                {
                  end: "12:18:00",
                  start: "12:15:00",
                },
                {
                  end: "12:21:00",
                  start: "12:18:00",
                },
                {
                  end: "12:24:00",
                  start: "12:21:00",
                },
                {
                  end: "12:27:00",
                  start: "12:24:00",
                },
                {
                  end: "12:30:00",
                  start: "12:27:00",
                },
              ],
              municipi: "Susqueda",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Bergued�",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Vilada",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Bergued�",
              hores: [
                {
                  end: "09:03:00",
                  start: "09:00:00",
                },
                {
                  end: "09:06:00",
                  start: "09:03:00",
                },
                {
                  end: "09:09:00",
                  start: "09:06:00",
                },
                {
                  end: "09:12:00",
                  start: "09:09:00",
                },
                {
                  end: "09:15:00",
                  start: "09:12:00",
                },
                {
                  end: "09:18:00",
                  start: "09:15:00",
                },
                {
                  end: "09:21:00",
                  start: "09:18:00",
                },
                {
                  end: "09:24:00",
                  start: "09:21:00",
                },
                {
                  end: "09:27:00",
                  start: "09:24:00",
                },
                {
                  end: "09:30:00",
                  start: "09:27:00",
                },
              ],
              municipi: "Montclar",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Bergued�",
              hores: [
                {
                  end: "09:33:00",
                  start: "09:30:00",
                },
                {
                  end: "09:36:00",
                  start: "09:33:00",
                },
                {
                  end: "09:39:00",
                  start: "09:36:00",
                },
                {
                  end: "09:42:00",
                  start: "09:39:00",
                },
                {
                  end: "09:45:00",
                  start: "09:42:00",
                },
                {
                  end: "09:48:00",
                  start: "09:45:00",
                },
                {
                  end: "09:51:00",
                  start: "09:48:00",
                },
                {
                  end: "09:54:00",
                  start: "09:51:00",
                },
                {
                  end: "09:57:00",
                  start: "09:54:00",
                },
                {
                  end: "10:00:00",
                  start: "09:57:00",
                },
              ],
              municipi: "Nou de Bergued�",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Bergued�",
              hores: [
                {
                  end: "10:03:00",
                  start: "10:00:00",
                },
                {
                  end: "10:06:00",
                  start: "10:03:00",
                },
                {
                  end: "10:09:00",
                  start: "10:06:00",
                },
                {
                  end: "10:12:00",
                  start: "10:09:00",
                },
                {
                  end: "10:15:00",
                  start: "10:12:00",
                },
                {
                  end: "10:18:00",
                  start: "10:15:00",
                },
                {
                  end: "10:21:00",
                  start: "10:18:00",
                },
                {
                  end: "10:24:00",
                  start: "10:21:00",
                },
                {
                  end: "10:27:00",
                  start: "10:24:00",
                },
                {
                  end: "10:30:00",
                  start: "10:27:00",
                },
              ],
              municipi: "Sant Juli� de Cerdanyola",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Ripoll�s",
              hores: [
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
              ],
              municipi: "Planoles",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Ripoll�s",
              hores: [
                {
                  end: "11:33:00",
                  start: "11:30:00",
                },
                {
                  end: "11:36:00",
                  start: "11:33:00",
                },
                {
                  end: "11:39:00",
                  start: "11:36:00",
                },
                {
                  end: "11:42:00",
                  start: "11:39:00",
                },
                {
                  end: "11:45:00",
                  start: "11:42:00",
                },
                {
                  end: "11:48:00",
                  start: "11:45:00",
                },
                {
                  end: "11:51:00",
                  start: "11:48:00",
                },
                {
                  end: "11:54:00",
                  start: "11:51:00",
                },
                {
                  end: "11:57:00",
                  start: "11:54:00",
                },
                {
                  end: "12:00:00",
                  start: "11:57:00",
                },
              ],
              municipi: "Llosses",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Ripoll�s",
              hores: [
                {
                  end: "12:03:00",
                  start: "12:00:00",
                },
                {
                  end: "12:06:00",
                  start: "12:03:00",
                },
                {
                  end: "12:09:00",
                  start: "12:06:00",
                },
                {
                  end: "12:12:00",
                  start: "12:09:00",
                },
                {
                  end: "12:15:00",
                  start: "12:12:00",
                },
                {
                  end: "12:18:00",
                  start: "12:15:00",
                },
                {
                  end: "12:21:00",
                  start: "12:18:00",
                },
                {
                  end: "12:24:00",
                  start: "12:21:00",
                },
                {
                  end: "12:27:00",
                  start: "12:24:00",
                },
                {
                  end: "12:30:00",
                  start: "12:27:00",
                },
              ],
              municipi: "Toses",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-20 08:00:00",
            pd: {
              comarca: "Ripoll�s",
              hores: [
                {
                  end: "08:03:00",
                  start: "08:00:00",
                },
                {
                  end: "08:06:00",
                  start: "08:03:00",
                },
                {
                  end: "08:09:00",
                  start: "08:06:00",
                },
                {
                  end: "08:12:00",
                  start: "08:09:00",
                },
                {
                  end: "08:15:00",
                  start: "08:12:00",
                },
                {
                  end: "08:18:00",
                  start: "08:15:00",
                },
                {
                  end: "08:21:00",
                  start: "08:18:00",
                },
                {
                  end: "08:24:00",
                  start: "08:21:00",
                },
                {
                  end: "08:27:00",
                  start: "08:24:00",
                },
                {
                  end: "08:30:00",
                  start: "08:27:00",
                },
              ],
              municipi: "Queralbs",
              temps_estimat: 30,
            },
          },
        ],
        itinerari4: [
          {
            data: "2024-06-06 08:00:00",
            pd: {
              comarca: "Baix Camp",
              hores: [
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
              ],
              municipi: "Pratdip",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-06 08:00:00",
            pd: {
              comarca: "Baix Camp",
              hores: [
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
              ],
              municipi: "Alforja",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-06 08:00:00",
            pd: {
              comarca: "Baix Camp",
              hores: [
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
              ],
              municipi: "Albiol",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-06 08:00:00",
            pd: {
              comarca: "Baix Camp",
              hores: [
                {
                  end: "11:33:00",
                  start: "11:30:00",
                },
                {
                  end: "11:36:00",
                  start: "11:33:00",
                },
                {
                  end: "11:39:00",
                  start: "11:36:00",
                },
                {
                  end: "11:42:00",
                  start: "11:39:00",
                },
                {
                  end: "11:45:00",
                  start: "11:42:00",
                },
                {
                  end: "11:48:00",
                  start: "11:45:00",
                },
                {
                  end: "11:51:00",
                  start: "11:48:00",
                },
                {
                  end: "11:54:00",
                  start: "11:51:00",
                },
                {
                  end: "11:57:00",
                  start: "11:54:00",
                },
                {
                  end: "12:00:00",
                  start: "11:57:00",
                },
              ],
              municipi: "Duesaig�es",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-06 08:00:00",
            pd: {
              comarca: "Tarragon�s",
              hores: [
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
                {
                  end: "12:36:00",
                  start: "12:30:00",
                },
                {
                  end: "12:42:00",
                  start: "12:36:00",
                },
                {
                  end: "12:48:00",
                  start: "12:42:00",
                },
                {
                  end: "12:54:00",
                  start: "12:48:00",
                },
                {
                  end: "13:00:00",
                  start: "12:54:00",
                },
              ],
              municipi: "Perafort",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-07 08:00:00",
            pd: {
              comarca: "Tarragon�s",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Riera de Gai�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-12 08:00:00",
            pd: {
              comarca: "Giron�s",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Llambilles",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-12 08:00:00",
            pd: {
              comarca: "Giron�s",
              hores: [
                {
                  end: "12:06:00",
                  start: "12:00:00",
                },
                {
                  end: "12:12:00",
                  start: "12:06:00",
                },
                {
                  end: "12:18:00",
                  start: "12:12:00",
                },
                {
                  end: "12:24:00",
                  start: "12:18:00",
                },
                {
                  end: "12:30:00",
                  start: "12:24:00",
                },
                {
                  end: "12:36:00",
                  start: "12:30:00",
                },
                {
                  end: "12:42:00",
                  start: "12:36:00",
                },
                {
                  end: "12:48:00",
                  start: "12:42:00",
                },
                {
                  end: "12:54:00",
                  start: "12:48:00",
                },
                {
                  end: "13:00:00",
                  start: "12:54:00",
                },
              ],
              municipi: "Jui�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-13 08:00:00",
            pd: {
              comarca: "Giron�s",
              hores: [
                {
                  end: "08:06:00",
                  start: "08:00:00",
                },
                {
                  end: "08:12:00",
                  start: "08:06:00",
                },
                {
                  end: "08:18:00",
                  start: "08:12:00",
                },
                {
                  end: "08:24:00",
                  start: "08:18:00",
                },
                {
                  end: "08:30:00",
                  start: "08:24:00",
                },
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
              ],
              municipi: "Sant Joan de Mollet",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-13 08:00:00",
            pd: {
              comarca: "Pla Estany",
              hores: [
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
                {
                  end: "09:36:00",
                  start: "09:30:00",
                },
                {
                  end: "09:42:00",
                  start: "09:36:00",
                },
                {
                  end: "09:48:00",
                  start: "09:42:00",
                },
                {
                  end: "09:54:00",
                  start: "09:48:00",
                },
                {
                  end: "10:00:00",
                  start: "09:54:00",
                },
              ],
              municipi: "Palol de Revardit",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-13 08:00:00",
            pd: {
              comarca: "Pla Estany",
              hores: [
                {
                  end: "10:06:00",
                  start: "10:00:00",
                },
                {
                  end: "10:12:00",
                  start: "10:06:00",
                },
                {
                  end: "10:18:00",
                  start: "10:12:00",
                },
                {
                  end: "10:24:00",
                  start: "10:18:00",
                },
                {
                  end: "10:30:00",
                  start: "10:24:00",
                },
                {
                  end: "10:36:00",
                  start: "10:30:00",
                },
                {
                  end: "10:42:00",
                  start: "10:36:00",
                },
                {
                  end: "10:48:00",
                  start: "10:42:00",
                },
                {
                  end: "10:54:00",
                  start: "10:48:00",
                },
                {
                  end: "11:00:00",
                  start: "10:54:00",
                },
              ],
              municipi: "Fontcoberta",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-13 08:00:00",
            pd: {
              comarca: "Selva",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Brunyola i Sant Mart� Sapresa",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Bergued�",
              hores: [
                {
                  end: "08:36:00",
                  start: "08:30:00",
                },
                {
                  end: "08:42:00",
                  start: "08:36:00",
                },
                {
                  end: "08:48:00",
                  start: "08:42:00",
                },
                {
                  end: "08:54:00",
                  start: "08:48:00",
                },
                {
                  end: "09:00:00",
                  start: "08:54:00",
                },
                {
                  end: "09:06:00",
                  start: "09:00:00",
                },
                {
                  end: "09:12:00",
                  start: "09:06:00",
                },
                {
                  end: "09:18:00",
                  start: "09:12:00",
                },
                {
                  end: "09:24:00",
                  start: "09:18:00",
                },
                {
                  end: "09:30:00",
                  start: "09:24:00",
                },
              ],
              municipi: "Borred�",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Bergued�",
              hores: [
                {
                  end: "09:33:00",
                  start: "09:30:00",
                },
                {
                  end: "09:36:00",
                  start: "09:33:00",
                },
                {
                  end: "09:39:00",
                  start: "09:36:00",
                },
                {
                  end: "09:42:00",
                  start: "09:39:00",
                },
                {
                  end: "09:45:00",
                  start: "09:42:00",
                },
                {
                  end: "09:48:00",
                  start: "09:45:00",
                },
                {
                  end: "09:51:00",
                  start: "09:48:00",
                },
                {
                  end: "09:54:00",
                  start: "09:51:00",
                },
                {
                  end: "09:57:00",
                  start: "09:54:00",
                },
                {
                  end: "10:00:00",
                  start: "09:57:00",
                },
              ],
              municipi: "Capolat",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Bergued�",
              hores: [
                {
                  end: "10:03:00",
                  start: "10:00:00",
                },
                {
                  end: "10:06:00",
                  start: "10:03:00",
                },
                {
                  end: "10:09:00",
                  start: "10:06:00",
                },
                {
                  end: "10:12:00",
                  start: "10:09:00",
                },
                {
                  end: "10:15:00",
                  start: "10:12:00",
                },
                {
                  end: "10:18:00",
                  start: "10:15:00",
                },
                {
                  end: "10:21:00",
                  start: "10:18:00",
                },
                {
                  end: "10:24:00",
                  start: "10:21:00",
                },
                {
                  end: "10:27:00",
                  start: "10:24:00",
                },
                {
                  end: "10:30:00",
                  start: "10:27:00",
                },
              ],
              municipi: "Quar",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Bergued�",
              hores: [
                {
                  end: "10:33:00",
                  start: "10:30:00",
                },
                {
                  end: "10:36:00",
                  start: "10:33:00",
                },
                {
                  end: "10:39:00",
                  start: "10:36:00",
                },
                {
                  end: "10:42:00",
                  start: "10:39:00",
                },
                {
                  end: "10:45:00",
                  start: "10:42:00",
                },
                {
                  end: "10:48:00",
                  start: "10:45:00",
                },
                {
                  end: "10:51:00",
                  start: "10:48:00",
                },
                {
                  end: "10:54:00",
                  start: "10:51:00",
                },
                {
                  end: "10:57:00",
                  start: "10:54:00",
                },
                {
                  end: "11:00:00",
                  start: "10:57:00",
                },
              ],
              municipi: "Gisclareny",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Ripoll�s",
              hores: [
                {
                  end: "11:06:00",
                  start: "11:00:00",
                },
                {
                  end: "11:12:00",
                  start: "11:06:00",
                },
                {
                  end: "11:18:00",
                  start: "11:12:00",
                },
                {
                  end: "11:24:00",
                  start: "11:18:00",
                },
                {
                  end: "11:30:00",
                  start: "11:24:00",
                },
                {
                  end: "11:36:00",
                  start: "11:30:00",
                },
                {
                  end: "11:42:00",
                  start: "11:36:00",
                },
                {
                  end: "11:48:00",
                  start: "11:42:00",
                },
                {
                  end: "11:54:00",
                  start: "11:48:00",
                },
                {
                  end: "12:00:00",
                  start: "11:54:00",
                },
              ],
              municipi: "Llanars",
              temps_estimat: 60,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Ripoll�s",
              hores: [
                {
                  end: "12:03:00",
                  start: "12:00:00",
                },
                {
                  end: "12:06:00",
                  start: "12:03:00",
                },
                {
                  end: "12:09:00",
                  start: "12:06:00",
                },
                {
                  end: "12:12:00",
                  start: "12:09:00",
                },
                {
                  end: "12:15:00",
                  start: "12:12:00",
                },
                {
                  end: "12:18:00",
                  start: "12:15:00",
                },
                {
                  end: "12:21:00",
                  start: "12:18:00",
                },
                {
                  end: "12:24:00",
                  start: "12:21:00",
                },
                {
                  end: "12:27:00",
                  start: "12:24:00",
                },
                {
                  end: "12:30:00",
                  start: "12:27:00",
                },
              ],
              municipi: "Vallfogona de Ripoll�s",
              temps_estimat: 30,
            },
          },
          {
            data: "2024-06-19 08:00:00",
            pd: {
              comarca: "Ripoll�s",
              hores: [
                {
                  end: "12:33:00",
                  start: "12:30:00",
                },
                {
                  end: "12:36:00",
                  start: "12:33:00",
                },
                {
                  end: "12:39:00",
                  start: "12:36:00",
                },
                {
                  end: "12:42:00",
                  start: "12:39:00",
                },
                {
                  end: "12:45:00",
                  start: "12:42:00",
                },
                {
                  end: "12:48:00",
                  start: "12:45:00",
                },
                {
                  end: "12:51:00",
                  start: "12:48:00",
                },
                {
                  end: "12:54:00",
                  start: "12:51:00",
                },
                {
                  end: "12:57:00",
                  start: "12:54:00",
                },
                {
                  end: "13:00:00",
                  start: "12:57:00",
                },
              ],
              municipi: "Setcases",
              temps_estimat: 30,
            },
          },
        ],
      },
    ],
    municipis: [
      "Prats de Rei",
      "Bruc",
      "Vallbona d'Anoia",
      "Castellfollit de Riubreg�s",
      "Montmaneu",
      "Orp�",
      "Passanant i Belltall",
      "For�s",
      "Torroella de Fluvi�",
      "Far d'Empord�",
      "Cabanes",
      "Espolla",
      "Vilamalla",
      "Pedret i Marz�",
      "Vilamaniscle",
      "Castellfollit del Boix",
      "Collbat�",
      "Ullastrell",
      "Vallgorguina",
      "Fogars de Montcl�s",
      "Figar�-Montmany",
      "Sant Mart� Sesgueioles",
      "Castellol�",
      "Llacuna",
      "Pujalt",
      "Rubi�",
      "Santa Maria de Miralles",
      "Piles",
      "Rocafort de Queralt",
      "Vilamacolum",
      "Forti�",
      "Pau",
      "Ordis",
      "Vila�r",
      "Selva de Mar",
      "Palau de Santa Eul�lia",
      "Castellgal�",
      "Castellv� de Rosanes",
      "Sant Lloren� Savall",
      "Vilalba Sasserra",
      "Gualba",
      "Montseny",
      "Copons",
      "Cabrera d'Anoia",
      "Carme",
      "Sant Pere Sallavinera",
      "Veciana",
      "Conesa",
      "Savall� del Comtat",
      "Borrass�",
      "Santa Llogaia d'�lguema",
      "Avinyonet de Puigvent�s",
      "Pont�s",
      "Siurana",
      "Mollet de Peralada",
      "Mura",
      "�rrius",
      "Gallifa",
      "Campins",
      "Sant Pere de Vilamajor",
      "Sant Esteve de Palautordera",
      "Jorba",
      "Torre de Claramunt",
      "Calonge de Segarra",
      "Argen�ola",
      "Bellprat",
      "Llorac",
      "Vallfogona de Riucorb",
      "Sant Miquel de Fluvi�",
      "Garrig�s",
      "Vila-sacra",
      "Masarac",
      "Vilafant",
      "Riumors",
      "Rab�s",
      "Marganell",
      "Talamanca",
      "Rellinars",
      "Santa Maria de Martorelles",
      "C�noves i Samal�s",
      "Tagamanent",
      "Pontons",
      "Sant Cugat Sesgarrigues",
      "Olesa de Bonesvalls",
      "Torrelavit",
      "Maslloren�",
      "Vespella de Gai�",
      "Llad�",
      "Sant Lloren� de la Muga",
      "Cantallops",
      "Mieres",
      "Argelaguer",
      "Montagut i Oix",
      "Fonollosa",
      "Sant Feliu Sasserra",
      "Santa Maria de Merl�s",
      "Perafita",
      "Monistrol de Calders",
      "Collsuspina",
      "Torrelles de Foix",
      "Santa Fe del Pened�s",
      "Puigd�lber",
      "Albinyana",
      "Montmell",
      "Vilanant",
      "Terrades",
      "Albany�",
      "Sant Aniol de Finestres",
      "Riudaura",
      "Tortell�",
      "Rajadell",
      "Olvan",
      "Olost",
      "Alpens",
      "Sant Quirze Safaja",
      "Estany",
      "Mediona",
      "Cabanyes",
      "Vilob� del Pened�s",
      "Sant Lloren� d'Hortons",
      "Bonastre",
      "Olivella",
      "Navata",
      "Boadella i les Escaules",
      "Capmany",
      "Vajol",
      "Mai� de Montcal",
      "Sant Jaume de Llierca",
      "Sales de Llierca",
      "Castellnou de Bages",
      "Viver i Serrateix",
      "Orist�",
      "Sant Mart� d'Albars",
      "Calders",
      "Granera",
      "Font-rub�",
      "Pacs del Pened�s",
      "Castellet i la Gornal",
      "Subirats",
      "Santa Oliva",
      "Salom�",
      "Cabanelles",
      "Cistella",
      "Pont de Molins",
      "Biure",
      "Sant Ferriol",
      "Vall de Bianya",
      "Beuda",
      "Aguilar de Segarra",
      "Sant Mateu de Bages",
      "Sag�s",
      "Llu��",
      "Sobremunt",
      "Castellcir",
      "Figuerola del Camp",
      "Mas�",
      "Puigpelat",
      "Mont-ral",
      "Pira",
      "Vallclara",
      "Ventall�",
      "Vall-llobrega",
      "Pera",
      "Gualta",
      "Bellcaire d'Empord�",
      "Serra de Dar�",
      "Torrent",
      "Muntanyola",
      "Vilanova de Sau",
      "Rupit i Pruit",
      "Sant Boi de Llu�an�s",
      "Brull",
      "Sora",
      "Espinelves",
      "Aiguam�rcia",
      "Montferri",
      "Vallmoll",
      "Vilabella",
      "Garidells",
      "Vilaverd",
      "Vilanova de Prades",
      "Viladamat",
      "Cru�lles, Monells i Sant Sadurn� de l'Heura",
      "Rupi�",
      "Ull�",
      "Jafre",
      "Colomers",
      "Ultramort",
      "Folgueroles",
      "Sant Mart� de Centelles",
      "Sant Bartomeu del Grau",
      "Sant Vicen� de Torell�",
      "Santa Cec�lia de Voltreg�",
      "Vidr�",
      "Cabra del Camp",
      "Rodony�",
      "Ali�",
      "Nulles",
      "Mil�",
      "Senan",
      "Palau-sator",
      "Forallac",
      "Cor��",
      "Tallada d'Empord�",
      "Ullastret",
      "Garrigoles",
      "Santa Eug�nia de Berga",
      "Gurb",
      "Masies de Voltreg�",
      "Montesquiu",
      "Tavertet",
      "Sant Agust� de Llu�an�s",
      "Querol",
      "Riba",
      "Br�fim",
      "Rourell",
      "Blancafort",
      "Pontils",
      "Regenc�s",
      "Parlav�",
      "Foix�",
      "Albons",
      "Fontanilles",
      "Vilopriu",
      "Malla",
      "Santa Eul�lia de Riuprimer",
      "Masies de Roda",
      "Or�s",
      "Tav�rnoles",
      "Santa Maria de Besora",
      "Sant Sadurn� d'Osormort",
      "Riudecanyes",
      "Maspujols",
      "Almoster",
      "Arbol�",
      "Pobla de Mafumet",
      "Catllar",
      "Aiguaviva",
      "Madremanya",
      "Sant Andreu Salou",
      "Vilademuls",
      "Sant Miquel deCampmajor",
      "Osor",
      "Vallcebre",
      "Castellar del Riu",
      "Castell de l'Areny",
      "G�sol",
      "Moll�",
      "Campelles",
      "Ogassa",
      "Vilanova d'Escornalbou",
      "Riudecols",
      "Argentera",
      "Capafonts",
      "Vilallonga del Camp",
      "Secuita",
      "Sant Mart� de Ll�mena",
      "Sant Mart� Vell",
      "Viladasens",
      "Crespi�",
      "Massanes",
      "Fogars de la Selva",
      "Espunyola",
      "Saldes",
      "F�gols",
      "Sant Jaume de Frontany�",
      "Castellar de n'Hug",
      "Vilallonga de Ter",
      "Gombr�n",
      "Pardines",
      "Botarell",
      "Aleixar",
      "Vilaplana",
      "Colldejou",
      "Febr�",
      "Nou de Gai�",
      "Renau",
      "Campllong",
      "Canet d'Adri",
      "Cervi� de Ter",
      "Cam�s",
      "Esponell�",
      "Sant Feliu de Buixalleu",
      "Susqueda",
      "Vilada",
      "Montclar",
      "Nou de Bergued�",
      "Sant Juli� de Cerdanyola",
      "Planoles",
      "Llosses",
      "Toses",
      "Queralbs",
      "Pratdip",
      "Alforja",
      "Albiol",
      "Duesaig�es",
      "Perafort",
      "Riera de Gai�",
      "Llambilles",
      "Jui�",
      "Sant Joan de Mollet",
      "Palol de Revardit",
      "Fontcoberta",
      "Brunyola i Sant Mart� Sapresa",
      "Borred�",
      "Capolat",
      "Quar",
      "Gisclareny",
      "Llanars",
      "Vallfogona de Ripoll�s",
      "Setcases",
    ],
    selectedDate: null,
    selectedMunicipi: null,
    selectedHours: [],
    selectedHour: "",
    hoursCounter: 0,
    hours: [
      ["16:00", "16:10", "16:20", "16:30", "16:40", "16:50"],
      ["12:00", "12:10", "12:20", "12:30", "12:40", "12:50", "13:00"],
      [
        "09:00",
        "09:06",
        "09:12",
        "09:18",
        "09:24",
        "09:30",
        "09:36",
        "09:42",
        "09:48",
        "09:54",
      ],
    ],
    stage: 0,
  }),
  methods: {
    onDateChanged: function (foo) {
      this.selectedDate = foo;
      this.updateHoras();
    },
    onLocationSelected: function (foo) {
      this.selectedMunicipi = foo;
      this.updateHoras();
    },
    onHourSelected: function (foo) {
      this.selectedHour = this.selectedHours[foo];
      console.log(this.selectedHour);
    },
    updateHoras: function () {
      if (this.selectedDate && this.selectedMunicipi) {
        this.selectedHours = this.hours[this.hoursCounter];
      }
      if (this.hoursCounter == 2) {
        this.hoursCounter = 0;
      } else {
        this.hoursCounter++;
      }
    },
    async book() {
      this.stage = -1;
      setTimeout(() => {
        this.stage = 1;
        setTimeout(() => {
          this.stage = -1;
          setTimeout(() => {
            this.stage = 2;
          }, 1000);
        }, 3000);
      }, 1000);
    },
  },
};
</script>

<style>
.v-enter-active,
.v-leave-active {
  transition: opacity 1s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>