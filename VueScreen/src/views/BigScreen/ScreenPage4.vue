<template>
    <div class="leftTop">
        <span class="angle1"></span>
        <span class="angle2"></span>
        <span class="angle3"></span>
        <span class="angle4"></span>
        <div class="left1">
            <div class="grid-content ep-bg-purple" id="mychart4"></div>
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
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'shadow'
                }
            },
            title: {
                text: '上网质量占比TOP15',
                left: 10,
                top: 10,
                textStyle: {
                    color: '#75deef',
                    fontSize: "20px"
                },
            },
            legend: {
                bottom: 0,
                left: 'center',
                textStyle: {
                    color: '#75deef',
                },
            },
            grid: {
                left: '3%',
                right: '4%',
                bottom: '10%',
                containLabel: true
            },
            dataZoom: [
                {
                    show: true,
                    type: "slider",
                    borderColor: "rgb(19, 63, 100)",
                    showDetail: false,
                    endValue: 4,
                    yAxisIndex: [0, 1],
                    width: 1,
                    height: "100%",
                    right: 3,
                    handleSize: 0,
                    zoomLoxk: true,
                    top: "middle",
                },
                {
                    type: "inside",
                    yAxisIndex: [0, 1],
                    zoomOnMouseWheel: false,
                    moveOnMouseMove: true,
                    moveOnMouseWheel: true,
                },
            ],
            xAxis: {
                type: 'value',
                splitLine: {
                    show: false
                },
                axisLabel: {
                    color: '#75deef',
                    interval: 0
                }
            },
            yAxis: {
                type: 'category',
                data: ['昆明', '玉溪', '曲靖', '昭通', '保山', '丽江', '普洱'],
                axisLabel: {
                    color: '#75deef',

                }
            },
            series: [{
                name: '1-6分',
                type: 'bar',
                stack: 'total',
                label: {
                    show: false,
                    fontSize: "7px"
                },
                emphasis: {
                    focus: 'series'
                },
                data: [320, 302, 301, 334, 390, 330, 320],
                itemStyle: {color: 'red'}
            },
                {
                    name: '7-9分',
                    type: 'bar',
                    stack: 'total',
                    label: {
                        show: false,
                        fontSize: "8px"
                    },
                    emphasis: {
                        focus: 'series'
                    },
                    data: [1210, 132, 101, 134, 90, 230, 210],
                    itemStyle: {color: 'yellow'}
                },
                {
                    name: '10及以上',
                    type: 'bar',
                    stack: 'total',
                    label: {
                        show: false,
                        fontSize: "8px"
                    },
                    emphasis: {
                        focus: 'series'
                    },
                    data: [220, 182, 191, 234, 290, 330, 310],
                    itemStyle: {
                        color: 'blue'
                    }
                },
                //     {
                //     name: '其他',
                //     type: 'bar',
                //     stack: 'total',
                //     label: {
                //         show: true
                //     },
                //     emphasis: {
                //         focus: 'series'
                //     },
                //     data: [220, 182, 191, 234, 290, 330, 310],
                //     itemStyle: {
                //         color: 'gray'
                //     }
                // }
            ]
        });

        onMounted(async () => {
            try {
                const response = await axios.get("/api/screen/proportion/internet/quality/");

                option.yAxis.data = response.data.county_list;
                option.series[0].data = response.data.one_to_six_points_count_list;
                option.series[1].data = response.data.seven_to_nine_points_count_list;
                option.series[2].data = response.data.ten_points_count_list;
                // option.series[3].data = response.data.other_count_list;
                // console.log(option)
                let echartBox = document.getElementById("mychart4");
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
#mychart4 {
    height: 230px;
}
</style>