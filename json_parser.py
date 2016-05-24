
from json_response import json_response

json_response = json_response("10.3.31.52","8080")

class json_parser():
    def output(self,query,sid,vid):
        server_ids_list = json_response.servers()
        if query == "Cluster Health":
            return (json_response.cluster_health())
        elif query == "nedge-version":
            return (json_response.nedge_version())
        elif query == "Installation GUID":
            return (json_response.nedge_license("Installation GUID"))
        elif query == "License Expiration Date":
            return (json_response.nedge_license("License Expiration Date"))
        elif query == "License Serial Number":
            return (json_response.nedge_license("License Serial Number"))
        elif query == "License Type":
            return (json_response.nedge_license("License Type"))
        elif query == "License Base Capacity":
            return (json_response.nedge_license("License Base Capacity"))
        elif query == "License Status":
            return (json_response.nedge_license("License Status"))
        elif query == "Total IOPS":
            return (json_response.total_iops())
        elif query == "Average Latency":
            return (json_response.average_latency())
        elif query == "Logical Used":
            return (json_response.response_stats_summary("total_logical_used"))
        elif query == "Number of Objects":        
            return (json_response.response_stats_summary("total_num_objects"))
        elif query == "Total Raw Capacity":
            return (json_response.response_stats_summary("total_capacity"))
        elif query == "Physical Allocated":
            return (json_response.response_stats_summary("total_physical_used"))
        elif query == "Physical Free":
            return (json_response.response_stats_summary("total_available"))
        elif query == "Utilization":
            return (json_response.response_stats_summary("total_utilization"))
        elif query == "Estimated Reduction Ratio":
            return (json_response.response_stats_summary("reduction_ratio"))
        elif query == "Estimated Available":
            return (json_response.response_stats_summary("est_total_available"))
        elif query == "Estimated Capacity Savings":
            return (json_response.response_stats_summary("est_capacity_savings"))
        elif query == "servers":
            return (json_response.servers())
        elif query == "Nodes":
            return (json_response.number_of_nodes())
        elif query == "Servers Online/Degraded":
            return (json_response.server_status())
        elif query == "VDEVS Online/Degraded":
            return (json_response.total_vdevs_status())
        elif query == "server_query":
            for index in range(len(server_ids_list)):
                if str(sid) == str(server_ids_list[index]):
                    text = "Server Matched with API"
                    return text
        elif query == "serverid":
            for index in range(len(server_ids_list)):
                if str(sid) == str(server_ids_list[index]):
                    return json_response.server_details(server_ids_list[index],"serverid")
        elif query == "hostname":
            for index in range(len(server_ids_list)):
                if str(sid) == str(server_ids_list[index]):
                    return json_response.server_details(server_ids_list[index],"hostname")
        elif query == "MEM":
            for index in range(len(server_ids_list)):
                if str(sid) == str(server_ids_list[index]):
                    return json_response.server_details(server_ids_list[index],"memtotal")
        elif query == "LAT":
            for index in range(len(server_ids_list)):
                if str(sid) == str(server_ids_list[index]):
                    return json_response.server_details(server_ids_list[index],"latency")
        elif query == "IOPS":
            for index in range(len(server_ids_list)):
                if str(sid) == str(server_ids_list[index]):
                    return json_response.server_details(server_ids_list[index],"iops")
        elif query == "CAPACITY":
            for index in range(len(server_ids_list)):
                if str(sid) == str(server_ids_list[index]):
                    return json_response.server_details(server_ids_list[index],"capacity")
        elif query == "CPU":
            for index in range(len(server_ids_list)):
                if str(sid) == str(server_ids_list[index]):
                    return json_response.server_details(server_ids_list[index],"cpu")
        elif query == "ZONE":
            for index in range(len(server_ids_list)):
                if str(sid) == str(server_ids_list[index]):
                    return json_response.server_details(server_ids_list[index],"zone")
        elif query == "UTILIZATION":
            for index in range(len(server_ids_list)):
                if str(sid) == str(server_ids_list[index]):
                    return json_response.server_details(server_ids_list[index],"utilization")
        elif query == "number_of_vdevs":
            for index in range(len(server_ids_list)):
                if str(sid) == str(server_ids_list[index]):
                    return json_response.number_of_vdevs(server_ids_list[index])
        elif query == "vdev_query":            
            for index in range(len(server_ids_list)):
                if str(sid) == str(server_ids_list[index]):
                    vdevs_ids_list = json_response.vdevs(server_ids_list[index])
                    for vdevs_index in range(len(vdevs_ids_list)):
                        if str(vid) == str(vdevs_ids_list[vdevs_index]):
                            text = "VDEV Matched with API"
                            return text
        elif query == "vdevid":            
            for index in range(len(server_ids_list)):
                if str(sid) == str(server_ids_list[index]):
                    vdevs_ids_list = json_response.vdevs(server_ids_list[index])
                    for vdevs_index in range(len(vdevs_ids_list)):
                        if str(vid) == str(vdevs_ids_list[vdevs_index]):
                            return json_response.vdevs_details(server_ids_list[index],vdevs_ids_list[vdevs_index],"vdevid")
        elif query == "devname":            
            for index in range(len(server_ids_list)):
                if str(sid) == str(server_ids_list[index]):
                    vdevs_ids_list = json_response.vdevs(server_ids_list[index])
                    for vdevs_index in range(len(vdevs_ids_list)):
                        if str(vid) == str(vdevs_ids_list[vdevs_index]):
                            return json_response.vdevs_details(server_ids_list[index],vdevs_ids_list[vdevs_index],"devname")
        elif query == "CAP":            
            for index in range(len(server_ids_list)):
                if str(sid) == str(server_ids_list[index]):
                    vdevs_ids_list = json_response.vdevs(server_ids_list[index])
                    for vdevs_index in range(len(vdevs_ids_list)):
                        if str(vid) == str(vdevs_ids_list[vdevs_index]):
                            return json_response.vdevs_details(server_ids_list[index],vdevs_ids_list[vdevs_index],"capacity")
        elif query == "UTIL":            
            for index in range(len(server_ids_list)):
                if str(sid) == str(server_ids_list[index]):
                    vdevs_ids_list = json_response.vdevs(server_ids_list[index])
                    for vdevs_index in range(len(vdevs_ids_list)):
                        if str(vid) == str(vdevs_ids_list[vdevs_index]):
                            return json_response.vdevs_details(server_ids_list[index],vdevs_ids_list[vdevs_index],"utilization")
        elif query == "RLAT":            
            for index in range(len(server_ids_list)):
                if str(sid) == str(server_ids_list[index]):
                    vdevs_ids_list = json_response.vdevs(server_ids_list[index])
                    for vdevs_index in range(len(vdevs_ids_list)):
                        if str(vid) == str(vdevs_ids_list[vdevs_index]):
                            return json_response.vdevs_details(server_ids_list[index],vdevs_ids_list[vdevs_index],"rlat")
        elif query == "WLAT":            
            for index in range(len(server_ids_list)):
                if str(sid) == str(server_ids_list[index]):
                    vdevs_ids_list = json_response.vdevs(server_ids_list[index])
                    for vdevs_index in range(len(vdevs_ids_list)):
                        if str(vid) == str(vdevs_ids_list[vdevs_index]):
                            return json_response.vdevs_details(server_ids_list[index],vdevs_ids_list[vdevs_index],"wlat")
        elif query == "DEVs":            
            for index in range(len(server_ids_list)):
                if str(sid) == str(server_ids_list[index]):
                    return json_response.vdevs_status(server_ids_list[index])
            



            
            







