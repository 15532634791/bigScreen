<template>
    <div class="login-container">
        <div class="login-background"></div>
        <div class="login-form">
            <el-card class="login-card">
                <h1 class="login-title">
                    <el-text class="mx-1" type="primary" size="large" >大屏展示系统</el-text >
                </h1>
                <el-form
                    ref="loginForm"
                    :rules="rules"
                    :model="loginData"
                    label-width="80px"
                >
                    <el-form-item prop="username">
                        <el-input size="large" v-model="loginData.username" placeholder="Username">
                            <template #prepend>
                                <el-icon style="font-size: 24px;"><User /></el-icon>
                            </template>
                        </el-input>
                    </el-form-item>
                    <el-form-item prop="password">
                        <el-input size="large" type="password" v-model="loginData.password" placeholder="PassWord" @keyup.enter.native="login">
                            <template #prepend>
                                <el-icon style="font-size: 24px;"><Key /></el-icon>
                            </template>
                        </el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button style="width:100%" type="primary" @click="login"> 登 录</el-button >
                    </el-form-item>
                </el-form>
            </el-card>
        </div>
    </div>
</template>

<script>
import { reactive } from "vue";
import {
    ElForm,
    ElFormItem,
    ElInput,
    ElButton,
    ElCard,
    ElMessage,
} from "element-plus";
import { useRouter } from "vue-router";
import axios from "axios";

export default {
    components: {
        ElForm,
        ElFormItem,
        ElInput,
        ElButton,
        ElCard,
    },
    setup() {
        const loginData = reactive({
            username: "",
            password: "",
        });

        const rules = {
            username: [
                { required: true, message: "请输入用户名", trigger: "blur" },
            ],
            password: [
                { required: true, message: "请输入密码", trigger: "blur" },
            ],
        };
        const router = useRouter();
        const login = () => {
            router.push("/screen");
            axios .post("/api/user/login/", {
                username: loginData.username,
                password: loginData.password,
            }).then((response) => {
                const token = response.data.token;
                localStorage.setItem("userId", response.data.id);
                localStorage.setItem("token", token);
                localStorage.setItem("username", response.data.username);
                router.push("/screen");
            }).catch((error) => {
                ElMessage({
                    message: "用户名或密码错误",
                    type: "error",
                });
            });
        };

        return {
            loginData,
            rules,
            login,
        };
    },
};
</script>

<style scoped>
.login-container {
    display: flex;
    height: 100vh;
    z-index: 1;
    flex: 1;
    justify-content: center;
    align-items: center;
}

.login-background {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-image: url("@/assets/background.jpg");
    background-size: cover;
}

.login-form {
    z-index: 1;
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
}

.login-card {
    width: 550px;
    padding: 20px;
    background-color: #f5f7fa;
}

.login-title {
    font-size: 20px;
    margin-bottom: 20px;
    text-align: center;
}

.login-form .el-form-item:last-child {
    text-align: center;
}

.login-form .el-button {
    margin-left: auto;
    margin-right: auto;
    display: block;
}

.n-gradient-text {
    font-size: 30px;
}
</style>