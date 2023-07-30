from functools import wraps
from flask_jwt_extended import verify_jwt_in_request,  get_jwt_identity,exceptions
from lib import response_code, pretty_result


def user_power(api_role=[]):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            try:
                verify_jwt_in_request()
            except exceptions.NoAuthorizationError as e:
                return pretty_result(response_code.AUTHORIZATION_ERROR,data=None,msg='请求头错误！')
            except Exception as new_e:
                return pretty_result(response_code.AUTHORIZATION_ERROR,data=None,msg=str(new_e))
            if len(api_role) !=0:
                # 获取到用户信息
                current_user = get_jwt_identity()
                permissionList=current_user['user_permissions']
                for each_api_role in api_role:
                    if each_api_role not in permissionList:
                        return pretty_result(response_code.AUTHORIZATION_ERROR,data=None,msg='抱歉，您没有相关权限！')
            a=0
            return fn(*args, **kwargs)

        return decorator

    return wrapper
