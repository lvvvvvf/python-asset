# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import abc
import typing
import pkg_resources

from google import auth
from google.api_core import exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.api_core import operations_v1  # type: ignore
from google.auth import credentials  # type: ignore

from google.cloud.asset_v1.types import asset_service
from google.longrunning import operations_pb2 as operations  # type: ignore
from google.protobuf import empty_pb2 as empty  # type: ignore


try:
    _client_info = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution("google-cloud-asset",).version,
    )
except pkg_resources.DistributionNotFound:
    _client_info = gapic_v1.client_info.ClientInfo()


class AssetServiceTransport(abc.ABC):
    """Abstract transport class for AssetService."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    def __init__(
        self,
        *,
        host: str = "cloudasset.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: typing.Optional[str] = None,
        scopes: typing.Optional[typing.Sequence[str]] = AUTH_SCOPES,
        quota_project_id: typing.Optional[str] = None,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scope (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
        """
        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = auth.load_credentials_from_file(
                credentials_file, scopes=scopes, quota_project_id=quota_project_id
            )

        elif credentials is None:
            credentials, _ = auth.default(
                scopes=scopes, quota_project_id=quota_project_id
            )

        # Save the credentials.
        self._credentials = credentials

        # Lifted into its own function so it can be stubbed out during tests.
        self._prep_wrapped_messages()

    def _prep_wrapped_messages(self):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.export_assets: gapic_v1.method.wrap_method(
                self.export_assets, default_timeout=60.0, client_info=_client_info,
            ),
            self.batch_get_assets_history: gapic_v1.method.wrap_method(
                self.batch_get_assets_history,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        exceptions.ServiceUnavailable, exceptions.DeadlineExceeded,
                    ),
                ),
                default_timeout=60.0,
                client_info=_client_info,
            ),
            self.create_feed: gapic_v1.method.wrap_method(
                self.create_feed, default_timeout=60.0, client_info=_client_info,
            ),
            self.get_feed: gapic_v1.method.wrap_method(
                self.get_feed,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        exceptions.ServiceUnavailable, exceptions.DeadlineExceeded,
                    ),
                ),
                default_timeout=60.0,
                client_info=_client_info,
            ),
            self.list_feeds: gapic_v1.method.wrap_method(
                self.list_feeds,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        exceptions.ServiceUnavailable, exceptions.DeadlineExceeded,
                    ),
                ),
                default_timeout=60.0,
                client_info=_client_info,
            ),
            self.update_feed: gapic_v1.method.wrap_method(
                self.update_feed, default_timeout=60.0, client_info=_client_info,
            ),
            self.delete_feed: gapic_v1.method.wrap_method(
                self.delete_feed,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        exceptions.ServiceUnavailable, exceptions.DeadlineExceeded,
                    ),
                ),
                default_timeout=60.0,
                client_info=_client_info,
            ),
            self.search_all_resources: gapic_v1.method.wrap_method(
                self.search_all_resources,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        exceptions.ServiceUnavailable, exceptions.DeadlineExceeded,
                    ),
                ),
                default_timeout=15.0,
                client_info=_client_info,
            ),
            self.search_all_iam_policies: gapic_v1.method.wrap_method(
                self.search_all_iam_policies,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        exceptions.ServiceUnavailable, exceptions.DeadlineExceeded,
                    ),
                ),
                default_timeout=15.0,
                client_info=_client_info,
            ),
        }

    @property
    def operations_client(self) -> operations_v1.OperationsClient:
        """Return the client designed to process long-running operations."""
        raise NotImplementedError()

    @property
    def export_assets(
        self,
    ) -> typing.Callable[
        [asset_service.ExportAssetsRequest],
        typing.Union[operations.Operation, typing.Awaitable[operations.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def batch_get_assets_history(
        self,
    ) -> typing.Callable[
        [asset_service.BatchGetAssetsHistoryRequest],
        typing.Union[
            asset_service.BatchGetAssetsHistoryResponse,
            typing.Awaitable[asset_service.BatchGetAssetsHistoryResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_feed(
        self,
    ) -> typing.Callable[
        [asset_service.CreateFeedRequest],
        typing.Union[asset_service.Feed, typing.Awaitable[asset_service.Feed]],
    ]:
        raise NotImplementedError()

    @property
    def get_feed(
        self,
    ) -> typing.Callable[
        [asset_service.GetFeedRequest],
        typing.Union[asset_service.Feed, typing.Awaitable[asset_service.Feed]],
    ]:
        raise NotImplementedError()

    @property
    def list_feeds(
        self,
    ) -> typing.Callable[
        [asset_service.ListFeedsRequest],
        typing.Union[
            asset_service.ListFeedsResponse,
            typing.Awaitable[asset_service.ListFeedsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_feed(
        self,
    ) -> typing.Callable[
        [asset_service.UpdateFeedRequest],
        typing.Union[asset_service.Feed, typing.Awaitable[asset_service.Feed]],
    ]:
        raise NotImplementedError()

    @property
    def delete_feed(
        self,
    ) -> typing.Callable[
        [asset_service.DeleteFeedRequest],
        typing.Union[empty.Empty, typing.Awaitable[empty.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def search_all_resources(
        self,
    ) -> typing.Callable[
        [asset_service.SearchAllResourcesRequest],
        typing.Union[
            asset_service.SearchAllResourcesResponse,
            typing.Awaitable[asset_service.SearchAllResourcesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def search_all_iam_policies(
        self,
    ) -> typing.Callable[
        [asset_service.SearchAllIamPoliciesRequest],
        typing.Union[
            asset_service.SearchAllIamPoliciesResponse,
            typing.Awaitable[asset_service.SearchAllIamPoliciesResponse],
        ],
    ]:
        raise NotImplementedError()


__all__ = ("AssetServiceTransport",)
