
<template>
  <div class="comment-list">
    <div class="top-title">
      <span>{{ total }} 条评论</span>
      <el-button type="primary" :loading="loading" @click="refreshComments">刷新评论</el-button>
    </div>
    <div v-for="(item, i) in comments" :key="i" class="item">
      <Comment :comment="item" />
      <div class="item-comment">
        <div class="message">
          <!-- 第二层回复 -->
          <el-button size="small" @click="showCommentModal(item.id, item.content, 2)">回复</el-button>
        </div>
      </div>
      <div v-for="(e, i2) in item.sub_comment" :key="i2" class="item-other">
        <Comment :comment="e" />
        <!-- 第三层回复 -->
        <el-button size="small" @click="showCommentModal(e.id, e.content, 3)">回复</el-button>
        <div v-for="(j, i3) in e.sub_comment" :key="i3" class="item-other">
          <Comment :comment="j" />
        </div>
      </div>
    </div>
    <pagination
      v-show="total>0"
      :total="total"
      :page.sync="listQuery.page"
      :limit.sync="listQuery.limit"
      @pagination="getList"
    />
    <el-card :body-style="{ padding: '5px', height: '300px' }">
      <div slot="header">
        <span>欢迎评论：</span>
      </div>
      <!-- card body -->
      <CommentForm :form="form" class="comment-form" />
      <el-button type="primary" @click="onSubmit(form)">立即评论</el-button>
    </el-card>
    <el-dialog
      :visible.sync="seen"
      width="90%"
      @close="!seen"
    >
      <span>回复给：{{ sub_content }}</span>
      <CommentForm :form="sub_form" class="comment-form" />
      <el-button type="primary" @click="onSubmit(sub_form)">立即回复</el-button>
    </el-dialog>
  </div>
</template>

<script>
import { getComments, createComment } from '@/api/blog'
import CommentForm from './comment-form'
import Pagination from '@/components/Pagination'
import Comment from '@/components/Comment'

export default {
  components: { CommentForm, Pagination, Comment },
  data() {
    return {
      seen: false,
      comments: [],
      total: 0,
      id: this.$route.params && this.$route.params.id,
      form: {
        content: 'sm syi**sorry**',
        user: '匿名',
        blog: this.$route.params && this.$route.params.id
      },
      sub_content: null,
      level: null,
      sub_form: {
        content: '子评论content',
        user: '匿名',
        parent_comment: null
      },
      listQuery: {
        page: 1,
        limit: 10,
        blog: null
      },
      loading: false
    }
  },
  created() {
    this.getList(this.listQuery)
  },
  methods: {
    getList(listQuery) {
      this.listQuery.blog = this.id
      console.log(this.listQuery)
      this.loading = true
      getComments(this.listQuery).then(resp => {
        this.comments = resp.data.items
        this.total = resp.data.total

        setTimeout(() => {
          this.loading = false
        }, 200)
      })
    },
    showCommentModal(parent_comment_id, sub_content, level) {
      this.sub_form.parent_comment = parent_comment_id
      this.sub_content = sub_content
      this.level = level
      this.seen = true
    },
    onSubmit(comment) {
      createComment(comment).then(resp => {
        this.$message({
          message: '保存成功',
          type: 'success',
          showClose: true,
          duration: 1000
        })
        this.seen = false
        const data = resp.items
        console.log('data ', data)
        if (comment.blog) {
          // 一级评论
          this.comments.unshift(data)
          console.log('add 1 level')
        } else if (this.level === 3) {
          // 三级评论
          this.comments.forEach((x, i, comments) => {
            // console.log(i, x)
            x.sub_comment.forEach((xs, j, c) => {
              // console.log(j, xs)
              if (xs.id === data.parent_comment) {
                xs.sub_comment.unshift(data)
                // console.log('add 3 level')
              }
            })
          })
          console.log('level 3')
        } else if (this.level === 2) {
          // 二级评论
          this.comments.forEach((x, i, comments) => {
            if (x.id === data.parent_comment) {
              x.sub_comment.unshift(data)
              console.log('add 2 level')
            }
          })
        }
      })
    },
    refreshComments() {
      this.getList(this.listQuery)
    }
  }
}

</script>

<style lang="scss" scoped>
.comment-list {
  text-align: center;
}
.comment-list {
  position: relative;
  text-align: left;
  padding-top: 30px;
  margin-top: 30px;
  border-top: 1px solid #eee;
  .avatar {
    position: absolute;
    left: 0px;
  }
  .el-icon-circle-plus {
    font-size: 40px;
  }
}
.clearfix {
  clear: both;
}
.comment-list {
  margin-top: 30px;
  .top-title {
    padding-bottom: 20px;
    font-size: 17px;
    font-weight: 700;
    border-bottom: 1px solid #f0f0f0;
  }
  .item {
    padding: 20px 0 30px;
    border-bottom: 1px solid #f0f0f0;
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
    .item-comment {
      .like {
        margin-right: 20px;
      }
    }
  }
}
.item-other {
  margin: 20px;
  padding: 10px;
  border-left: 2px solid #f0f0f0;
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
        width: 38px;
        height: 38px;
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
    border-bottom: 1px dashed #f0f0f0;
  }
  .message {
    padding: 10px;
  }
}
</style>
