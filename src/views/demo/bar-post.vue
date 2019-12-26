<template>
  <el-card class="box-card" shadow="hover">
    <router-link :to="'/blogs/'+post.id" class="link-type">
      <p stype="fontSize: 60px">{{ post.title }}</p>
    </router-link>
    <span>{{ post.created | parseTime }}</span>
    <p v-html="marked(post.body)" />
  </el-card>
</template>

<script>
import MarkdownIt from 'markdown-it'

const md = new MarkdownIt()

export default {
  props: {
    post: {
      type: Object,
      default: null
    }
  },
  methods: {
    marked(content) {
      return md.render(content)
    }
  }
}
</script>

<style scoped>
h3 {
  margin-left: 10px;
  /* padding: 20px; */
}
</style>
