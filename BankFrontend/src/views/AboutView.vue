<template>
  <div class="about">
    <div class="container">
      <div class="left">
        <el-input v-model="textarea" @mouseup="handleSelect()" :rows="20" type="textarea" placeholder="输入需要查询的外规"/>
        <el-tooltip class="box-item" effect="dark" content="查询的外规不得少于30字">
          <el-button @click="query()">查询外规</el-button>
        </el-tooltip>
      </div>
      <div class="right">
        <ContactView :selectedText="selectedText"/>
      </div>
    </div>
  </div>
</template>

<script>
import ContactView from '@/views/ContactView.vue'

export default {
  data () {
    return {
      textarea: '',
      selectedText: '',
    }
  },
  components: {
    ContactView
  },
  methods: {
    query () {
      this.selectedText = this.textarea
    },
    handleSelect () {
      const selection = window.getSelection()
      this.selectedText = selection.toString().trim()
    }
  }
}
</script>

<style>
.container {
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

</style>
