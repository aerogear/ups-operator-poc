asb-modules
=========

This role loads modules for [Ansible Service Broker](https://github.com/openshift/ansible-service-broker) and is intended for execution from [Ansible Playbook Bundles](https://github.com/ansibleplaybookbundle/ansible-playbook-bundle).  It is included in apb-base so all modules should be available if your image is built `FROM ansibleplaybookbundle/apb-base`


Installation and use
----------------

Use the Galaxy client to install the role:

```
$ ansible-galaxy install ansibleplaybookbundle.asb-modules
```

Once installed, use the modules in playbook or role:
```yaml
- name: Encodes fields for Ansible Service Broker
  roles:
    - ansibleplaybookbundle.asb-modules
  tasks:
    - name: encode bind credentials
      asb_encode_binding:
        fields:
          ENV_VAR: "value"
          ENV_VAR2: "value2"
```

Modules
-------
- [asb_encode_binding](library/asb_encode_binding.py) - Takes a dictionary of fields and makes them available to Ansible Service Broker to read and create a binding when running the action (provision, bind, etc)
- [asb_save_test_result](library/asb_save_test_result.py) - Takes a message and a test status (failure or success) and will make them available to the APB tool to read and output. This is meant to be used during the test action.

License
-------

Apache V2
