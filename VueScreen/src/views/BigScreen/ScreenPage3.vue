<template>
    <div class="common-layout">
        <el-container>
            <el-header class="header" style="height: 153px;">
                <el-row>
                    <el-col :span="12" class="topq">
                        <p>装维满意度</p>
                        <div class="top">1-6分: {{ install_1_6_value }}</div>
                        <div class="top">7-9分: {{ install_7_9_value }}</div>
                        <div class="top">其他: {{ install_other_value }}</div>
                    </el-col>
                    <el-col :span="12" class="topq">
                        <p>上网质量满意度</p>
                        <div class="bot">1-6分: {{ internet_1_6_value }}</div>
                        <div class="bot">7-9分: {{ internet_7_9_value }}</div>
                        <div class="bot"> 其他: {{ internet_other_value }}</div>
                    </el-col>
                </el-row>

            </el-header>
            <el-main style="overflow-x: hidden;">
                <div class="leftTop">
                    <span class="angle1"></span>
                    <span class="angle2"></span>
                    <span class="angle3"></span>
                    <span class="angle4"></span>
                    <div class="left1">
                        <div class="grid-content" id="mychart3"></div>
                    </div>
                </div>
            </el-main>
        </el-container>
    </div>
</template>
<script>
import {onMounted, reactive, ref} from "vue";
import * as echarts from "echarts";
import axios from "axios";

export default {
    setup() {
        const install_other_value = ref()
        const install_7_9_value = ref()
        const install_1_6_value = ref()

        const internet_other_value = ref()
        const internet_7_9_value = ref()
        const internet_1_6_value = ref()


        let option = reactive({
            title: {
                text: '区县满意度Top15',
                left: 10,
                top: 10,
                textStyle: {
                    color: '#75deef',
                    fontSize: "20px"
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
                    '全省', '版纳', '保山', '大理', '怒江', '普洱', "数据1", "数据1", "数据1", "数据1",
                    "数据1", "数据1", "数据1", "数据1", "数据1", "数据1", "数据1", "数据1", "数据1", "数据1"
                ],
                splitLine: {
                    show: false
                },
                axisLabel: {
                    color: '#75deef',
                    rotate: 40
                }
            },
            yAxis: {
                type: 'value',
                splitLine: {
                    show: false
                },
                axisLabel: {
                    color: '#75deef'
                }
            },
            series: [{
                name: '',
                type: 'bar',
                barWidth: 10,
                data: [
                    1230, 1200, 1190, 1180, 1170, 1100, 1050, 1000, 980, 950,
                    900, 850, 800, 750, 700, 650, 600, 550, 500, 450
                ],
                itemStyle: {
                    borderRadius: [50, 50, 0, 0],
                    color: "yellow  "
                }
            }]
        });

        onMounted(async () => {
            try {
                const response = await axios.get("/api/screen/screen/satisfaction/county/");

                option.series[0].data = response.data.comprehensive_score_list;
                option.xAxis.data = response.data.counties;
                // console.log(option)
                let echartBox = document.getElementById("mychart3");
                echartBox.removeAttribute("_echarts_instance_");
                let myChart = echarts.init(echartBox);
                myChart.setOption(option);


                const internet_response = await axios.get("/api/screen/score/internet/quality/");
                const maintain_response = await axios.get("/api/screen/score/install/maintain/");

                // console.log(internet_response.data)
                // console.log(maintain_response.data)

                install_1_6_value.value = maintain_response.data.one_to_six_points_count
                internet_1_6_value.value = internet_response.data.one_to_six_points_count
                //
                install_7_9_value.value = maintain_response.data.seven_to_nine_points_count
                internet_7_9_value.value = internet_response.data.seven_to_nine_points_count
                //
                install_other_value.value = maintain_response.data.other_count
                internet_other_value.value = internet_response.data.other_count


            } catch (error) {
                console.log(error);
            }
        });
        return {
            install_7_9_value,
            install_other_value,
            install_1_6_value,
            internet_other_value,
            internet_7_9_value,
            internet_1_6_value

        };


    },
};
</script>
<style lang="less" scoped>
#mychart3 {
  height: 310px;
}

.header {
  color: #fff;

  .grid-content {
    //background-color: #2871EA;
  }
}

.ep-bg-purple {
  height: 175px;
  font-size: 28px;
  text-align: center;
  line-height: 150px;
}

.topq {
  height: 100px;
  text-align: center;

  .left_top, .right_bot {
    margin-left: 7%;
  }

  .top {
    width: 30%;
    height: 100%;
    margin-right: 5px;
    float: left;
    line-height: 100px;
    background-color: #FACE49;
  }

  .bot {
    width: 30%;
    height: 100%;
    margin-right: 5px;
    float: left;
    line-height: 100px;
    background-color: #60E11C;
  }

  p {
    margin: 0;
    padding: 0 0 0 10px;
    line-height: 30px;
    font-weight: bold;
    color: #75deef;
    //letter-spacing: 10px;
  }

}

.clear:after {
  display: block;
  content: "";
  clear: both;

}

</style>