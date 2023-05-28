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
        params: {saveAddress :paramss}
    });
}

// 修改商户状态
export function changeMerchantState(paramss) {
    return request({
        url: "/changemerchantstate",
        method: "get",
        params:{saveGender :paramss}
    });
}

// 修改商户所在城市
export function changeMerchantCity(paramss) {
    return request({
        url: "/changemerchantcity",
        method: "get",
        params:{saveGender:paramss}
    });
}

// 搜索
export function normalSearch(paramss) {
    return request({
        url: "/normalsearch",
        method: "get",
        params: {search :paramss}
    });
}

// 模糊搜索
export function fuzzySearch(paramss) {
    return request({
        url: "/fuzzysearch",
        method: "get",
        params :{submit1:paramss}
    });
}

// 展示界面
export function showInfo(paramss) {
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
    return request({
        url: "/recommendbystate",
        method: "get",
        params: {recommendByState: paramss}
    });
}

// 根据city推荐商家
export function recommendByCity(paramss) {
    return request({
        url: "/recommendbycity",
        method: "get",
        params: {recommendByCity: paramss}
    });
}

// 根据state和city推荐商家
export function recommendByStateAndCity(paramss) {
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






















