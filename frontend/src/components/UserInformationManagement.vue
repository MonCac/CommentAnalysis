<!-- 用户个人信息修改页面  -->
<template>
  <div>
    <nav class="nav">
      <!-- nav-menu -->
      <el-row class="row">
        <el-col :span="4"></el-col>
        <el-col :span="8">
          <el-input v-model="input" placeholder="请输入搜索内容">
            <el-button slot="append" @click="search">搜索</el-button></el-input
          ></el-col
        >
        <el-col :span="12">
          <div class="nav-info" v-if="loginData">
            <div @click="home">首页</div>
            <div @click="list">书籍列表</div>
            <div @click="order">订单查询</div>
            <div @click="customer">客服</div>
            <div @click="logout">[ 登 出 ]</div>
          </div>
          <div class="nav-info" v-if="!loginData">
            <div @click="login">[ 未 登 录 ]</div>
          </div></el-col
        >
      </el-row>
      <!-- nav-info-end -->
    </nav>

    <!-- 个人信息 -->
    <div class="person">
      <div class="title">
        <div class="name">用户信息</div>
        <el-button type="success" @click="changeMessage">编辑用户信息</el-button>
      </div>
      <el-form ref="form" :model="form" label-width="80px" disabled>
        <el-form-item label="姓名">
          <el-input v-model="form.uname"></el-input>
        </el-form-item>
        <el-form-item label="联系方式">
          <el-input v-model="form.userPhone"></el-input>
        </el-form-item>
        <el-form-item label="性别">
          <el-input v-model="form.usex"></el-input>
        </el-form-item>
        <el-form-item label="出生日期">
          <el-input v-model="form.ubirth"></el-input>
        </el-form-item>
        <el-form-item label="住址">
          <el-input v-model="form.uaddress"></el-input>
        </el-form-item>
      </el-form>
    </div>
    <!-- person-info-end -->

    <footer>
      <a href="#">©2023 点评数据分析与推荐</a>
      <a href="#"
        >意见反馈&nbsp;&nbsp;&nbsp;联系我们&nbsp;&nbsp;&nbsp;隐私权声明&nbsp;&nbsp;&nbsp;使用条款</a
      >
    </footer>
  </div>
</template>
<script>
// import { getSession } from '@/util/util';
// import { get, deleteData } from '../http/request';
export default {
  data() {
    return {
      loginData: false,
      input: '',
      form: {
        userPhone: '',
        uname: '',
        uaddress: '',
        usex: '',
        ubirth: '',
      },
      activeName: 'first',
      listData: [],
      userData: [],
    };
  },
  async created() {
    this.getList();
  },
  mounted() {
    this.loginData = getSession('loginData');
  },
  methods: {
    async getList() {
      const data = await get('/api/user/info');
      if (data) {
        this.form = {
          ...data.data,
        };
        this.userData = data.data;
      } else {
        this.$message({
          showClose: true,
          message: '登录失效,请重新登陆',
          type: 'error',
        });
        this.$router.push('/login');
      }

      const list = await get(
        `https://oldbook.fansionia.xyz/book/getByUser/${data.data.uid}`
      );
      this.listData = list.data;
    },
    login() {
      this.$router.push('/login');
    },
    home() {
      this.$router.push('/');
    },
    goDetail(item) {
      this.$router.push({
        path: '/detail',
        query: { id: item.bid },
      });
    },
    search() {
      this.$router.push({ path: '/', query: { value: this.input } });
    },
    handleClick(tab, event) {
      console.log(tab, event);
    },
    changeMessage() {
      this.$router.push({
        path: '/change',
        query: { value: this.userData.uid },
      });
    },
    customer() {
      this.$router.push({ path: '/customer' });
    },
    order() {
      this.$router.push({ path: '/order' });
    },
    list() {
      this.$router.push({ path: '/', query: { value: '' } });
    },
    logout() {
      this.$router.replace('/login');
      sessionStorage.clear();
    },
    async deletedata(item) {
      await this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      });
      try {
        await deleteData(`https://oldbook.fansionia.xyz/book/${item.bid}`);
        this.getList();
      } catch (e) {
        this.$message('删除失败,请重试');
      }
    },
  },
};
</script>
<style scoped>
@import '../css/page.css';
</style>
