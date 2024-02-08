<template>
    <div class="leftTop">
        <span class="angle1"></span>
        <span class="angle2"></span>
        <span class="angle3"></span>
        <span class="angle4"></span>
        <div class="left1">
            <div class="grid-content ep-bg-purple" id="mychart10"></div>
            <el-select
                class="mySelect"
                size="small"
                v-model="value"
                placeholder="Select"
            >
                <el-option
                    v-for="item in options"
                        :key="item.value"
                    :label="item.label"
                    :value="item.value"
                />
            </el-select>
        </div>
    </div>
    
</template>
<script>
import { onMounted, reactive, ref} from "vue";
import * as echarts from "echarts";
export default {
    setup() {
        const value = ref('')
        const options = [ {
            value: 'Option1',
            label: 'Option1',
        }, {
            value: 'Option2',
            label: 'Option2',
        }, {
            value: 'Option3',
            label: 'Option3',
        }, {
            value: 'Option4',
            label: 'Option4',
        }, {
            value: 'Option5',
            label: 'Option5',
        }]
        let option = reactive({
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'shadow'
                }
            },
            title: {
                text: '区县装维服务',
                left: 'center',
                textStyle: {
                    color: '#75deef',
                },
            },
            legend: {
                bottom : 0,
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
                type: 'value',
                splitLine: {
                    show:false
                },
                axisLabel: {
                    color: '#75deef'
                }
            },
            yAxis: {
                type: 'category',
                data: ['网格一'],
                splitLine: {
                    show:false
                },
                axisLabel: {
                    color: '#75deef'
                }
            },
            series: [{
                name: '装维服务1-6分',
                type: 'bar',
                stack: 'total',
                label: {
                    show: true,
                },
                emphasis: {
                    focus: 'series'
                },
                data: [320],
                barWidth: '40%',
                itemStyle: {
                    color: 'red'
                }
            },
            {
                name: '装维服务7-9分',
                type: 'bar',
                stack: 'total',
                label: {
                    show: true
                },
                emphasis: {
                    focus: 'series'
                },
                data: [120],
                itemStyle: {
                    color: 'yellow'
                }
            },
            {
                name: '装维服务10分',
                type: 'bar',
                stack: 'total',
                label: {
                    show: true
                },
                emphasis: {
                    focus: 'series'
                },
                data: [220],
                itemStyle: {
                    color: 'blue'
                }
            },
            {
                name: '评价不明',
                type: 'bar',
                stack: 'total',
                label: {
                    show: true
                },
                emphasis: {
                    focus: 'series'
                },
                data: [0],
                itemStyle: {
                    color: 'grey'
                }
            } ]
        });
        onMounted(() => {
            let echartBox = document.getElementById("mychart10");
            echartBox.removeAttribute('_echarts_instance_')
            let myChart = echarts.init(echartBox);
            myChart.setOption(option);
        });
        return {
            options,
            value
        };
    },
};
</script>
<style scoped>
    #mychart10{
        height: 400px;
    }
    .mySelect{
        width: 100px;
        position: absolute;
        top: 28px;
    }
</style>