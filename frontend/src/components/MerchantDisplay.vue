<!-- 商户展示页面 -->
<template>
  <div>
    <header class="navbar">
      <div class="nav-info" v-if="loginData">
        <div @click="personalClick">个人空间</div>
        <div @click="order">订单查询</div>
        <div @click="customer">客服</div>
        <div @click="logout">[ 登 出 ]</div>
      </div>
      <div class="nav-info" v-if="!loginData">
        <div @click="login">[ 您 还 未 登 录，请 先 登 录 ]</div>
      </div>
      <!-- nav-info -->
      <el-row class="row">
        <el-col :span="8">
          <img src="../img/logo.png" class="logo-img"/>
        </el-col>
        <el-col :span="8">
          <el-input v-model="input" placeholder="请输入搜索内容">
            <el-button slot="append" @click="search">搜索</el-button>
          </el-input>
        </el-col>
      </el-row>
      <!--  nav-search -->
    </header>
  <div class="merchant-details">
    <h1>{{ merchant.name }}</h1>
    <div class="address">{{ merchant.address }}</div>
    <div class="city-state">{{ merchant.city }}, {{ merchant.state }}</div>
    <div class="rating">
      <span class="stars">
        <template v-for="i in convertRatingToStarsCount(merchant.rating)">
          <i class="star" :class="{ filled: i >= 1 }"></i>
          <i class="half-star" v-if="i >= 0.5 && i < 1"></i>
        </template>
      </span>
      <span class="rating-count">{{ merchant.ratingCount }} Reviews</span>
    </div>
    <div class="status" :class="{ open: merchant.isOpen }">{{ merchant.isOpen ? 'Open Now' : 'Closed' }}</div>
    <div class="features">
      <div v-for="feature in merchant.features" :key="feature" class="feature">{{ feature }}</div>
    </div>
    <div class="categories">
      <div v-for="category in merchant.categories" :key="category" class="category">{{ category }}</div>
    </div>
    <div class="hours">
      <div class="hours-title">Hours:</div>
      <div class="hours-days">
        <div v-for="day in daysOfWeek" :key="day" class="day">{{ day }}</div>
      </div>
      <div class="hours-times">
        <div v-for="(hours, day) in merchant.hours" :key="day" class="hours-day">
          <div v-for="time in hours" :key="time" class="time">{{ time }}</div>
        </div>
      </div>
    </div>
    <!-- User comments section -->
    <div class="comments">
      <h2>Comments</h2>
        <div v-for="comment in comments" :key="comment.id" class="comment">
          <div class="comment-header">
            <span class="comment-author">{{ comment.author }}</span>
            <span class="comment-date">{{ comment.date }}</span>
          </div>
          <div class="comment-body">{{ comment.body }}</div>
        </div>
        <form @submit.prevent="addComment" class="comment-form">
          <h3>Add a comment</h3>
            <label for="author">Name:</label>
            <input v-model="newComment.author" type="text" id="author" required>
            <label for="body">Comment:</label>
            <textarea v-model="newComment.body" id="body" required></textarea>
            <button type="submit">提交</button>
        </form>
    </div>
  </div>
</div>
</template>

<script>
export default {
  data() {
    return {
      daysOfWeek: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
      merchant: {
        name: 'Example Merchant',
        address: '123 Main St',
        city: 'Example City',
        state: 'Example State',
        rating: 4.5,
        ratingCount: 100,
        isOpen: true,
        features: ['Free Wi-Fi', 'Outdoor Seating', 'Parking'],
        categories: ['Restaurant', 'Coffee Shop'],
        hours: {
          Monday: ['8:00 AM - 5:00 PM'],
          Tuesday: ['8:00 AM - 5:00 PM'],
          Wednesday: ['8:00 AM - 5:00 PM'],
          Thursday: ['8:00 AM - 5:00 PM'],
          Friday: ['8:00 AM - 5:00 PM'],
          Saturday: ['10:00 AM - 3:00 PM', '5:00 PM - 10:00 PM'],
          Sunday: ['10:00 AM - 3:00 PM', '5:00 PM - 10:00 PM']
        }},
        comments: [ { id: 1, author: 'John Doe',
                      date: '2023-05-25 12:00:00',
                      body: 'This merchant is great!' },
                   { id: 2, author: 'Jane Smith', 
                     date: '2023-05-25 13:00:00', 
                     body: 'I had a terrible experience here!' } ], 
        newComment: { author: '', body: '' } 
    };
  },
  methods: {
    login() {
      this.$router.push('/login');
    },
    convertRatingToStarsCount(rating) {
      const fullStars = Math.floor(rating);
      const halfStar = Math.round(rating - fullStars) === 0.5;
      return fullStars + (halfStar ? 0.5 : 0);
    },
    addComment() { const newId = this.comments.length + 1; 
                     const currentDate = new Date(); 
                     const formattedDate = `${currentDate.getFullYear()}-${currentDate.getMonth()+1}-${currentDate.getDate()} ${currentDate.getHours()}:${currentDate.getMinutes()}:${currentDate.getSeconds()}`;
                     const newComment = { id: newId, author: this.newComment.author, date: formattedDate, body: this.newComment.body }; 
                     this.comments.push(newComment); 
                     this.newComment = { author: '', body: '' }; 
    }
  }
}
</script>

<style>
@import '../css/page.css';
.merchant-details {
  max-width: 1200px;
  margin: 0 auto;
  padding: 30px;
  background-color: #fff;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  font-family: Arial, sans-serif;
}

.merchant-details h1 {
  margin-top: 0;
  font-size: 32px;
  font-weight: bold;
}

.merchant-details .address {
  margin: 10px 0;
  font-size: 16px;
}

.merchant-details .city-state {
  margin-bottom: 10px;
  font-size: 16px;
  color: #666;
}

.merchant-details .rating {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.merchant-details .rating .stars {
  display: inline-flex;
  align-items: center;
  margin-right: 10px;
}

.merchant-details .rating .stars .star {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath fill='%23ffcc00' d='M12 2.276l3.09 6.272 6.902.999-5 4.867 1.182 6.877L12 18.156l-6.174 3.085 1.182-6.877-5-4.867 6.09-.999L12 2.276z'/%3E%3C/svg%3E");
  background-size: contain;
  width: 16px;
  height: 16px;
  margin-right: 2px;
}

.merchant-details .rating .stars .half-star {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath fill='%23ffcc00' d='M12 2.276l3.09 6.272 6.902.999-5 4.867 1.182 6.877L12 18.156l-6.174 3.085 1.182-6.877-5-4.867 6.09-.999L12 2.276zM12 4.715l-2.98 6.06.567 3.298-2.413 2.355 3.33.484L12 15.423l1.496.774 3.33-.484-2.413-2.355.567-3.298L12 4.715z'/%3E%3C/svg%3E");
  background-size: contain;
  width: 16px;
  height: 16px;
  margin-right: 2px;
}

.merchant-details .rating .rating-count {
  font-size: 16px;
  color: #666;
}

.merchant-details .status {
  display: inline-block;
  padding: 5px 10px;
  font-size: 16px;
  font-weight: bold;
  color: #fff;
  border-radius: 20px;
  background-color: #4caf50;
}

.merchant-details.status.closed {
  background-color: #f44336;
}

.merchant-details .features {
  margin: 20px 0;
}

.merchant-details .features .feature {
  display: inline-block;
  padding: 5px 10px;
  margin-right: 10px;
  font-size: 16px;
  font-weight: bold;
  color: #fff;
  border-radius: 20px;
  background-color: #2196f3;
}

.merchant-details .categories {
  margin: 20px 0;
}

.merchant-details .categories .category {
  display: inline-block;
  padding: 5px 10px;
  margin-right: 10px;
  font-size: 16px;
  font-weight: bold;
  color: #fff;
  border-radius: 20px;
  background-color: #9c27b0;
}

.merchant-details .hours {
  margin-top: 20px;
}

.merchant-details .hours .hours-title {
  font-size: 20px;
  font-weight: bold;
}

.merchant-details .hours .hours-days {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
}

.merchant-details .hours .day {
  flex: 1;
  text-align: center;
  font-size: 16px;
  font-weight: bold;
  color: #666;
}

.merchant-details .hours .hours-times {
  display: flex;
  justify-content: space-between;
}

.merchant-details .hours .hours-day {
  flex: 1;
  text-align: center;
  font-size: 16px;
  font-weight: bold;
  color: #666;
}

.merchant-details .hours .time {
  margin-bottom: 5px;
  font-size: 16px;
  color: #666;
}

.merchant-details .comments {
margin-top: 30px;
}

.merchant-details .comments h2 {
font-size: 24px;
font-weight: bold;
margin-bottom: 20px;
}

.merchant-details .comments .comment {
margin-bottom: 30px;
padding-bottom: 20px;
border-bottom: 1px solid #ccc;
}

.merchant-details .comments .comment-header {
display: flex;
justify-content: space-between;
margin-bottom: 10px;
font-size: 16px;
}

.merchant-details .comments .comment-author {
font-weight: bold;
}

.merchant-details .comments .comment-date {
color: #666;
}

.merchant-details .comments .comment-body {
font-size: 16px;
}

.merchant-details .comment-form {
display: flex;
flex-direction: column;
}

.merchant-details .comment-form h3 {
font-size: 20px;
font-weight: bold;
margin-bottom: 20px;
}

.merchant-details .comment-form input,
.merchant-details .comment-form textarea {
padding: 10px;
margin-bottom: 20px;
font-size: 16px;
border: 1px solid #ccc;
border-radius: 4px;
}

.merchant-details .comment-form button {
padding: 10px 20px;
font-size: 16px;
border: none;
border-radius: 4px;
background-color: #2196f3;
color: #fff;
cursor: pointer;
}
</style>