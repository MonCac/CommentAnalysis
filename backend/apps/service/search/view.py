from backend.apps.service.search import search


# 正常搜索
@search.route('/normalsearch')
def normalSearch(params):
    return


# 模糊搜索
@search.route('/fuzzysearch')
def fuzzySearch(params):
    return
