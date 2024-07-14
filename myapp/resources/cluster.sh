k3d cluster create raycluster --servers 1 --agents 2 -p "5000:80@loadbalancer" --k3s-arg "--disable=traefik@server:0" --image "rancher/k3s:v1.29.0-k3s1" --registry-config registry-config.yaml

