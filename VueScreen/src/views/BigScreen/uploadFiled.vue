<template>
    <el-row>
        <el-col :span="16"></el-col>
        <el-col :span="8">
            <el-row>
                <el-col :span="16">
                    <el-upload
                            class="upload-demo"
                            action="/api/screen/upload/"
                            :on-change="handleChange"
                    >
                        <el-button type="primary" style="width: 90px">
                            <el-icon>
                                <UploadFilled/>
                            </el-icon>
                            上传
                        </el-button>
                        <el-button type="primary" @click="exitLogin">退出</el-button>
                    </el-upload>
                </el-col>

            </el-row>
        </el-col>
    </el-row>
</template>
<script>
import {useRouter} from "vue-router";
import {ElNotification} from 'element-plus'

export default {
    setup() {
        const router = useRouter();
        // 上传函数
        const handleChange = async (file) => {
            // 判断最后上传的文件是否已经完成上传
            if (file.status === 'success') {
                ElNotification.success({
                    title: file.name,
                    message: '文件上传成功,请稍后刷新页面',
                    showClose: true,
                });
            } else if (file.status === 'fail') {
                ElNotification.error({
                    title: file.name,
                    message: '文件上传失败',
                    showClose: true,
                });
            }


        };

        // 删除前的函数

        const exitLogin = () => {
            localStorage.removeItem('token')
            localStorage.removeItem('username')
            localStorage.removeItem('userId')
            router.push("/login")
            return

        }
        return {

            handleChange,
            exitLogin
        }
    }
}
</script>
  