<template>
  <div>
    <el-form ref="form" :model="blog">
      <el-form-item label="标题">
        <el-input v-model="blog.title" />
      </el-form-item>
      <el-form-item label="分类">
        <el-select v-model="blog.category" placeholder="请选择分类">
          <el-option
            v-for="item in categoies"
            :key="item.id"
            :label="item.name"
            :value="item.id"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="标签">
        <el-select v-model="blog.tags" multiple placeholder="请选择标签">
          <el-option
            v-for="item in tags"
            :key="item.id"
            :label="item.name"
            :value="item.id"
          />
        </el-select>
      </el-form-item>
      <el-form-item>
        <markdown-editor v-model="blog.body" :options="{ toolbarItems: ['heading','bold','italic']}" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="addBlog">立即创建</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { createBlog, getCategories, getTags } from '@/api/blog'
import MarkdownEditor from '@/components/MarkdownEditor'

const content = `
**This is test**

* vue
* element
* webpack

`
export default {
  name: 'CreateBlog',
  components: { MarkdownEditor },
  data() {
    return {
      blog: {
        title: 'blog title',
        body: content,
        tags: null,
        category: null
      },
      loading: false,
      tags: [],
      categoies: []
    }
  },
  created() {
    this.getTags()
    this.getCategories()
  },
  methods: {
    addBlog() {
      this.loading = true
      createBlog(this.blog).then(response => {
        this.$message({
          message: '保存成功',
          type: 'success',
          showClose: true,
          duration: 1000
        })
      })
      this.loading = false
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
    }
  }
}
</script>

<style scoped>

</style>
