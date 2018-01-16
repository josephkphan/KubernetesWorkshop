# KubernetesWorkshop
Kubernetes Workshop that will deploy a python web app with Flask and Redis in minikube

## Setup Process

### Install Minikube
```
curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.24.1/minikube-darwin-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/
```

### Install kubectl
```
curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/darwin/amd64/kubectl && chmod +x ./kubectl && sudo mv ./kubectl /usr/local/bin/kubectlkubectl 
```

### Start Minikube
```
minikube start --vm-driver=virtualbox
```

---

## Useful Commands

### Check Pods
```
kubectl get pods
```

### Check for Services
```
kubectl get svc
```

### Check for replication controllers
```
kubectl get rc
```

### Cleanup Pods
```
kubectl delete pod redis
kubectl delete svc redis
kubectl delete svc flask-redis-app
kubectl delete pod flask-redis-app
```

### Create Pods 
```
kubectl create -f db-pod.yml
kubectl create -f db-svc.yml
kubectl create -f app-pod.yml
kubectl create -f app-svc.yml
```

### Get into Pod
```
kubectl exec -it flask-redis-app bash
kubectl exec -it redis bash
```

### Create replication controller
```
kubectl create -f app-rc.yml
```

### view the controller
```
kubectl get rc
```

### Scaling the pods manually
```
kubectl scale rc flask-redis-app --replicas=10
```

### Get Details on a service
```
kubectl describe svc <pod_name>
```

### Get Minikube ip
```
minikube ip
```

### Get Exposed Port
```
kubectl get svc flask-redis-app 
```
Look at the port mapping from 5000:<exposed_NodePort> 

### Changing the service live
```
kubectl edit svc flask-redis-app
```


### Make Request to Counter
```
curl <minikube_ip>:<exposed_NodePort>
```

---

### For my notes on kubernetes
https://docs.google.com/document/d/1kpnZqGaHbxbWsH9Tfq60piP8a-LdejdlqAwWbKnHPo8/edit?usp=sharing

### Credit
This project was inspired by Janakiram's Kubernetes webinar series 
