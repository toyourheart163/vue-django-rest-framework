<template>
  <el-form ref="form" :model="form" label-width="80px">
    <el-form-item label="Username">
      <el-input v-model="form.username" />
    </el-form-item>
    <el-form-item label="Password">
      <el-input v-model="form.password" />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">登陆</el-button>
      <el-button type="danger" @click="register">注册</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import { login } from '@/api/user'

export default {
  name: 'DemoForm',
  data() {
    return {
      form: {
        username: 'bar',
        password: 'ok'
      },
      password1: '',
      redirect: undefined
    }
  },
  watch: {
    $route: {
      handler: function(route) {
        this.redirect = route.query && route.query.redirect
      },
      immediate: true
    }
  },
  methods: {
    onSubmit() {
      login(this.form).then(resp => {
        console.log(resp.data)
      })
    },
    register() {
      //
    }
  }
}
</script>
