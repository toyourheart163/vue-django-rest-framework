<template>
  <div>
    <el-input v-model="form.user" placeholder="用户名" />
    <markdown-editor v-model="form.content" :options="{hideModeSwitch:true,previewStyle:'tab'}" height="180px" />
  </div>
</template>

<script>
import MarkdownEditor from '@/components/MarkdownEditor'

export default {
  components: { MarkdownEditor },
  props: {
    form: {
      type: Object,
      default: null
    }
  },
  data() {
    return {
      seen: false
    }
  }
}

</script>
