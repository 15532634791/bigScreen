<template>
    <div class="leftTop">
        <span class="angle1"></span>
        <span class="angle2"></span>
        <span class="angle3"></span>
        <span class="angle4"></span>
        <div class="left1">
            <div class="grid-content ep-bg-purple" id="mychart2"></div>
        </div>
    </div>
</template>
<script>
import {onMounted, reactive} from "vue";
import * as echarts from "echarts";
import axios from "axios";

export default {
    setup() {
        let option = reactive({
            title: {
                text: '上网质量满意度',
                left: 10,
                top: 10,
                textStyle: {
                    color: '#75deef',
                    fontSize: "20px"
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
                    fontSize: "14px"
                },
            },
            series: [{
                name: '',
                type: 'pie',
                radius: ["40%", "50%"],
                avoidLabelOverlap: false,
                itemStyle: {
                    borderRadius: 10,
                    borderColor: '#fff',
                    borderWidth: 2
                },
                label: {
                    show: true,
                    position: 'outside',
                    color: '#fff',
                    fontSize: "14px",
                    formatter: '{c},\n{d}%'
                },
                emphasis: {
                    itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                },
                labelLine: {
                    // show: false
                },
                data: [
                    {value: 59, name: '1-6分', itemStyle: {color: 'red'}},
                    {value: 123, name: '7-9分', itemStyle: {color: 'yellow'}},
                    {value: 321, name: '10分', itemStyle: {color: 'blue'}},
                    // { value: 0, name: '评价不明',itemStyle: { color: 'grey' } },
                ]
            }]
        });

        onMounted(async () => {
            try {
                const response = await axios.get("/api/screen/score/internet/quality/");
                option.series[0].data[0].value = response.data.one_to_six_points_count;
                option.series[0].data[1].value = response.data.seven_to_nine_points_count;
                option.series[0].data[2].value = response.data.ten_points_count;
                let echartBox = document.getElementById("mychart2");
                echartBox.removeAttribute("_echarts_instance_");
                let myChart = echarts.init(echartBox);
                myChart.setOption(option);
            } catch (error) {
                console.log(error);
            }
        });
        return {};
    },
};
</script>
<style scoped>
#mychart2 {
    height: 230px;
}
</style>