class Routes {
    constructor(
        public itinerari1: Itinerari[],
        public itinerari2: Itinerari[],
        public itinerari3: Itinerari[],
        public itinerari4: Itinerari[],
    ) {}
}
class Itinerari {
    constructor(
        public data: Date| string,
        public pd: PointDestination
    ) {}
}

class PointDestination {
    constructor(
        public comarca: string,
        public hores: Interval[],
        public municipi: string,
        public temps_estimat: number
    ) {}
}

class Interval {
    constructor(
        public start: Date | string,
        public end: Date| string
    ) {}
}