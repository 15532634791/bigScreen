<template>
    <div class="leftTop">
        <span class="angle1"></span>
        <span class="angle2"></span>
        <span class="angle3"></span>
        <span class="angle4"></span>
        <div class="left1">
            <div class="grid-content ep-bg-purple" id="mychart7"></div>
        </div>
    </div>
</template>
<script>
import { onMounted, reactive } from "vue";
import * as echarts from "echarts";
import axios from "axios";
export default {
    setup() {
        let option = reactive({
            title: {
                text: '网格满意度Top15',
                left: 10,
                top:10,
                textStyle: {
                    color: '#75deef',
                    fontSize:"20px"
                },
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                type: 'shadow'
                }
            },
            legend: {
                bottom: 10,
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
            xAxis: {
                type: 'category',
                data: [
                    '全省','版纳','保山','大理','怒江','普洱',"数据1","数据1","数据1","数据1",
                    "数据1","数据1","数据1","数据1","数据1","数据1","数据1","数据1","数据1","数据1"
                ],
                splitLine: {
                    show:false
                },
                axisLabel: {
                    color: '#75deef',
                    rotate:40
                }
            },
            yAxis: {
                type: 'value',
                splitLine: {
                    show:false
                },
                axisLabel: {
                    color: '#75deef'
                }
            },
            series: [ {
                name: '',
                type: 'bar',
                barWidth: 10,
                data: [
                    1230, 1200, 1190, 1180, 1170, 1100,1050,1000,980,950,
                    900,850,800,750,700,650,600,550,500,450 
                ],
                itemStyle: {
                    borderRadius:[50, 50, 0, 0],
                    color: "blue"
                }
            }]
        });
        // onMounted(() => {
        //     let echartBox = document.getElementById("mychart7");
        //     echartBox.removeAttribute('_echarts_instance_')
        //     let myChart = echarts.init(echartBox);
        //     myChart.setOption(option);
        // });

        onMounted(async () => {
            try {
                const response = await axios.get("/api/screen/screen/satisfaction/grid/");
                console.log('--------------------')
                console.log(response.data.comprehensive_score_list)
                console.log(response.data.grids)
                console.log('--------------------')
                option.series[0].data = response.data.comprehensive_score_list;
                option.xAxis.data = response.data.grids;
                // console.log(option)
                let echartBox = document.getElementById("mychart7");
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
    #mychart7{
        height: 300px;
    }
</style>