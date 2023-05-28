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
              <el-input placeholder="请输入密码" type="password" show-password prefix-icon="el-icon-lock"
                v-model="pwdLoginForm.password" required>
              </el-input>
            </el-form-item>
            <!-- 按钮区域 -->
            <el-form-item class="login-btns">
              <button class="el-button el-button--primary" @click="pwdUserLogin" :disabled="loading">{{ loading ? '登录中' :
                '登录' }}</button>
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
              <el-input placeholder="请输入密码" type="password" show-password prefix-icon="el-icon-lock"
                v-model="pwdLoginForm.password">
              </el-input>
            </el-form-item>
            <!-- 按钮区域 -->
            <el-form-item class="login-btns">
              <button class="el-button el-button--primary" @click="pwdMerchantLogin" :disabled="loading">{{ loading ? '登录中'
                : '登录' }}</button>
              <button class="el-button el-button--text" @click='goMerchantRegister'>注册</button>
            </el-form-item>
          </el-form>
        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>

<script>
import { login } from "../util/api";
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
    pwdUserLogin() {
      // 这里可以添加注册的逻辑，比如发送请求到后端保存用户信息
      console.log(`用户名：${this.pwdLoginForm.username}，密码：${this.pwdLoginForm.password}`)
      login(this.pwdLoginForm).then((res) => {
        if (res.status == 200) {
          this.$router.push({ path: '/recommend', query: { username: this.pwdLoginForm.username, business_id: res.data.business_id } })
        }
        else {
          console.log("出错了")
        }
      })
    },
    pwdMerchantLogin() {
      // 这里可以添加注册的逻辑，比如发送请求到后端保存用户信息
      console.log(`用户名：${this.pwdLoginForm.username}，密码：${this.pwdLoginForm.password}`)
      login(this.pwdLoginForm).then((res) => {
        if (res.status == 200) {
          this.$router.push({ path: '/merchantinformationmanagement', query: { username: this.pwdLoginForm.username } })
        }
        else {
          console.log("出错了")
        }
      })
    },
    handleClick(tab, event) {
      console.log(tab, event)
    },
    goUserRegister() {
      debugger
      this.$router.push('/userregister')
    },
    goMerchantRegister() {
      debugger
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
  background-size: cover;
  /* 背景图覆盖整个页面 */
  background-repeat: no-repeat;
  /* 背景图不重复 */
}

.title {
  margin-bottom: 30px;
  text-align: center;
}

.title h2 {
  font-size: 50px;
  font-family: "Arial", sans-serif;
  text-align: center;
  color: #fff;
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

.el-form-item__label {
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
}</style>

