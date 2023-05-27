<!-- 用户注册界面  -->
<template>
  <div class="wrapper">
    <div class="register-container">
      <h2 class="title">用户注册</h2>
      <form class="form">
        <div class="form-group">
          <label for="username">用户名</label>
          <input type="text" id="username" v-model="pwdUserRegisterForm.username" placeholder="请输入用户名" required>
        </div>
        <div class="form-group">
          <label for="password">密码</label>
          <input type="password" id="password" v-model="pwdUserRegisterForm.password" placeholder="请输入密码" required>
        </div>
        <div class="form-group">
          <label for="confirm-password">确认密码</label>
          <input type="password" id="confirm-password" v-model="confirmPassword" placeholder="请再次输入密码" required>
        </div>
        <button type="submit" class="btn" @click="register">注册</button>
      </form>
      <div class="footer">
        <span>已有账号？</span>
        <a href="#" @click.prevent="$router.push('/login')">立即登录</a>
      </div>
    </div>
  </div>
</template>

<script>
import Axios from "axios"
import { userRegister } from "../util/api"
export default {
  data() {
    return {
      pwdUserRegisterForm: {
        username: '',
        password: ''
      },
      confirmPassword: ''
    }
  },
  methods: {
    register() {
      // 这里可以添加注册的逻辑，比如发送请求到后端保存用户信息
      if (this.pwdUserRegisterForm.password != this.confirmPassword) {
        alert('密码不一致')
      }
      else if (this.pwdUserRegisterForm.username.length < 6) {
        alert('用户名太短')
      }
      else if (this.pwdUserRegisterForm.password.length < 6) {
        alert('密码太短')
      }
      else if (this.pwdUserRegisterForm.password.length > 40) {
        alert('密码太长')
      }
      else {
        userRegister(this.pwdUserRegisterForm).then((res) => {
          if (res.status == 200) {
            console.log("ok")
          }
          else {
            debugger
            console.log("出错了")
            debugger
          }
        })
      }

    },
    goToRecommend() {
      this.$router.push('/recommend');
    }
  }
}
</script>

<style>
.wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f5f5;
}

.register-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  max-width: 500px;
  width: 100%;
  background-color: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

.title {
  /* font-size: 24px;
  margin-bottom: 20px; */
  text-align: center;
}

.form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.form-group {
  margin-bottom: 20px;
  width: 100%;
  max-width: 400px;
  text-align: left;
}

label {
  display: block;
  font-size: 16px;
  margin-bottom: 5px;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.btn {
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 20px;
}

.footer {
  margin-top: 20px;
  font-size: 14px;
  color: #666;
}

.footer a {
  color: #007bff;
  text-decoration: none;
}

.footer a:hover {
  text-decoration: underline;
}
</style>