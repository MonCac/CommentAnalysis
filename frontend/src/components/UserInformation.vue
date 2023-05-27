<template>
  <div class="home">
    <header class="navbar">
      <div class="nav-info" v-if="loginData">
        <div >个人空间</div>
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
        <el-col :span="1"></el-col>
        <el-col :span="8">
          <el-input v-model="input" placeholder="请输入搜索内容">
            <el-button slot="append" @click="search">搜索</el-button>
          </el-input>
        </el-col>
      </el-row>
      <!--  nav-search -->
    </header>
    <div class="personal-space">
      
      <h1>{{ username }} 的个人空间</h1>
      <div class="user-info">
        <h2>个人信息</h2>
        <div class="info-item">
          <span class="label">联系方式：</span>
          <span v-if="!editContact">{{ contact }}</span>
          <input v-else v-model="newContact" type="text" class="edit-input" />
          <button @click="saveContact" class="edit-btn">{{ editContact ? '保存' : '编辑' }}</button>
        </div>
        <div class="info-item">
          <span class="label">性别：</span>
          <span v-if="!editGender">{{ gender }}</span>
          <select v-else v-model="newGender" class="edit-select">
            <option value="男">男</option>
            <option value="女">女</option>
          </select>
          <button @click="saveGender" class="edit-btn">{{ editGender ? '保存' : '编辑' }}</button>
        </div>
        <div class="info-item">
          <span class="label">出生日期：</span>
          <span v-if="!editBirthday">{{ birthday }}</span>
          <input v-else v-model="newBirthday" type="date" class="edit-input" />
          <button @click="saveBirthday" class="edit-btn">{{ editBirthday ? '保存' : '编辑' }}</button>
        </div>
        <div class="info-item">
          <span class="label">住址：</span>
          <span v-if="!editAddress">{{address }}</span>
          <input v-else v-model="newAddress" type="text" class="edit-input" />
          <button @click="saveAddress" class="edit-btn">{{ editAddress ? '保存' : '编辑' }}</button>
        </div>
        <div class="info-item">
          <span class="label">个性签名：</span>
          <span v-if="!editSignature">{{ signature }}</span>
          <textarea v-else v-model="newSignature" class="edit-input"></textarea>
          <button @click="saveSignature" class="edit-btn">{{ editSignature ? '保存' : '编辑' }}</button>
        </div>
      </div>
      <div class="friend-list">
        <h2>好友列表</h2>
        <ul>
          <li v-for="friend in friends" :key="friend.id">{{ friend.name }}</li>
        </ul>
        
      </div>
      <div class="comment-list">
        <h2>历史评论</h2>
        <ul>
          <li v-for="comment in comments" :key="comment.id">
            <div class="comment-header">
              <span class="comment-author">{{ username }}</span>
              <span class="comment-time">{{ comment.time }}</span>
            </div>
            <div class="comment-content">{{ comment.content }}</div>
          </li>
        </ul>
     </div>
    <!-- container end-->
  </div>
  <footer>
      <a href="#">©2023 点评数据分析与推荐</a>
      <a href="#">意见反馈&nbsp;&nbsp;&nbsp;联系我们&nbsp;&nbsp;&nbsp;隐私权声明&nbsp;&nbsp;&nbsp;使用条款</a>
    </footer>
</div>
</template>

<script>
export default {
  mounted() {
    this.id = this.$route.query.username
    if (this.id != ''){
      this.loginData = true
    }
  },
  data() {
    return {
      username: '张三',
      contact: '123456789',
      gender: '男',
      birthday: '1990-01-01',
      address: '北京市海淀区',
      signature: '生命在于折腾！',
      friends: [
        { id: 1, name: '李四' },
        { id: 2, name: '王五' },
        { id: 3, name: '赵六' },
      ],
      comments: [
        {
          id: 1,
          time: '2022-05-01',
          content: '这是一条评论',
        },
        {
          id: 2,
          time: '2022-05-02',
          content: '这是另一条评论',
        },
      ],
      editContact: false,
      editGender: false,
      editBirthday: false,
      editAddress: false,
      editSignature: false,
      newContact: '',
      newGender: '',
      newBirthday: '',
      newAddress: '',
      newSignature: '',
      input: '',
      loginData: false,
      id: ''
    };
  },
  methods: {
    login() {
      // 登录逻辑
      this.$router.push('/login');
    },
    logout() {
      // 登出逻辑
      this.$router.replace('/login');
      sessionStorage.clear();
    },

    search() {
      // 搜索逻辑
    },
    saveContact() {
      if (this.editContact) {
        // 保存联系方式
        this.contact = this.newContact;
      }
      this.editContact = !this.editContact;
    },
    saveGender() {
      if (this.editGender) {
        // 保存性别
        this.gender = this.newGender;
      }
      this.editGender = !this.editGender;
    },
    saveBirthday() {
      if (this.editBirthday) {
        // 保存出生日期
        this.birthday = this.newBirthday;
      }
      this.editBirthday = !this.editBirthday;
    },
    saveAddress() {
      if (this.editAddress) {
        // 保存住址
        this.address = this.newAddress;
      }
      this.editAddress = !this.editAddress;
    },
    saveSignature() {
      if (this.editSignature) {
        // 保存个性签名
        this.signature = this.newSignature;
      }
      this.editSignature = !this.editSignature;
    },
  },
};
</script>

<style scoped>
@import url(../css/page.css);
.home {
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  color: #333;
  max-width: 100%;
  margin: 0 auto;
}

.personal-space {
  background-color: #fff;
  width: 1200px;
  align-content: center;
  margin: 0 auto;
  padding: 30px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  font-family: Arial, sans-serif;
}
.personal-space  h1{
  font-size: 50px;
  font-family:"宋体", SimSun, STSong, "Microsoft YaHei", Arial, sans-serif;
}
.user-info {
  margin-top: 40px;
  margin-bottom: 40px;
}

.user-info h2{
  margin-top: 40px;
  margin-bottom: 40px;
}

.info-item {
  margin-bottom: 20px;
}

.label {
  font-weight: bold;
  font-size: large;
  
}

.edit-input,
.edit-select,
.edit-textarea {
  border: 1px solid #ccc;
  padding: 5px;
  margin-right: 10px;
  width: 200px;
}

.edit-select {
  height: 28px;
}

.edit-btn {
  margin-left: 50px;
  width: 50px;
  border-radius: 10px;
  display: inline-block; /* Add this line */
  border: 1px solid #ccc;
  background-color: #fff;
  color: #333;
  padding: 5px 10px;
  cursor: pointer;
}

.edit-btn:hover {
  background-color: #ccc;
  color: #fff;
}

.friend-list {
  margin-bottom: 40px;
  display: flex;
  gap: 50px; /* 设置标题和列表之间的间隙 */
  
  
}

.friend-list h2{
  display: block;
}
.friend-list ul{
  display: block;
  margin: 0;
  padding: 0;
  
}
.comment-list {
  margin-bottom: 40px;
}

.comment-list h2{
  margin-bottom: 40px;
}
.comment-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
}

.comment-author {
  font-weight: bold;
}

.comment-time {
  color: #999;
}

.comment-content {
  margin-bottom: 20px;
}

footer {
  margin-top: 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top: 1px solid #ccc;
  padding-top: 20px;
  font-size: 12px;
}

footer a {
  color: #333;
  text-decoration: none;
  margin-right: 20px;
}

footer a:hover {
  text-decoration: underline;
}
</style>