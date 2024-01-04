<template>
  <div class="search-container">
    <img src="../assets/search.png" alt="Search Icon" class="search-icon" />
    <input v-model="searchTerm" placeholder="Searching..." />
  </div>
  <ul>
    <li v-for="(item, index) in filteredFileList" :key="index" @click="navigateToDetail(item)">
      {{ item }}
    </li>
  </ul>
</template>

<script>

export default {
  data () {
    return {
      searchTerm: '',
      fileList: [],
      activeFileName: ''
    }
  },
  computed: {
    filteredFileList () {
      // 根据搜索词过滤文件列表
      return this.fileList.filter(item => item.includes(this.searchTerm))
    }
  },
  methods: {
    navigateToDetail (item) {
      // 使用 $router.push 导航到详情页，假设详情页的路由名称是 'detail'
      this.$router.push({ name: 'detail', params: { itemId: item } })
    },
    // 从后端获取文件列表的方法，你需要根据你的后端接口来实现
    // 这里仅作为示例
    fetchFileList () {
      // eslint-disable-next-line no-return-assign
      this.$axios.get('/api/external/list')
        .then(response => {
          this.fileList = response.data
          console.log(this.fileList)
        })
        .catch(error => {
          console.error('获取文件列表失败', error)
        })
      // 使用axios或其他HTTP库向后端请求数据
      // 示例：axios.get ('/api/files').then (response => this.fileList = response.data);
    }
  },
  mounted () {
    // 组件挂载时从后端获取文件列表
    this.fetchFileList()
  }
}
</script>

<style scoped>
/* 样式可以根据需要进行调整 */
ul {
  list-style-type: none;
  padding: 0;
}

li {
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  margin-bottom: 10px;
  cursor: pointer;
}

li:hover {
  background-color: #f0f0f0;
}

.search-container {
  display: flex;
  align-items: center; /* 垂直居中 */
}

.search-icon {
  width: 20px; /* 调整图标的宽度 */
  height: 20px; /* 调整图标的高度 */
  margin-right: 8px; /* 调整图标与输入框之间的距离 */
}
</style>
