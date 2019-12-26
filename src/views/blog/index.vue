<template>
  <div>
    <el-container>
      <el-header class="hidden-s-only">
        <el-row>
          <el-col>
            <el-menu
              :default-active="activeIndex"
              mode="horizontal"
              @select="handleSelect"
            >
              <el-menu-item index="1"><a href="#/home">首页</a></el-menu-item>
              <el-menu-item index="3"><a href="#/blogs">博客列表</a></el-menu-item>
              <el-menu-item index="4"><a target="_blank" href="#/dashboard">Dashboard</a></el-menu-item>
              <el-menu-item index="5"><a href="#/blogs/tags/">Timeline</a></el-menu-item>
              <el-submenu index="2" style="float: right">
                <template slot="title">我的工作台</template>
                <el-menu-item index="2-1">
                  <a target="_blank" href="https://github.com/PanJiaChen/vue-admin-template/">Github</a>
                </el-menu-item>
                <el-menu-item index="2-2">
                  <a target="_blank" href="https://panjiachen.github.io/vue-element-admin-site/#/">Docs</a>
                </el-menu-item>
                <el-menu-item index="2-5">
                  <span style="display:block;" @click="logout">退出登陆</span>
                </el-menu-item>
              </el-submenu>
              <el-menu-item index="6" style="float: right">
                <Screenfull />
              </el-menu-item>
            </el-menu>
          </el-col>
        </el-row>
      </el-header>
      <el-header class="hidden-s-and-up">
        <el-row>
          <el-col :span="20">
            <el-menu>
              <el-menu-item>
                <a class="el-icon-home" href="#/home">首页</a>
              </el-menu-item>
            </el-menu>
          </el-col>
          <el-col :span="4">
            <el-button class="el-icon-menu" @click="seen=!seen" />
          </el-col>
        </el-row>
      </el-header>
      <el-menu
        v-if="seen"
        :default-active="activeIndex"
        background-color="#402EFF"
        text-color="white"
      >
        <el-menu-item index="3"><a href="#/blogs">博客列表</a></el-menu-item>
        <el-menu-item index="5"><a href="#/blogs/tags/">Timeline</a></el-menu-item>
        <el-submenu index="2">
          <template slot="title">我的工作台</template>
          <el-menu-item index="2-1">
            <a target="_blank" href="https://github.com/PanJiaChen/vue-admin-template/">Github</a>
          </el-menu-item>
          <el-menu-item index="2-2">
            <a target="_blank" href="https://panjiachen.github.io/vue-element-admin-site/#/">Docs</a>
          </el-menu-item>
          <el-menu-item index="2-3">
            <span style="display:block;" @click="logout">退出登陆</span>
          </el-menu-item>
        </el-submenu>
      </el-menu>
      <el-container>
        <el-main>
          <router-view />
        </el-main>
        <Slide />
      </el-container>
    </el-container>
  </div>
</template>

<script>
import 'element-ui/lib/theme-chalk/display.css'
import Slide from './vside'
import Screenfull from '@/components/Screenfull/index'

export default {
  components: { Slide, Screenfull },
  data() {
    return {
      activeIndex: '3',
      seen: false
    }
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath)
    },
    async logout() {
      await this.$store.dispatch('user/logout')
      this.$router.push(`/login?redirect=${this.$route.fullPath}`)
    }
  }
}
</script>

<style scoped lang='scss'>
.right.slider {
  width: 30%;
}

.el-header, .el-footer {
  /* background-color: #B3C0D1; */
  color: #333;
  text-align: center;
  line-height: 46px;
}

.el-aside {
  background-color: #D3DCE6;
  color: #333;
}
</style>
