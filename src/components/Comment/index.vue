<template>
  <div>
    <div class="item-header">
      <div class="author">
        <div class="avatar">
          <img src="../../assets/user.png" alt="avatar">
        </div>
      </div>
      <div class="info">
        <div class="name">
          {{ comment.user }}
        </div>
        <div class="time">
          {{ comment.created | parseTime }}
        </div>
      </div>
    </div>
    <div class="comment-detail" v-html="marked(comment.content)" />
  </div>
</template>

<script>
import MarkdownIt from 'markdown-it'
import hljs from 'highlight.js'
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
  props: {
    comment: {
      type: Object,
      required: true
    }
  },
  methods: {
    marked(content) {
      return md.render(content)
    }
  }
}
</script>

<style lang="scss" scoped>
.item-header {
  position: relative;
  padding-left: 45px;
  padding-bottom: 10px;
  .author {
    position: absolute;
    left: 0;
    display: inline-block;
    .avatar {
      display: inline-block;
      margin-right: 5px;
      width: 40px;
      height: 40px;
      vertical-align: middle;
      img {
        width: 100%;
        height: 100%;
        border-radius: 50%;
      }
    }
  }
  .info {
    display: inline-block;
    .name {
      font-size: 15px;
      color: #333;
    }
    .time {
      font-size: 12px;
      color: #969696;
    }
  }
}
.comment-detail {
  min-height: 40px;
}
</style>
