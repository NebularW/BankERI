<template>
  <div id="app">
    <TopNavigation />
    <div class="main-container">
      <SideNavigation />
      <div class="content-container">
        <router-view />
      </div>
    </div>
  </div>
</template>

<style>
#app {
  display: flex;
  flex-direction: column;
  height: 100vh; /* 使用视窗高度作为高度单位 */
}

.main-container {
  display: flex;
  flex: 1;
  overflow: hidden; /* 防止内容溢出滚动 */
}
.content-container {
  flex: 1;
  overflow: auto; /* 如果内容溢出，启用滚动条 */
  padding: 20px; /* 可根据需要添加一些内边距 */
}

/* 样式调整 */
.top-navigation {
  padding: 5px;
  z-index: 2; /* 使顶部导航栏位于最上层 */
}

.side-navigation {
  height: 100vh;
  width: 250px;
  display: flex;
  flex-direction: column;
  z-index: 1; /* 使侧边导航栏位于主页面之下 */
}

.side-navigation a {
  cursor: pointer;
  transition: background-color 0.3s;
  display: block;
}
</style>
<script setup>
import TopNavigation from '@/components/TopNav.vue'
import SideNavigation from '@/components/SideMenu.vue'
</script>
