import json as jsmod


def main():
    with open("./cache.json", "r+") as fc, open("./python_input", "r") as fi:
        source = jsmod.loads(fi.read())
        cache = jsmod.loads(fc.read())
        for item in source:
            if item["meter"] == "apisix_bandwidth":
                tagstr = item["tags"]
                tags = tagstr.split(",")
                tag_map = {}
                for tag in tags:
                    tag_map[tag.split("=")[0]] = tag.split("=")[1]
                if tag_map["type"]:
                    cache_value = 0
                    # cache: map["apisix_bandwidth"][{route}][{node}][{type}] = {value}
                    if tag_map["route"] in cache["apisix_bandwidth"]:
                        if tag_map["node"] in cache["apisix_bandwidth"][tag_map["route"]]:
                            if tag_map["type"] in cache["apisix_bandwidth"][tag_map["route"]][tag_map["node"]]:
                                cache_value = cache["apisix_bandwidth"][tag_map["route"]][tag_map["node"]][tag_map["type"]]
                        else:
                            cache["apisix_bandwidth"][tag_map["route"]][tag_map["node"]] = {}
                    else:
                        cache["apisix_bandwidth"][tag_map["route"]] = {}
                    temp = item["value"]
                    item["value"] = int(temp) - cache_value
                    if not tag_map["node"] in cache["apisix_bandwidth"][tag_map["route"]]:
                        cache["apisix_bandwidth"][tag_map["route"]][tag_map["node"]] = {}
                    cache["apisix_bandwidth"][tag_map["route"]][tag_map["node"]][tag_map["type"]] = int(temp)
            if item["meter"] == "apisix_http_latency_count":
                tagstr = item["tags"]
                tags = tagstr.split(",")
                tag_map = {}
                for tag in tags:
                    tag_map[tag.split("=")[0]] = tag.split("=")[1]
                cache_value = 0
                if tag_map["route"] in cache["apisix_http_latency_count"]:
                    if tag_map["node"] in cache["apisix_http_latency_count"][tag_map["route"]]:
                        if tag_map["type"] in cache["apisix_http_latency_count"][tag_map["route"]][tag_map["node"]]:
                            cache_value = cache["apisix_http_latency_count"][tag_map["route"]][tag_map["node"]][tag_map["type"]]
                    else:
                        cache["apisix_http_latency_count"][tag_map["route"]][tag_map["node"]] = {}
                else:
                    cache["apisix_http_latency_count"][tag_map["route"]] = {}
                temp = item["value"]
                item["value"] = int(temp) - cache_value
                if not tag_map["node"] in cache["apisix_http_latency_count"][tag_map["route"]]:
                    cache["apisix_http_latency_count"][tag_map["route"]][tag_map["node"]] = {}
                cache["apisix_http_latency_count"][tag_map["route"]][tag_map["node"]][tag_map["type"]] = int(temp)
            if item["meter"] == "apisix_http_status":
                tagstr = item["tags"]
                tags = tagstr.split(",")
                tag_map = {}
                for tag in tags:
                    tag_map[tag.split("=")[0]] = tag.split("=")[1]
                if tag_map["code"]:
                    cache_value = 0
                    # cache: map["apisix_http_status"][{route}][{node}][{code}] = {value}
                    if tag_map["route"] in cache["apisix_http_status"]:
                        if tag_map["node"] in cache["apisix_http_status"][tag_map["route"]]:
                            if tag_map["code"] in cache["apisix_http_status"][tag_map["route"]][tag_map["node"]]:
                                cache_value = cache["apisix_http_status"][tag_map["route"]][tag_map["node"]][tag_map["code"]]
                        else:
                            cache["apisix_http_status"][tag_map["route"]][tag_map["node"]] = {}
                    else:
                        cache["apisix_http_status"][tag_map["route"]] = {}
                    temp = item["value"]
                    item["value"] = int(temp) - cache_value
                    if not tag_map["node"] in cache["apisix_http_status"][tag_map["route"]]:
                        cache["apisix_http_status"][tag_map["route"]][tag_map["node"]] = {}
                    cache["apisix_http_status"][tag_map["route"]][tag_map["node"]][tag_map["code"]] = int(temp)
            if item["value"] < 0:
                item["value"] = 0
        fc.truncate(0)
        fc.seek(0)
        fc.write(jsmod.dumps(cache))
        with open("./python_output", "w+") as fo:
            fo.write(jsmod.dumps(source))


main()
