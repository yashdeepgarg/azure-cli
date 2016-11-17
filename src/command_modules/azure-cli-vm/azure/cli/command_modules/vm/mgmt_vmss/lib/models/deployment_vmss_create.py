# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
#pylint: skip-file
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DeploymentVmssCreate(Model):
    """
    Deployment operation parameters.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar uri: URI referencing the template. Default value:
     "https://azuresdkci.blob.core.windows.net/templatehost/CreateVmssCreate_2016-07-19/azuredeploy.json"
     .
    :vartype uri: str
    :param content_version: If included it must match the ContentVersion in
     the template.
    :type content_version: str
    :ivar _artifacts_location: Container URI of of the template. Default
     value:
     "https://azuresdkci.blob.core.windows.net/templatehost/CreateVmssCreate_2016-07-19"
     .
    :vartype _artifacts_location: str
    :param admin_password: Password for the Virtual Machine.  Required if SSH
     (Linux only) is not specified.
    :type admin_password: str
    :param admin_username: Username for the Virtual Machine.
    :type admin_username: str
    :param authentication_type: Password or SSH Public Key authentication.
     Possible values include: 'password', 'ssh'. Default value: "password" .
    :type authentication_type: str or :class:`authenticationType
     <vmsscreatecreationclient.models.authenticationType>`
    :param custom_os_disk_type: Custom image OS type. Possible values
     include: 'windows', 'linux'. Default value: "windows" .
    :type custom_os_disk_type: str or :class:`customOsDiskType
     <vmsscreatecreationclient.models.customOsDiskType>`
    :param custom_os_disk_uri: URI to a custom disk image.
    :type custom_os_disk_uri: str
    :param dns_name_for_public_ip: Globally unique DNS Name for the Public IP
     used to access the Virtual Machine.  Requires a new public IP to be
     created by setting Public IP Address Type to New.
    :type dns_name_for_public_ip: str
    :param dns_name_type: Associate VMs with a public IP address to a DNS
     name. Possible values include: 'none', 'new'. Default value: "none" .
    :type dns_name_type: str or :class:`dnsNameType
     <vmsscreatecreationclient.models.dnsNameType>`
    :param instance_count: Number of VMs in scale set. Default value: "2" .
    :type instance_count: str
    :param load_balancer_backend_pool_name: Name of load balancer backend
     pool.
    :type load_balancer_backend_pool_name: str
    :param load_balancer_name: Name for load balancer.
    :type load_balancer_name: str
    :param load_balancer_type: Whether to use an existing load balancer,
     create a new one, or use no load balancer. Possible values include:
     'new', 'existing', 'none'. Default value: "new" .
    :type load_balancer_type: str or :class:`loadBalancerType
     <vmsscreatecreationclient.models.loadBalancerType>`
    :param location: Location for VM resources.
    :type location: str
    :param name: The VM name.
    :type name: str
    :param nat_backend_port: Backend NAT port to map. Default value: "22" .
    :type nat_backend_port: str
    :param nat_end_port: End of NAT port range. Default value: "50099" .
    :type nat_end_port: str
    :param nat_start_port: Begining of NAT port range. Default value: "50000"
     .
    :type nat_start_port: str
    :param os_disk_name: Name of new VM OS disk. Default value: "osdiskimage"
     .
    :type os_disk_name: str
    :param os_disk_type: Use a custom image URI from the OS Disk URI
     parameter or use a provider's image. Possible values include:
     'provided', 'custom'. Default value: "provided" .
    :type os_disk_type: str or :class:`osDiskType
     <vmsscreatecreationclient.models.osDiskType>`
    :param os_offer: The OS Offer to install. Default value: "WindowsServer" .
    :type os_offer: str
    :param os_publisher: The OS publisher of the OS image. Default value:
     "MicrosoftWindowsServer" .
    :type os_publisher: str
    :param os_sku: The OS SKU to install. Default value: "2012-R2-Datacenter"
     .
    :type os_sku: str
    :param os_type: Common OS choices.  Choose 'Custom' to specify an image
     with the osPublisher, osOffer, osSKU, and osVersion parameters. Possible
     values include: 'Win2012R2Datacenter', 'Win2012Datacenter',
     'Win2008R2SP1', 'Custom'. Default value: "Win2012R2Datacenter" .
    :type os_type: str or :class:`osType
     <vmsscreatecreationclient.models.osType>`
    :param os_version: The OS version to install. Default value: "latest" .
    :type os_version: str
    :param overprovision: Overprovision option (see
     https://azure.microsoft.com/en-us/documentation/articles/virtual-machine-scale-sets-overview/
     for details). Possible values include: 'true', 'false', 'True', 'False'.
     Default value: "true" .
    :type overprovision: str or :class:`overprovision
     <vmsscreatecreationclient.models.overprovision>`
    :param public_ip_address_allocation: Public IP address allocation method.
     Possible values include: 'dynamic', 'static'. Default value: "dynamic" .
    :type public_ip_address_allocation: str or
     :class:`publicIpAddressAllocation
     <vmsscreatecreationclient.models.publicIpAddressAllocation>`
    :param public_ip_address_name: Name of public IP address to use.
    :type public_ip_address_name: str
    :param public_ip_address_type: Use a public IP Address for the VM Nic.
     Possible values include: 'none', 'new', 'existingName'. Default value:
     "new" .
    :type public_ip_address_type: str or :class:`publicIpAddressType
     <vmsscreatecreationclient.models.publicIpAddressType>`
    :param ssh_dest_key_path: Destination file path on VM for SSH key.
    :type ssh_dest_key_path: str
    :param ssh_key_value: SSH key file data.
    :type ssh_key_value: str
    :param storage_caching: Storage caching type. Possible values include:
     'ReadOnly', 'ReadWrite'. Default value: "ReadOnly" .
    :type storage_caching: str or :class:`storageCaching
     <vmsscreatecreationclient.models.storageCaching>`
    :param storage_container_name: Name of storage container for the VM OS
     disk. Default value: "vhds" .
    :type storage_container_name: str
    :param storage_redundancy_type: The VM storage type (Standard_LRS,
     Standard_GRS, Standard_RAGRS). Default value: "Standard_LRS" .
    :type storage_redundancy_type: str
    :param subnet_ip_address_prefix: The subnet address prefix in CIDR
     format. Default value: "10.0.0.0/24" .
    :type subnet_ip_address_prefix: str
    :param subnet_name: The subnet name.
    :type subnet_name: str
    :param tags: Tags object.
    :type tags: object
    :param upgrade_policy_mode: Manual or Automatic upgrade mode. Possible
     values include: 'manual', 'automatic'. Default value: "manual" .
    :type upgrade_policy_mode: str or :class:`upgradePolicyMode
     <vmsscreatecreationclient.models.upgradePolicyMode>`
    :param virtual_network_ip_address_prefix: The virtual network IP address
     prefix in CIDR format. Default value: "10.0.0.0/16" .
    :type virtual_network_ip_address_prefix: str
    :param virtual_network_name: Name of virtual network to add VM to.
    :type virtual_network_name: str
    :param virtual_network_type: Whether to use an existing VNet or create a
     new one. Possible values include: 'new', 'existing'. Default value:
     "new" .
    :type virtual_network_type: str or :class:`virtualNetworkType
     <vmsscreatecreationclient.models.virtualNetworkType>`
    :param vm_sku: Size of VMs in the VM Scale Set.  See
     https://azure.microsoft.com/en-us/pricing/details/virtual-machines/ for
     size info. Default value: "Standard_D1_v2" .
    :type vm_sku: str
    :ivar mode: Gets or sets the deployment mode. Default value:
     "Incremental" .
    :vartype mode: str
    """ 

    _validation = {
        'uri': {'required': True, 'constant': True},
        '_artifacts_location': {'required': True, 'constant': True},
        'admin_username': {'required': True},
        'name': {'required': True},
        'mode': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'uri': {'key': 'properties.templateLink.uri', 'type': 'str'},
        'content_version': {'key': 'properties.templateLink.contentVersion', 'type': 'str'},
        '_artifacts_location': {'key': 'properties.parameters._artifactsLocation.value', 'type': 'str'},
        'admin_password': {'key': 'properties.parameters.adminPassword.value', 'type': 'str'},
        'admin_username': {'key': 'properties.parameters.adminUsername.value', 'type': 'str'},
        'authentication_type': {'key': 'properties.parameters.authenticationType.value', 'type': 'authenticationType'},
        'custom_os_disk_type': {'key': 'properties.parameters.customOsDiskType.value', 'type': 'customOsDiskType'},
        'custom_os_disk_uri': {'key': 'properties.parameters.customOsDiskUri.value', 'type': 'str'},
        'dns_name_for_public_ip': {'key': 'properties.parameters.dnsNameForPublicIP.value', 'type': 'str'},
        'dns_name_type': {'key': 'properties.parameters.dnsNameType.value', 'type': 'dnsNameType'},
        'instance_count': {'key': 'properties.parameters.instanceCount.value', 'type': 'str'},
        'load_balancer_backend_pool_name': {'key': 'properties.parameters.loadBalancerBackendPoolName.value', 'type': 'str'},
        'load_balancer_name': {'key': 'properties.parameters.loadBalancerName.value', 'type': 'str'},
        'load_balancer_type': {'key': 'properties.parameters.loadBalancerType.value', 'type': 'loadBalancerType'},
        'location': {'key': 'properties.parameters.location.value', 'type': 'str'},
        'name': {'key': 'properties.parameters.name.value', 'type': 'str'},
        'nat_backend_port': {'key': 'properties.parameters.natBackendPort.value', 'type': 'str'},
        'nat_end_port': {'key': 'properties.parameters.natEndPort.value', 'type': 'str'},
        'nat_start_port': {'key': 'properties.parameters.natStartPort.value', 'type': 'str'},
        'os_disk_name': {'key': 'properties.parameters.osDiskName.value', 'type': 'str'},
        'os_disk_type': {'key': 'properties.parameters.osDiskType.value', 'type': 'osDiskType'},
        'os_offer': {'key': 'properties.parameters.osOffer.value', 'type': 'str'},
        'os_publisher': {'key': 'properties.parameters.osPublisher.value', 'type': 'str'},
        'os_sku': {'key': 'properties.parameters.osSKU.value', 'type': 'str'},
        'os_type': {'key': 'properties.parameters.osType.value', 'type': 'osType'},
        'os_version': {'key': 'properties.parameters.osVersion.value', 'type': 'str'},
        'overprovision': {'key': 'properties.parameters.overprovision.value', 'type': 'overprovision'},
        'public_ip_address_allocation': {'key': 'properties.parameters.publicIpAddressAllocation.value', 'type': 'publicIpAddressAllocation'},
        'public_ip_address_name': {'key': 'properties.parameters.publicIpAddressName.value', 'type': 'str'},
        'public_ip_address_type': {'key': 'properties.parameters.publicIpAddressType.value', 'type': 'publicIpAddressType'},
        'ssh_dest_key_path': {'key': 'properties.parameters.sshDestKeyPath.value', 'type': 'str'},
        'ssh_key_value': {'key': 'properties.parameters.sshKeyValue.value', 'type': 'str'},
        'storage_caching': {'key': 'properties.parameters.storageCaching.value', 'type': 'storageCaching'},
        'storage_container_name': {'key': 'properties.parameters.storageContainerName.value', 'type': 'str'},
        'storage_redundancy_type': {'key': 'properties.parameters.storageRedundancyType.value', 'type': 'str'},
        'subnet_ip_address_prefix': {'key': 'properties.parameters.subnetIpAddressPrefix.value', 'type': 'str'},
        'subnet_name': {'key': 'properties.parameters.subnetName.value', 'type': 'str'},
        'tags': {'key': 'properties.parameters.tags.value', 'type': 'object'},
        'upgrade_policy_mode': {'key': 'properties.parameters.upgradePolicyMode.value', 'type': 'upgradePolicyMode'},
        'virtual_network_ip_address_prefix': {'key': 'properties.parameters.virtualNetworkIpAddressPrefix.value', 'type': 'str'},
        'virtual_network_name': {'key': 'properties.parameters.virtualNetworkName.value', 'type': 'str'},
        'virtual_network_type': {'key': 'properties.parameters.virtualNetworkType.value', 'type': 'virtualNetworkType'},
        'vm_sku': {'key': 'properties.parameters.vmSku.value', 'type': 'str'},
        'mode': {'key': 'properties.mode', 'type': 'str'},
    }

    uri = "https://azuresdkci.blob.core.windows.net/templatehost/CreateVmssCreate_2016-07-19/azuredeploy.json"

    _artifacts_location = "https://azuresdkci.blob.core.windows.net/templatehost/CreateVmssCreate_2016-07-19"

    mode = "Incremental"

    def __init__(self, admin_username, name, content_version=None, admin_password=None, authentication_type="password", custom_os_disk_type="windows", custom_os_disk_uri=None, dns_name_for_public_ip=None, dns_name_type="none", instance_count="2", load_balancer_backend_pool_name=None, load_balancer_name=None, load_balancer_type="new", location=None, nat_backend_port="22", nat_end_port="50099", nat_start_port="50000", os_disk_name="osdiskimage", os_disk_type="provided", os_offer="WindowsServer", os_publisher="MicrosoftWindowsServer", os_sku="2012-R2-Datacenter", os_type="Win2012R2Datacenter", os_version="latest", overprovision="true", public_ip_address_allocation="dynamic", public_ip_address_name=None, public_ip_address_type="new", ssh_dest_key_path=None, ssh_key_value=None, storage_caching="ReadOnly", storage_container_name="vhds", storage_redundancy_type="Standard_LRS", subnet_ip_address_prefix="10.0.0.0/24", subnet_name=None, tags=None, upgrade_policy_mode="manual", virtual_network_ip_address_prefix="10.0.0.0/16", virtual_network_name=None, virtual_network_type="new", vm_sku="Standard_D1_v2"):
        self.content_version = content_version
        self.admin_password = admin_password
        self.admin_username = admin_username
        self.authentication_type = authentication_type
        self.custom_os_disk_type = custom_os_disk_type
        self.custom_os_disk_uri = custom_os_disk_uri
        self.dns_name_for_public_ip = dns_name_for_public_ip
        self.dns_name_type = dns_name_type
        self.instance_count = instance_count
        self.load_balancer_backend_pool_name = load_balancer_backend_pool_name
        self.load_balancer_name = load_balancer_name
        self.load_balancer_type = load_balancer_type
        self.location = location
        self.name = name
        self.nat_backend_port = nat_backend_port
        self.nat_end_port = nat_end_port
        self.nat_start_port = nat_start_port
        self.os_disk_name = os_disk_name
        self.os_disk_type = os_disk_type
        self.os_offer = os_offer
        self.os_publisher = os_publisher
        self.os_sku = os_sku
        self.os_type = os_type
        self.os_version = os_version
        self.overprovision = overprovision
        self.public_ip_address_allocation = public_ip_address_allocation
        self.public_ip_address_name = public_ip_address_name
        self.public_ip_address_type = public_ip_address_type
        self.ssh_dest_key_path = ssh_dest_key_path
        self.ssh_key_value = ssh_key_value
        self.storage_caching = storage_caching
        self.storage_container_name = storage_container_name
        self.storage_redundancy_type = storage_redundancy_type
        self.subnet_ip_address_prefix = subnet_ip_address_prefix
        self.subnet_name = subnet_name
        self.tags = tags
        self.upgrade_policy_mode = upgrade_policy_mode
        self.virtual_network_ip_address_prefix = virtual_network_ip_address_prefix
        self.virtual_network_name = virtual_network_name
        self.virtual_network_type = virtual_network_type
        self.vm_sku = vm_sku
