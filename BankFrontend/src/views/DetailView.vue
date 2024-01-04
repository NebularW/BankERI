<template>
  <div class="main">
    <div class="main-container">
      <div class="left">
        <div  class="header" >
          <img src="../assets/back.png" @click="goback()">
          <h3>《 {{ $route.params.itemId }}》</h3>
        </div>
        <el-scrollbar height="600px"  >
          <div >
            <el-text @mouseup="handleSelect">{{ allText}}</el-text>
          </div>
        </el-scrollbar>
      </div>
      <div class="right">
        <ContactView :textName="textName" :selectedText="selectedText"/>
      </div>
    </div>
  </div>
</template>

<script>
import ContactView from '@/views/ContactView.vue'

export default {
  data () {
    return {
      allText: '',
      textName: '',
      Selection: '',
      selectedText: ''
    }
  },
  components: {
    ContactView
  },
  mounted () {
    // 在组件生命周期中获取路由参数
    const apiUrl = '/api//external/text'
    const name = this.$route.params.itemId
    this.textName = name
    this.$axios.get(`${apiUrl}?name=${name}`)
      .then(response => {
        // 处理响应数据
        this.allText = response.data
        console.log(response.data)
      })
      .catch(error => {
        // 处理错误
        console.error('请求失败', error)
      })
  },
  methods: {
    goback () {
      this.$router.go(-1)
    },
    handleSelect () {
      const selection = window.getSelection()
      this.selectedText = selection.toString().trim()
    }
  }
}
</script>

<style>
.main-container {
  display: flex;
}

.left {
  flex: 1; /* 占据剩余空间 */
  margin-right: 20px; /* 可根据需要调整左右间距 */
  background-color: #eeecec;
  padding: 20px;
  border: #131313;
}

.right {
  flex: 1; /* 占据剩余空间 */
  background-color: #ffffff;
}

h3{
  margin: 0px;
  padding: 15px;
}

img{
  height: 25px;
  width: 25px;
  margin-right: 30px;
}
.header{
  display: flex;
  align-items: center; /* 垂直居中 */
}
</style>
