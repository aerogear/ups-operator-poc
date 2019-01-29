# UPS Ansible Operator POC

This is a POC of an Ansible Operator by converting an existing APB for UPS.

Here are the main steps to create this operator:

1. Use the `operator-sdk` cli to generate the structure of the new opeartor with type `Ansible`.
2. Copy the roles from the UPS APB
3. Add the `ansible.kubernetes-modules` and `ansibleplaybookbundle.asb-modules` to the roles as the APB depends on these 2 modules
4. Add `oc` to the built docker image
5. Modify UPS APBs. The main changes are:
  a. Set the `namespace` variable
  b. Use the Ansible `k8s` module instead of the `ansible.kubernetes-modules`. The problem is that the ansible proxy doesn't work with the old module.

To run this operator:

1. Build the image using `operator-sdk build` command
2. Push the operator image to a registry
3. In the target openshift cluster, create the required resources (CRD, roles, rolebindings, serviceaccount etc) that are in the `deploy` directory.
4. Deploy the operator using `deploy/operator.yaml` file.
5. Create the CR `deploy/crds/aerogear_v1alph1_ups_cr.yaml`.
6. Check the logs of the operator and you should see some services are being provisioned into the same namespace.

The main problems I have when creating this operator:

1. Can't get the `operator-sdk up local` command to work. Something to do with how python is setup on my local machine. I ended up building and pushing container images to do testing, which is not very productive.
2. Writing the k8s definitions in YAML is slow. You need to look up the spec and then write the YAML.
3. The logs are hard to read when there is an error occured in the Ansible playbook.
4. Compared to Go, Ansible is a lot harder to write, because it is not a programming language. Because of this, the Operator is missing some logic to not provision the services again if they are already provisioned.

My conclusion:

If the APB is not too complicated, it might be better to just write it in Go because it will be a lot easier to develop, test, write and maintain.
