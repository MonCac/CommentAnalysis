from backend.apps.service.suggestion import suggestion


# 市场分析建议
@suggestion.route('/marketanalysissuggestion')
def marketAnalysisSuggestion(params):
    return


# 设施需求建议
@suggestion.route('/facilityrequirementssuggestion')
def facilityRequirementsSuggestion(params):
    return


# 用户经营建议
@suggestion.route('/usermanagementsuggestion')
def userManagementSuggestion(params):
    return
