from urllib.request import urlopen
from datetime import datetime
import json, re, requests, time, math
from custom_calculation import custom_calculation

custom_calculation = custom_calculation()

class json_response():
    def __init__(self,ip,port):        
        url = 'http://'+ip+':'+port+'/system/stats'
        response = urlopen(url)
        string = response.read().decode('utf-8')
        self.json_obj = json.loads(string)
        
        url_nedge_version = 'http://'+ip+':'+port+'/nedge-version'
        response_nedge_version = urlopen(url_nedge_version)
        string_nedge_version = response_nedge_version.read().decode('utf-8')
        self.json_obj_nedge_version = json.loads(string_nedge_version)
        
        url_nedge_license = 'http://'+ip+':'+port+'/system/license'
        response_nedge_license = requests.get(url_nedge_license, auth=('admin', 'nexenta'))
        self.json_obj_nedge_license = json.loads(response_nedge_license.text)

    def nedge_version(self):
        return str(self.json_obj_nedge_version['response']['version'])

    def nedge_license(self,query):
        nedge_license = self.json_obj_nedge_license['response']['metadata']['X-system-license']
        nedge_license = nedge_license.replace("\\","")
        nedge_license = nedge_license.replace("\"","")
        nedge_license = nedge_license.split(",")
        if query == "Installation GUID":
            nedge_license_query = nedge_license[10].split(":")
            return str(nedge_license_query[1])        
        elif query == "License Expiration Date":
            nedge_license_query = nedge_license[11].split(":")
            return str(nedge_license_query[1])
        elif query == "License Serial Number":
            nedge_license_query = nedge_license[5].split(":")
            return str(nedge_license_query[1])
        elif query == "License Type":
            nedge_license_query = nedge_license[9].split(":")
            return str(nedge_license_query[1])
        elif query == "License Base Capacity":
            nedge_license_query1 = nedge_license[15].split(":")
            nedge_license_query2 = nedge_license[16].split(":")
            nedge_license_query3 = nedge_license[17].split(":")
            return (str(nedge_license_query1[1])+" "+str(nedge_license_query2[1])+", "+str(nedge_license_query3[1]))
        elif query == "License Status":
            date_expiry = nedge_license[11].split(":")
            date_current=str(datetime.now()).split()[0]
            date_current=time.strptime(date_current, "%Y-%m-%d")
            date_expiry=time.strptime(date_expiry[1], "%m/%d/%Y")
            if date_current > date_expiry:
                return ("License has expired")
            else:
                return("")
    
    def response_stats_summary(self,query):
        if query == "total_logical_used":
            total_logical_used_bytes = int(self.json_obj['response']['stats']['summary']['total_logical_used'])
            if str(custom_calculation.byte_conversion(total_logical_used_bytes)) == "0.00GB":
                return ("0.00")
            else:
                return (custom_calculation.byte_conversion(total_logical_used_bytes))
        elif query == "total_num_objects":
            return(self.json_obj['response']['stats']['summary']['total_num_objects'])
        elif query == "total_capacity":
            total_capacity_bytes = self.json_obj['response']['stats']['summary']['total_capacity']
            return (custom_calculation.byte_conversion(total_capacity_bytes))
        elif query == "total_physical_used":
            total_physical_used_bytes = self.json_obj['response']['stats']['summary']['total_physical_used']
            return (custom_calculation.byte_conversion(total_physical_used_bytes))
        elif query == "total_available":
            total_available_bytes = self.json_obj['response']['stats']['summary']['total_available']
            return (custom_calculation.byte_conversion(total_available_bytes))
        elif query == "total_utilization":
            return (str((self.json_obj['response']['stats']['summary']['total_utilization']))+"%")
        elif query == "reduction_ratio":
            reduction_ratio = self.json_obj['response']['stats']['summary']['reduction_ratio']
            reduction_ratio = reduction_ratio.split(".")
            if reduction_ratio[1] == "00":
                return (reduction_ratio[0])
            else:
                return (self.json_obj['response']['stats']['summary']['reduction_ratio'])
        elif query == "est_total_available":
            est_total_available_bytes = self.json_obj['response']['stats']['summary']['est_total_available']
            return (custom_calculation.byte_conversion(est_total_available_bytes))
        elif query == "est_capacity_savings":
            est_capacity_savings_bytes = self.json_obj['response']['stats']['summary']['est_capacity_savings']
            if custom_calculation.byte_conversion(est_capacity_savings_bytes) == "0.00GB":
                return ("0.00")
            else:
                return custom_calculation.byte_conversion(est_capacity_savings_bytes)
        
    def average_latency(self):
        a = 0
        match = 0
        latency = 0
        if self.json_obj["response"]["stats"]["latencies"] == [[]]:
            return ("0")
        else:
            for i in self.json_obj["response"]["stats"]["latencies"]:
                match = match + 1
                latency = latency + int(self.json_obj["response"]["stats"]["latencies"][a]["put_latency"]) + int(self.json_obj["response"]["stats"]["latencies"][a]["get_latency"])
            a = a + 1
            if match == 0:
                return ("0")
            else:
                return str(math.ceil(latency/(match*2)))

    def total_iops(self):
        a = 0
        match = 0
        latency = 0
        if self.json_obj["response"]["stats"]["latencies"] == [[]]:
            return ("0")
        else:
            for i in self.json_obj["response"]["stats"]["latencies"]:
                match = match + 1
                latency = latency + int(self.json_obj["response"]["stats"]["latencies"][a]["put_iops"]) + int(self.json_obj["response"]["stats"]["latencies"][a]["get_iops"])
            a = a + 1
            if match == 0:
                return ("0")
            else:
                return str(math.ceil(latency/(match*2)))

    def number_of_nodes(self):
        number_of_nodes = 0
        for data in self.json_obj['response']['stats']['servers']:
            number_of_nodes = number_of_nodes + 1
        return (number_of_nodes)

    def servers(self):
        servers = self.json_obj["response"]["stats"]["servers"]
        server_ids = servers.keys()
        server_ids = re.sub('^dict_keys', '', str(server_ids))
        server_ids = (((((server_ids.replace("(","")).replace(")","")).replace("\'","")).replace("[","")).replace("]","")).replace(" ","")
        server_ids_list = server_ids.split(",")
        return server_ids_list

    def server_status(self):
        number_of_degraded_nodes = 0
        number_of_online_nodes = 0
        servers = self.json_obj["response"]["stats"]["servers"]
        server_ids = servers.keys()
        server_ids = re.sub('^dict_keys', '', str(server_ids))
        server_ids = (((((server_ids.replace("(","")).replace(")","")).replace("\'","")).replace("[","")).replace("]","")).replace(" ","")
        server_ids_list = server_ids.split(",")        
        for index in range(len(server_ids_list)):
            if str(self.json_obj["response"]["stats"]["servers"][server_ids_list[index]]["health"]) == "100":
                number_of_online_nodes = number_of_online_nodes + 1
            else:
                number_of_degraded_nodes = number_of_degraded_nodes + 1  
        server_status = str(number_of_online_nodes)+"/"+str(number_of_degraded_nodes)
        return server_status

    def cluster_health(self):
        number_of_nodes = 0
        for data in self.json_obj['response']['stats']['servers']:
            number_of_nodes = number_of_nodes + 1
        health = 0
        servers = self.json_obj["response"]["stats"]["servers"]
        server_ids = servers.keys()
        server_ids = re.sub('^dict_keys', '', str(server_ids))
        server_ids = (((((server_ids.replace("(","")).replace(")","")).replace("\'","")).replace("[","")).replace("]","")).replace(" ","")
        server_ids_list = server_ids.split(",")        
        for index in range(len(server_ids_list)):
            health = health + int(self.json_obj["response"]["stats"]["servers"][server_ids_list[index]]["health"])
        return str(int(health/number_of_nodes))+"%"
    
    def total_vdevs_status(self):
        number_of_degraded_vdevs = 0
        number_of_online_vdevs = 0
        servers = self.json_obj["response"]["stats"]["servers"]
        server_ids = servers.keys()
        server_ids = re.sub('^dict_keys', '', str(server_ids))
        server_ids = (((((server_ids.replace("(","")).replace(")","")).replace("\'","")).replace("[","")).replace("]","")).replace(" ","")
        server_ids_list = server_ids.split(",")        
        for index in range(len(server_ids_list)):
            vdevs = self.json_obj["response"]["stats"]["servers"][server_ids_list[index]]['vdevs']
            vdevs_ids = vdevs.keys()
            vdevs_ids = re.sub('^dict_keys', '', str(vdevs_ids))
            vdevs_ids = (((((vdevs_ids.replace("(","")).replace(")","")).replace("\'","")).replace("[","")).replace("]","")).replace(" ","")
            vdevs_ids_list = vdevs_ids.split(",")
            for vdevs_index in range(len(vdevs_ids_list)):
                if str(self.json_obj["response"]["stats"]["servers"][server_ids_list[index]]["vdevs"][vdevs_ids_list[vdevs_index]]["online"]) == "1":
                    if str(self.json_obj["response"]["stats"]["servers"][server_ids_list[index]]["vdevs"][vdevs_ids_list[vdevs_index]]["vdevid"]) != "00000000000000000000000000000000":
                        number_of_online_vdevs = number_of_online_vdevs + 1
                else:
                    number_of_degraded_vdevs = number_of_degraded_vdevs + 1
        total_vdevs_status = str(number_of_online_vdevs)+"/"+str(number_of_degraded_vdevs)
        return total_vdevs_status

    def server_details(self,key,query):
        if query == "serverid":
            return self.json_obj["response"]["stats"]["servers"][key]["serverid"]
        elif query == "hostname":
            return self.json_obj["response"]["stats"]["servers"][key]["hostname"]
        elif query == "memtotal":
            return custom_calculation.byte_conversion_ram(self.json_obj["response"]["stats"]["servers"][key]["memtotal"])
        elif query == "capacity":
            if custom_calculation.byte_conversion(self.json_obj["response"]["stats"]["servers"][key]["capacity"]) == "0.00GB":
                return ("0.00")
            else:
                return custom_calculation.byte_conversion(self.json_obj["response"]["stats"]["servers"][key]["capacity"])
        elif query == "cpu":
            numcpu = self.json_obj["response"]["stats"]["servers"][key]["numcpu"]
            cpuspeed = self.json_obj["response"]["stats"]["servers"][key]["cpuspeed"]
            cpuspeed = round((int(cpuspeed)/1000),2)
            cpu = str(numcpu)+"@"+str(cpuspeed)+"0Ghz"
            return cpu
        elif query == "zone":
            return self.json_obj["response"]["stats"]["servers"][key]["zone"]
        elif query == "utilization":
            capacity = self.json_obj["response"]["stats"]["servers"][key]["capacity"]
            physical_used = self.json_obj["response"]["stats"]["servers"][key]["physical_used"]
            if int(self.json_obj["response"]["stats"]["servers"][key]["available"]) == 0:
                return "0.00%"
            elif int(self.json_obj["response"]["stats"]["servers"][key]["available"]) > 0:
                utilization = (float(physical_used)/float(capacity))*10000
                utilization = round(utilization,2)
                if utilization == 0.0:
                    return ("0.00%")
                else:
                    return str(utilization)+"%"
        elif query == "latency":
            a = 0
            match = 0
            latency = 0
            if self.json_obj["response"]["stats"]["latencies"] == [[]]:
                return ("0")
            else:
                for i in self.json_obj["response"]["stats"]["latencies"]:
                    if self.json_obj["response"]["stats"]["latencies"][a]["SID"] == key:
                        match = match + 1
                        latency = latency + int(self.json_obj["response"]["stats"]["latencies"][a]["put_latency"]) + int(self.json_obj["response"]["stats"]["latencies"][a]["get_latency"])
                    a = a + 1
                if match == 0:
                    return ("0")
                else:
                    return str(math.ceil(latency/(match*2)))
        elif query == "iops":
            a = 0
            match = 0
            latency = 0
            if self.json_obj["response"]["stats"]["latencies"] == [[]]:
                return ("0")
            else:
                for i in self.json_obj["response"]["stats"]["latencies"]:
                    if self.json_obj["response"]["stats"]["latencies"][a]["SID"] == key:
                        match = match + 1
                        latency = latency + int(self.json_obj["response"]["stats"]["latencies"][a]["put_iops"]) + int(self.json_obj["response"]["stats"]["latencies"][a]["get_iops"])
                    a = a + 1
                if match == 0:
                    return ("0")
                else:
                    return str(math.ceil(latency/(match*2)))

    def number_of_vdevs(self,key):
        number_of_vdevs = 0
        for data in self.json_obj['response']["stats"]["servers"][key]['vdevs']:
            number_of_vdevs = number_of_vdevs + 1
        return (number_of_vdevs)

    def vdevs(self,key):
        vdevs = self.json_obj["response"]["stats"]["servers"][key]['vdevs']
        vdevs_ids = vdevs.keys()
        vdevs_ids = re.sub('^dict_keys', '', str(vdevs_ids))
        vdevs_ids = (((((vdevs_ids.replace("(","")).replace(")","")).replace("\'","")).replace("[","")).replace("]","")).replace(" ","")
        vdevs_ids_list = vdevs_ids.split(",")
        return vdevs_ids_list

    def vdevs_status(self,server_key):
        number_of_degraded_vdevs = 0
        number_of_online_vdevs = 0
        vdevs = self.json_obj["response"]["stats"]["servers"][server_key]['vdevs']
        vdevs_ids = vdevs.keys()
        vdevs_ids = re.sub('^dict_keys', '', str(vdevs_ids))
        vdevs_ids = (((((vdevs_ids.replace("(","")).replace(")","")).replace("\'","")).replace("[","")).replace("]","")).replace(" ","")
        vdevs_ids_list = vdevs_ids.split(",")
        for vdevs_index in range(len(vdevs_ids_list)):
            if str(self.json_obj["response"]["stats"]["servers"][server_key]["vdevs"][vdevs_ids_list[vdevs_index]]["online"]) == "1":
                number_of_online_vdevs = number_of_online_vdevs + 1
            else:
                number_of_degraded_vdevs = number_of_degraded_vdevs + 1
        vdevs_status = str(number_of_online_vdevs)+"/"+str(number_of_degraded_vdevs+number_of_online_vdevs)
        return vdevs_status

    def vdevs_details(self,server_key,vdev_key,query):
        if vdev_key == "00000000000000000000000000000000":
            if query == "vdevid":
                return self.json_obj["response"]["stats"]["servers"][server_key]["vdevs"][str(vdev_key)]["vdevid"]
            elif query == "devname":
                #return self.json_obj["response"]["stats"]["servers"][server_key]["vdevs"][str(vdev_key)]["devname"]
                return "NODEV"
            elif query == "capacity":
                return custom_calculation.byte_conversion_gib(self.json_obj["response"]["stats"]["servers"][server_key]["vdevs"][str(vdev_key)]["available"])
            elif query == "utilization":
                return (str(self.json_obj["response"]["stats"]["servers"][server_key]["vdevs"][str(vdev_key)]["utilization"])+"%")
            elif query == "rlat":
                return ("")
            elif query == "wlat":
                return ("")
        else:
            if query == "vdevid":
                return self.json_obj["response"]["stats"]["servers"][server_key]["vdevs"][str(vdev_key)]["vdevid"]
            elif query == "devname":
                return self.json_obj["response"]["stats"]["servers"][server_key]["vdevs"][str(vdev_key)]["devname"]
            elif query == "capacity":
                return custom_calculation.byte_conversion_gib(self.json_obj["response"]["stats"]["servers"][server_key]["vdevs"][str(vdev_key)]["capacity"])
            elif query == "utilization":
                return (str(self.json_obj["response"]["stats"]["servers"][server_key]["vdevs"][str(vdev_key)]["utilization"])+"%")
            elif query == "rlat":
                return (str(self.json_obj["response"]["stats"]["servers"][server_key]["vdevs"][str(vdev_key)]["get_latency"]))
            elif query == "wlat":
                return (str(self.json_obj["response"]["stats"]["servers"][server_key]["vdevs"][str(vdev_key)]["put_latency"]))
