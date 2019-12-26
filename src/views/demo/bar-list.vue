<template>
  <div>
    <blog-post
      v-for="post in posts"
      :key="post.id"
      :post="post"
    />
  </div>
</template>

<script>
import { getBlogs } from '@/api/blog'
import BlogPost from './bar-post'

export default {
  name: 'BarPost',
  components: { BlogPost },

  data() {
    return {
      posts: [],
      list: null,
      total: 0,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 10
      }
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = true
      getBlogs(this.listQuery).then(response => {
        const resp = response.data
        this.posts = resp.items
        this.total = resp.total

        // Just to simulate the time of the request
        setTimeout(() => {
          this.listLoading = false
        }, 0.5 * 1000)
      })
    }
  }
}
</script>

<style scoped>
.el-card {
  margin-top: 8px;
}
div {
  margin: 0 2px 0 2px;
}
</style>
