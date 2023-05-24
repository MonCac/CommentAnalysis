import request from "./request";

// 登陆
export function login() {
    return request({
        url: "/login/",
        method: "get"
    });
}

// 用户注册
export function userRegister(params) {
    return request({
        url: "/userregister",
        method: "post",
        params
    });
}

// 商户注册
export function merchantRegister(params) {
    return request({
        url: "/merchantregister",
        method: "post",
        params
    });
}

// 修改密码
export function changePassword(params) {
    return request({
        url: "/changepassword",
        method: "post",
        params
    });
}

// 修改商户名称
export function changeMerchantName(params) {
    return request({
        url: "/changemerchantname",
        method: "post",
        params
    });
}

// 修改商户地址
export function changeMerchantAddress(params) {
    return request({
        url: "/changemerchantaddress",
        method: "post",
        params
    });
}

// 修改商户状态
export function changeMerchantState(params) {
    return request({
        url: "/changemerchantstate",
        method: "post",
        params
    });
}

// 修改商户所在城市
export function changeMerchantCity(params) {
    return request({
        url: "/changemerchantcity",
        method: "post",
        params
    });
}

// 搜索
export function normalSearch(params) {
    return request({
        url: "/normalsearch",
        method: "post",
        params
    });
}

// 模糊搜索
export function fuzzySearch(params) {
    return request({
        url: "/fuzzysearch",
        method: "post",
        params
    });
}

// 根据浏览推荐商家
export function recommendByBrowsing(params) {
    return request({
        url: "/recommendbybrowsing",
        method: "post",
        params
    });
}

// 根据位置推荐商家
export function recommendByPosition(params) {
    return request({
        url: "/recommendbyposition",
        method: "post",
        params
    });
}

// 默认推荐排序
export function recommendDefault(params) {
    return request({
        url: "/recommenddefault",
        method: "post",
        params
    });
}

// 选择推荐方式
export function recommendByChoice(params) {
    return request({
        url: "/recommendbychoice",
        method: "post",
        params
    });
}

// 量化排序推荐
export function recommendByQuantization(params) {
    return request({
        url: "/recommendbyquantization",
        method: "post",
        params
    });
}

// 个性化推荐
export function recommendPersonalized(params) {
    return request({
        url: "/recommendPersonalized",
        method: "post",
        params
    });
}

// 市场分析建议
export function marketAnalysisSuggestion() {
    return request({
        url: "/marketanalysissuggestion",
        method: "get"
    });
}

// 设施需求建议
export function facilityRequirementsSuggestion() {
    return request({
        url: "/facilityrequirementssuggestion",
        method: "get"
    });
}

// 用户经营建议
export function userManagementSuggestion() {
    return request({
        url: "/usermanagementsuggestion",
        method: "get"
    });
}

// 相似商户评价推荐好友
export function evaluationRecommendFriend() {
    return request({
        url: "/evaluationrecommendfriend",
        method: "get"
    });
}

// 相似好友推荐好友
export function friendRecommendFriend() {
    return request({
        url: "/friendrecommendfriend",
        method: "get"
    });
}






















