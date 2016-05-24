class custom_calculation():

    def byte_conversion(self,data_bytes):
        data_kb = data_bytes/1024
        if data_kb < 1024:
            data_kb = round(float(data_kb),2)
            if data_bytes == 0:
                return (str(data_kb)+"0GB")
            else:
                if int(data_kb)== data_kb:
                    return (str(data_kb)+"0KB")
                elif data_kb*10 == int(data_kb*10):
                    return (str(data_kb)+"0KB")
                else:
                    return (str(data_kb)+"KB")
        elif data_kb > 1024 and data_kb < 1024*1024:
            data_mb = round(float(data_kb/1024),2)
            if int(data_mb)== data_mb:
                return (str(data_mb)+"0MB")
            elif data_mb*10 == int(data_mb*10):
                    return (str(data_mb)+"0MB")
            else:
                return (str(data_mb)+"MB")
        elif data_kb > 1024*1024 and data_kb < 1024*1024*1024:
            data_gb = round(float((data_kb/1024)/1024),2)
            if int(data_gb)== data_gb:
                return (str(data_gb)+"0GB")
            elif data_gb*10 == int(data_gb*10):
                    return (str(data_gb)+"0GB")
            else:
                return (str(data_gb)+"GB")
        elif data_kb > 1024*1024*1024 and data_kb < 1024*1024*1024*1024:
            data_tb = round(float(((data_kb/1024)/1024)/1024),2)
            if int(data_tb)== data_tb:
                return (str(data_tb)+"0TB")
            elif data_tb*10 == int(data_tb*10):
                    return (str(data_tb)+"0TB")
            else:
                return (str(data_tb)+"TB")
        elif data_kb > 1024*1024*1024*1024 and data_kb < 1024*1024*1024*1024*1024:
            data_pb = round(float((((data_kb/1024)/1024)/1024)/1024),2)
            if int(data_pb)== data_pb:
                return (str(data_pb)+"0PB")
            elif data_pb*10 == int(data_pb*10):
                    return (str(data_pb)+"0PB")
            else:
                return (str(data_pb)+"PB")

    def byte_conversion_ram(self,data_kb):
        data_mb = round(float(data_kb/1024),2)
        if data_mb < 1024:
            return (str(data_mb)+"MB")
        elif data_mb > 1024 and data_mb < 1024*1024:
            data_gb = round(float(data_mb/1024),2)
            return (str(data_gb)+"GB")
        elif data_mb > 1024*1024 and data_mb < 1024*1024*1024:
            data_tb = round(float((data_mb/1024)/1024),2)
            return (str(data_tb)+"TB")

    def byte_conversion_gib(self,data_bytes):
        data_kb = round(float(data_bytes/1000),2)
        if data_kb < 1024:
            if data_bytes == 0:
                return (str(data_kb)+"0GB")
            else:
                return (str(data_kb)+"KB")
        elif data_kb > 1000 and data_kb < 1000*1000:
            data_mb = round(float(data_kb/1000),2)
            return (str(data_mb)+"MB")
        elif data_kb > 1000*1000 and data_kb < 1000*1000*1000:
            data_gb = round(float((data_kb/1000)/1000),2)
            return (str(data_gb)+"GB")
        elif data_kb > 1000*1000*1000 and data_kb < 1000*1000*1000*1000:
            data_tb = round(float(((data_kb/1000)/1000)/1000),2)
            return (str(data_tb)+"TB")
        elif data_kb > 1000*1000*1000*1000 and data_kb < 1000*1000*1000*1000*1000:
            data_pb = round(float((((data_kb/1000)/1000)/1000)/1000),2)
            return (str(data_pb)+"PB")

    def decimal_approximation(self,value):
        return round(float(value))


