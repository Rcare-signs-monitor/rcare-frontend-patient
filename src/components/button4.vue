<script setup>
const props = defineProps(['isViewing', 'signs'])

import { ref, computed, watch } from 'vue';
const timeLeft = ref(5);
const border = ref(25);
const width = ref(25)
const dashLen = (100 - border.value / 2) * Math.PI * 2;

const dashOffset = computed(() => (timeLeft.value - 1) / 5 * dashLen)

watch(
    () => props.isViewing,
    (value, oldValue) => {
        if (value == true) {
            timeLeft.value = 5
            const interval = setInterval(() => {
                timeLeft.value -= 1
                if (timeLeft.value <= 0) {
                    clearInterval(interval)
                }
            }, 1000)
        }
    }, { immediate: true }
)

</script>

<template>
    <div class="main" :class="{ active: props.isViewing }">
        <div class="card">
            <div class="img"></div>
            <div class="textBox">
                <div class="textContent">
                    <p class="h1">心率</p>
                    <svg style="margin-right: 10px;" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"
                        :width="width" :height="width">
                        <circle cx="100" cy="100" :r="100 - border / 2" fill="none" opacity="0.4" stroke="#038CD9"
                            :stroke-width="border" />
                        <circle cx="100" cy="100" :r="100 - border / 2" fill="none" transform="rotate(270,100,100)"
                            stroke="#038CD9" :stroke-width="border" :stroke-dasharray="dashLen"
                            :stroke-dashoffset="dashOffset" style="transition: stroke-dashoffset 0.4s" />
                    </svg>
                    <span class="span" style="display: flex; justify-content: center; align-items: center;">
                        {{ props.signs.time.split(" ")[1] }}
                    </span>
                </div>
                <p class="p">{{ props.signs.heart }} <spans style="font-size: 15px;">bpm</spans>
                </p>
                <div>
                </div>
            </div>
        </div>
        <div class="card">
            <div class="img"></div>
            <div class="textBox">
                <div class="textContent">
                    <p class="h1">呼吸率</p>
                    <span class="span">{{ props.signs.time.split(" ")[1] }}</span>
                </div>
                <p class="p">{{ props.signs.respire }} <spans style="font-size: 15px;">bpm</spans>
                </p>
                <div>
                </div>
            </div>
        </div>
        <div class="card">
            <div class="img"></div>
            <div class="textBox">
                <div class="textContent">
                    <p class="h1">血压</p>
                    <span class="span">{{ props.signs.time.split(" ")[1] }}</span>
                </div>
                <p class="p">{{ props.signs.sbp }} / {{ props.signs.dbp }} <spans style="font-size: 15px;">mmHg</spans>
                </p>
                <div>
                </div>
            </div>
        </div>
        <p class="text">查&nbsp;看<br>体&nbsp;征</p>

        <div class="main_back"></div>
    </div>
</template>

<style scoped>
.main_back {
    position: absolute;
    border-radius: 10px;
    transform: rotate(90deg);
    width: 16.5em;
    height: 16.5em;
    /* background: radial-gradient( circle farthest-corner at 10% 20%,  rgba(255,94,247,1) 17.8%, rgba(2,245,255,1) 100.2% ); */
    z-index: -2;
    box-shadow: inset 0px 0px 180px 5px #93acff;
    transition: opacity 1s, border-radius .3s;
}

.main {
    display: flex;
    flex-wrap: wrap;
    width: 20em;
    align-items: center;
    justify-content: center;
    margin: 20px;
}

.card {
    width: 240px;
    height: 82px;
    border-top-left-radius: 10px;
    background: lightgrey;
    transition: .3s ease, .15s background-color, .15s background-image ease-in-out;
    background: rgba(255, 255, 255);
    border: 1px solid transparent;
    backdrop-filter: blur(5px);
    -webkit-backdrop-filter: blur(5px);
    color: white;

    background-size: 300% 300%;
    transition: 0.5s;
    animation: gradient_301 5s ease infinite;
    border: double 4px transparent;
    background-image: linear-gradient(#dedede, #dedede), linear-gradient(137.48deg, #ffdb3b 10%, #FE53BB 45%, #8F51EA 67%, #0044ff 87%);
    background-origin: border-box;
    background-clip: content-box, border-box;
}

.active .card {
    border-radius: 20px;
    display: flex;
    align-items: center;
    justify-content: left;
    backdrop-filter: blur(10px);
}

.img {
    display: none;
    width: 50px;
    height: 50px;
    margin-left: 18px;
    border-radius: 10px;
}

.card:nth-child(1) .img {
    background: linear-gradient(#d7cfcf, #9198e5);
}

.card:nth-child(2) .img {
    background: linear-gradient(#7af1f5, #23f4ae);
}

.card:nth-child(3) .img {
    background: linear-gradient(#89f0f4, #9798dd);
}

.active .img {
    display: block;
}

.textBox {
    display: none;
}

.active .textBox {
    display: block;
    width: calc(100% - 110px);
    margin-left: 25px;
    color: white;
    font-family: 'Poppins' sans-serif;
}

.textContent {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.span {
    font-size: 20px;
}

.h1 {
    font-size: 18px;
    font-weight: bold;
}

.p {
    font-size: 24px;
    font-weight: lighter;
}

.card:nth-child(1) {
    border-top-right-radius: 10px;
    border-top-left-radius: 10px;
}

.card:nth-child(3) {
    border-bottom-right-radius: 10px;
    border-bottom-left-radius: 10px;
}

.card:nth-child(1) {
    border-bottom: 0;
}

.card:nth-child(2) {
    border-top: 0;
    border-bottom: 0;
}

.card:nth-child(3) {
    border-top: 0;
}

.card {
    border-radius: 0px;
}

.main.active .main_back {
    opacity: 0;
    border-radius: 30px;
}

.main.active .card {
    --hover-edge-radius: 100%;
    --hover-edge-offset: 10%;
    margin: .2em;
    border-radius: 10px;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.3);
    background: rgba(255, 255, 255, 0.4);
}

.main.active .text {
    opacity: 0;
    z-index: -3;
}

.main.active div {
    opacity: 1;
}

.main.active .card {
    width: 360px;
    height: 105px;
}

.card.active {
    width: 360px;
    height: 120px;
    animation: backgroundIMG .1s;
    animation-fill-mode: forwards;
}

.card.active .uiverse #paint0_linear_501_142 stop {
    stop-color: white;
}

.card.active .uiverse #paint1_linear_501_142 stop {
    stop-color: white;
}

.card.active .uiverse #paint2_linear_501_142 stop {
    stop-color: white;
}

@keyframes backgroundIMG {
    100% {
        background-image: linear-gradient(#BF66FF, #6248FF, #00DDEB);
    }
}

@keyframes gradient_301 {
    0% {
        background-position: 0% 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0% 50%;
    }
}

.text {
    position: absolute;
    font-size: 4em;
    transition: .4s ease-in-out;
    color: rgb(109, 64, 121);
    text-align: center;
    font-weight: bold;
    /* letter-spacing: 0.33em; */
    z-index: 3;
}
</style>