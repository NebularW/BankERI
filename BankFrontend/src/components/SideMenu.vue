<template>
  <div class="side-navigation">
    <router-link to="/" :class="{ active: isRouteActive('/detail') }">政策解读</router-link>
    <router-link to="/about" :class="{ active: currentRoute === '/about' }">上传外规</router-link>
  </div>
</template>

<script>
export default {
  name: 'SideNavigation',
  data () {
    return {
      currentRoute: this.$route.path, // 获取当前路由路径
    }
  },
  watch: {
    $route (to, from) {
      this.currentRoute = to.path // 监听路由变化，更新 currentRoute
    },
  },
  methods: {
    isRouteActive (route) {
      return this.currentRoute === '/' || this.currentRoute.startsWith(route)
    },
  }

}
</script>

<style scoped>
.side-navigation {
  height: 100vh;
  /* 使用视窗高度作为高度单位 */
  width: 200px;
  background-color: #2d2d2d;
  color: #000000;
  display: flex;
}

.side-navigation a {
  display: flex;
  align-items: center;
  /* 垂直居中对齐 */
  height: 40px;
  text-decoration: none;
  color: #ffffff;
  padding: 10px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.side-navigation a:hover {
  background-color: #131313;
  color: #ffffff;
}

.side-navigation a.active {
  background-color: #131313;
  color: #ffdd00;
  border-right: 2px solid #ffdd00;
  /* 右侧添加黄色竖线 */
}</style>
