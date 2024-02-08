<template>
    <div class="leftTop">
        <span class="angle1"></span>
        <span class="angle2"></span>
        <span class="angle3"></span>
        <span class="angle4"></span>
        <div class="left1">
            <div class="grid-content ep-bg-purple" id="mychart11"></div>
        </div>
    </div>
</template>
<script>
import { onMounted, reactive } from "vue";
import * as echarts from "echarts";
export default {
    setup() {
        let option1 = reactive({
            title: {
                text: '网格上网质量',
                left: 10,
                top:10,
                textStyle: {
                    color: '#75deef',
                    fontSize:"20px"
                },
            },
            tooltip: {
                trigger: 'item'
            },
            legend: {
                bottom: 10,
                left: 'center',
                textStyle: {
                    color: '#75deef',
                    fontSize:"14px"
                },
            },
            series: [ {
                name: '',
                type: 'pie',
                radius: ["40%", "50%"],
                data: [
                    { value: 289, name: '上网质量1-6分'},
                    { value: 345, name: '上网质量7-9分' },
                    { value: 368, name: '上网质量10分' },
                    { value: 0, name: '评价不明' },
                ],
                emphasis: {
                    itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                },
                itemStyle: {
                    borderRadius: 5,
                    borderWidth: 60,
                },
                label: {
                    show: true,
                    position: 'outside',
                    color: '#fff',
                    fontSize:"14px",
                    formatter: '{c},\n{d}%'
                },
                color: ["red","yellow","blue","grey"],
            } ]
        });
        onMounted(() => {
            let echartBox = document.getElementById("mychart11");
            echartBox.removeAttribute('_echarts_instance_')
            let myChart = echarts.init(echartBox);
            myChart.setOption(option1);
        });
        return {};
    },
};
</script>
<style lang="less" scoped>
    #mychart11{
        height: 400px;
    }
</style>