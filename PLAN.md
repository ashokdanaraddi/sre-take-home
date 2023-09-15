Plan:
Approach taken to implement the solution

1. Created the namespace user-hasher in the cluster to isolate the application running in dedicated namespace
Manifest file: [user_hasher-namespace.yaml]

2. Created the deployment Manifest to schedule the pods and taken care of following scenario
   1) Created 2 replicas so that load can be distributed. We can increase the replica count based on the load
   2) Added the rollingUpdate strategy so that pods existing pods will not be terminated until new pods spins up during new service version updating
   3) Added the CPU and Memory resource request and limits for the container
   4) Mounted the secret as environment variable
Manifest file: [user_hasher-deployment.yaml]

3. Created the service for the application in order to access the service from other service or outside using service name. 
   1) Service will takes care of Load balancing and forwards the requests to one of the available pods
Manifest file: [user_hasher-service.yaml]

4. Created the secrets under namespace config and secrets so that these values are passed to container as part of environment variable
Manifest file: [user_salt-secret.yaml]

5. Created PDB (pod distribution budget) so that minimum number of pods available/scheduled to handle to request during maintenance of worker nodes or crash of nodes
Manifest file: [user_hasher-pdb.yaml]

6. Created Horizontal Pod Autoscaler to scale up and down based on the metrics
Manifest file: [user_hasher-hpa.yaml]

   
This implementation is specific to given requirement but can be improved with below additions

1. Utilize the load balancers like HAProxy in Data Center and ALB in AWS
2. Add the ingress controller and add ingress rules with host and path based routing traffic.
3. Add Horizontal Auto Scaling(HPA) and increase/Decrease the pod counts based on the matrx like High CPU or Memory utilization during high traffic
4. Add an anti affinity rules so that same service pods are distributed on nodes 
5. Add liveliness and readiness probes 
6. Add Roll based access control(RBAC) to restrict the access 
7. Setup SSL/TLS certificate on ingress controller for Kubernetes Cluster






