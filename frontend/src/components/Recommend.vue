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
                  <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value"
                    @click.native="sortMerchant(item.label)" />
                </el-select>
              </div>
            </div>
            <div class="merchant-items">
              <el-card v-for="merchant in recommendedMerchants" :key="merchant.id" class="merchant-card">
                <img class="merchant-img" :src="merchant.imgUrl" alt="商家图片">
                <div @click="seeaInformation(merchant.id)" class="merchant-info">
                  <div @click="seeaInformation(merchant.id)" class="merchant-business_id">{{ merchant.business_id }}</div>
                  <div @click="seeaInformation(merchant.id)" class="merchant-name">{{ merchant.name }}</div>
                  <div @click="seeaInformation(merchant.id)" class="merchant-stars">{{ merchant.stars }}</div>
                  <div @click="seeaInformation(merchant.id)" class="merchant-address">{{ merchant.address }}</div>
                </div>
              </el-card>
            </div>
          </el-card>
        </el-tab-pane>
        <el-tab-pane label="商户筛选" name="second">
          <el-card class="merchant-list">
            <div slot="header" class="clearfix">
              <span class="'shaixuan'">商户筛选</span>
              <div class="input-container">
                <el-input type="text" v-model="input1" placeholder="请输入州名" class="filter-input"></el-input>
                <el-input type="text" v-model="input2" placeholder="请输入区域名" class="filter-input"></el-input>
              </div>
              <el-button @click="submit" class="filter-submit">提交</el-button>
            </div>
            <div class="merchant-items">
              <el-card v-for="merchant in recommendedMerchants" :key="merchant.id" class="merchant-card">
                <img class="merchant-img" :src="merchant.imgUrl" alt="商家图片">
                <div @click="seeaInformation(merchant.id)" class="merchant-info">
                  <div @click="seeaInformation(merchant.id)" class="merchant-business_id">{{ merchant.business_id }}</div>
                  <div @click="seeaInformation(merchant.id)" class="merchant-name">{{ merchant.name }}</div>
                  <div @click="seeaInformation(merchant.id)" class="merchant-stars">{{ merchant.stars }}</div>
                  <div @click="seeaInformation(merchant.id)" class="merchant-address">{{ merchant.address }}</div>
                </div>
              </el-card>
            </div>
          </el-card>
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

import { recommendByChoice } from "../util/api"


import { evaluationRecommendFriend } from "../util/api"
import { normalSearch } from "../util/api";

export default {
  data() {
    return {
      banner: [],
      recommendedMerchants: [
        {
          id: 1,
          business_id: '_ab50qdWOk0DdB6XOrBitw',
          name: 'Acme Oyster House',
          stars: '4.0',
          address: '724 Iberville St',
          imgUrl: 'https://picsum.photos/200'
        },
        {
          id: 2,
          business_id: 'ac1AeYqs8Z4_e2X5M3if2A',
          name: 'Oceana Grill',
          stars: '4.0',
          address: '739 Conti St',
          imgUrl: 'https://picsum.photos/200'
        },
        {
          id: 3,
          business_id: 'GXFMD0Z4jEVZBCsbPf4CTQ',
          name: 'Hattie B’s Hot Chicken - Nashville',
          stars: '4.5',
          address: '112 19th Ave S',
          imgUrl: 'https://picsum.photos/200'
        },
        {
          id: 4,
          business_id: 'ytynqOUb3hjKeJfRj5Tshw',
          name: 'Reading Terminal Market',
          stars: '4.5',
          address: '51 N 12th St',
          imgUrl: 'https://picsum.photos/200'
        },
        {
          id: 5,
          business_id: 'oBNrLz4EDhiscSlbOl8uAw',
          name: 'Ruby Slipper - New Orleans',
          stars: '4.5',
          address: '200 Magazine St',
          imgUrl: 'https://picsum.photos/200'
        },
        {
          id: 6,
          business_id: 'iSRTaT9WngzB8JJ2YKJUig',
          name: "Mother's Restaurant",
          stars: ' 3.5',
          address: '401 Poydras St',
          imgUrl: 'https://picsum.photos/200'
        },
        {
          id: 7,
          business_id: 'VQcCL9PiNL_wkGf-uF3fjg',
          name: 'Royal House',
          stars: '4.0',
          address: '441 Royal St',
          imgUrl: 'https://picsum.photos/200'
        },
        {
          id: 8,
          business_id: '_C7QiQQc47AOEv4PE3Kong',
          name: "Commander's Palace",
          stars: '4.5',
          address: '1403 Washington Ave',
          imgUrl: 'https://picsum.photos/200'
        },
        {
          id: 9,
          business_id: 'GBTPC53ZrG1ZBY3DT8Mbcw',
          name: 'Luke',
          stars: '4.0',
          address: '333 Saint Charles Ave',
          imgUrl: 'https://picsum.photos/200'
        },
        {
          id: 10,
          business_id: '6a4gLLFSgr-Q6CZXDLzBGQ',
          name: 'Cochon',
          stars: '4.0',
          address: '930 Tchoupitoulas St',
          imgUrl: 'https://picsum.photos/200'
        },
        {
          id: 11,
          business_id: '1b5mnK8bMnnju_cvU65GqQ',
          name: 'Biscuit Love: Gulch',
          stars: '4.0',
          address: '316 11th Ave S',
          imgUrl: 'https://picsum.photos/200'
        },
        {
          id: 12,
          business_id: 'PP3BBaVxZLcJU54uP_wL6Q',
          name: "Pat's King of Steaks",
          stars: ' 3.0',
          address: '1237 E Passyunk Ave',
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
          label: 'stars',
        },
        {
          value: 'Option2',
          label: 'review_count',
        },
        {
          value: 'Option3',
          label: 'score',
        }
      ],
      activeName: 'first',
      loginData: false,
      input: '',
      data: '',
      value: '',
      id: '',
      input1: '',
      input2: '',
    };
  },
  computed: {},

  created() {
    debugger
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
    console.log(this.recommendedFriends)
    // this.friendRecommend()
  },
  mounted() {
    debugger
    this.id = this.$route.query.username
    debugger
    console.log(this.id)
    if (this.id != '') {
      this.loginData = true
    }
    debugger
  },
  methods: {
    sortMerchant(target) {
      recommendByChoice(target).then((res) => {
        if (res.status == 200) {
          console.log("ok");
          for (var i = 0; i <= 11; i++) {
            debugger
            console.log("ok")
            this.recommendedMerchants[i].id = i + 1
            this.recommendedMerchants[i].business_id = res.data[i].business_id
            this.recommendedMerchants[i].name = res.data[i].name
            this.recommendedMerchants[i].stars = res.data[i].stars
            this.recommendedMerchants[i].address = res.data[i].address
          }
        }
        else {

          console.log("出错了")

        }


      })
    },
    login() {
      this.$router.push('/login');
    },
    handleClick(tab, event) {
      console.log(tab, event);
    },
    personalClick() {
      this.$router.push({ path: '/userinformation', query: { username: this.id } })
    },
    search() {
      this.data = this.input;
      this.activeName = 'second';
      normalSearch(this.data).then((res) => {
        if (res.status == 200) {
          console.log("ok")
          for (var i = 0; i <= 9; i++) {
            this.recommendedMerchants[i].id = res.data[i].business_id
            this.recommendedMerchants[i].name = res.data[i].name
            this.recommendedMerchants[i].type = res.data[i].categories
            this.recommendedMerchants[i].address = res.data[i].address
          }
        }
        else {
          console.log("出错")
        }
      })
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
    submit() {
      if(input1 == ''){
        // 只输入了区域
      }else if(input2 == ''){
        // 只输入了州
      }else{
        // 州和区域都输入
      }
    },
    friendRecommend() {
      evaluationRecommendFriend(this.id).then((res) => {
        if (res.status == 200) {
          console.log("ok")
          for (var i = 0; i <= 9; i++) {
            this.recommendedFriends[i].id = res.data[i].id
            this.recommendedFriends[i].name = res.data[i].name
            this.recommendedFriends[i].intro = '我是' + res.data[i].name + '，很高兴认识你！'
          }

        }
        else {
          console.log("出错了")
        }
      })
    },
    seeaInformation(merchantId) {
      debugger
      console.log(merchantId)
      debugger
      this.$router.push({ path: '/merchantdisplay', query: { id: merchantId } })
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

.shaixuan {
  font-size: 18px;
  margin-right: 10px;
}

.input-container {
  display: flex;
  align-items: center;
}

.filter-input {
  width: 150px;
  margin-right: 10px;
}

.filter-submit {
  margin-right: 60px;
  background-color: #409EFF;
}
</style>
