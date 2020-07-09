# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/asset_v1p1beta1/proto/assets.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/asset_v1p1beta1/proto/assets.proto",
    package="google.cloud.asset.v1p1beta1",
    syntax="proto3",
    serialized_options=b"\n com.google.cloud.asset.v1p1beta1B\nAssetProtoP\001ZAgoogle.golang.org/genproto/googleapis/cloud/asset/v1p1beta1;asset\370\001\001\252\002\034Google.Cloud.Asset.V1P1Beta1\312\002\034Google\\Cloud\\Asset\\V1p1beta1",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n/google/cloud/asset_v1p1beta1/proto/assets.proto\x12\x1cgoogle.cloud.asset.v1p1beta1\x1a\x1agoogle/iam/v1/policy.proto\x1a\x1cgoogle/api/annotations.proto"\xc2\x02\n\x18StandardResourceMetadata\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nasset_type\x18\x02 \x01(\t\x12\x0f\n\x07project\x18\x03 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x1d\n\x15\x61\x64\x64itional_attributes\x18\n \x03(\t\x12\x10\n\x08location\x18\x0b \x01(\t\x12R\n\x06labels\x18\x0c \x03(\x0b\x32\x42.google.cloud.asset.v1p1beta1.StandardResourceMetadata.LabelsEntry\x12\x14\n\x0cnetwork_tags\x18\r \x03(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xa3\x03\n\x15IamPolicySearchResult\x12\x10\n\x08resource\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x03 \x01(\t\x12%\n\x06policy\x18\x04 \x01(\x0b\x32\x15.google.iam.v1.Policy\x12T\n\x0b\x65xplanation\x18\x05 \x01(\x0b\x32?.google.cloud.asset.v1p1beta1.IamPolicySearchResult.Explanation\x1a\xe9\x01\n\x0b\x45xplanation\x12t\n\x13matched_permissions\x18\x01 \x03(\x0b\x32W.google.cloud.asset.v1p1beta1.IamPolicySearchResult.Explanation.MatchedPermissionsEntry\x1a\x64\n\x17MatchedPermissionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x38\n\x05value\x18\x02 \x01(\x0b\x32).google.cloud.asset.v1p1beta1.Permissions:\x02\x38\x01""\n\x0bPermissions\x12\x13\n\x0bpermissions\x18\x01 \x03(\tB\xb4\x01\n com.google.cloud.asset.v1p1beta1B\nAssetProtoP\x01ZAgoogle.golang.org/genproto/googleapis/cloud/asset/v1p1beta1;asset\xf8\x01\x01\xaa\x02\x1cGoogle.Cloud.Asset.V1P1Beta1\xca\x02\x1cGoogle\\Cloud\\Asset\\V1p1beta1b\x06proto3',
    dependencies=[
        google_dot_iam_dot_v1_dot_policy__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_STANDARDRESOURCEMETADATA_LABELSENTRY = _descriptor.Descriptor(
    name="LabelsEntry",
    full_name="google.cloud.asset.v1p1beta1.StandardResourceMetadata.LabelsEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.cloud.asset.v1p1beta1.StandardResourceMetadata.LabelsEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.cloud.asset.v1p1beta1.StandardResourceMetadata.LabelsEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=417,
    serialized_end=462,
)

_STANDARDRESOURCEMETADATA = _descriptor.Descriptor(
    name="StandardResourceMetadata",
    full_name="google.cloud.asset.v1p1beta1.StandardResourceMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.asset.v1p1beta1.StandardResourceMetadata.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="asset_type",
            full_name="google.cloud.asset.v1p1beta1.StandardResourceMetadata.asset_type",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="project",
            full_name="google.cloud.asset.v1p1beta1.StandardResourceMetadata.project",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="display_name",
            full_name="google.cloud.asset.v1p1beta1.StandardResourceMetadata.display_name",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="description",
            full_name="google.cloud.asset.v1p1beta1.StandardResourceMetadata.description",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="additional_attributes",
            full_name="google.cloud.asset.v1p1beta1.StandardResourceMetadata.additional_attributes",
            index=5,
            number=10,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="location",
            full_name="google.cloud.asset.v1p1beta1.StandardResourceMetadata.location",
            index=6,
            number=11,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="labels",
            full_name="google.cloud.asset.v1p1beta1.StandardResourceMetadata.labels",
            index=7,
            number=12,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="network_tags",
            full_name="google.cloud.asset.v1p1beta1.StandardResourceMetadata.network_tags",
            index=8,
            number=13,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[_STANDARDRESOURCEMETADATA_LABELSENTRY],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=140,
    serialized_end=462,
)


_IAMPOLICYSEARCHRESULT_EXPLANATION_MATCHEDPERMISSIONSENTRY = _descriptor.Descriptor(
    name="MatchedPermissionsEntry",
    full_name="google.cloud.asset.v1p1beta1.IamPolicySearchResult.Explanation.MatchedPermissionsEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.cloud.asset.v1p1beta1.IamPolicySearchResult.Explanation.MatchedPermissionsEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.cloud.asset.v1p1beta1.IamPolicySearchResult.Explanation.MatchedPermissionsEntry.value",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=784,
    serialized_end=884,
)

_IAMPOLICYSEARCHRESULT_EXPLANATION = _descriptor.Descriptor(
    name="Explanation",
    full_name="google.cloud.asset.v1p1beta1.IamPolicySearchResult.Explanation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="matched_permissions",
            full_name="google.cloud.asset.v1p1beta1.IamPolicySearchResult.Explanation.matched_permissions",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        )
    ],
    extensions=[],
    nested_types=[_IAMPOLICYSEARCHRESULT_EXPLANATION_MATCHEDPERMISSIONSENTRY],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=651,
    serialized_end=884,
)

_IAMPOLICYSEARCHRESULT = _descriptor.Descriptor(
    name="IamPolicySearchResult",
    full_name="google.cloud.asset.v1p1beta1.IamPolicySearchResult",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="resource",
            full_name="google.cloud.asset.v1p1beta1.IamPolicySearchResult.resource",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="project",
            full_name="google.cloud.asset.v1p1beta1.IamPolicySearchResult.project",
            index=1,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="policy",
            full_name="google.cloud.asset.v1p1beta1.IamPolicySearchResult.policy",
            index=2,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="explanation",
            full_name="google.cloud.asset.v1p1beta1.IamPolicySearchResult.explanation",
            index=3,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[_IAMPOLICYSEARCHRESULT_EXPLANATION],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=465,
    serialized_end=884,
)


_PERMISSIONS = _descriptor.Descriptor(
    name="Permissions",
    full_name="google.cloud.asset.v1p1beta1.Permissions",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="permissions",
            full_name="google.cloud.asset.v1p1beta1.Permissions.permissions",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=886,
    serialized_end=920,
)

_STANDARDRESOURCEMETADATA_LABELSENTRY.containing_type = _STANDARDRESOURCEMETADATA
_STANDARDRESOURCEMETADATA.fields_by_name[
    "labels"
].message_type = _STANDARDRESOURCEMETADATA_LABELSENTRY
_IAMPOLICYSEARCHRESULT_EXPLANATION_MATCHEDPERMISSIONSENTRY.fields_by_name[
    "value"
].message_type = _PERMISSIONS
_IAMPOLICYSEARCHRESULT_EXPLANATION_MATCHEDPERMISSIONSENTRY.containing_type = (
    _IAMPOLICYSEARCHRESULT_EXPLANATION
)
_IAMPOLICYSEARCHRESULT_EXPLANATION.fields_by_name[
    "matched_permissions"
].message_type = _IAMPOLICYSEARCHRESULT_EXPLANATION_MATCHEDPERMISSIONSENTRY
_IAMPOLICYSEARCHRESULT_EXPLANATION.containing_type = _IAMPOLICYSEARCHRESULT
_IAMPOLICYSEARCHRESULT.fields_by_name[
    "policy"
].message_type = (
    google_dot_iam_dot_v1_dot_policy__pb2.google_dot_iam_dot_v1_dot_policy__pb2._POLICY
)
_IAMPOLICYSEARCHRESULT.fields_by_name[
    "explanation"
].message_type = _IAMPOLICYSEARCHRESULT_EXPLANATION
DESCRIPTOR.message_types_by_name["StandardResourceMetadata"] = _STANDARDRESOURCEMETADATA
DESCRIPTOR.message_types_by_name["IamPolicySearchResult"] = _IAMPOLICYSEARCHRESULT
DESCRIPTOR.message_types_by_name["Permissions"] = _PERMISSIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StandardResourceMetadata = _reflection.GeneratedProtocolMessageType(
    "StandardResourceMetadata",
    (_message.Message,),
    {
        "LabelsEntry": _reflection.GeneratedProtocolMessageType(
            "LabelsEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _STANDARDRESOURCEMETADATA_LABELSENTRY,
                "__module__": "google.cloud.asset_v1p1beta1.proto.assets_pb2"
                # @@protoc_insertion_point(class_scope:google.cloud.asset.v1p1beta1.StandardResourceMetadata.LabelsEntry)
            },
        ),
        "DESCRIPTOR": _STANDARDRESOURCEMETADATA,
        "__module__": "google.cloud.asset_v1p1beta1.proto.assets_pb2",
        "__doc__": """The standard metadata of a cloud resource.
  
  Attributes:
      name:
          The full resource name. For example: ``//compute.googleapis.co
          m/projects/my_project_123/zones/zone1/instances/instance1``.
          See `Resource Names <https://cloud.google.com/apis/design/reso
          urce_names#full_resource_name>`__ for more information.
      asset_type:
          The type of this resource. For example:
          “compute.googleapis.com/Disk”.
      project:
          The project that this resource belongs to, in the form of
          ``projects/{project_number}``.
      display_name:
          The display name of this resource.
      description:
          One or more paragraphs of text description of this resource.
          Maximum length could be up to 1M bytes.
      additional_attributes:
          Additional searchable attributes of this resource.
          Informational only. The exact set of attributes is subject to
          change. For example: project id, DNS name etc.
      location:
          Location can be “global”, regional like “us-east1”, or zonal
          like “us-west1-b”.
      labels:
          Labels associated with this resource. See `Labelling and
          grouping GCP resources
          <https://cloud.google.com/blog/products/gcp/labelling-and-
          grouping-your-google-cloud-platform-resources>`__ for more
          information.
      network_tags:
          Network tags associated with this resource. Like labels,
          network tags are a type of annotations used to group GCP
          resources. See `Labelling GCP resources
          <lhttps://cloud.google.com/blog/products/gcp/labelling-and-
          grouping-your-google-cloud-platform-resources>`__ for more
          information.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.asset.v1p1beta1.StandardResourceMetadata)
    },
)
_sym_db.RegisterMessage(StandardResourceMetadata)
_sym_db.RegisterMessage(StandardResourceMetadata.LabelsEntry)

IamPolicySearchResult = _reflection.GeneratedProtocolMessageType(
    "IamPolicySearchResult",
    (_message.Message,),
    {
        "Explanation": _reflection.GeneratedProtocolMessageType(
            "Explanation",
            (_message.Message,),
            {
                "MatchedPermissionsEntry": _reflection.GeneratedProtocolMessageType(
                    "MatchedPermissionsEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _IAMPOLICYSEARCHRESULT_EXPLANATION_MATCHEDPERMISSIONSENTRY,
                        "__module__": "google.cloud.asset_v1p1beta1.proto.assets_pb2"
                        # @@protoc_insertion_point(class_scope:google.cloud.asset.v1p1beta1.IamPolicySearchResult.Explanation.MatchedPermissionsEntry)
                    },
                ),
                "DESCRIPTOR": _IAMPOLICYSEARCHRESULT_EXPLANATION,
                "__module__": "google.cloud.asset_v1p1beta1.proto.assets_pb2",
                "__doc__": """Explanation about the IAM policy search result.
    
    Attributes:
        matched_permissions:
            The map from roles to their included permission matching the
            permission query (e.g. containing
            ``policy.role.permissions:``). A sample role string:
            “roles/compute.instanceAdmin”. The roles can also be found in
            the returned ``policy`` bindings. Note that the map is
            populated only if requesting with a permission query.
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.asset.v1p1beta1.IamPolicySearchResult.Explanation)
            },
        ),
        "DESCRIPTOR": _IAMPOLICYSEARCHRESULT,
        "__module__": "google.cloud.asset_v1p1beta1.proto.assets_pb2",
        "__doc__": """The result for a IAM Policy search.
  
  Attributes:
      resource:
          The `full resource name <https://cloud.google.com/apis/design/
          resource_names#full_resource_name>`__ of the resource
          associated with this IAM policy.
      project:
          The project that the associated GCP resource belongs to, in
          the form of ``projects/{project_number}``. If an IAM policy is
          set on a resource (like VM instance, Cloud Storage bucket),
          the project field will indicate the project that contains the
          resource. If an IAM policy is set on a folder or orgnization,
          the project field will be empty.
      policy:
          The IAM policy directly set on the given resource. Note that
          the original IAM policy can contain multiple bindings. This
          only contains the bindings that match the given query. For
          queries that don’t contain a constrain on policies (e.g. an
          empty query), this contains all the bindings.
      explanation:
          Explanation about the IAM policy search result. It contains
          additional information to explain why the search result
          matches the query.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.asset.v1p1beta1.IamPolicySearchResult)
    },
)
_sym_db.RegisterMessage(IamPolicySearchResult)
_sym_db.RegisterMessage(IamPolicySearchResult.Explanation)
_sym_db.RegisterMessage(IamPolicySearchResult.Explanation.MatchedPermissionsEntry)

Permissions = _reflection.GeneratedProtocolMessageType(
    "Permissions",
    (_message.Message,),
    {
        "DESCRIPTOR": _PERMISSIONS,
        "__module__": "google.cloud.asset_v1p1beta1.proto.assets_pb2",
        "__doc__": """IAM permissions
  
  Attributes:
      permissions:
          A list of permissions. A sample permission string:
          “compute.disk.get”.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.asset.v1p1beta1.Permissions)
    },
)
_sym_db.RegisterMessage(Permissions)


DESCRIPTOR._options = None
_STANDARDRESOURCEMETADATA_LABELSENTRY._options = None
_IAMPOLICYSEARCHRESULT_EXPLANATION_MATCHEDPERMISSIONSENTRY._options = None
# @@protoc_insertion_point(module_scope)
