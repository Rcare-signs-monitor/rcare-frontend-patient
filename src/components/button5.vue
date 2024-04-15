<script setup>
const props = defineProps(['isCalling'])

import { ref, computed, watch } from 'vue';
const timeLeft = ref(5);
const border = ref(25);
const width = ref(25)
const dashLen = (100 - border.value / 2) * Math.PI * 2;

const dashOffset = computed(() => (timeLeft.value - 1) / 5 * dashLen)

watch(
    () => props.isCalling,
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
    <div class="main" :class="{ active: props.isCalling }">
        <div class="card">
            <div class="notification">
                <div class="notiglow" style="margin-top: 50px;"></div>
                <div class="notiborderglow"></div>
                <div class="notititle">呼叫护士</div>
                <div class="notibody">正在为您呼叫，请稍等</div>

                <svg style="margin-top: 50px;" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" :width="width"
                    :height="width">
                    <circle cx="100" cy="100" :r="100 - border / 2" fill="none" opacity="0.4" stroke="#038CD9"
                        :stroke-width="border" />
                    <circle cx="100" cy="100" :r="100 - border / 2" fill="none" transform="rotate(270,100,100)"
                        stroke="#038CD9" :stroke-width="border" :stroke-dasharray="dashLen"
                        :stroke-dashoffset="dashOffset" style="transition: stroke-dashoffset 0.4s" />
                </svg>
            </div>
        </div>
        <p class="text">呼&nbsp;叫<br>护&nbsp;士</p>
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
    display: block;
    width: 240px;
    height: 240px;
    border-top-left-radius: 10px;
    background: lightgrey;
    transition: .3s ease, .15s background-color, .15s background-image ease-in-out;
    background: rgba(255, 255, 255, 0.596);
    border: 1px solid transparent;
    backdrop-filter: blur(5px);
    -webkit-backdrop-filter: blur(5px);
    display: flex;
    align-items: center;
    justify-content: center;

    background-size: 300% 300%;
    transition: 0.5s;
    animation: gradient_301 5s ease infinite;
    border: double 4px transparent;
    background-image: linear-gradient(#dedede, #dedede), linear-gradient(137.48deg, #ffdb3b 10%, #FE53BB 45%, #8F51EA 67%, #0044ff 87%);
    background-origin: border-box;
    background-clip: content-box, border-box;
}

.card:nth-child(1) {
    border-top-right-radius: 10px;
    border-top-left-radius: 10px;
    border-bottom-right-radius: 10px;
    border-bottom-left-radius: 10px;
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
    height: 330px;
}

.card.active {
    width: 360px;
    height: 100px;
    animation-fill-mode: forwards;
}

.notification {
    display: none;
}

.active .notification {
    display: flex;
    flex-direction: column;
    align-items: center;
    font-size: 23px;
    --gradient: linear-gradient(to bottom, #2eadff, #3d83ff, #7e61ff);
    --color: #32a6ff
}

.notification:after {
    position: absolute;
    content: "";
    width: 0.25rem;
    inset: 0.65rem auto 0.65rem 0.5rem;
    border-radius: 0.125rem;
    background: var(--gradient);
    transition: transform 300ms ease;
    z-index: 4;
}

.notification:after {
    transform: translateX(0.15rem)
}

.notititle {
    color: var(--color);
    padding: 0.65rem 0.25rem 0.4rem 1.25rem;
    font-weight: 500;
    font-size: 1.8rem;
    transition: transform 300ms ease;
    z-index: 5;
}

.notification .notititle {
    transform: translateX(0.15rem)
}

.notibody {
    color: #e5e5e5;
    padding: 0 0.25rem 0 1.25em;
    transition: transform 300ms ease;
    z-index: 5;
}

.notiglow {
    z-index: 3;
}

.notiborderglow {
    z-index: 1;
}

.notification .notiglow {
    opacity: 0.1
}

.notification .notiborderglow {
    opacity: 0.1
}

.note {
    color: var(--color);
    position: fixed;
    top: 80%;
    left: 50%;
    transform: translateX(-50%);
    text-align: center;
    font-size: 0.9rem;
    width: 75%;
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