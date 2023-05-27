<template>
  <div class="home">
    <header class="navbar">
      <div class="nav-info" v-if="loginData">
        <div @click="personalClick">个人空间</div>
        <div @click="logout">[ 登 出 ]</div>
      </div>
      <div class="nav-info" v-if="!loginData">
        <div @click="login">[ 您 还 未 登 录，请 先 登 录 ]</div>
      </div>
      <!-- nav-info -->
      <el-row class="row">
        <el-col :span="8">
          <img src="../img/logo.png" class="logo-img" />
        </el-col>
        <el-col :span="1">

        </el-col>
        <el-col :span="8">
          <el-input v-model="input" placeholder="请输入搜索内容">
            <el-button slot="append" @click="search">搜索</el-button>
          </el-input>
        </el-col>
      </el-row>
      <!--  nav-search -->
    </header>
    <div class="tabs">
      <el-tabs v-model="activeName" @tab-click="handleClick">
        <el-tab-pane label="首页" name="first">
          <el-card class="merchant-list">
            <div slot="header" class="clearfix">
              <span>商户推荐</span>
              <div class="sort">
                <el-select v-model="value" clearable placeholder="默认排序">
                  <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value" />
                </el-select>
              </div>
            </div>
            <div class="merchant-items">
              <el-card v-for="merchant in recommendedMerchants" :key="merchant.id" class="merchant-card">
                <img class="merchant-img" :src="merchant.imgUrl" alt="商家图片">
                <div class="merchant-info">
                  <div class="merchant-name">{{ merchant.name }}</div>
                  <div class="merchant-type">{{ merchant.type }}</div>
                  <div class="merchant-address">{{ merchant.address }}</div>
                </div>
              </el-card>
            </div>
          </el-card>
        </el-tab-pane>
        <el-tab-pane label="商户筛选" name="second">

        </el-tab-pane>
        <el-tab-pane label="好友推荐" name="third">
          <div class="friend-list">
            <div class="friend-card" v-for="friend in recommendedFriends" :key="friend.id">
              <img :src="friend.avatar" alt="好友头像">
              <div class="friend-info">
                <div class="friend-name">{{ friend.name }}</div>
                <div class="friend-intro">{{ friend.intro }}</div>
                <div class="friend-action">
                  <el-button type="primary" size="small" @click="addFriend(friend)">添加好友</el-button>
                </div>
              </div>
            </div>
          </div>
        </el-tab-pane>
      </el-tabs>
    </div>

    <!-- container end-->
    <footer>
      <a href="#">©2023 点评数据分析与推荐</a>
      <a href="#">意见反馈&nbsp;&nbsp;&nbsp;联系我们&nbsp;&nbsp;&nbsp;隐私权声明&nbsp;&nbsp;&nbsp;使用条款</a>
    </footer>
  </div>
</template>
<script>

import { evaluationRecommendFriend } from "../util/api"

export default {
  data() {
    return {
      recommendedMerchants: [
        {
          id: 1,
          name: '小肥羊',
          type: '火锅',
          address: '上海市徐汇区田林路',
          imgUrl: 'https://picsum.photos/200'
        },
        {
          id: 2,
          name: '星巴克',
          type: '咖啡',
          address: '上海市长宁区虹桥路',
          imgUrl: 'https://picsum.photos/200'
        },
        {
          id: 3,
          name: '华莱士',
          type: '快餐',
          address: '上海市闵行区吴中路',
          imgUrl: 'https://picsum.photos/200'
        },
        {
          id: 4,
          name: '必胜客',
          type: '披萨',
          address: '上海市宝山区长江西路',
          imgUrl: 'https://picsum.photos/200'
        },
        {
          id: 5,
          name: '麦当劳',
          type: '快餐',
          address: '上海市黄浦区南京东路',
          imgUrl: 'https://picsum.photos/200'
        },
        {
          id: 6,
          name: '海底捞',
          type: '火锅',
          address: '上海市杨浦区国权路',
          imgUrl: 'https://picsum.photos/200'
        },
        {
          id: 7,
          name: '必胜客',
          type: '披萨',
          address: '上海市闸北区大宁路',
          imgUrl: 'https://picsum.photos/200'
        },
        {
          id: 8,
          name: '肯德基',
          type: '快餐',
          address: '上海市静安区南京西路',
          imgUrl: 'https://picsum.photos/200'
        }
        // 添加更多商家数据
      ],
      recommendedFriends: [
        {
          id: 1,
          name: '张三',
          intro: '我是张三，很高兴认识你！',
          avatar: 'https://picsum.photos/200'
        },
        {
          id: 2,
          name: '李四',
          intro: '我是李四，欢迎加入我的好友圈！',
          avatar: 'https://picsum.photos/200'
        },
        {
          id: 3,
          name: '王五',
          intro: '我是王五，喜欢旅行和美食！',
          avatar: 'https://picsum.photos/200'
        },
        {
          id: 4,
          name: '赵六',
          intro: '我是赵六，是一名程序员！',
          avatar: 'https://picsum.photos/200'
        },
        {
          id: 5,
          name: '赵六',
          intro: '我是赵六，是一名程序员！',
          avatar: 'https://picsum.photos/200'
        },
        {
          id: 6,
          name: '赵六',
          intro: '我是赵六，是一名程序员！',
          avatar: 'https://picsum.photos/200'
        },
        {
          id: 7,
          name: '赵六',
          intro: '我是赵六，是一名程序员！',
          avatar: 'https://picsum.photos/200'
        },
        {
          id: 8,
          name: '赵六',
          intro: '我是赵六，是一名程序员！',
          avatar: 'https://picsum.photos/200'
        },
        {
          id: 9,
          name: '赵六',
          intro: '我是赵六，是一名程序员！',
          avatar: 'https://picsum.photos/200'
        },
        {
          id: 10,
          name: '赵六',
          intro: '我是赵六，是一名程序员！',
          avatar: 'https://picsum.photos/200'
        }
        // 添加更多好友数据
      ],
      options: [
        {
          value: 'Option1',
          label: '按星级优先',
        },
        {
          value: 'Option2',
          label: '按评论数优先',
        },
        {
          value: 'Option3',
          label: '按好评优先',
        },
      ],
      activeName: 'first',
      loginData: false,
      input: '',
      data: '',
      value: '',
      id: '',
    };
  },
  computed: {},
  
  created() {
    this.value = this.$route.query.value;
    if (this.$route.query.page === '2') {
      this.activeName = 'second';
    }
    if (this.$route.query.search) {
      this.data = this.$route.query.search;
      this.input = this.$route.query.search;
    }
    if (this.value !== undefined) {
      this.data = this.value;
      this.input = this.value;
      this.activeName = 'second';
    }
    debugger
    console.log(this.recommendedFriends)
    this.friendRecommend()
  },
  mounted() {
    this.id = this.$route.query.username
    if (this.id != ''){
      this.loginData = true
    }
  },
  methods: {
    login() {
      this.$router.push('/login');
    },
    handleClick(tab, event) {
      console.log(tab, event);
    },
    personalClick() {
      this.$router.push({path:'/userinformation', query:{username: this.id}})
    },
    search() {
      this.data = this.input;
      this.$router.push('/');
      this.activeName = 'second';
    },
    order() {
      this.$router.push({ path: '/order' });
    },
    customer() {
      this.$router.push({ path: '/customer' });
    },
    logout() {
      this.$router.replace('/login');
      sessionStorage.clear();
    },
    addFriend(friend) {
      // 添加好友的逻辑
      console.log('添加好友:', friend);
    },
    friendRecommend() {
      evaluationRecommendFriend(this.id).then((res) => {
        if (res.status == 200) {
          console.log("ok")
          for (var i = 0; i <= 9; i++) {
            this.recommendedFriends[i].id = res.data[i].id
            this.recommendedFriends[i].name = res.data[i].name
            this.recommendedFriends[i].intro = '我是'+res.data[i].name+'，很高兴认识你！'
          }

        }
        else {
          console.log("出错了")
        }
      })
    }
  },
};
</script>
<style>
@import '../css/page.css';

* {
  padding: 0px;
  margin: 0px;
  font-family: Microsoft Yahei;
  box-sizing: border-box;
}

/*navbar*/
.navbar {
  height: 200px;
  width: 100%;
  background-color: white;
  position: relative;
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  justify-content: flex-start;
}

.nav-info {
  height: 40px;
  background-color: #4b4d52;
  display: flex;
  justify-content: flex-end;
  flex-wrap: wrap;
}

.nav-info div {
  color: #d6d2d2 !important;
  font-size: 14px;
  line-height: 40px;
  margin-left: 5px;
  margin-right: 25px;
}

.nav-info a:hover {
  color: white !important;
}

.nav-search {
  height: 100px;
  width: 100%;
  /*background-color: gray;*/
  display: flex;
  justify-content: flex-start;
  align-content: center;
  position: relative;
}

/*商家推荐 */
.clearfix {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.sort {
  display: flex;
  align-items: center;
}

.merchant-list {
  margin-top: 20px;
}

.merchant-items {
  display: flex;
  flex-wrap: wrap;
}

.merchantt-card {
  width: 300px;
  margin-right: 20px;
  margin-bottom: 20px;
}

.merchant-img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.merchant-info {
  padding: 15px;
}

.merchant-name {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 10px;
}

.merchant-type {
  color: #999;
  margin-bottom: 5px;
}

.merchant-address {
  font-size: 14px;
  color: #999;
}

/*脚步*/
footer {
  border-top: 1px solid #ccc;
  width: 100%;
  height: 70px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: center;
}

footer a {
  text-align: center;
  font-size: 15px;
  /*margin-left: 30%;*/
  text-decoration: none;
  color: gray;
}

.friend-list {
  display: flex;
  flex-wrap: wrap;
}

.friend-card {
  width: 300px;
  margin-right: 20px;
  margin-bottom: 20px;
  display: flex;
}

.friend-card img {
  width: 100px;
  height: 100px;
  object-fit: cover;
  border-radius: 50%;
  margin-right: 20px;
}

.friend-info {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.friend-name {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 10px;
}

.friend-intro {
  font-size: 14px;
  margin-bottom: 10px;
}

.friend-action {
  margin-top: 10px;
}

.tabs .el-tabs__nav-wrap {
  background-color: #f2f1ea;
}
.tabs .el-tabs__nav-wrap::after {
  background-color: #f2f1ea;
}
.tabs .el-tabs__active-bar {
  background-color: #b5aa9a;
}
.tabs .el-tabs__nav {
  margin-left: 17%;
}
.tabs .el-tabs__item.is-active {
  color: #3f4247;
  font-size: 16px;
  font-weight: 600;
}
.tabs .el-tabs__item {
  font-size: 16px;
}
.tabs .el-tabs__item:hover {
  color: #3f4247;
  font-weight: 600;
}
</style>
