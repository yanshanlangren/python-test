# -*- coding: UTF-8 -*-
from fnmatch import fnmatch
import json
import time
import random
import requests
import copy
import hmac
import base64
import hashlib
import urllib
from hashlib import sha256

MUSTACHE_WHOLE_PATTERN = "(\{\{(.*?)\}\}( *([\*\-+\/]) *([0-9]+|\{\{.*?\}\}))*)"
IGNORE_FILES = [
    "hello-*",
]
arr = ["hello-1", "world-2,", "love-3"]


class TestObject:
    def TestMethod(a):
        a.cease()


import re


def is_mustache_parameter(parameter):
    """
    Judge if is a mustache parameter
    """
    m = re.search(MUSTACHE_WHOLE_PATTERN, parameter)
    if m:
        return True
    else:
        return False


def FuncA(a):
    a["s"] = "b"


def FuncB(q):
    if q:
        return "aaa"
    else:
        return {"a": 1, "b": 2}


def func_c():
    for key in arr:
        ignore_matched = [arr for ignore_file in IGNORE_FILES if
                          fnmatch(key, ignore_file)]
    print(ignore_matched)


def func_d():
    for key in arr:
        ignore_matched = []
        for ignore_file in IGNORE_FILES:
            if fnmatch(key, ignore_file):
                ignore_matched.append(key)
        print(ignore_matched)
    for key in arr:
        ignore_matched = []
        for ignore_file in IGNORE_FILES:
            if fnmatch(key, ignore_file):
                ignore_matched.append(key)
        print(ignore_matched)


def func_d():
    a = ""

    if not a:
        print("a is none")

    print("main function started")
    a = ["a", "b", "c"]
    if "a" in a:
        print("yes")
    else:
        print("no")
    if None:
        print("true")
    else:
        print("false")

    b = TestObject()
    b.TestMethod()
    print("main function finished")
    key = "nodes.pg.count"
    map = {key: 2}
    value = map.get(key)
    # ({{(.*?)}}( *([*-+/]) *([0-9]+|{{.*?}}))*)

    if not map.get(key):
        print("null")
    elif is_mustache_parameter(map.get(key)):
        print("true")
    else:
        print("false")
    a = True
    if a is None:
        print("a None")
    if not a:
        print("not a")


def func_e():
    map_arr = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
    for m in map_arr:
        m["c"] = 0
    print(map_arr)


def func_f(str="asd"):
    print(str)


def func_g(a=1, b=2, c=3):
    print(a, b, c)


def func_h():
    params = {}
    request_param = {"a": 3}
    params.update(**request_param)
    print(params)
    func_g(**params)


def func_i():
    a = None
    if not a:
        print("a none")
    else:
        print("else")


# pop = eliminate element from map
def func_j():
    m = {"a": 1, "b": 2, "c": 3}
    print("before pop %s" % m)
    m.pop("a")
    print("after pop %s" % m)


def decode_base64(base64str):
    return base64.standard_b64decode(base64str)


def func_k():
    a = "aGVsbG8lMjB3b3JsZA=="
    content = decode_base64(a)
    print(content)


def __func_l(a, b):
    a["key"] = "qqq"
    b["key"] = "www"


def func_m():
    map = {"a": 1, "b": 2}
    for k in map:
        print("key[%s], value[%s]" % (k, map[k]))
    arr = []
    arr.append("a")
    arr.append("b")
    print("%s" % arr)


def func_n():
    map = {"a": 1, "b": 2}
    if "a" in map:
        print("a in map")
    if "a" in map.keys():
        print("key a in map")
    if "c" in map:
        print("c in map")
    # print(map["c"])


def func_o():
    map = {"a": 1, "b": 2}
    print("%s" % len(map))


def func_p():
    map = None
    if map is None:
        print("is None")
    else:
        print("not None")


def func_q(str, **kwargs):
    print("string parmeter[%s], others[%s]" % (str, kwargs))


def func_q1(str):
    print("string parmeter[%s]" % str)


def func_r(str):
    d = json.loads(str)
    print("[%s]" % d)
    return d


def func_s(dic):
    str = json.dumps(dic)
    str = str.replace("\"", "\\\"")
    print("%s" % str)
    return str


def func_t():
    print("%s" % time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime(int(time.time()))))


def func_u():
    dic = {
        u'name': u'qqq'
    }
    print("dic[%s]" % dic)
    ExUnicode(dic)
    print("Ex dic[%s]" % dic)


def ExUnicode(input):
    li = []
    for item in input:
        dic = {}
        dic[item] = input[item].encode('utf-8')
        # dic[item.encode("utf-8")] = dic[item.encode("utf-8")].encode("utf-8")
    li.append(dic)
    return li


def func_v():
    dic = {
        "name": "abc",
        "gender": "male",
    }
    print("name[%s]" % dic.get("name", "default"))
    print("age[%s]" % dic.get("age", "0"))


def func_w():
    dic = {
        "name": "anc",
    }
    print("name[%s]" % dic.pop("name"))


def func_x():
    dic = {u'name': u'ZooKeeper',
           'service': {'services': [], 'version': '2.0'},
           u'multi_zone_policy': u'round_robin',
           u'advanced_actions': [u'change_vxnet', u'scale_horizontal'],
           u'env': {u'zkAdminUsername': u'super', u'maxClientCnxns': 1000,
                    u'autopurge.purgeInterval': 1, u'syncLimit': 5,
                    u'zkVersion': u'3.4.13', u'zkAdminPassword': u'Super12345',
                    u'initLimit': 10, u'zkAdminEnabled': False,
                    u'tickTime': 2000, u'autopurge.snapRetainCount': 3},
           u'nodes': [{u'count': 3, 'auto_scale_step': {},
                       u'vertical_scaling_policy': u'sequential',
                       u'container': {u'image': u'img-jlpv3z6s',
                                      u'type': u'kvm', u'zone': u'devops'},
                       u'server_id_upper_bound': 255,
                       u'volume': {u'class': 0, u'size': 10},
                       u'instance_class': 0, u'memory': 2048, u'services': {
                   u'start': {
                       u'cmd': u'bash -e /opt/zkapp/bin/zkServer.sh start'},
                   u'init': {u'cmd': u'bash -e /opt/zkapp/bin/init.sh'},
                   u'upgrade': {u'cmd': u'bash -e /opt/zkapp/bin/init.sh'},
                   u'stop': {
                       u'cmd': u'bash -e /opt/zkapp/bin/zkServer.sh stop'}},
                       u'cpu': 1}],
           u'endpoints': {u'client': {u'protocol': u'tcp', u'port': 65535},
                          u'rest': {u'protocol': u'tcp', u'port': 9998},
                          u'reserved_ips': {u'wvip': {u'value': u''}}},
           u'vxnet': u'', u'description': u''}
    print(dic["health_check"])


def func_y():
    a = u'\u5927\u6570\u636e lambda \u67b6\u6784\u6a21\u677f'.encode("utf-8")
    c = 'asdada'.encode("utf-8")
    b = '\xe5\xa4\xa7\xe6\x95\xb0\xe6\x8d\xae lambda \xe6\x9e\xb6\xe6\x9e\x84\xe6\xa8\xa1\xe6\x9d\xbf'.encode(
        "utf-8")
    if b == a:
        print("equals")
    else:
        print("not equals")

    print(c)


def func_z():
    a = {"name": 123}
    b = {"age": 13}
    print("a_name[%s]" % a.get("sex", 0))


def func_aa():
    a = False
    b = True
    print("%s" % (a ^ b))


def func_ab():
    a = {"name": "qqq", "age": 9}
    func_ac(**a)


def func_ac(**params):
    print(params)


def func_ad():
    search_str = " and (version_id like %%%s%% or version_name like %%%s%% or app_id like %%%s%% or app_name like %%%s%%)" % (
        "a", "b", "c", "d")

    search_word = ""

    if search_word:
        search_str = " and (version_id like '%%%s%%' or version_name like\
         '%%%s%%' or app_id like '%%%s%%' or app_name like '%%%s%%')" % (
            search_word, search_word, search_word, search_word)
    print(search_str)


def func_ae():
    status = ["submitted", "qqq"]
    status_sql = ''
    for status_item in status:
        print(status_item)
        status_sql += "'"
        status_sql += status_item
        status_sql += "',"
    status_sql = status_sql[:-1]
    print(status_sql)


def func_af():
    a = "abc"
    b = "def"
    print(b + a)


def func_ag():
    join_keys = []
    join_keys.append(
        (("a", "app_id"), ("b", "app_id"))
    )
    print(join_keys)


def func_ah():
    a = {"a": "q", "b": "d"}
    print(a.values())


def func_ai():
    a = 0b01,
    print("%d" % a)


def func_aj():
    a = [
        {"name": "ann"}
    ]
    for ele in a:
        ele["age"] = 10
    print(a)


def func_ak():
    APP_REVIEWS = {
        0: [],
        1: ['dev'],
        2: ['chanel'],
        3: ['dev', 'chanel']
    }
    result = [{'reviews': 1}]
    # add passed_reviews
    for app in result:
        reviews = app.get('reviews', 0)
        passed_reviews = APP_REVIEWS.get(reviews, [])
        app["passed_reviews"] = passed_reviews

    print(result)


def func_al():
    print(3 | 1)


def func_am():
    a = {'apprv-wwww': {
        'app_id': 'app-2mvdqrny',
        'remarks': '',
        'create_time': '2019',
        'review_role': 'dev',
        'app_review_id': 'apprv-wwww',
        'operator_name': '',
        'operator': '',
        'operator_email': '',
        'action': 'approved'
    },
        'apprv-qqqq': {
            'app_id': 'app-2mvdqrny',
            'remarks': '',
            'create_time': '',
            'review_role': 'dev',
            'app_review_id': 'apprv-qqqq',
            'operator_name': '',
            'operator': '',
            'operator_email': '',
            'action': 'submitted'
        }
    }
    b = {"name": 123, "age": 10}
    for key, value in a.items():
        print("id[%s], set[%s]" % (key, value))


def func_an():
    directive = {}
    sort_key = directive.get("sort_key")
    if not sort_key:
        sort_key = "submit_time"
    if sort_key not in ["submit_time", "review_time"]:
        return None


def func_ao(a, b=""):
    print("%s, %s" % (a, b))


def func_ap():
    a = {"name": "ann", "age": 10}
    a.pop("age")
    print(a)


def func_aq():
    a = None
    if a:
        print("a is not empty")
    else:
        print("empty")


def func_ar():
    version_set = {"a": "123"}
    for version_id in version_set:
        version_id += "'" + version_id + "',"
    print(version_id)


def func_as():
    reviews = 2
    _review_role = 0
    status = "approved"
    app_set = {"status": "submitted"}

    new_reviews = reviews | _review_role
    if status == "approved":
        new_status = app_set.get('status', '')
        if new_reviews == 3:
            new_status = "approved"
    else:
        new_status = status
    print(new_status)


def func_at():
    a = [{"name": "ann"}, {"name": "elvis"}]
    for record in a:
        record["age"] = 10
    print(a)


def func_au():
    a = [{"name": "ann"}, {"name": "elvis"}]
    for record in a:
        print(record.pop("name", ""))
    print(a)


def func_av():
    a = {"reviews": None}
    b = a.get("reviews", 0)
    if not b:
        b = 0
    print(b)


def func_aw():
    app_ids = ["a", "b", "c", "a"]
    print(app_ids)
    app_cond = {"app_id": list(set(app_ids))}
    print(app_cond)


def func_ax():
    a = None
    for b in a:
        print(b)
    print("finished")


def func_ay():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(random.choice(a))


def func_az():
    a = ["a", "b", "a"]
    print(a)
    b = list(set(a))
    print(b)


def func_ba():
    a = ["1", "2", "3"]
    print(",".join(a))


def func_bb():
    method = "GET"
    directory = "accesssystems"
    req = {
        "action": "CreateAccessSysId",
        "owner": "admin",
        "name": "testing",
        "access_sys_code": "app-uvmtab3x"
    }
    headers = {
        # "Grpc-Metadata-nb": "1",
        # "Authorization": "",

        # 'Authorization': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY3IiOiIxIiwiYXVkIjoiaWFtIiwiYXpwIjoiaWFtIiwiY29ucyI6ImFscGhhY2xvdWQiLCJjdWlkIjoiaWFtci1wOWN6enM2YiIsImVpc2siOiI2SlRxTUZBYTlfZ2xTV1Nib0NsWlF3dmN0U29TMm9yZkJPSlhmQnZ2dHBNPSIsImV4cCI6MTU5MjY2MzA0MywiaWF0IjoxNTkyNjU5NDQzLCJpc3MiOiJzdHMiLCJqdGkiOiJydU9EUm9kcFRmRlFzMmhUWDZyT3o5IiwibmJmIjowLCJvcmdpIjoiYXBwLXV2bXRhYjN4Iiwib3d1ciI6ImFkbWluIiwicHJlZiI6InFybjphbHBoYWNsb3VkOmlhbToiLCJyb3VyIjoiYWRtaW4iLCJydHlwIjoicm9sZSIsInN1YiI6InN0cyIsInR5cCI6IklEIn0.h53G4vQR2TcRyLN3FAMZ18SHV9EWIPs5oVk_3rz379UbnfiYodutWI_0xxPo1D1x-dlyLySsaVevjuluXRLJ4Ry5W7pZ5sL_a0Len9HUeSuHVhYe7xf25I0LvQIGVMgadfEnHSQ91isZBfwyQmLZ6Scaz1by6tNMx0gw1vYhmXA',
        'Grpc-Metadata-nb': '1'
    }
    base_url = 'http://139.198.121.68:19300/v1/'
    if not directory:
        return None
    url = base_url + directory
    rest_case = {
        "GET": requests.get,
        "POST": requests.post,
        "PATCH": requests.patch,
        "DELETE": requests.delete,
    }
    rest_medthod = rest_case.get(method, None)
    if not url:
        print("Error")
    data = json.dumps(req)
    rep = rest_medthod(url=url, data=data, headers=headers)
    print("rep[%s]" % rep.status_code)
    if rep.status_code == 200:
        print(rep.json())
    else:
        print("error")


def func_bc():
    actions = ["NBGetBalance", "NBCreateBalance", "NBListCharges",
               "NBCreateCharge", "NBListRecharges", "NBCreateRecharge",
               "NBDescribeActions", "NBDeleteAction", "NBCreateAction",
               "NBModifyAction", "NBBindingAccessSystemUser",
               "NBChangePassword", "NBInviteUser", "NBLogin", "NBLogout",
               "NBResetPassword", "NBBindingRoleAction", "NBRoleDetail",
               "NBDescribeRoles", "NBDeleteRole", "NBCreateRole",
               "NBModifyRole", "NBBindingRoleUser", "NBSendEmail",
               "NBSwitchAccessSys", "NBDescribeToken", "NBRefreshToken",
               "NBDescribeUsersDetail", "NBDescribeAccessSystem",
               "NBDescribeApiIds", "NBBindingUserRole", "NBDescribeUsers",
               "NBCreateUser", "NBModifyUser", "NBSendMessage",
               "NBCreateSender", "NBGetSender", "NBDeleteSender",
               "NBListReceivers", "NBAddReceiver", "NBDeleteReceiver",
               "NBClearReceivers", "NBCreateAccessSystemCatalog",
               "NBDescribeAccessSystems", "NBDeleteAccessSystems",
               "NBCreateAccessSystem", "NBModifyAccessSystem",
               "NBDescribeAttributes", "NBDeleteAttributes",
               "NBCreateAttribute", "NBModifyAttribute", "NBDescribeCatalogs",
               "NBDeleteCatalogs", "NBCreateCatalog", "NBModifyCatalog",
               "NBDescribeComponents", "NBDeleteComponents",
               "NBCreateComponent", "NBModifyComponent", "NBGetCosts",
               "NBDescribeFilters", "NBDeleteFilters", "NBCreateFilter",
               "NBModifyFilter", "NBModifyFilterName", "NBDescribePlans",
               "NBDeletePlans", "NBCreatePlan", "NBModifyPlan",
               "NBDescribeProducts", "NBDeleteProducts", "NBCreateProduct",
               "NBModifyProduct", "NBDescribeStrategies", "NBDeleteStrategies",
               "NBCreateStrategy", "NBModifyStrategy",
               "NBDescribeChargeFactors", "NBDeleteChargeFactors",
               "NBCreateChargeFactor", "NBModifyChargeFactor",
               "NBDescribePublicAttributes", "NBDescribeProdInstances",
               "NBRenewProdInstance", "NBStopProdInstance",
               "NBDescribeBillingJobs", "NBPerformBillingJob",
               "NBDescribeBills", "NBGetBill", "NBCreatePrdOrder",
               "NBCancelPrdOrder", "NBChargePrdOrder", "NBDescribePrdSuborder",
               "NBDescribePrdSuborderDetail"]
    pattern = "[A-Z]"
    for action in actions:
        name = action[2:]
        name_arr = re.sub(pattern, lambda x: "_" + x.group(0), name)
        new_name_arr = []
        for name_str in name_arr:
            new_name_arr.append(name_str.upper())
        new_name = "".join(new_name_arr)
        new_name = "ACTION_NB" + new_name
        print("%s: \"\"," % new_name)


def func_bm():
    actions = ["ACTION_NB_GET_RECHARGE", "ACTION_NB_GET_WALLET",
               "ACTION_NB_CREATE_WALLET", "ACTION_NB_DESCRIBE_MEMBERS",
               "ACTION_NB_BINDING_MEMBER_ROLE",
               "ACTION_NB_DELETE_UNACTIVITY_ACCESS_SYSTEM_USER",
               "ACTION_NB_MODIFY_ACCESS_SYSTEM_USER",
               "ACTION_NB_BINDING_ROLES_MEMBERS",
               "ACTION_NB_REFRESH_OPEN_API_TOKEN",
               "ACTION_NB_DESCRIBE_USER_ACCESS_SYSTEMS",
               "ACTION_NB_RESET_PWD_SEND_EMAIL",
               "ACTION_NB_MODIFY_ACCESS_SYSTEM_CONFIG",
               "ACTION_NB_VERIFY_ACCESS_SYSTEM_CONFIG",
               "ACTION_NB_GET_PRICING_INFOS", "ACTION_NB_GET_COSTS_SIMPLE",
               "ACTION_NB_CREATE_DISCOUNT", "ACTION_NB_PAUSE_PROD_INSTANCE",
               "ACTION_NB_RESUME_PROD_INSTANCE",
               "ACTION_NB_PUSH_METERING_DATA",
               "ACTION_NB_CREATE_PRD_SUBORDER_SIMPLE"]
    pattern = "[A-Z]"
    for action in actions:
        name = action[10:]
        name_arr = name.split("_")
        new_name = ""
        for name_str in name_arr:
            new_name += name_str[0] + name_str.lower()[1:]
        print("%s," % action)


def func_bd():
    a = {"name": "ann", "age": 18}
    a.update({"height": 180})
    func_be(**a)


def func_be(name, **params):
    print("name[%s]" % name)
    print("params[%s]" % params)


def func_bf():
    a = ["a", "b", "c"]
    b = {}
    b.update({a: ""})
    print(b)


def func_bg():
    a = "2020-09-13"
    b = "2022-09-13"
    timeArray = time.strptime(a, "%Y-%m-%d")
    print(timeArray)
    timeStamp = int(time.mktime(timeArray))
    print(timeStamp)


def func_bh():
    a = ["qqqq", "aaaa", "ssss"]
    b = copy.copy(a)
    for str in b:
        print("str[%s]" % str)
        print("b[%s]" % b)
        b.remove(str)
        print("b[%s]" % b)


def func_bi():
    a = 'elb:DescribeLoadBalancerPolicyRewriteRules,elb:DescribeLoadBalancerListeners,elb:DescribeWAFRules,elb:DescribeLoadBalancerBackends,elb:DescribeLoadBalancers,elb:DescribeWAFDomainPolicies,elb:DescribeLoadBalancerPolicies,elb:DescribeWAFParameters,elb:DescribeWAFParameterGroups,elb:DescribeWAFRuleGroups,elb:AddLoadBalancerPolicyRewriteRules,elb:AttachWAFDomainPolicies,elb:DeleteLoadBalancerPolicyRules,elb:DeleteWAFRuleGroups,elb:DeleteWAFParameterGroups,elb:ApplyLoadBalancerPolicy,elb:DetachWAFDomainPolicies,elb:ResetWAFParameters,elb:UpdateWAFParameters,elb:DeleteLoadBalancerListeners,elb:ResizeLoadBalancers,elb:ModifyWAFParameterGroupAttributes,elb:ApplyWAFParameterGroup,elb:AddLoadBalancerBackends,elb:ModifyLoadBalancerPolicyRewriteRuleAttributes,elb:AddLoadBalancerPolicyRules,elb:ModifyLoadBalancerPolicyAttributes,elb:ModifyLoadBalancerBackendAttributes,elb:DeleteLoadBalancerPolicyRewriteRules,elb:CreateWAFParameterGroup,elb:DeleteLoadBalancerBackends,elb:DeleteLoadBalancerPolicies,elb:DissociateEipsFromLoadBalancer,elb:ModifyLoadBalancerPolicyRuleAttributes,elb:AddWAFRules,elb:AddLoadBalancerListeners,elb:DeleteWAFRules,elb:CreateLoadBalancerPolicy,elb:ModifyLoadBalancerAttributes,elb:UpdateLoadBalancers,elb:CreateWAFRuleGroup,elb:ModifyLoadBalancerListenerAttributes,elb:AssociateEipsToLoadBalancer,elb:StartLoadBalancers,elb:DeleteLoadBalancers,elb:StopLoadBalancers,elb:CreateWAFDomainPolicy,elb:DeleteWAFDomainPolicies,elb:CreateLoadBalancer'
    a.split(",")
    print(a.split(","))


def func_bj():
    a = ''
    print(a == 'yes' or a == 'true' or a)
    if "" and True:
        print("yes")


def func_bk():
    if True and '':
        print(True)


def func_bl():
    url = "http://www.baidu.com/asdsad"
    a = {"owner": "admin", "name": "aaaa"}
    url += "?"
    for name, value in a.items():
        url += name + "=" + value + "&"
    url = url[:-1]
    print(url)


def func_bn():
    url = "http://www.baidu.com/{user_id}/{}"
    req = {
        "user_id": "anny",
        "school": "BIT"
    }
    if not url.__contains__("{"):
        print("do not have { in")
        return
    while url.__contains__("{") and url.__contains__("}"):
        left = url.index("{")
        right = url.index("}")
        if left + 1 > len(url) or right + 1 > len(url) or left > right:
            print("fail")
            return
        key = url[left + 1:right]
        print("key[%s]" % key)
        url = url[:left] + req.get(key, "") + url[right + 1:]
    print(url)


def func_bo():
    file_path = "C:\\Users\\Elvis\\Desktop\\appcenter.yaml"
    with open(file_path) as f:
        print(f.read())


def func_bp():
    a = "ab-cd"
    print([a])


def func_bq():
    app = {'service_fee_rate': 0, 'sub_category': '', 'cover_img': '', 'terms_of_service': '', 'app_id': 'app-fufbtcah',
           'console_id': 'ehpccloud', 'create_time': '',
           'plugins': '{"hide_nav":0}', 'owner': 'admin', 'message': '', 'screenshots': '', 'app_name': 'test', 'category': '',
           'app_type': 'web', 'company_url': '', 'status_time': '', 'status': 'draft',
           'access_sys_id': 'sys_LOjwPWBrWrQG', 'abstraction': '', 'app_contract_status': 'new', 'description': '', 'tags': '',
           'auth_level': 0, 'visibility': 'public', 'client_id': '', 'app_iam_policy_id': '', 'usage_instructions': '',
           'icon': '', 'app_instance_id': '', 'usage_instructions_token': '', 'reviews': 0, 'url': '', 'root_user_id': 'admin',
           'contact': '', 'zone_info': '["ehpca","ehpc"]', 'terms_of_service_token': ''}
    if app['app_type'] == 'web' and app.get('access_sys_id', ''):
        print("123")
        if not app.get('app_iam_policy_id'):
            print("321")


qqq = ""


def func_br():
    return 2


def func_bs():
    a = "asda"
    b = a if a else ""
    print(b)


def func_bt():
    a = {"name": "ann"}
    print(a)
    print(a.__str__())


def func_bu():
    a = "asdasda@123"
    if a.__contains__("@"):
        print("contains")


def func_bv():
    a = "asd"
    b = a.split(",")
    print(b)


def func_bw():
    a = 'ACTION_NB_GET_TOKEN = "NBGetToken",ACTION_NB_GET_RECHARGE = "NBGetRecharge",ACTION_NB_GET_WALLET = "NBGetWallet",ACTION_NB_CREATE_WALLET = "NBCreateWallet",ACTION_NB_DESCRIBE_MEMBERS = "NBDescribeMembers",ACTION_NB_BINDING_MEMBER_ROLE = "NBBindingMemberRole",ACTION_NB_DELETE_UNACTIVITY_ACCESS_SYSTEM_USER = "NBDeleteUnactivityAccessSystemUser",ACTION_NB_MODIFY_ACCESS_SYSTEM_USER = "NBModifyAccessSystemUser",ACTION_NB_BINDING_ROLES_MEMBERS = "NBBindingRolesMembers",ACTION_NB_REFRESH_OPEN_API_TOKEN = "NBRefreshOpenApiToken",ACTION_NB_DESCRIBE_USER_ACCESS_SYSTEMS = "NBDescribeUserAccessSystems",ACTION_NB_RESET_PWD_SEND_EMAIL = "NBResetPwdSendEmail",ACTION_NB_MODIFY_ACCESS_SYSTEM_CONFIG = "NBModifyAccessSystemConfig",ACTION_NB_VERIFY_ACCESS_SYSTEM_CONFIG = "NBVerifyAccessSystemConfig",ACTION_NB_GET_PRICING_INFOS = "NBGetPricingInfos",ACTION_NB_GET_COSTS_SIMPLE = "NBGetCostsSimple",ACTION_NB_CREATE_DISCOUNT = "NBCreateDiscount",ACTION_NB_PAUSE_PROD_INSTANCE = "NBPauseProdInstance",ACTION_NB_RESUME_PROD_INSTANCE = "NBResumeProdInstance",ACTION_NB_PUSH_METERING_DATA = "NBPushMeteringData",ACTION_NB_CREATE_PRD_SUBORDER_SIMPLE = "NBCreatePrdSuborderSimple",ACTION_NB_RECHARGE_ALIPAY_RETURN = "NBChargeAlipayReturn",ACTION_NB_GET_BALANCE = "NBGetBalance",ACTION_NB_CREATE_BALANCE = "NBCreateBalance",ACTION_NB_LIST_CHARGES = "NBListCharges",ACTION_NB_CREATE_CHARGE = "NBCreateCharge",ACTION_NB_LIST_RECHARGES = "NBListRecharges",ACTION_NB_CREATE_RECHARGE = "NBCreateRecharge",ACTION_NB_DESCRIBE_ACTIONS = "NBDescribeActions",ACTION_NB_DELETE_ACTION = "NBDeleteAction",ACTION_NB_CREATE_ACTION = "NBCreateAction",ACTION_NB_MODIFY_ACTION = "NBModifyAction",ACTION_NB_BINDING_ACCESS_SYSTEM_USER = "NBBindingAccessSystemUser",ACTION_NB_CHANGE_PASSWORD = "NBChangePassword",ACTION_NB_INVITE_USER = "NBInviteUser",ACTION_NB_LOGIN = "NBLogin",ACTION_NB_LOGOUT = "NBLogout",ACTION_NB_RESET_PASSWORD = "NBResetPassword",ACTION_NB_BINDING_ROLE_ACTION = "NBBindingRoleAction",ACTION_NB_ROLE_DETAIL = "NBRoleDetail",ACTION_NB_DESCRIBE_ROLES = "NBDescribeRoles",ACTION_NB_DELETE_ROLE = "NBDeleteRole",ACTION_NB_CREATE_ROLE = "NBCreateRole",ACTION_NB_MODIFY_ROLE = "NBModifyRole",ACTION_NB_BINDING_ROLE_USER = "NBBindingRoleUser",ACTION_NB_SEND_EMAIL = "NBSendEmail",ACTION_NB_SWITCH_ACCESS_SYS = "NBSwitchAccessSys",ACTION_NB_DESCRIBE_TOKEN = "NBDescribeToken",ACTION_NB_REFRESH_TOKEN = "NBRefreshToken",ACTION_NB_DESCRIBE_USERS_DETAIL = "NBDescribeUsersDetail",ACTION_NB_DESCRIBE_ACCESS_SYSTEM = "NBDescribeAccessSystem",ACTION_NB_DESCRIBE_API_IDS = "NBDescribeApiIds",ACTION_NB_BINDING_USER_ROLE = "NBBindingUserRole",ACTION_NB_DESCRIBE_USERS = "NBDescribeUsers",ACTION_NB_CREATE_USER = "NBCreateUser",ACTION_NB_MODIFY_USER = "NBModifyUser",ACTION_NB_SEND_MESSAGE = "NBSendMessage",ACTION_NB_CREATE_SENDER = "NBCreateSender",ACTION_NB_GET_SENDER = "NBGetSender",ACTION_NB_DELETE_SENDER = "NBDeleteSender",ACTION_NB_LIST_RECEIVERS = "NBListReceivers",ACTION_NB_ADD_RECEIVER = "NBAddReceiver",ACTION_NB_DELETE_RECEIVER = "NBDeleteReceiver",ACTION_NB_CLEAR_RECEIVERS = "NBClearReceivers",ACTION_NB_CREATE_ACCESS_SYSTEM_CATALOG = "NBCreateAccessSystemCatalog",ACTION_NB_DESCRIBE_ACCESS_SYSTEMS = "NBDescribeAccessSystems",ACTION_NB_DELETE_ACCESS_SYSTEMS = "NBDeleteAccessSystems",ACTION_NB_CREATE_ACCESS_SYSTEM = "NBCreateAccessSystem",ACTION_NB_MODIFY_ACCESS_SYSTEM = "NBModifyAccessSystem",ACTION_NB_DESCRIBE_ATTRIBUTES = "NBDescribeAttributes",ACTION_NB_DELETE_ATTRIBUTES = "NBDeleteAttributes",ACTION_NB_CREATE_ATTRIBUTE = "NBCreateAttribute",ACTION_NB_MODIFY_ATTRIBUTE = "NBModifyAttribute",ACTION_NB_DESCRIBE_CATALOGS = "NBDescribeCatalogs",ACTION_NB_DELETE_CATALOGS = "NBDeleteCatalogs",ACTION_NB_CREATE_CATALOG = "NBCreateCatalog",ACTION_NB_MODIFY_CATALOG = "NBModifyCatalog",ACTION_NB_DESCRIBE_COMPONENTS = "NBDescribeComponents",ACTION_NB_DELETE_COMPONENTS = "NBDeleteComponents",ACTION_NB_CREATE_COMPONENT = "NBCreateComponent",ACTION_NB_MODIFY_COMPONENT = "NBModifyComponent",ACTION_NB_GET_COSTS = "NBGetCosts",ACTION_NB_DESCRIBE_FILTERS = "NBDescribeFilters",ACTION_NB_DELETE_FILTERS = "NBDeleteFilters",ACTION_NB_CREATE_FILTER = "NBCreateFilter",ACTION_NB_MODIFY_FILTER = "NBModifyFilter",ACTION_NB_MODIFY_FILTER_NAME = "NBModifyFilterName",ACTION_NB_DESCRIBE_PLANS = "NBDescribePlans",ACTION_NB_DELETE_PLANS = "NBDeletePlans",ACTION_NB_CREATE_PLAN = "NBCreatePlan",ACTION_NB_MODIFY_PLAN = "NBModifyPlan",ACTION_NB_DESCRIBE_PRODUCTS = "NBDescribeProducts",ACTION_NB_DELETE_PRODUCTS = "NBDeleteProducts",ACTION_NB_CREATE_PRODUCT = "NBCreateProduct",ACTION_NB_MODIFY_PRODUCT = "NBModifyProduct",ACTION_NB_DESCRIBE_STRATEGIES = "NBDescribeStrategies",ACTION_NB_DELETE_STRATEGIES = "NBDeleteStrategies",ACTION_NB_CREATE_STRATEGY = "NBCreateStrategy",ACTION_NB_MODIFY_STRATEGY = "NBModifyStrategy",ACTION_NB_DESCRIBE_CHARGE_FACTORS = "NBDescribeChargeFactors",ACTION_NB_DELETE_CHARGE_FACTORS = "NBDeleteChargeFactors",ACTION_NB_CREATE_CHARGE_FACTOR = "NBCreateChargeFactor",ACTION_NB_MODIFY_CHARGE_FACTOR = "NBModifyChargeFactor",ACTION_NB_DESCRIBE_PUBLIC_ATTRIBUTES = "NBDescribePublicAttributes",ACTION_NB_DESCRIBE_PROD_INSTANCES = "NBDescribeProdInstances",ACTION_NB_RENEW_PROD_INSTANCE = "NBRenewProdInstance",ACTION_NB_STOP_PROD_INSTANCE = "NBStopProdInstance",ACTION_NB_DESCRIBE_BILLING_JOBS = "NBDescribeBillingJobs",ACTION_NB_PERFORM_BILLING_JOB = "NBPerformBillingJob",ACTION_NB_DESCRIBE_BILLS = "NBDescribeBills",ACTION_NB_GET_BILL = "NBGetBill",ACTION_NB_CREATE_PRD_ORDER = "NBCreatePrdOrder",ACTION_NB_CANCEL_PRD_ORDER = "NBCancelPrdOrder",ACTION_NB_CHARGE_PRD_ORDER = "NBChargePrdOrder",ACTION_NB_DESCRIBE_PRD_SUBORDER = "NBDescribePrdSuborder",ACTION_NB_DESCRIBE_PRD_SUBORDER_DETAIL = "NBDescribePrdSuborderDetail"'
    array = a.split(",")
    for b in array:
        print(b.split("=")[1])


def spamrun(fn):
    def sayspam(*args):
        print("spam,spam,spam")
        fn(*args)

    print("initial spamrun")
    return sayspam


# @spamrun
# def func_bx(a, b):
#     print(a * b)


def func_by():
    a = None
    b = a["asd"]
    print(b["qq"])


def func_bz():
    a = "778832e2c,701b85dcf,a876081ba,62546acb9,515a24acc,420fad9f9,83e5b4353,fef161d85,4cc137882,5ce5dc599,e0b80862e,4add0aa19,5e373c13e,2870e2023,b927a6947,313b32cf2,3e6db06a4,eb72cd057,6c65373c1,7bea44e71,d06d4462d,52339b88f,efd1cad2b,6061ee68e,12a32a7b6,052b06684,8dd76795d,03ebb54dc,492492da8,dd526a500,a8764f8b3,049d782cb,fec673ea3,847d1c36f,9bda2d110,48b39e9b1,b5d6421e2,7f970c178,40b279909,2b68cba95,a93dcd958,385d70503,084507dc2,ef05083b2,3ef24a982,a2bbd3c9d,671e75152,a18c04f04,b27e00753,57ddc3fd1,8c4cea722,be8df541a,a81bdd0e8,a7f968146,4686f69ed,a0d836ce9,793e49a5e,192ce8aca,32865eb40,f2244f6be,b424e2868,7ffbb322d,99540858a"
    array = a.split(',')
    n = len(array) - 1
    for i in range(len(array)):
        print("git cherry-pick %s" % array[n])
        print("git cherry-pick --continue")
        n = n - 1


def func_ca():
    print("starting...")
    while True:
        res = yield 4
        print("res: ", res)


def func_cb():
    print("1")
    yield 1
    print("2")
    yield 2
    print("3")
    yield 3


x = 1


def func_cc():
    global x
    x = 2
    return


def func_cd():
    a = " a "
    print(a)
    print(a.strip())


def func_ce():
    a = {
        "app_type": "web",
    }
    if a['app_type'] == 'web' and a.get('access_sys_id', ''):
        print("validation passed")
    print("failed")


class TestA(object):
    def __init__(self):
        print("inited")

    def __getattr__(self, item):
        try:
            if item == "asd":
                print("get attribute asd")
                return "qqq"
        except:
            pass
        return None


def func_cg():
    a = ["a", "b"]
    print("%s" % a)


def func_ch(a="", b=""):
    if not a:
        print("not a")
    if not b:
        print("not b")
    if a is None:
        print("a None")
    if b is None:
        print("b None")


def func_ci():
    a = "qqqq"
    print("array %s" % [a])


def func_cj():
    requests.get()


global_a = {}


def func_ck():
    a = "asda"
    b = 1
    print(a + str(b))


def func_cl():
    with open("C:\\Users\\Elvis\\Desktop\\nb_saas_api.json") as server_file:
        obj = json.loads(server_file.read())
        paths = obj['paths']
        for path, path_value in paths.items():
            for method, method_value in path_value.items():
                operation_id = method_value['operationId']
                orgin_action = operation_id.split('_')[1]
                action_name = 'ACTION_NB_' + '_'.join(re.findall('[A-Z][^A-Z]*', orgin_action)).upper()
                action = "NB" + orgin_action
                method = method.upper()
                # print("path[%s] method[%s] action_name[%s] action[%s]" % (path, method, action_name, action))
                # print("%s = \"%s\"" % (action_name, action))
                # print("%s," % action_name)
                # print("%s: \"%s\"," % (action_name, path))
                # print("%s: \"%s\"," % (action_name, method))
                # print("%s: {CHANNEL_API: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER, ROLE_PARTNER, ROLE_CONSOLE_ADMIN, ROLE_TICKET_MGR, ROLE_ZONE_ADMIN], CHANNEL_IAM: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER, ROLE_PARTNER, ROLE_CONSOLE_ADMIN, ROLE_TICKET_MGR, ROLE_ZONE_ADMIN], CHANNEL_SESSION: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER, ROLE_PARTNER, ROLE_CONSOLE_ADMIN, ROLE_TICKET_MGR, ROLE_ZONE_ADMIN], CHANNEL_CONSOLE: [ROLE_GLOBAL_ADMIN, ROLE_CONSOLE_ADMIN], CHANNEL_BOSS: [ROLE_CONSOLE_ADMIN, ROLE_GLOBAL_ADMIN, ROLE_ZONE_ADMIN], }," % action_name)
                # print("%s: self.new_billing," % action_name)
                print("%s: NewBillingHandler.handle_new_billing," % action_name)


def func_cm():
    if "a" in ["a", "b", "c"]:
        print("a in array")


def func_cn():
    string_a = '{"node":{"value":{"priority":0,"methods":["GET"],"upstream":{"nodes":{"127.0.0.1:9999":1},"hash_on":"vars","type":"roundrobin"},"plugins":{"qingcloud-auth":{"api_id":"test_api_id"}},"uri":"\/test1"},"createdIndex":157,"key":"\/apisix\/routes\/00000000000000000157","modifiedIndex":157},"action":"create"}'
    a = json.loads(string_a)
    key = a.get('node', {}).get('key')
    print(str(key))
    print(str.split(str(key), '/apisix/routes/')[1])


def func_cq():
    a = 'a' - 'A'
    # for i in range(128):
    print(a)


def func_cr():
    dic = {'usr-bVXQlUSY': [{'monthly': '2021-02', 'root_user_id': 'usr-bVXQlUSY', 'fee': 40000.0}],
           'usr-1zrddJKf': [{'monthly': '2021-02', 'root_user_id': 'usr-1zrddJKf', 'fee': 80000.0}]}
    for k, v in dic.items():
        print(k, ":", v)


def func_cs():
    params = {
        "name": "elvis",
        "age": "31",
    }
    app_key = "sadsadas"
    h1 = hashlib.md5()
    string_to_sign = ""
    for k, v in params.items():
        string_to_sign += "%s=%s&" % (k, v)
    string_to_sign += "key=%s" % app_key
    print("string to sign: %s" % string_to_sign)
    h1.update(string_to_sign.encode("utf-8"))
    sign = h1.hexdigest()
    print("signed string: %s" % sign)


def func_ct():
    params = {
        "name": "elvis",
        "age": "31",
    }
    app_key = "sadsadas".encode("utf-8")
    string_to_sign = ""
    for k, v in params.items():
        string_to_sign += "%s=%s&" % (k, v)
    string_to_sign += "key=%s" % app_key
    print("string to sign: %s" % string_to_sign)
    signature = base64.b64encode(hmac.new(app_key, string_to_sign.encode("utf-8"), digestmod=hashlib.sha256).digest())
    print("signed string: %s" % signature)


def func_cu():
    total = "123"
    total = int(total) + 321
    print(total)


def func_cv():
    a = "%.4f" % (1230000 / 10.0 ** 4)
    print(a.rstrip('0').rstrip('.'))


ISO8601 = '%Y-%m-%dT%H:%M:%SZ'
ISO8601_MS = '%Y-%m-%dT%H:%M:%S.%fZ'


def parse_ts(ts):
    ''' parse formatted UTC time to timestamp '''
    ts = ts.strip()
    try:
        ts_s = time.strptime(ts, ISO8601)
        return time.mktime(ts_s)
    except ValueError:
        try:
            ts_s = time.strptime(ts, ISO8601_MS)
            return time.mktime(ts_s)
        except ValueError:
            return 0


class Coordinate:
    x = 1
    y = 2
    z = 3


def func_cw():
    o = Coordinate()
    if hasattr(o, "x"):
        print("has attribute of x")
    if hasattr(o, "elvis"):
        print("has elvis")


from datetime import date
import time


def func_cx():
    first_day_of_month = date.today().replace(day=1)
    ts_s = time.strptime(first_day_of_month.strftime('%Y-%m-%d %H:%M:%S'), "%Y-%m-%d %H:%M:%S")
    t = int(time.mktime(ts_s))
    print(t)
    if 1617206400.0 >= t:
        print("true")


def func_cy():
    url = "http://192.168.10.145"
    seg = str.split(url, "://")
    print(seg)


def func_cz():
    url = "x.y.z"
    index = url.index(".")
    print(url[:index])
    print(url[index + 1:])


def func_da():
    a = []
    if a is None:
        print("a is None")
    if not a:
        print("not a")


def get_utf8_value(value):
    if not isinstance(value, str) and not isinstance(value, unicode):
        value = str(value)
    if isinstance(value, unicode):
        return value.encode('utf-8')
    else:
        return value


def get_ts(ts=None):
    if not ts:
        ts = time.gmtime()
    return time.strftime(ISO8601, ts)


def get_signature(path, secret_access_key, date, params={}):
    string_to_sign = "GET\n%s\n%s" % (date, path)
    keys = sorted(params.keys())
    pairs = []
    for key in keys:
        val = get_utf8_value(params[key])
        pairs.append(urllib.quote(key, safe='') + '=' + urllib.quote(val, safe='-_~'))
    qs = '&'.join(pairs)
    string_to_sign += qs
    print("string to sign: [%s]" % string_to_sign)
    h = hmac.new(secret_access_key, digestmod=sha256)
    h.update(string_to_sign)
    sign = base64.b64encode(h.digest()).strip()
    # signature = urllib.quote_plus(sign)
    return sign


def db():
    ts = time.gmtime()
    print(time.strftime("Date: %a, %d %b %Y %H:%M:%S GMT", ts))


import os


def dc():
    for f in os.listdir("C:\\Users\\Elvis\\Desktop"):
        print(f)


def de():
    file_dir = "C:\\Users\\Elvis\\Desktop"
    for root, dirs, files in os.walk(file_dir):
        print(root)  # 当前目录路径
        print(dirs)  # 当前路径下所有子目录
        print(files)  # 当前路径下所有非目录子文件


def dd():
    a = '["aaaaa"]'
    print(json.loads(a) if a else None)


def df(a):
    print(-a)
    return a & -a == a


def dg(a=None):
    cond = {}
    if a:
        cond["a"] = a
    print("cond[%s]" % cond)


def dh():
    a = [{"name": "elvis"}]
    for k in a:
        k["age"] = 9
    print(a)


def di():
    a = [{"name": "123"}, {"name": "321"}]
    b = [item["name"] for item in a]
    print(b)


import uuid


def dj():
    keys = ["a", "b"]
    for k, v in enumerate(keys):
        print("key[%s]" % k)
        print("valeu[%s]" % v)


def dk():
    t1 = "2021-06-01 15:30:51"
    t2 = "2021-06-01 15:30:30"
    print(time.mktime(time.strptime(t1, "%Y-%m-%d %H:%M:%S")))
    if time.mktime(time.strptime(t1, "%Y-%m-%d %H:%M:%S")) > time.mktime(time.strptime(t2, "%Y-%m-%d %H:%M:%S")):
        print(">")
    else:
        print("<=")


def dl():
    ret = {"c": {"count": 11}, "d": {"count": 1}, "a": {"count": 2}}
    # print("ret[%s]" % ret.values())
    count = [{"id": "d", "age": 11}]
    for c in count:
        ret[c.get("id")]["age"] = c.get("age")

    print("ret[%s]" % sorted(ret.values(), key=lambda q: q['count'], reverse=True))


def dm():
    print(uuid.uuid1())
    return uuid.uuid1()


def dn():
    display_columns = {
        "TB_API_PLUGIN_BINDING": ["binding_id", "user_id", "plugin_id", "api_id", "create_time"],
        "TB_API_PLUGIN": ["type", "name", "strategy"],
        "TB_GATEWAY_API": ["api_name"],
        "TB_API_GROUP": ["group_name"]
    }
    display_columns["TB_GATEWAY_API"].append("description")
    print(display_columns)


def do():
    url = "http://139.198.27.223:9080/test"
    payload = {}
    headers = {
        'apikey': 'test_key'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    print("%s" % response.headers)


def dp():
    a = "HTTP"
    print(a.lower())


def dq():
    a = "1"
    print(a.split(","))


def dr():
    url = 'https://www.juhe.cn/docs/api/id/39'
    r = requests.get(url)  # 发送get请求
    print(r.status_code)  # 打印状态码
    print(r.headers)  # 打印返回的报头（头部）
    print(r.text)  # 查看返回结果的文本形式（body部分）


# asd
def ds(custom_cmd, service_param_json):
    if not service_param_json:
        return custom_cmd

    # need to reload json
    _cmd = custom_cmd + " '" + service_param_json + "'"
    cmd_json = json.dumps(_cmd)
    if cmd_json is None:
        print("dump custom cmd [%s] failed", _cmd)

    # remove double quotation marks in the cmd Json
    print("".join(list(cmd_json))[1:-1])


def dt():
    a = [
        u'{"action":"create","node":{"key":"\\/apisix\\/routes\\/00000000000000000107","value":{"plugins":{"prometheus":{"prefer_name":false}},"update_time":1629357503,"status":1,"create_time":1629357503,"methods":["GET"],"uri":"\\/aitrix\\/log\\/","upstream":{"pass_host":"pass","nodes":{"1.1.1.1:9080":1},"hash_on":"vars","type":"roundrobin","scheme":"http"},"priority":0}}}']
    print(a[0])
    obj = json.loads(a[0])
    print(obj)


def du():
    url = "https://xueqiu.com/"
    try:
        resp = requests.request("GET", url)
    except Exception as e:
        print(e)
        return
    print(resp)


def dv():
    key_controller = "pitrix"
    CONTROLLER_PITRIX = "pitrix"
    if key_controller is CONTROLLER_PITRIX:
        print("true")
        is_pitrix_request = True


def dw():
    methods = ["OPTIONS"]
    method = "GET"
    methods.append(method)
    print(methods)


def dx():
    a = "apisix/[username]/hahaha"
    a, _ = re.subn("\[[a-z0-9_]*\]", "*", a)
    print(a)


def dy(name):
    ret = re.sub('[^0-9a-zA-Z_]', '', name)
    print(ret)
    ret = re.sub('^[^a-zA-Z_]+', '', ret)
    print(ret)
    return name and ret


def dz():
    print("" and "a")


def ea():
    parameter = "[{\"type\":\"string\",\"required\":true,\"default\":\"runoob\",\"description\":\"query描述\",\"enum\":[],\"regex\":\"runoo+b\",\"name\":\"query\",\"position\":\"query\"},{\"type\":\"string\",\"required\":true,\"default\":\"colour\",\"description\":\"header描述\",\"enum\":[],\"regex\":\"colou?r\",\"name\":\"header\",\"position\":\"header\"},{\"type\":\"string\",\"required\":true,\"default\":\"44\",\"description\":\"body描述\",\"enum\":[],\"name\":\"body1\",\"position\":\"body\"},{\"type\":\"string\",\"required\":true,\"default\":\"11\",\"description\":\"path描述\",\"enum\":[],\"regex\":\"\",\"name\":\"path\",\"position\":\"path\"}]"
    # parameter
    vars = []
    para = json.loads(parameter)
    for p_item in para:
        key = p_item.get("name")
        prefix = ""
        if p_item.get("position") == "query":
            prefix = "arg_"
        if p_item.get("position") == "header":
            prefix = "http_"
        if prefix:
            if p_item.get("enum"):
                enum = [item for item in p_item.get("enum")]
                vars.append(["%s%s" % (prefix, key), "in", enum])
            if p_item.get("regex"):
                vars.append(["%s%s" % (prefix, key), "~~", p_item.get("regex")])
    print(vars)


def eb():
    t = time.time()
    print(int(round(t * 1000)))


def ec():
    # resp = requests.request(method="GET", url="https://www.baidu.com", data=None, headers=None, timeout=(3, 5), verify=False, proxies={'http': '172.31.11.240:33033'})
    resp = requests.request(method="GET", url="http://192.168.12.209:9080/helloworld", data=None, headers=None, timeout=(3, 5),
                            verify=False,
                            proxies={'http': '172.31.11.240:33033'})
    print(resp.status_code)
    print(resp.text)
    # print(resp.json())


import threading


def ed():
    threading.Thread(target=ed_threading).start()
    threading.Thread(target=ed_threading).start()
    print("main thread stopped...")


def ed_threading():
    # while True:
    time.sleep(5)
    print("%s invoking threading...\n" % time.strftime("%Y-%m-%d %H:%M:%S"))


def ee():
    print('Enter your name:')
    api_name = input()
    _api_name = input()
    if api_name and _api_name != api_name.encode("UTF-8"):
        print("yes")
    else:
        print("no")


def ef():
    print(float("11923.829"))
    f = 11923.829
    print(f * 123.2)


def eg():
    print(round(221.112345, 2))


import sched


def eh_sched():
    print(time.time())


def eh():
    schedule = sched.scheduler(time.time, time.sleep)
    schedule.enter(10, 0, eh_sched, ())
    schedule.run()


from threading import Timer

import datetime

count = 0


def ei_task():
    global count
    count += 1
    print("in time: %s" % time.time())
    timer = threading.Timer(0, ei_task)
    if count > 10000:
        raise Exception("asdad")
    timer.start()


def ei():
    Timer(0, ei_task, ()).start()
    while True:
        print(time.time())
        time.sleep(10)


def ej():
    try:
        while True:
            print(time.time())
            time.sleep(1)
    finally:
        print("123123")


def ek():
    if "0" > 0:
        print("true")
    else:
        print("false")


def el():
    parameter = '[{"name":"test","type":"string","required":false,"default":"","description":"","position":"query","enum":["color","colour"],"regex":"colou?r"}]'

    vars = []
    para = json.loads(parameter)
    if para is not None:
        for p_item in para:
            key = p_item.get("name")
            prefix = ""
            if p_item.get("position") == "query":
                prefix = "arg_"
            if p_item.get("position") == "header":
                prefix = "http_"
            if prefix:
                if p_item.get("enum"):
                    enum = [item for item in p_item.get("enum")]
                    vars.append(["%s%s" % (prefix, key), "in", enum])
                if p_item.get("regex"):
                    vars.append(["%s%s" % (prefix, key), "~~", p_item.get("regex")])
    print(json.dumps(vars))


import copy


def em():
    dic = {"phone": "12345"}
    a = {"name": "elvis", "age": 24, "info": dic}
    # b = a
    b = copy.copy(a)
    # b = copy.deepcopy(a)
    # b["name"] = "ann"
    c = a["name"]
    c = "ryan"
    print(a)


def _get_spec_string_from_config(spec_item):
    apisix = spec_item.get("apisix")
    apisix_count = apisix.get("count")
    # apisix_volume_size = apisix.get("volume_size")
    apisix_instance_class = apisix.get("instance_class")
    apisix_cpu = apisix.get("cpu")
    apisix_memory = apisix.get("memory")

    redis = spec_item.get("redis")
    redis_count = redis.get("count")
    # redis_volume_size = redis.get("volume_size")
    redis_instance_class = redis.get("instance_class")
    redis_cpu = redis.get("cpu")
    redis_memory = redis.get("memory")

    haproxy = spec_item.get("haproxy")
    haproxy_count = haproxy.get("count")
    # haproxy_volume_size = haproxy.get("volume_size")
    haproxy_instance_class = haproxy.get("instance_class")
    haproxy_cpu = haproxy.get("cpu")
    haproxy_memory = haproxy.get("memory")

    # conf = '{"cluster":{"apisix":{"count":%s,"volume_size":%s,"instance_class":%s,"cpu":%s,"memory":%s},"redis":{"count":%s,"volume_size":%s,"instance_class":%s,"cpu":%s,"memory":%s},"haproxy":{"count":%s,"volume_size":%s,"instance_class":%s,"cpu":%s,"memory":%s}}}' \
    #        % (apisix_count, apisix_volume_size, apisix_instance_class, apisix_cpu, apisix_memory, redis_count,
    #           redis_volume_size, redis_instance_class, redis_cpu, redis_memory, haproxy_count, haproxy_volume_size,
    #           haproxy_instance_class, haproxy_cpu, haproxy_memory)
    conf = [{
        'cnt': int(haproxy_count),
        'g': 0,
        'm': int(haproxy_memory),
        'c': int(haproxy_cpu),
        'repl': 1,
        'sc': 0,
        'r': 'haproxy',
        'hpvr': 'lxc',
        'gcls': 0,
        'cls': int(haproxy_instance_class)
    }, {
        'cnt': int(apisix_count),
        'g': 0,
        'm': int(apisix_memory),
        'c': int(apisix_cpu),
        'repl': 1,
        'sc': 0,
        'r': 'apisix',
        'hpvr': 'kvm',
        'gcls': 0,
        'cls': int(apisix_instance_class)
    }, {
        'cnt': int(redis_count),
        'g': 0,
        'm': int(redis_memory),
        'c': int(redis_cpu),
        'repl': 1,
        'sc': 0,
        'r': 'redis',
        'hpvr': 'lxc',
        'gcls': 0,
        'cls': int(redis_instance_class)
    }]
    return conf


def _get_spec_string_from_config_get_cluster_price(spec_item):
    apisix = spec_item.get("apisix")
    apisix_count = apisix.get("count")
    apisix_volume_size = apisix.get("volume_size")
    apisix_instance_class = apisix.get("instance_class")
    apisix_cpu = apisix.get("cpu")
    apisix_memory = apisix.get("memory")

    redis = spec_item.get("redis")
    redis_count = redis.get("count")
    redis_volume_size = redis.get("volume_size")
    redis_instance_class = redis.get("instance_class")
    redis_cpu = redis.get("cpu")
    redis_memory = redis.get("memory")

    haproxy = spec_item.get("haproxy")
    haproxy_count = haproxy.get("count")
    haproxy_volume_size = haproxy.get("volume_size")
    haproxy_instance_class = haproxy.get("instance_class")
    haproxy_cpu = haproxy.get("cpu")
    haproxy_memory = haproxy.get("memory")

    conf = '{"cluster":{"apisix":{"count":%s,"volume_size":%s,"instance_class":%s,"cpu":%s,"memory":%s},"redis":{"count":%s,"volume_size":%s,"instance_class":%s,"cpu":%s,"memory":%s},"haproxy":{"count":%s,"volume_size":%s,"instance_class":%s,"cpu":%s,"memory":%s}}}' \
           % (apisix_count, apisix_volume_size, apisix_instance_class, apisix_cpu, apisix_memory, redis_count,
              redis_volume_size, redis_instance_class, redis_cpu, redis_memory, haproxy_count, haproxy_volume_size,
              haproxy_instance_class, haproxy_cpu, haproxy_memory)
    return conf


def en():
    a = "3",
    print(a)


def eo():
    a = {"a": "hello"}
    print(len(a))


def ep():
    a = {}
    if a:
        print("yes")
    else:
        print("no")
    print(a.keys())


def eq():
    a = {"1": {"name": "elvis", "age": 10}}
    b = {}
    for k, v in a.items():
        b[v.get("name")] = v
    print(b)
    b["elvis"]["age"] = 11
    print(a)


def er():
    a = {'ad-p6qlmv8b': {'global_uuid': '47420299864860913', 'vxnet_id': 'vxnet-auwvrm7',
                         'create_time': datetime.datetime(2022, 1, 20, 11, 9, 57), 'cluster_id': 'cl-emdfczpg',
                         'domain_id': 'ad-p6qlmv8b', 'user_id': 'admin', 'job_id': 'j-g3urzne7rt3', 'zone': 'delta',
                         'specification': 'base',
                         'domain_name': '\xe6\xb5\x8b\xe8\xaf\x95\xe5\xae\x89\xe5\x85\xa8\xe7\xbb\x84\xe5\x88\x9b\xe5\xbb\xba',
                         'dns_record_id': None, 'status': 'active', 'update_time': datetime.datetime(2022, 1, 20, 11, 17, 23),
                         'description': None, 'transition_status': '', 'admin_key': '72b7b628799e11ec973a00163e3afe6c',
                         'eip_bandwidth': None, 'eip_billing_mode': None, 'eip_id': 'eip-9gyqy9al', 'api_count': 1,
                         'vip_id': 'vip-eatlsi9q', 'charge_mode': 'elastic', 'admin_url': 'http://192.168.8.134:9080',
                         'dns_url': 'ad-p6qlmv8b.qingcloud.link.', 'vip_ip': '172.17.253.253', 'region': 'staging'},
         'ad-ebdks3wi': {'global_uuid': '04420299864505231', 'vxnet_id': 'vxnet-auwvrm7',
                         'create_time': datetime.datetime(2022, 1, 19, 17, 37, 59), 'cluster_id': 'cl-rv3koczc',
                         'domain_id': 'ad-ebdks3wi', 'user_id': 'admin', 'job_id': 'j-1rwizyy3308', 'zone': 'delta',
                         'specification': 'base',
                         'domain_name': '\xe5\x85\xa5\xe9\x97\xa8\xe7\x89\x88\xe5\x8d\x87\xe7\xba\xa7\xe6\xb5\x8b\xe8\xaf\x95999',
                         'dns_record_id': None, 'status': 'upgrading',
                         'update_time': datetime.datetime(2022, 1, 19, 17, 41, 33), 'description': None,
                         'transition_status': '', 'admin_key': '7d65407e790b11ec973a00163e3afe6c', 'eip_bandwidth': None,
                         'eip_billing_mode': None, 'eip_id': 'eip-ql50ijqj', 'vip_id': 'vip-tslf8psz', 'charge_mode': 'monthly',
                         'admin_url': 'http://192.168.8.83:9080', 'dns_url': 'ad-ebdks3wi.qingcloud.link.',
                         'vip_ip': '172.17.253.245', 'region': 'staging'},
         'ad-8x09vkxs': {'global_uuid': '77420299864861242', 'vxnet_id': 'vxnet-auwvrm7',
                         'create_time': datetime.datetime(2022, 1, 20, 11, 23, 39), 'cluster_id': 'cl-w2lbdvqe',
                         'domain_id': 'ad-8x09vkxs', 'user_id': 'admin', 'job_id': 'j-gdp8xb2zc1r', 'zone': 'delta',
                         'specification': 'base',
                         'domain_name': '\xe6\xb5\x8b\xe8\xaf\x95\xe5\xae\x89\xe5\x85\xa8\xe7\xbb\x84\xe5\x88\x9b\xe5\xbb\xba2',
                         'dns_record_id': None, 'status': 'active', 'update_time': datetime.datetime(2022, 1, 20, 11, 30, 8),
                         'description': None, 'transition_status': '', 'admin_key': '5be0d02279a011ec973a00163e3afe6c',
                         'eip_bandwidth': None, 'eip_billing_mode': None, 'eip_id': 'eip-i9vkj2oh', 'vip_id': 'vip-wnb36pt5',
                         'charge_mode': 'elastic', 'admin_url': 'http://192.168.8.78:9080',
                         'dns_url': 'ad-8x09vkxs.qingcloud.link.', 'vip_ip': '172.17.253.252', 'region': 'staging'},
         'ad-ajmxu788': {'global_uuid': '12420299864531867', 'vxnet_id': 'vxnet-auwvrm7',
                         'create_time': datetime.datetime(2022, 1, 19, 16, 7, 23), 'cluster_id': 'cl-p67zpo32',
                         'domain_id': 'ad-ajmxu788', 'user_id': 'admin', 'job_id': 'j-q38y4603oho', 'zone': 'delta',
                         'specification': 'trial',
                         'domain_name': '\xe5\x85\xa5\xe9\x97\xa8\xe7\x89\x88\xe5\x8d\x87\xe7\xba\xa7\xe6\xb5\x8b\xe8\xaf\x95',
                         'dns_record_id': None, 'status': 'upgrading',
                         'update_time': datetime.datetime(2022, 1, 19, 16, 13, 59), 'description': None,
                         'transition_status': '', 'admin_key': 'd4ef475278fe11ec973a00163e3afe6c', 'eip_bandwidth': None,
                         'eip_billing_mode': None, 'eip_id': 'eip-lb7uv0g1', 'vip_id': 'vip-z60a1fk6', 'charge_mode': 'monthly',
                         'admin_url': 'http://192.168.8.45:9080', 'dns_url': 'ad-ajmxu788.qingcloud.link.',
                         'vip_ip': '172.17.253.249', 'region': 'staging'}}
    clusters = {}
    for domain_id, domain in a.items():
        if domain.get("cluster_id"):
            clusters[domain.get("cluster_id")] = domain
    print(clusters)


def es():
    a = u'ipv4\u57ce\u5e02\u7ea7'
    b = b'ipv4\xe5\x9f\x8e\xe5\xb8\x82\xe7\xba\xa7'
    api_name = 'ipv4城市级'
    dic = {"name": a}
    print("%s" % (api_name is not None))
    print("api.api_name[%s]" % a)
    print(dic)
    if b != api_name:
        print("not equals")
    else:
        print("equals")
    print(a.encode("utf-8"))
    print(b.decode("utf-8"))
    print("hello".decode("utf-8"))


def et():
    pass


def eu():
    domain_to_sync = {}
    cluster_status = json.loads(
        "[{\"cluster_tag\":\"\",\"vxnet_id\":\"vxnet-uoi07cr\",\"auto_backup_time\":-1,\"alias_id\":\"\",\"app_id\":\"app-cqkewf6m\",\"create_time\":\"2022-01-27T14:55:59\",\"cluster_id\":\"cl-6p0tjeiu\",\"owner\":\"usr-Uh2ZocVn\",\"alias_name\":\"\",\"upgrade_time\":\"2022-01-27T14:55:59\",\"sub_code\":1,\"add_links\":null,\"security_group_id\":\"\",\"upgrade_status\":\"\",\"status_time\":\"2022-02-17T13:58:38\",\"app_version\":\"appv-swv0n1uk\",\"status\":\"ceased\",\"backup_chain_len\":-1,\"description\":\"\\u661f\\u8fb0\\u59d0\\u6211\\u62ff\\u4f60\\u7684\\u8d26\\u53f7\\u6d4b\\u8bd5\\u4e00\\u4e0b\\u90e8\\u7f72\",\"transition_status\":\"\",\"shared_app\":false,\"name\":\"\\u661f\\u8fb0\\u59d0\\u6211\\u62ff\\u4f60\\u7684\\u8d26\\u53f7\\u6d4b\\u8bd5\\u4e00\\u4e0b\\u90e8\\u7f72\",\"partner_access\":false,\"zone_id\":\"pek3c\",\"app_patch\":\"\",\"backup_chain\":-1,\"cluster_size\":3,\"debug\":false,\"endpoints\":\"{\\\"rest\\\":{\\\"protocol\\\":\\\"tcp\\\",\\\"port\\\":9080},\\\"reserved_ips\\\":{\\\"vip\\\":{\\\"value\\\":\\\"192.168.100.251\\\"}}}\"}]")
    clusters = {
        "cl-6p0tjeiu": json.loads(
            "{\"global_uuid\":\"15242219867488573\",\"vxnet_id\":\"vxnet-uoi07cr\",\"app_id\":null,\"create_time\":\"2022-01-27T14:55:37Z\",\"cluster_id\":\"cl-6p0tjeiu\",\"domain_id\":\"ad-ik1mzeav\",\"eip_id\":\"eip-fjb0gpmj\",\"job_id\":\"j-fz88rwypvjg\",\"zone\":\"pek3c\",\"specification\":\"base\",\"domain_name\":\"zjj测试实例\",\"app_version\":null,\"dns_record_id\":\"35392\",\"spec\":{\"specification\":\"base\",\"value\":{\"haproxy\":{\"count\":1,\"volume_size\":10,\"instance_class\":203,\"cpu\":2,\"memory\":4096},\"max_con\":50000,\"hour_price\":5.8,\"redis\":{\"count\":1,\"volume_size\":10,\"instance_class\":101,\"cpu\":1,\"memory\":1024},\"config_type\":1,\"bandwidth\":20,\"max_req_sec\":5000,\"year_price\":29481.6,\"sla\":\"99.95%\",\"apisix\":{\"count\":1,\"volume_size\":20,\"instance_class\":101,\"cpu\":1,\"memory\":1024},\"month_price\":2960}},\"status\":\"active\",\"update_time\":\"2022-03-15T14:03:37Z\",\"description\":null,\"transition_status\":\"\",\"admin_key\":\"21ce3e6c7f3e11eca36100163e55e477\",\"eip_bandwidth\":null,\"eip_billing_mode\":null,\"user_id\":\"usr-Uh2ZocVn\",\"api_count\":1,\"vip_id\":\"vip-nl7y8m8h\",\"charge_mode\":\"elastic\",\"admin_url\":\"http://139.198.16.192:9080\",\"dns_url\":\"ad-ik1mzeav.apig.qingcloud.link.\",\"vip_ip\":\"192.168.100.251\",\"region\":\"pek3\"}")
    }
    for cluster_status_item in cluster_status:
        cluster_id = cluster_status_item.get("cluster_id")
        status = cluster_status_item.get("status")
        transition_status = cluster_status_item.get("transition_status")

        _status = clusters.get(cluster_id).get("status")
        _transition_status = clusters.get(cluster_id).get("transition_status")

        if _status in ["upgrading", "failed"]:
            continue

        if (transition_status == _transition_status or (not transition_status and not _transition_status)) and (
                status == _status or (not status and not _status)):
            continue

        if transition_status and transition_status not in ["creating", "deleting"]:
            transition_status = "upgrading"

        if transition_status != _transition_status:
            clusters.get(cluster_id)["transition_status"] = transition_status
        if status != _status:
            clusters.get(cluster_id)["status"] = status
        to_update = copy.copy(clusters.get(cluster_id))
        if to_update.get("api_count"):
            to_update.pop("api_count")
        domain_to_sync[clusters.get(cluster_id).get("domain_id")] = to_update
    print(clusters)


def ev():
    s = u'''{
  "text": [
    {
      "content": "降级阿斯顿撒大大多撒大所大所多"
    }
  ]
}'''
    print(s.encode("utf-8"))
    ret = requests.request(method="POST", url="http://192.168.27.239:9080/hellocn", data=s.encode("utf-8"),
                           headers={"Content-Type": "application/json;charset=utf-8"}, timeout=(3, 5), verify=False)
    print(ret.text)


def ew():
    print(ord(u'翟'))
    print(ord(u'炼'))
    print(chr(32735))
    print(chr(28860))


# def ex():
#     print("1".append("2"))


if __name__ == "__main__":
    # ex()
