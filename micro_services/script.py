import os
microservices = os.listdir(".")
print(microservices)
microservices.remove("review")
microservices.remove("restaurant")
microservices.remove("controller")
microservices.remove("script.py")
print(microservices)
microservices=['plate', 'favorite', 'user', 'question', 'report', 'checkin', 'block']
for service in microservices:
    print("Service " + service)
    os.chdir(str(service))
    os.system("ls")
    os.system("docker build --no-cache -t=" + str(service) +"s_service .")
    os.system("docker tag " +str(service)+"s_service hazemsalah/micro_services:" +str(service) +"s_service")
    os.system("docker push hazemsalah/micro_services:"+str(service)+"s_service")
    os.chdir("..")