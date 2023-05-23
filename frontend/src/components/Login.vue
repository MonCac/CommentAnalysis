<!-- 登陆界面-->
<template>
    <div class="login-container">
      <h2 class="title">用户登录</h2>
      <form class="form" @submit.prevent="login">
        <div class="form-group">
          <label for="username">用户名</label>
          <input type="text" id="username" v-model="username" required>
        </div>
        <div class="form-group">
          <label for="password">密码</label>
          <input type="password" id="password" v-model="password" required>
        </div>
        <button type="submit" class="btn">登录</button>
      </form>
      <button @click="goUserRegister">用户注册</button>
      <router-link :to="{path: '/userregister'}"> 用户注册</router-link>
    </div>
  </template>
  
<script>
export default {
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    login() {
    // 这里可以添加登录的逻辑，比如发送请求到后端验证用户名和密码
      console.log(`用户名：${this.username}，密码：${this.password}`)
    },
    goUserRegister() {
      this.$router.push('/userregister')
    }
  }
  
}
</script>
  
<style>
.login-container {
  max-width: 500px;
  margin: 0 auto;
  text-align: center;
}
.title {
  font-size: 24px;
  margin-bottom: 20px;
}
.form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.form-group {
  margin-bottom: 20px;
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
  font-size: 16px;
}
</style>