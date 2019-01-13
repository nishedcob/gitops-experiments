#! /bin/bash

if [ ! -x "$(command -v minikube)" ]; then
  echo "No minikube command found. Installing..."
  cd ~/Downloads ; curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64; and sudo install minikube-linux-amd64 /usr/local/bin/minikube
fi
if [ ! -x "$(command -v kubectl)" ]; then
  echo "No kubectl command found. Installing..."
  cd ~/Downloads ; curl -Lo kubectl https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl; and chmod +x kubectl; and sudo cp kubectl /usr/local/bin/; and rm kubectl
fi
if [ ! -x "$(command -v helm)" ]; then
  echo "No helm command found. Installing..."
  cd ~/Downloads ; curl -L https://raw.githubusercontent.com/helm/helm/master/scripts/get -o helm; and chmod +x helm; and sudo install helm /usr/local/bin/helm
fi
if [ ! -x "$(command -v fluxctl)" ]; then
  echo "No helm command found. Installing..."
  cd ~/Downloads ; url -L https://github.com/weaveworks/flux/releases/download/1.8.2/fluxctl_linux_amd64 -o fluxctl ; and chmod -c +x fluxctl ; and sudo cp -v fluxctl /usr/local/bin/ ; and rm -v fluxctl
fi

minikube status || minikube start
kubectl -n kube-system create sa tiller
kubectl create clusterrolebinding tiller-cluster-rule --clusterrole=cluster-admin --serviceaccount=kube-system:tiller
helm init --skip-refresh --upgrade --service-account tiller
helm repo add weaveworks https://weaveworks.github.io/flux
kubectl apply -f deploy
