# Copyright 2015 Rackspace
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import urllib

from oslo_serialization import jsonutils
from tempest.common import service_client


class PoolsClientJSON(service_client.ServiceClient):
    """
    Test Pools API
    """

    def list_pools(self, params=None):
        """List all pools"""
        url = 'v2.0/lbaas/pools'
        if params:
            url = '{0}?{1}'.format(url, urllib.urlencode(params))
        resp, body = self.get(url)
        body = jsonutils.loads(body)
        self.expected_success(200, resp.status)
        return service_client.ResponseBodyList(resp, body['pools'])

    def get_pool(self, pool_id, params=None):
        """List details of a pool"""
        url = 'v2.0/lbaas/pools/{pool_id}'.format(pool_id=pool_id)
        if params:
            url = '{0}?{1}'.format(url, urllib.urlencode(params))
        resp, body = self.get(url)
        body = jsonutils.loads(body)
        self.expected_success(200, resp.status)
        return service_client.ResponseBody(resp, body['pool'])

    def create_pool(self, **kwargs):
        """Create a pool"""
        url = 'v2.0/lbaas/pools'
        post_body = jsonutils.dumps({'pool': kwargs})
        resp, body = self.post(url, post_body)
        body = jsonutils.loads(body)
        self.expected_success(201, resp.status)
        return service_client.ResponseBody(resp, body['pool'])

    def update_pool(self, pool_id, **kwargs):
        """Update a pool"""
        url = 'v2.0/lbaas/pools/{pool_id}'.format(pool_id=pool_id)
        post_body = jsonutils.dumps({'pool': kwargs})
        resp, body = self.put(url, post_body)
        body = jsonutils.loads(body)
        self.expected_success(200, resp.status)
        return service_client.ResponseBody(resp, body['pool'])

    def delete_pool(self, pool_id):
        """Delete Pool"""
        url = 'v2.0/lbaas/pools/{pool_id}'.format(pool_id=pool_id)
        resp, body = self.delete(url)
        self.expected_success(204, resp.status)
        return service_client.ResponseBody(resp, body)
