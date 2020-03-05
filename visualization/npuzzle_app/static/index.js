let app = new Vue({
    el: '#app',
    data: {
        list: [],
        message: "Hello!"
    },
    mounted() {
        this.$http.get('').then( (req) => this.list = req.data)
    },
    created: function () {
        console.log('Значение a: ' + this.message)
    }
})