<template>
  <div>
    <el-card class="box-card" shadow="hover">
      <article>
        <h2>{{ blog.title }}</h2>
        <span>发表于 {{ blog.created | parseTime('{y}-{m}-{d} {h}:{i}:{s}') }}</span>
        <div v-html="blog.body" />
      </article>
    </el-card>
    <commentList />
  </div>
</template>

<script>
import { getBlog } from '@/api/blog'
import MarkdownIt from 'markdown-it'
import hljs from 'highlight.js'
import commentList from './comment-list'

import 'highlight.js/styles/solarized-dark.css'

const md = new MarkdownIt({
  highlight: function(str, lang) {
    if (lang && hljs.getLanguage(lang)) {
      try {
        return '<pre class="hljs"><code>' +
               hljs.highlight(lang, str, true).value +
               '</code></pre>'
      } catch (__) {
        return 'error'
      }
    }
    return ''
  }
})

export default {
  name: 'BlogDetail',
  components: { commentList },
  data() {
    return {
      blog: {
        body: '',
        title: ''
      },
      id: this.$route.params && this.$route.params.id
    }
  },
  watch: {
    $route: {
      immediate: true,
      handler(to, from) {
        this.getBlogDetail(this.id)
      }
    }
  },
  methods: {
    getBlogDetail(id) {
      getBlog(id).then(resp => {
        this.blog = resp.item
        this.blog.body = md.render(resp.item.body)
      })
    }
  }
}

</script>

<style scoped>
.editor-container{
  margin-bottom: 3px;
}
.tag-title{
  margin-bottom: 5px;
}

pre {
	display: block;
	padding: 10px;
	margin: 0 0 10px;
	font-size: 14px;
	line-height: 1.42857143;
	color: #abb2bf;
	background: #23241f;
	word-break: break-all;
	word-wrap: break-word;
	overflow: auto;
	border-radius: 5px;
}
</style>
