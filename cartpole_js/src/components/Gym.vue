<script setup>
import { CartPole, renderCartPole } from "./cartpole";
</script>

<template>
    <div>
        <p>Step: {{ step }}, Done: {{ done }}</p>
        <canvas width="500" ref="canvas" :id="canvasId"></canvas>
    </div>
</template>

<script>
let canvas;

export default {
    props: ["start", "actionCallback", "canvasId"],
    data(){
        return {
            env: new CartPole(),
            step: 0,
            done: false,
        }
    },
    mounted(){
        canvas = document.getElementById(this.canvasId)
        console.log(canvas)
        renderCartPole(this.env, canvas);
    },
    watch: {
        start(_, __){
            if(this.step == 0) this.loop();
        }
    },
    methods: {
        loop(){
            const loop = setInterval(() => {
                this.step++;
                const action = this.actionCallback(this.env.getStateTensor());

                this.env.update(action);
                renderCartPole(this.env, canvas);
                
                if(this.env.isDone()) {
                    clearInterval(loop);
                    this.done = true;
                }
            }, 200);
        },
    }
}
</script>

<style scoped>
canvas {
    border: 1px solid black;
}
</style>