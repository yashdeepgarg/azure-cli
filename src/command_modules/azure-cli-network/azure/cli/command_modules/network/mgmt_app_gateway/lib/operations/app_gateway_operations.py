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

from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError
from msrestazure.azure_operation import AzureOperationPoller
import uuid

from .. import models


class AppGatewayOperations(object):
    """AppGatewayOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An objec model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def create_or_update(
            self, resource_group_name, deployment_name, application_gateway_name, content_version=None, capacity=2, cert_data=None, cert_password=None, frontend_port=None, frontend_type="privateIp", http_listener_protocol="http", http_settings_cookie_based_affinity="disabled", http_settings_port=80, http_settings_protocol="http", location=None, private_ip_address=None, private_ip_address_allocation="dynamic", public_ip_address=None, public_ip_address_allocation="dynamic", public_ip_address_type="none", routing_rule_type="Basic", servers=None, sku_name="Standard_Medium", sku_tier="Standard", subnet="default", subnet_address_prefix="10.0.0.0/24", subnet_type="new", tags=None, virtual_network_name=None, vnet_address_prefix="10.0.0.0/16", custom_headers=None, raw=False, **operation_config):
        """Create a new AppGateway.

        :param resource_group_name: The name of the resource group. The name
         is case insensitive.
        :type resource_group_name: str
        :param deployment_name: The name of the deployment.
        :type deployment_name: str
        :param application_gateway_name: The name of the application gateway.
        :type application_gateway_name: str
        :param content_version: If included it must match the ContentVersion
         in the template.
        :type content_version: str
        :param capacity: The number of instances to use with the application
         gateway.
        :type capacity: int
        :param cert_data: The contents of the PFX certificate file.
        :type cert_data: str
        :param cert_password: The certificate password.
        :type cert_password: str
        :param frontend_port: The front end port number.
        :type frontend_port: int
        :param frontend_type: Specify which kind of frontend configuration to
         create. Possible values include: 'publicIp', 'privateIp'
        :type frontend_type: str or :class:`frontendType
         <Default.models.frontendType>`
        :param http_listener_protocol: The HTTP listener protocol. Possible
         values include: 'http', 'https'
        :type http_listener_protocol: str or :class:`httpListenerProtocol
         <Default.models.httpListenerProtocol>`
        :param http_settings_cookie_based_affinity: Enable or disable HTTP
         settings cookie based affinity. Possible values include: 'enabled',
         'disabled'
        :type http_settings_cookie_based_affinity: str or
         :class:`httpSettingsCookieBasedAffinity
         <Default.models.httpSettingsCookieBasedAffinity>`
        :param http_settings_port: The HTTP settings port.
        :type http_settings_port: int
        :param http_settings_protocol: The HTTP settings protocol. Possible
         values include: 'http', 'https'
        :type http_settings_protocol: str or :class:`httpSettingsProtocol
         <Default.models.httpSettingsProtocol>`
        :param location: The location in which to create the application
         gateway.
        :type location: str
        :param private_ip_address: The static private IP address to associate
         with the application gateway frontend.
        :type private_ip_address: str
        :param private_ip_address_allocation: Specify the kind of private IP
         allocation. Possible values include: 'dynamic', 'static'
        :type private_ip_address_allocation: str or
         :class:`privateIpAddressAllocation
         <Default.models.privateIpAddressAllocation>`
        :param public_ip_address: The name or ID of the public IP address.
        :type public_ip_address: str
        :param public_ip_address_allocation: Specify the kind of public IP
         allocation for new public IPs. Possible values include: 'dynamic',
         'static'
        :type public_ip_address_allocation: str or
         :class:`publicIpAddressAllocation
         <Default.models.publicIpAddressAllocation>`
        :param public_ip_address_type: Specify the type of public IP address.
         Possible values include: 'none', 'new', 'existingName', 'existingId'
        :type public_ip_address_type: str or :class:`publicIpAddressType
         <Default.models.publicIpAddressType>`
        :param routing_rule_type: The request routing rule type. Possible
         values include: 'Basic', 'PathBasedRouting'
        :type routing_rule_type: str or :class:`routingRuleType
         <Default.models.routingRuleType>`
        :param servers: The list of IP addresses or DNS names corresponding
         to backend servers.
        :type servers: list of object
        :param sku_name: The name of the SKU. (Standard_Small,
         Standard_Medium, Standard_Large).
        :type sku_name: str
        :param sku_tier: The SKU tier.
        :type sku_tier: str
        :param subnet: The name or ID of the subnet.
        :type subnet: str
        :param subnet_address_prefix: The subnet prefix in CIDR format.
        :type subnet_address_prefix: str
        :param subnet_type: Use a new or existing subnet. Possible values
         include: 'new', 'existingId', 'existingName'
        :type subnet_type: str or :class:`subnetType
         <Default.models.subnetType>`
        :param tags: Tags object.
        :type tags: object
        :param virtual_network_name: The name of the virtual network (VNet)
         associated with the subnet.
        :type virtual_network_name: str
        :param vnet_address_prefix: The virtual network address range in CIDR
         format.
        :type vnet_address_prefix: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :rtype:
         :class:`AzureOperationPoller<msrestazure.azure_operation.AzureOperationPoller>`
         instance that returns :class:`DeploymentExtended
         <Default.models.DeploymentExtended>`
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        """
        parameters = models.DeploymentAppGateway(content_version=content_version, application_gateway_name=application_gateway_name, capacity=capacity, cert_data=cert_data, cert_password=cert_password, frontend_port=frontend_port, frontend_type=frontend_type, http_listener_protocol=http_listener_protocol, http_settings_cookie_based_affinity=http_settings_cookie_based_affinity, http_settings_port=http_settings_port, http_settings_protocol=http_settings_protocol, location=location, private_ip_address=private_ip_address, private_ip_address_allocation=private_ip_address_allocation, public_ip_address=public_ip_address, public_ip_address_allocation=public_ip_address_allocation, public_ip_address_type=public_ip_address_type, routing_rule_type=routing_rule_type, servers=servers, sku_name=sku_name, sku_tier=sku_tier, subnet=subnet, subnet_address_prefix=subnet_address_prefix, subnet_type=subnet_type, tags=tags, virtual_network_name=virtual_network_name, vnet_address_prefix=vnet_address_prefix)

        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName}'
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=64, min_length=1, pattern='^[-\w\._]+$'),
            'deploymentName': self._serialize.url("deployment_name", deployment_name, 'str', max_length=64, min_length=1, pattern='^[-\w\._]+$'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'DeploymentAppGateway')

        # Construct and send request
        def long_running_send():

            request = self._client.put(url, query_parameters)
            return self._client.send(
                request, header_parameters, body_content, **operation_config)

        def get_long_running_status(status_link, headers=None):

            request = self._client.get(status_link)
            if headers:
                request.headers.update(headers)
            return self._client.send(
                request, header_parameters, **operation_config)

        def get_long_running_output(response):

            if response.status_code not in [200, 201]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            deserialized = None

            if response.status_code == 200:
                deserialized = self._deserialize('DeploymentExtended', response)
            if response.status_code == 201:
                deserialized = self._deserialize('DeploymentExtended', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        if raw:
            response = long_running_send()
            return get_long_running_output(response)

        long_running_operation_timeout = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        return AzureOperationPoller(
            long_running_send, get_long_running_output,
            get_long_running_status, long_running_operation_timeout)
