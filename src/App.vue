<script setup>
import button1 from './components/button1.vue';
import button4 from './components/button4.vue';
import button5 from './components/button5.vue';

import axios from 'axios';

import { reactive, ref } from 'vue';
const config = reactive({
    value: 66,
    lineDash: [10, 2],
})

function delay(n) {
    return new Promise(function (resolve) {
        setTimeout(resolve, n * 1000);
    });
}

const isCalling = ref(false)
const isViewing = ref(false)
const signs = ref({
    "time": "",
    "heart": 0,
    "respire": 0,
    "sbp": 0,
    "dbp": 0
})
const getData = async () => {
    while (true) {
        let type;
        await axios.get("http://localhost:5000/").then(res => {
            console.log(res.data);
            if (res.data['type'] === 0) {
                type = 0
                isViewing.value = true
                console.log("正在查看体征")
                signs.value = res.data['data'][0]
                console.log(signs.value['time']);
            }
            else if (res.data['type'] === 1) {
                type = 1
                isCalling.value = true
                console.log("正在呼叫")
            }
        }).finally(async function () {
            await delay(14);
            if (type === 0)
                isViewing.value = false
            else if (type === 1)
                isCalling.value = false
        })
    }
}
getData()


const getSign = async () => {
    await axios.get("http://localhost:5000/api/sign").then(res => {
        console.log(res.data);
        isViewing.value = true
        console.log("正在查看体征")
        signs.value = res.data[0]
        console.log(signs.value['time']);
    }).finally(async function () {
        await delay(5);
        isViewing.value = false
    })
}

const getSHelp = async () => {
    await axios.get("http://localhost:5000/api/help").then(res => {
        console.log(res.data);
        isCalling.value = true
        console.log("正在呼叫")
    }).finally(async function () {
        await delay(5);
        isCalling.value = false
    })
}
</script>

<template>
    <div style="margin-top: 20px">
        <div style="display: flex; width: 100%">
            <dv-decoration-10 style="width: 26%; height: 5px" />
            <dv-decoration8 style="width: 12%; height: 50px" :color="['#757FB1', 'rgba(0,0,0,0)']" />
            <div style="display: flex; flex-grow: 1"></div>
            <dv-decoration8 :reverse="true" style="width: 12%; height: 50px" :color="['#757FB1', 'rgba(0,0,0,0)']" />
            <dv-decoration-10 style="width: 26%; height: 5px; transform: rotateY(180deg)" />
        </div>
        <div style="display: flex; width: 100%; margin-top: -10px">
            <div class="box"><span style=""><dv-percent-pond :config="config"
                        style="width:80px;height:30px;margin-top: 1px;" /></span></div>
            <div class="box2" style="transform: skew(45deg)"></div>
            <div class="title">
                <div style="font-size: 25px; margin-bottom: 10px; color: white;" align="center">非接触式<br />生命体征监测系统</div>
                <dv-decoration6 style="width: 270px; height: 7px" />
            </div>
            <div class="box2" style="transform: skew(-45deg)"></div>
            <div class="box" style="transform: rotateY(180deg)"><dv-decoration1 :color="['#4fd2dd', '#235fa7']"
                    style="width:200px;height:40px;" /></div>
        </div>
    </div>
    <dv-border-box8 :reverse="true" style="margin-top: 15px;" :dur="8">
        <div style="padding: 20px 40px;">
            <dv-border-box9>
                <div class="container">
                    <button4 :signs="signs" :isViewing="isViewing" @click="getSign"></button4>
                    <button1></button1>
                    <button5 :isCalling="isCalling" @click="getSHelp"></button5>
                </div>
            </dv-border-box9>
        </div>
    </dv-border-box8>
    <div style="position: fixed; right: 75px; bottom: 55px;">
        <dv-decoration-12 style="width:80px;height:80px;" />
    </div>
    <div>

    </div>
</template>


<style scoped>
:deep(.dv-percent-pond text) {
    display: none !important;
}

.container {
    height: 70vh;
    width: 88vw;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 10px;
}

.box {
    width: 25%;
    height: 0;
    border-right: 40px solid transparent;
    border-bottom: 40px solid #3a5991;
}

.box span {
    font-size: 15px;
    position: relative;
    top: 3px;
    left: 10px;
    color: rgb(219 219 219 / 84%);
}

.box2 {
    width: 10%;
    height: 40px;
    background-color: #151e3e;
}

.title {
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    align-items: center;
    margin: -40px 50px;
}
</style>
