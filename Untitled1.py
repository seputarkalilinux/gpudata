#!/usr/bin/env python
# coding: utf-8

# In[2]:


import GPUtil
from tabulate import tabulate

def grafik_info():
    gpus = GPUtil.getGPUs()
    list_gpus = []
    for gpu in gpus:
        gpu_id = gpu.id
        gpu_name = gpu.name
        gpu_load = f"{gpu.load*100}%"
        gpu_free_memory = f"{gpu.memoryFree}MB"
        gpu_used_memory = f"{gpu.memoryUsed}MB"
        gpu_total_memory = f"{gpu.memoryTotal}MB"
        gpu_temperature = f"{gpu.temperature} oC"
        gpu_uuid = gpu.uuid
        list_gpus.append((
            gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory, gpu_total_memory, gpu_temperature, gpu_uuid
        ))
    return str(tabulate(list_gpus, headers=("id","name","load", "free memory","used memory","total memory","temperature","uuid"), tablefmt="pretty"))
if __name__ == "__main__":
    print(grafik_info())
    


# In[ ]:





# In[ ]:




