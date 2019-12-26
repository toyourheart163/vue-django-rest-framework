<template>
  <div>
    <div class="radio">
      排序：
      <el-radio-group v-model="reverse">
        <el-radio :label="false">倒序</el-radio>
        <el-radio :label="true">正序</el-radio>
      </el-radio-group>
    </div>
    <el-timeline :reverse="reverse">
      <el-timeline-item
        v-for="blog in blogs"
        :key="blog.id"
        :timestamp="blog.created | parseTime"
      >
        <router-link :to="`/blogs/${blog.id}`">{{ blog.id }} {{ blog.title }}</router-link>
      </el-timeline-item>
    </el-timeline>
    <div v-if="loading">loading...</div>
    <el-button type="primary" :disabled="nomore" @click="next">more</el-button>
    <el-tooltip placement="top" content="tooltip">
      <back-to-top :visibility-height="300" :back-position="50" transition-name="fade" />
    </el-tooltip>
  </div>
</template>

<script>
import { getBlogs } from '@/api/blog'
import BackToTop from '@/components/BackToTop'

export default {
  name: 'Timeline',
  components: { BackToTop },
  data() {
    return {
      reverse: false,
      blogs: [],
      listQuery: {
        page: 1,
        limit: 10,
        tags: null
      },
      loading: false,
      nomore: false,
      total: 0
    }
  },
  beforeRouteUpdate(to, from, next) {
    this.listQuery.tags = to.params.id
    this.listQuery.page = 1
    this.getList(this.listQuery)
    next()
  },
  created() {
    this.$route.params.tag ? this.listQuery.tags = this.$route.params.id : false
    this.getList(this.listQuery)
  },
  methods: {
    getList(listQuery) {
      getBlogs(listQuery).then(resp => {
        this.blogs = resp.data.items
        this.total = resp.data.total
        if (this.listQuery.page > this.total / this.listQuery.limit) {
          this.nomore = true
        } else {
          this.nomore = false
        }
      })
    },
    next() {
      this.listQuery.page += 1
      if (this.listQuery.page > this.total / this.listQuery.limit) {
        this.nomore = true
      }
      this.loading = true
      getBlogs(this.listQuery).then(resp => {
        this.blogs = this.blogs.concat(resp.data.items)
        this.loading = false
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.radio {
  padding: 10px;
}
.infinite-list {
  height: 500px;
  width: 300px;
  text-align: center;
  .infinite-list-item {
    height: 70px;
    width: 100%;
    background: blue;
    padding: 5px;
    margin: 5px;
  }
}
</style>
