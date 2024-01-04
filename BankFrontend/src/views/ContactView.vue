<!-- ParentComponent.vue -->
<template>
  <div>
    <!--    <el-button @click="sortBySim"> 按sim排序 </el-button>-->
    <el-row align="middle">
      <el-col :span="12">
        <span>内规匹配</span>
        <el-tooltip content="默认显示查询全文对应的内规。若鼠标选中一段文本，将自动加载对应的内规" placement="bottom" effect="light">
          <el-icon>
            <QuestionFilled />
          </el-icon>
        </el-tooltip>
      </el-col>
      <el-col :span="12">
        <el-select v-model="selectedCategories" multiple collapse-tags placeholder="Select" style="width: 240px">
          <el-option v-for="item in allCategories" :key="item" :label="item" :value="item" />
        </el-select>
      </el-col>
    </el-row>
    <el-scrollbar height="620px">
      <DataItem v-for="item in filteredData" :key="item.name" :data="item" @toggleExpand="toggleExpand" />
    </el-scrollbar>
  </div>
</template>

<script>
import DataItem from './DataItem.vue'

export default {
  props: {
    textName: String,
    innerData: Array,
    selectedText: String
  },
  data () {
    return {
      name: '2020年银行保险机构公司治理监管评估结果总体情况',
      data: [], // 存放从后端获取的数据
      expandedItems: [], // 存放展开的数据项的name
      selectedCategories: [], // 保存选中的分类
      tooltipVisible: false, // 默认设置帮助信息不可见
    }
  },
  components: {
    DataItem,
  },
  methods: {
    sortBySim () {
      // 在此处按照 sim 进行排序
      this.data.sort((a, b) => b.sim - a.sim)
    }
  },
  computed: {
    allCategories () {
      // 从数据中提取所有的分类
      return Array.from(new Set(this.data.map(item => item.category)))
    },
    filteredData () {
      // 根据选中的分类筛选数据
      return this.data.filter(item => this.selectedCategories.includes(item.category))
    },
  },
  mounted () {
    // this.name = this.textName
    // this.$axios.get(`/api/cal?name=${this.name}`)
    //   .then(response => {
    //     // 处理响应数据
    //     // eslint-disable-next-line vue/no-mutating-props
    //     this.data = response.data
    //     this.selectedCategories = Array.from(new Set(this.data.map(item => item.category)))
    //     console.log(response.data)
    //   })
    //   .catch(error => {
    //     console.error('请求失败', error)
    //   })
    // 发送请求到后端获取数据
    // 例如，使用axios库：
    // axios.get('/api/data').then(response => {
    //   this.data = response.data;
    // });
    // this.data = [{
    //   sim: 0.2998456358909607,
    //   name: '《计算机网络管理办法》',
    //   category: '信息科技部-制度',
    //   text: '银行计算机网络管理办法第一章总则第一条为加强银行以下简称本行的网络管理保障系统安全运行建立良好的网络故障处理反应机制根据中华人····'
    // },
    // {
    //   sim: 0.3998456358909607,
    //   name: '《计算机网络管理办法2》',
    //   category: '信息科技部-制度',
    //   text: '银行计算机网络管理办法第一章总则第一条为加强银行以下简称本行的网络管理保障系统安全运行建立良好的网络故障处理反应机制根据中华人····'
    // },
    // {
    //   sim: 0.1998456358909607,
    //   name: '《计算机网络管理办法3》',
    //   category: '人力资源部-制度',
    //   text: '银行计算机网络管理办法第一章总则第一条为加强银行以下简称本行的网络管理保障系统安全运行建立良好的网络故障处理反应机制根据中华人····'
    // }]
  },
  watch: {
    textName (newText, oldText) {
      this.name = this.textName
      this.$axios.get(`/api/cal?name=${this.name}`)
        .then(response => {
          // 处理响应数据
          // eslint-disable-next-line vue/no-mutating-props
          this.data = response.data
          this.selectedCategories = Array.from(new Set(this.data.map(item => item.category)))
          console.log(response.data)
        })
        .catch(error => {
          console.error('请求失败', error)
        })
    },
    // 每当 selectedText 改变时，这个函数就会执行
    selectedText (newText, oldText) {
      console.log(newText.length)
      if (newText.length > 30) {
        const apiUrl = '/api//upload'
        this.data = []
        this.$axios.post(`${apiUrl}?text=${newText}`)
          .then(response => {
            this.data = response.data
            this.selectedCategories = Array.from(new Set(this.data.map(item => item.category)))
            console.log(response.data)
          })
          .catch(error => {
            // 处理错误
            console.error('请求内规失败', error)
          })
      }
    }
  }
}
</script>
