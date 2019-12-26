<template>
  <div class="app">
    <sticky :z-index="10">
      <el-button type="primary">
        <router-link to="/blogs/create">Add</router-link>
      </el-button>
    </sticky>
    <el-card
      v-for="blog in list"
      :key="blog.id"
      :body-style="{ padding: '5px' }"
      class="infinite-list-item"
    >
      <div @click="goTo(blog.id)">
        <el-row>
          <el-col :span="18">
            <h4>{{ blog.title }}</h4>
            <span>发表于：{{ blog.created | parseTime }}</span>
            <p v-html="blog.body" />
          </el-col>
          <el-col :span="6">
            <img
              style="width: 100px; height: 100px"
              src="../../assets/userLogo.jpeg"
            >
          </el-col>
        </el-row>
      </div>
    </el-card>
    <pagination
      v-show="total>0"
      :total="total"
      :page.sync="listQuery.page"
      :limit.sync="listQuery.limit"
      @pagination="getList"
    />
  </div>
</template>

<script>
import { getBlogs, getTags, getCategories } from '@/api/blog'
import Pagination from '@/components/Pagination'
import Sticky from '@/components/Sticky' // 粘性header组件

export default {
  name: 'Blogs',
  components: { Pagination, Sticky },
  data() {
    return {
      seen: false,
      list: null,
      total: 0,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 10
      },
      loading: false,
      tags: [],
      categoies: []
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = true
      getBlogs(this.listQuery).then(response => {
        console.log(response.data)
        this.list = response.data.items
        this.total = response.data.total

        // Just to simulate the time of the request
        setTimeout(() => {
          this.listLoading = false
        }, 200)
      })
    },
    getTags() {
      getTags().then(response => {
        console.log(response.data)
        this.tags = response.data.items
      })
    },
    getCategories() {
      getCategories().then(response => {
        console.log(response.data)
        this.categoies = response.data.items
      })
    },
    preload() {
      this.seen = true
      this.getCategories()
      this.getTags()
    },
    load() {
      this.page += 1
    },
    goTo(id) {
      this.$router.push({ path: '/blogs/' + id })
    }
  }
}
</script>

<style scoped>
.edit-input {
  padding-right: 100px;
}
.cancel-btn {
  position: absolute;
  right: 15px;
  top: 10px;
}
</style>
