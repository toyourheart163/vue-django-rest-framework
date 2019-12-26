import request from '@/utils/api'

export function getBlogs(query) {
  return request({
    url: '/blogs/',
    method: 'get',
    params: query
  })
}

export function getComments(query) {
  return request({
    url: `/comments/`,
    method: 'get',
    params: query
  })
}

export function createComment(data) {
  return request({
    url: '/comments/',
    method: 'post',
    data
  })
}

export function getBlog(id) {
  return request({
    url: `/blogs/${id}/`,
    method: 'get'
  })
}

export function createBlog(data) {
  return request({
    url: '/blogs/',
    method: 'post',
    data
  })
}

export function updateBlog(data) {
  return request({
    url: '/blogs/',
    method: 'post',
    data
  })
}

export function getTags() {
  return request({
    url: '/tags/',
    method: 'get'
  })
}

export function getCategories() {
  return request({
    url: '/categories/',
    method: 'get'
  })
}
