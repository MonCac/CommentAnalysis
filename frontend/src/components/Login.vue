<!-- 登陆界面-->
<template>
  <div class="login-container">
    <div class="title">
      <h2 style="text-align:center;">登录</h2>
    </div>
    <!-- 登录表单区域-->
    <div class="login-box">
      <el-tabs v-model="activeName" @tab-click="handleClick">
        <el-tab-pane label="用户登录" name="user">
          <!-- 用户账号密码登录表单 -->
          <el-form ref="pwdLoginFormRef" :model="pwdLoginForm" :rules="pwdLoginFormRules">
            <!-- 用户名 -->
            <el-form-item prop="username" label="用户名">
              <el-input placeholder="请输入用户名" prefix-icon="el-icon-user-solid" v-model="pwdLoginForm.username" required>
              </el-input>
            </el-form-item>
            <!-- 密码 -->
            <el-form-item prop="password" label="密码">
              <el-input placeholder="请输入密码" type="password" show-password prefix-icon="el-icon-lock" v-model="pwdLoginForm.password" required>
              </el-input>
            </el-form-item>
            <!-- 按钮区域 -->
            <el-form-item class="login-btns">
              <button class="el-button el-button--primary" @click="pwdLogin" :disabled="loading">{{loading ? '登录中' : '登录'}}</button>
              <button class="el-button el-button--text" @click='goUserRegister'>注册</button>
            </el-form-item>
          </el-form>
        </el-tab-pane>
        <el-tab-pane label="商户登录" name="merchant">
          <!-- 账号密码登录表单 -->
          <el-form ref="pwdLoginFormRef" :model="pwdLoginForm" :rules="pwdLoginFormRules">
              <!-- 用户名 -->
              <el-form-item prop="username" label="商户名">
                <el-input placeholder="请输入商户名" clearable prefix-icon="el-icon-user-solid" v-model="pwdLoginForm.username">
                </el-input>
              </el-form-item>
              <!-- 密码 -->
              <el-form-item prop="password" label="密码">
                <el-input placeholder="请输入密码" type="password" show-password prefix-icon="el-icon-lock" v-model="pwdLoginForm.password">
                </el-input>
              </el-form-item>
              <!-- 按钮区域 -->
              <el-form-item class="login-btns">
                <button class="el-button el-button--primary" @click="pwdLogin" :disabled="loading">{{loading ? '登录中' : '登录'}}</button>
                <button class="el-button el-button--text" @click='goMerchantRegister'>注册</button>
              </el-form-item>
            </el-form>
        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>

<script>
import {
    ref,
    reactive,
    toRefs,
    getCurrentInstance
  } from 'vue'
  import qs from 'qs'
  import axios from 'axios'
  import {
    useRouter
  } from 'vue-router'
  export default {
    data() {
      return {
        activeName: 'user',
        pwdLoginForm: {
          username: '',
          password: ''
        },
        loading: false
      }
    },
    methods: {
      pwdLogin: async () => {
        state.loading = true
        const obj = {
          username: state.pwdLoginForm.username,
          password: state.pwdLoginForm.password
        }
        try {
          const res = await new proxy.$request(proxy.$urls.m().pwdLogin, qs.stringify(obj)).modepost()
          console.log(res)
          if (res.data.success != true) {
            new proxy.$tips(res.data.message, 'warning').mess_age()
          } else {
            new proxy.$tips(res.data.message, 'success').mess_age()
            localStorage.setItem('token', res.data.data.token)
            debugger
            console.log(1234)
            // 成功跳转页面
            router.push('/recommend') // 使用 Vue Router 实现跳转到 home 页面
            debugger
          }recommend
          state.loading = false
        } catch (e) {
          state.loading = false
          new proxy.$tips('服务器发生错误', 'error').mess_age()
        }
      },
      handleClick(tab, event) {
        console.log(tab, event)
      },
      goUserRegister() {
        this.$router.push('/userregister')
      },
      goMerchantRegister() {
        this.$router.push('/merchantregister')
      }
    }
  }
</script>

<style scoped>
  .login-container {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    max-width: 100%;
    margin: 0 auto;
    text-align: center;
    background-image: url("../img/normal.jpeg");
    background-size: cover; /* 背景图覆盖整个页面 */
    background-repeat: no-repeat; /* 背景图不重复 */
  }

  .title {
    margin-bottom: 30px;
    text-align: center;
  }

  .title h2 {
    font-size: 50px;
    font-family:"Arial", sans-serif;
    text-align:center;
  }

  .login-box {
    width: 100%;
    max-width: 400px;
    background-color: #fff;
    padding: 40px;
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  }

  .login-btns {
    margin-top: 30px;
    text-align: center;
  }

  .el-form-item__label{
    font-size: 18px;
  }

  .el-input__inner {
    font-size: 18px;
  }

  /* Style for buttons */
  .el-button--primary {
    margin-right: 20px;
  }

  .el-button--text {
    color: #409EFF;
  }
</style>

