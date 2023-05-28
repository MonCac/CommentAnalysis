import request from "./request";

// 登陆
export function login(paramss) {
    return request({
        url: "/login",
        method: "get",
        params: {login : paramss}
    });
}

// 用户注册
export function userRegister(paramss) {
    debugger
    console.log("gogogo")
    console.log(paramss)
    debugger
    return request({
        url: "/userregister",
        method: "get",
        params: {register : paramss}
    });
}

// 商户注册
export function merchantRegister(paramss) {
    return request({
        url: "/merchantregister",
        method: "get",
        params: {register : paramss}
    });
}

// 修改密码
export function changePassword(params) {
    return request({
        url: "/changepassword",
        method: "get",
        params
    });
}

// 修改商户名称
export function changeMerchantName(params) {
    return request({
        url: "/changemerchantname",
        method: "get",
        params
    });
}

// 修改商户地址
export function changeMerchantAddress(paramss) {
    return request({
        url: "/changemerchantaddress",
        method: "get",
        params: {search :paramss}
    });
}

// 修改商户状态
export function changeMerchantState(params) {
    return request({
        url: "/changemerchantstate",
        method: "get",
        params
    });
}

// 修改商户所在城市
export function changeMerchantCity(params) {
    return request({
        url: "/changemerchantcity",
        method: "get",
        params
    });
}

// 搜索
export function normalSearch(paramss) {
    console.log(paramss)
    return request({
        url: "/normalsearch",
        method: "get",
        params: {search :paramss}
    });
}

// 模糊搜索
export function fuzzySearch(params) {
    return request({
        url: "/fuzzysearch",
        method: "get",
        params
    });
}

// 展示界面
export function showInfo(paramss) {
    debugger
    console.log(paramss)
    return request({
        url: "/showinfo",
        method: "get",
        params: {showShopInfo:paramss}
    });
}

// 根据浏览推荐商家
export function recommendByBrowsing(params) {
    return request({
        url: "/recommendbybrowsing",
        method: "get",
        params
    });
}

// 根据state推荐商家
export function recommendByState(paramss) {
    debugger
    console.log("gogogo")
    console.log(paramss)
    debugger
    return request({
        url: "/recommendbystate",
        method: "get",
        params: {recommendByState: paramss}
    });
}

// 根据city推荐商家
export function recommendByCity(paramss) {
    debugger
    console.log("gogogo")
    console.log(paramss)
    debugger
    return request({
        url: "/recommendbycity",
        method: "get",
        params: {recommendByCity: paramss}
    });
}

// 根据state和city推荐商家
export function recommendByStateAndCity(paramss) {
    debugger
    console.log("gogogo")
    console.log(paramss)
    debugger
    return request({
        url: "/recommendbystateandcity",
        method: "get",
        params: {recommendByStateAndCity: paramss}
    });
}

// 默认推荐排序
// export function recommendDefault(params) {
//     return request({
//         url: "/recommenddefault",
//         method: "get",
//         // params
//     });
// }

// 选择推荐方式
export function recommendByChoice(paramss) {
    debugger
    console.log("gogogo")
    console.log(paramss)
    debugger
    return request({
        url: "/recommendbychoice",
        method: "get",
        params: {recommendByChoice: paramss}
    })
}

// 量化排序推荐
export function recommendByQuantization(params) {
    return request({
        url: "/recommendbyquantization",
        method: "get",
        params
    });
}

// 个性化推荐
export function recommendPersonalized(params) {
    return request({
        url: "/recommendPersonalized",
        method: "get",
        params
    });
}

// 市场分析建议
export function marketAnalysisSuggestion(params) {
    return request({
        url: "/marketanalysissuggestion",
        method: "get",
        // params: {: paramss}
    });
}

// 设施需求建议
export function facilityRequirementsSuggestion(paramss) {
    debugger
    console.log("gogogo")
    console.log(paramss)
    debugger
    return request({
        url: "/facilityrequirementssuggestion",
        method: "get",
        params:{ facilityrequirementssuggestion : paramss }
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
export function evaluationRecommendFriend(paramss) {
    return request({
        url: "/evaluationrecommendfriend",
        method: "get",
        params: {friendRecommend :paramss}
    });
}

// 相似好友推荐好友
export function friendRecommendFriend() {
    return request({
        url: "/friendrecommendfriend",
        method: "get"
    });
}






















