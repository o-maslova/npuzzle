Vue.component('board', {
    data: function () {
        return {
            height: 30,
            width: 30,
        }
    },
    props: {
        size: Number,
        state: Object,
        delay: Number,
    },
    computed: {
        styleCell() {
            return {
                width: (this.width - 3) / this.size + 'vw',
                height: (this.height - 3) /this.size + 'vw',
                fontSize: (this.width - 4) / this.size + 'vw',
                textAlign: 'center',
                border: '0.4vw groove',
                backgroundColor: 'rgba(222, 175, 138, 1)',
                borderColor: 'rgba(210, 197, 170, 1)'
            }
        },
        styleEmptyCell() {
            return {
                backgroundColor: 'rgba(69, 34, 5, 1)',
                borderColor: 'rgba(69, 34, 5, 1)',
                border: '0.4vw solid'
            }
        },
        styleBoardRow() {
            return {
                top: '0',
                bottom: '0',
                margin: 'auto 0',
                display: 'flex',
                flexDirection: 'row',
                justifyContent: 'space-around',
                alignItems: 'center',
                background: 'rgba(69, 34, 5, 1)',
                width: this.width + 'vw',
                height: this.height / this.size + 'vw',
            }
        },
        styleBoard() {
            return {
                display: 'flex',
                flexDirection: 'column',
                width: this.width + 'vw',
                height: this.height + 'vw',
                border: '10px inset',
                background: 'rgba(69, 34, 5, 1)',
                borderRadius: '5px',
                borderColor: 'rgba(107, 65, 31, 1)'
            }
        },
    },
    template: '<div v-bind:style="styleBoard">' +
        '           <div v-bind:style="styleBoardRow" v-for="row in state">' +
        '               <div v-for="cell in row" v-if="">' +
        '                   <div v-if="cell == 0" v-bind:style="[styleCell, styleEmptyCell]"></div>' +
        '                   <div v-else v-bind:style="styleCell">{{ cell }}</div>' +
        '               </div>' +
        '           </div>' +
        '      </div>',
});


function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

const app = new Vue({
    el: '#app',
    delimiters : ['[[',']]'],
    data: {
        is_started: false,
        play_array: [],
        steps: {},
        num_of_squares: 0,
        speed: 500,
    },
    created() {
        axios.get("http://127.0.0.1:8000/solving/").then((response) =>
        {
            this.num_of_squares = response.data.num_of_squares;
            this.play_array = response.data.steps;
            this.steps = this.play_array[0]
        });
    },
    methods: {
        start_play: async function () {
            this.delay = 1000;
            this.is_started = true;
            let i = this.play_array.indexOf(this.steps);
            while (i < this.play_array.length && this.is_started === true)
            {
                this.steps = this.play_array[i];
                await sleep(this.speed);
                i++;
            }
            this.is_started = false
        },
        next_step: function () {
            // console.log("Vse norm tut!")
            let current_state_index = this.play_array.indexOf(this.steps);
            // console.log((current_state_index));
            if (current_state_index < this.play_array.length - 1) {
                this.steps = this.play_array[current_state_index + 1]
            }
        },
        prev_step: function () {
            let current_state_index = this.play_array.indexOf(this.steps);
            if (current_state_index > 0) {
                this.steps = this.play_array[current_state_index - 1]
            }
        },
        pause: function () {
            this.is_started = false
        },
        speed_up: function () {
            if (this.speed > 0) {
                this.speed -= 100;
            }
        },
        speed_down: function () {
            if (this.speed < 2000) {
                this.speed += 100;
            }
        }
    }
});
