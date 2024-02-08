<template>
    <div class="common-layout">
        <el-container>
            <el-header>
                <el-row>
                    <el-col :span="8" class="pageTab">
                        <el-text @click="page1">首页</el-text>
                        <el-text @click="page2">详细</el-text>
                    </el-col>
                    <el-col :span="8"><div class="title">可视化大屏分析</div></el-col>
                    <el-col :span="8" class="pageTab">
                        <uploadFiled/>
                    </el-col>
<!--                    <el-col :span="4"> <span style="color: white"> </span></el-col>
                    <el-col :span="2"> <span style="color: white; margin-top: 15px">上传</span></el-col>
                    <el-col :span="2"> <span style="color: white; margin-top: 15px">退出</span></el-col>-->
                </el-row>
            </el-header>
            <el-main>
                <div v-if="tab1">
                    <page1 />
<!--                    <el-row :gutter="24">-->
<!--                        <el-col :span="24">-->
<!--                            <el-row :gutter="24">-->
<!--                                <el-col :span="8" > <ScreenPage8/></el-col>-->
<!--                                <el-col :span="8" ><ScreenPage9/></el-col>-->
<!--                                <el-col :span="8" ><ScreenPage10/></el-col>-->
<!--                            </el-row>-->
<!--                        </el-col>-->
<!--                    </el-row>-->

<!--                    <el-row :gutter="24">-->
<!--                        <el-col :span="24">-->
<!--                            <el-row :gutter="24">-->
<!--                                <el-col :span="8" ><ScreenPage11/></el-col>-->
<!--                                <el-col :span="8" ><ScreenPage12/></el-col>-->
<!--                                <el-col :span="8" ><ScreenPage13/></el-col>-->
<!--                            </el-row>-->
<!--                        </el-col>-->
<!--                    </el-row>-->


                </div>
                <div v-if="tab2">
                    <el-row :gutter="24">
                        <el-col :span="6" > 
                            <el-row :gutter="24">
                                <el-col :span="24" ><ScreenPage1/></el-col>
                            </el-row>
                            <el-row :gutter="24">
                                <el-col :span="24" ><ScreenPage2/></el-col>
                            </el-row>
                        </el-col>
                        <el-col :span="12" ><ScreenPage3/></el-col>
                        <el-col :span="6" >
                            <el-row :gutter="24">
                                <el-col :span="24" ><ScreenPage4/></el-col>
                            </el-row>
                            <el-row :gutter="24">
                                <el-col :span="24" ><ScreenPage5/></el-col>
                            </el-row>
                        </el-col>
                    </el-row>
                    <el-row :gutter="24">
                        <el-col :span="12" ><ScreenPage6/></el-col>
                        <el-col :span="12" ><ScreenPage7/></el-col>
                    </el-row>
                </div>
            </el-main>
        </el-container>
    </div>
</template>

<script>
    import { ref } from "vue";
    import page1 from './page1.vue';
    import ScreenPage1 from './ScreenPage1.vue';
    import ScreenPage2 from './ScreenPage2.vue';
    import ScreenPage3 from './ScreenPage3.vue';
    import ScreenPage4 from './ScreenPage4.vue';
    import ScreenPage5 from './ScreenPage5.vue';
    import ScreenPage6 from './ScreenPage6.vue';
    import ScreenPage7 from './ScreenPage7.vue';
    import ScreenPage8 from './ScreenPage8.vue';
    import ScreenPage9 from './ScreenPage9.vue';
    import ScreenPage10 from './ScreenPage10.vue';
    import ScreenPage11 from './ScreenPage11.vue';
    import ScreenPage12 from './ScreenPage12.vue';
    import ScreenPage13 from './ScreenPage13.vue';
    import uploadFiled from "./uploadFiled.vue";
    export default {
        components: {
            page1,
            ScreenPage1,
            ScreenPage2,
            ScreenPage3,
            ScreenPage4,
            ScreenPage5,
            ScreenPage6,
            ScreenPage7,
            ScreenPage8,
            ScreenPage9,
            ScreenPage10,
            ScreenPage11,
            ScreenPage12,
            ScreenPage13,
            uploadFiled
        },
        setup() {
            const tab2 = ref(true);
            const tab1 = ref();
            const page1 = () =>{
                tab1.value = false
                tab2.value = true
            }
            const page2 = () =>{
                tab1.value = true
                tab2.value = false
            }
            return {
                tab1,
                tab2,
                page1,
                page2
            }
        },
    };
</script>

<style lang="less" scoped>
    .title{
        height: 80px;
        font-size: 30px;
        line-height: 80px;
        text-align: center;
        color: #75deef;
        align-items: center;
        letter-spacing: 10px;
    }
    .pageTab{
        height: 80px;
        font-size: 30px;
        line-height: 80px;
        .el-text{
            color: #75deef;
            margin-right: 20px;
        }
        .el-text:hover{
            cursor: pointer;
            // font-size: 18px;
            border-bottom: 1px solid #75deef;
        }
    }
    .el-row {
        margin-bottom: 20px;
    }
    .el-row:last-child {
        margin-bottom: 0;
    }
    .el-col {
        border-radius: 4px;
    }

    .grid-content {
        height: 50%;
    }
</style>