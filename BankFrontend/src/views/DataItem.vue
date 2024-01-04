<!-- DataItem.vue -->
<template>
  <div class="dataitem">
    <el-card class="box-card" style="width: 90%">
      <template #header>
        <div class="card-header">
          <span>{{ data.name }}</span>
          <span><el-tag type="success">{{data.category}}</el-tag></span>
          <el-icon @click="toggleExpand" ><ArrowUp  v-if="isExpanded" />  <ArrowDown v-else /></el-icon>
        </div>
      </template>
      <div >
        <el-text v-if="isExpanded" class="scrollable-text">
          {{data.text}}
          <el-row/>
          {{data.sim}}
        </el-text>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  props: {
    data: Object,
  },
  data () {
    return {
      isExpanded: false,
    }
  },
  methods: {
    toggleExpand () {
      this.isExpanded = !this.isExpanded
      this.$emit('toggleExpand', this.data.name)
    }
  },
}
</script>
<style>
.box-card{
  margin: 10px;
}
.scrollable-text {
  max-height: 100px; /* 设置最大高度，超过这个高度将出现垂直滚动条 */
  overflow-y: auto; /* 使用 auto 或 scroll 来启用垂直滚动条 */
}
</style>
