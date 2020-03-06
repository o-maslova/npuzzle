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
    },
    computed: {
        styleCell () {
            return {
                width: (this.width - 3) / this.size + 'vw',
                height: (this.height - 3) /this.size + 'vw',
                verticalAlign: 'middle',
                textAlign: 'center',
                alignContent: 'center',
                border: '1px solid',
                borderRadius: '5px'
            }
        },
        styleBoardRow () {
            return {
                top: '0',
                bottom: '0',
                margin: 'auto 0',
                display: 'flex',
                flexDirection: 'row',
                justifyContent: 'space-around',
                alignItems: 'center',
                width: this.width + 'vw',
                height: this.height / this.size + 'vw',
            }
        },
        styleBoard () {
            return {
                display: 'flex',
                flexDirection: 'column',
                width: this.width + 'vw',
                height: this.height + 'vw',
                border: '3px solid',
                borderRadius: '5px'
            }
        },
    },
    template: '<div v-bind:style="styleBoard">' +
        '           <div v-bind:style="styleBoardRow" v-for="row in state">' +
        '               <div v-bind:style="styleCell" v-for="cell in row">{{ cell }}</div>' +
        '           </div>' +
        '      </div>',
});

Vue.component('start-button', {
    props: ['title'],
    template: '<button v-on:click="start()">{{ title }}</button>',
    methods: {

    }
})

const app = new Vue({
    el: '#npuzzle',
    delimiters : ['[[',']]'],
    data: {
        message: "Hello!",
        play_array: [],
        steps: [],
        num_of_squares: 0
    },
    created() {
        axios.get("http://127.0.0.1:8000/solving/").then((response) =>
        {
            this.num_of_squares = response.data.num_of_squares;
            this.play_array = response.data.steps
            this.steps = this.play_array[0]
        });

        // this.getSolution();
        // this.$http.get('solving/').then( (req) => this.list = req.data).catch(error => console.log(error));
    },
    methods: {
        getSolution() {
            // console.log(JSON.stringify(this.list))
        }
    }
});
