<template>
    <div>
        <el-row :gutter="24">
            <el-col :span="24">
                <el-row :gutter="24">
                    <el-col :span="8">
                        <div class="leftTop">
                            <span class="angle1"></span>
                            <span class="angle2"></span>
                            <span class="angle3"></span>
                            <span class="angle4"></span>
                            <div class="left1">
                                <div class="grid-content ep-bg-purple" id="mychart8" style="height: 400px;"></div>
                                <el-select
                                        class="mySelect"
                                        size="small"
                                        v-model="grid_value"
                                        placeholder="Select"
                                        style="width: 200px"
                                >
                                    <el-option
                                            v-for="item in grid_options"
                                            :key="item.value"
                                            :label="item.label"
                                            :value="item.value"
                                    />
                                </el-select>
                            </div>
                        </div>
                    </el-col>
                    <el-col :span="8">
                        <div class="leftTop">
                            <span class="angle1"></span>
                            <span class="angle2"></span>
                            <span class="angle3"></span>
                            <span class="angle4"></span>
                            <div class="left1">
                                <div class="grid-content ep-bg-purple" id="mychart10" style="height: 400px;"></div>
                                <el-select
                                        class="mySelect"
                                        size="small"
                                        v-model="zones_value"
                                        placeholder="Select"
                                        style="width: 200px"
                                >
                                    <el-option
                                            v-for="item in zones_options"
                                            :key="item.value"
                                            :label="item.label"
                                            :value="item.value"
                                    />
                                </el-select>
                            </div>
                        </div>
                    </el-col>
                    <el-col :span="8">
                        <div class="leftTop">
                            <span class="angle1"></span>
                            <span class="angle2"></span>
                            <span class="angle3"></span>
                            <span class="angle4"></span>
                            <div class="left1">
                                <div class="grid-content ep-bg-purple" id="mychart9" style="height: 400px;"></div>
                                <el-select
                                        class="mySelect"
                                        size="small"
                                        v-model="county_value"
                                        placeholder="Select"
                                        style="width: 200px"
                                >
                                    <el-option
                                            v-for="item in county_options"
                                            :key="item.value"
                                            :label="item.label"
                                            :value="item.value"
                                    />
                                </el-select>
                            </div>
                        </div>
                    </el-col>

                </el-row>
            </el-col>
        </el-row>


        <el-row :gutter="24">
            <el-col :span="24">
                <el-row :gutter="24">
                    <el-col :span="8">
                        <div class="leftTop">
                            <span class="angle1"></span>
                            <span class="angle2"></span>
                            <span class="angle3"></span>
                            <span class="angle4"></span>
                            <div class="left1">
                                <div class="grid-content ep-bg-purple" id="mychart11" style="height: 400px;"></div>
                            </div>
                        </div>
                    </el-col>
                    <el-col :span="8">
                        <div class="leftTop">
                            <span class="angle1"></span>
                            <span class="angle2"></span>
                            <span class="angle3"></span>
                            <span class="angle4"></span>
                            <div class="left1">
                                <div class="grid-content ep-bg-purple" id="mychart13" style="height: 400px;"></div>
                            </div>
                        </div>
                    </el-col>
                    <el-col :span="8">
                        <div class="leftTop">
                            <span class="angle1"></span>
                            <span class="angle2"></span>
                            <span class="angle3"></span>
                            <span class="angle4"></span>
                            <div class="left1">
                                <div class="grid-content ep-bg-purple" id="mychart12" style="height: 400px;"></div>
                            </div>
                        </div>
                    </el-col>

                </el-row>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import {onMounted, reactive, ref, watch} from "vue";
import * as echarts from "echarts";
import axios from "axios";

export default {
    components: {},
    setup() {
        const zones_value = ref('温泉街道办责任区')
        const county_value = ref('安宁')
        const grid_value = ref('新-安宁上城区网格')

        const zones_options = ref([{
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
        }])
        const county_options = ref([{
            value: 'Option1',
            label: 'Option1',
        }])
        const grid_options =  ref([{
            value: 'Option1',
            label: 'Option1',
        }])

        let grid_option_01 = ref({
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'shadow'
                }
            },
            title: {
                text: '网格装维服务',
                left: 'center',
                subtext: "当前排名: 11, 评分: 78.97" ,
                subtextStyle: { // 副标题样式
                    color: '#909090', // 副标题颜色
                    fontSize: 14, // 副标题字体大小
                },
                textStyle: {
                    color: '#75deef',
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
            xAxis: {
                type: 'value',
                splitLine: {
                    show: false
                },
                axisLabel: {
                    color: '#75deef'
                }
            },
            yAxis: {
                type: 'category',
                data: ['网格一'],
                splitLine: {
                    show: false
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
                barWidth: '40%',
                data: [320],
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

                ]
        });
        let grid_option_02 = ref({
            title: {
                text: '网格上网质量',
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
                data: [
                    {value: 289, name: '上网质量1-6分'},
                    {value: 345, name: '上网质量7-9分'},
                    {value: 368, name: '上网质量10分'},

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
                    fontSize: "14px",
                    formatter: '{c},\n{d}%'
                },
                color: ["red", "yellow", "blue"],
            }]
        });

        let county_option_01 = ref({
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'shadow'
                }
            },
            title: {
                text: '区县装维服务',
                left: 'center',
                subtext: "当前排名：11, 评分：78.97" ,
                subtextStyle: { // 副标题样式
                    color: '#909090', // 副标题颜色
                    fontSize: 14, // 副标题字体大小
                },
                textStyle: {
                    color: '#75deef',
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
            xAxis: {
                type: 'value',
                splitLine: {
                    show: false
                },
                axisLabel: {
                    color: '#75deef'
                }
            },
            yAxis: {
                type: 'category',
                data: ['网格一'],
                splitLine: {
                    show: false
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
                barWidth: '40%',
                data: [320],
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

                ]
        });
        let county_option_02 = ref({
            title: {
                text: '区县上网质量',
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
                data: [
                    {value: 289, name: '上网质量1-6分'},
                    {value: 345, name: '上网质量7-9分'},
                    {value: 368, name: '上网质量10分'},

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
                    fontSize: "14px",
                    formatter: '{c},\n{d}%'
                },
                color: ["red", "yellow", "blue" ],
            }]
        });

        let zones_option_01 = ref({
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'shadow'
                }
            },
            title: {
                text: '责任区装维服务',
                left: 'center',
                subtext: "当前排名：11, 评分：78.97" ,
                subtextStyle: { // 副标题样式
                    color: '#909090', // 副标题颜色
                    fontSize: 14, // 副标题字体大小
                },
                textStyle: {
                    color: '#75deef',
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
            xAxis: {
                type: 'value',
                splitLine: {
                    show: false
                },
                axisLabel: {
                    color: '#75deef'
                }
            },
            yAxis: {
                type: 'category',
                data: ['网格一'],
                splitLine: {
                    show: false
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
                barWidth: '40%',
                data: [320],
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

                ]
        });
        let zones_option_02 = ref({
            title: {
                text: '责任区上网质量',
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
                data: [
                    {value: 289, name: '上网质量1-6分'},
                    {value: 345, name: '上网质量7-9分'},
                    {value: 368, name: '上网质量10分'},

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
                    fontSize: "14px",
                    formatter: '{c},\n{d}%'
                },
                color: ["red", "yellow", "blue"],
            }]
        });


        function grid(value) {
            console.log(value)
            const grid_response =  axios.get("/api/screen/rank/grid/?value="+value).then( (grid_response)=>{
                 console.log(grid_response.data)
                grid_options.value = grid_response.data.label
                grid_option_01.value.series[0].data =  grid_response.data.install.one_to_six_points_count
                grid_option_01.value.series[1].data = grid_response.data.install.seven_to_nine_points_count
                grid_option_01.value.series[2].data = grid_response.data.install.ten_points_count
                grid_option_01.value.title.subtext = "当前排名: "+grid_response.data.rank +","+ "评分: "+ grid_response.data.score

                    // 网格
                let grid_option_01_echartBox = document.getElementById("mychart8");
                grid_option_01_echartBox.removeAttribute('_echarts_instance_')
                let grid_option_01_myChart = echarts.init(grid_option_01_echartBox);
                grid_option_01_myChart.setOption(grid_option_01.value);

                grid_option_02.value.series[0].data[0] = {value: grid_response.data.internet.one_to_six_points_count[0], name: '上网质量1-6分'}
                grid_option_02.value.series[0].data[1] = {value: grid_response.data.internet.seven_to_nine_points_count[0], name: '上网质量7-9分'}
                grid_option_02.value.series[0].data[2] = {value: grid_response.data.internet.ten_points_count[0], name: '上网质量10分'}

                let grid_option_02_echartBox = document.getElementById("mychart11");
                grid_option_02_echartBox.removeAttribute('_echarts_instance_')
                let grid_option_02_myChart = echarts.init(grid_option_02_echartBox);
                grid_option_02_myChart.setOption(grid_option_02.value);

            });
        }

        watch(grid_value, (value) => {
            grid(value)

        })

        function county(value) {
            console.log(value)

            const county_response =  axios.get("/api/screen/rank/county/?value="+value).then( (county_response)=>{
                 console.log(county_response.data)
                county_options.value = county_response.data.label

                county_option_01.value.series[0].data =  county_response.data.install.one_to_six_points_count
                county_option_01.value.series[1].data = county_response.data.install.seven_to_nine_points_count
                county_option_01.value.series[2].data = county_response.data.install.ten_points_count
                county_option_01.value.title.subtext = "当前排名: "+county_response.data.rank +","+ "评分: "+ county_response.data.score

                    // 网格
                let county_option_01_echartBox = document.getElementById("mychart9");
                county_option_01_echartBox.removeAttribute('_echarts_instance_')
                let county_option_01_myChart = echarts.init(county_option_01_echartBox);
                county_option_01_myChart.setOption(county_option_01.value);

                county_option_02.value.series[0].data[0] = {value: county_response.data.internet.one_to_six_points_count[0], name: '上网质量1-6分'}
                county_option_02.value.series[0].data[1] = {value: county_response.data.internet.seven_to_nine_points_count[0], name: '上网质量7-9分'}
                county_option_02.value.series[0].data[2] = {value: county_response.data.internet.ten_points_count[0], name: '上网质量10分'}

                let county_option_02_echartBox = document.getElementById("mychart12");
                county_option_02_echartBox.removeAttribute('_echarts_instance_')
                let county_option_02_myChart = echarts.init(county_option_02_echartBox);
                county_option_02_myChart.setOption(county_option_02.value);

            });

        }

        watch(county_value, (value) => {
            county(value)
        })

        function zones(value) {
            console.log(value)
            const zones_response =  axios.get("/api/screen/rank/zone/?value="+value).then( (zones_response)=>{
                 console.log(zones_response.data)
                zones_options.value = zones_response.data.label

                zones_option_01.value.series[0].data =  zones_response.data.install.one_to_six_points_count
                zones_option_01.value.series[1].data = zones_response.data.install.seven_to_nine_points_count
                zones_option_01.value.series[2].data = zones_response.data.install.ten_points_count
                zones_option_01.value.title.subtext = "当前排名: "+zones_response.data.rank +","+ "评分: "+ zones_response.data.score

                    // 网格
                let zones_option_01_echartBox = document.getElementById("mychart10");
                zones_option_01_echartBox.removeAttribute('_echarts_instance_')
                let zones_option_01_myChart = echarts.init(zones_option_01_echartBox);
                zones_option_01_myChart.setOption(zones_option_01.value);

                zones_option_02.value.series[0].data[0] = {value: zones_response.data.internet.one_to_six_points_count[0], name: '上网质量1-6分'}
                zones_option_02.value.series[0].data[1] = {value: zones_response.data.internet.seven_to_nine_points_count[0], name: '上网质量7-9分'}
                zones_option_02.value.series[0].data[2] = {value: zones_response.data.internet.ten_points_count[0], name: '上网质量10分'}

                let zones_option_02_echartBox = document.getElementById("mychart13");
                zones_option_02_echartBox.removeAttribute('_echarts_instance_')
                let zones_option_02_myChart = echarts.init(zones_option_02_echartBox);
                zones_option_02_myChart.setOption(zones_option_02.value);

            });


        }

        watch(zones_value, (value) => {
            zones(value)
        })


        onMounted(async () => {

            grid(grid_value.value)
            county(county_value.value)
            zones(zones_value.value)

        });

        return {
            zones_value,
            grid_value,
            county_value,
            zones_options,
            grid_options,
            county_options,

        }
    },
};
</script>
<style lang="less" scoped>
.el-row {
  margin-bottom: 20px;
}

.el-row:last-child {
  margin-bottom: 0;
}

.mySelect {
  width: 100px;
  position: absolute;
  top: 28px;
}
</style>