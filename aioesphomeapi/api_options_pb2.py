# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api_options.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='api_options.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x61pi_options.proto\x1a google/protobuf/descriptor.proto\"\x06\n\x04void*F\n\rAPISourceType\x12\x0f\n\x0bSOURCE_BOTH\x10\x00\x12\x11\n\rSOURCE_SERVER\x10\x01\x12\x11\n\rSOURCE_CLIENT\x10\x02:E\n\x16needs_setup_connection\x12\x1e.google.protobuf.MethodOptions\x18\x8e\x08 \x01(\x08:\x04true:C\n\x14needs_authentication\x12\x1e.google.protobuf.MethodOptions\x18\x8f\x08 \x01(\x08:\x04true:/\n\x02id\x12\x1f.google.protobuf.MessageOptions\x18\x8c\x08 \x01(\r:\x01\x30:M\n\x06source\x12\x1f.google.protobuf.MessageOptions\x18\x8d\x08 \x01(\x0e\x32\x0e.APISourceType:\x0bSOURCE_BOTH:/\n\x05ifdef\x12\x1f.google.protobuf.MessageOptions\x18\x8e\x08 \x01(\t:3\n\x03log\x12\x1f.google.protobuf.MessageOptions\x18\x8f\x08 \x01(\x08:\x04true:9\n\x08no_delay\x12\x1f.google.protobuf.MessageOptions\x18\x90\x08 \x01(\x08:\x05\x66\x61lse'
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])

_APISOURCETYPE = _descriptor.EnumDescriptor(
  name='APISourceType',
  full_name='APISourceType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SOURCE_BOTH', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SOURCE_SERVER', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SOURCE_CLIENT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=63,
  serialized_end=133,
)
_sym_db.RegisterEnumDescriptor(_APISOURCETYPE)

APISourceType = enum_type_wrapper.EnumTypeWrapper(_APISOURCETYPE)
SOURCE_BOTH = 0
SOURCE_SERVER = 1
SOURCE_CLIENT = 2

NEEDS_SETUP_CONNECTION_FIELD_NUMBER = 1038
needs_setup_connection = _descriptor.FieldDescriptor(
  name='needs_setup_connection', full_name='needs_setup_connection', index=0,
  number=1038, type=8, cpp_type=7, label=1,
  has_default_value=True, default_value=True,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
NEEDS_AUTHENTICATION_FIELD_NUMBER = 1039
needs_authentication = _descriptor.FieldDescriptor(
  name='needs_authentication', full_name='needs_authentication', index=1,
  number=1039, type=8, cpp_type=7, label=1,
  has_default_value=True, default_value=True,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
ID_FIELD_NUMBER = 1036
id = _descriptor.FieldDescriptor(
  name='id', full_name='id', index=2,
  number=1036, type=13, cpp_type=3, label=1,
  has_default_value=True, default_value=0,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
SOURCE_FIELD_NUMBER = 1037
source = _descriptor.FieldDescriptor(
  name='source', full_name='source', index=3,
  number=1037, type=14, cpp_type=8, label=1,
  has_default_value=True, default_value=0,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
IFDEF_FIELD_NUMBER = 1038
ifdef = _descriptor.FieldDescriptor(
  name='ifdef', full_name='ifdef', index=4,
  number=1038, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=b"".decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
LOG_FIELD_NUMBER = 1039
log = _descriptor.FieldDescriptor(
  name='log', full_name='log', index=5,
  number=1039, type=8, cpp_type=7, label=1,
  has_default_value=True, default_value=True,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
NO_DELAY_FIELD_NUMBER = 1040
no_delay = _descriptor.FieldDescriptor(
  name='no_delay', full_name='no_delay', index=6,
  number=1040, type=8, cpp_type=7, label=1,
  has_default_value=True, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)


_VOID = _descriptor.Descriptor(
  name='void',
  full_name='void',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=61,
)

DESCRIPTOR.message_types_by_name['void'] = _VOID
DESCRIPTOR.enum_types_by_name['APISourceType'] = _APISOURCETYPE
DESCRIPTOR.extensions_by_name['needs_setup_connection'] = needs_setup_connection
DESCRIPTOR.extensions_by_name['needs_authentication'] = needs_authentication
DESCRIPTOR.extensions_by_name['id'] = id
DESCRIPTOR.extensions_by_name['source'] = source
DESCRIPTOR.extensions_by_name['ifdef'] = ifdef
DESCRIPTOR.extensions_by_name['log'] = log
DESCRIPTOR.extensions_by_name['no_delay'] = no_delay
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

void = _reflection.GeneratedProtocolMessageType('void', (_message.Message,), {
  'DESCRIPTOR' : _VOID,
  '__module__' : 'api_options_pb2'
  # @@protoc_insertion_point(class_scope:void)
  })
_sym_db.RegisterMessage(void)

google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(needs_setup_connection)
google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(needs_authentication)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(id)
source.enum_type = _APISOURCETYPE
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(source)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(ifdef)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(log)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(no_delay)

# @@protoc_insertion_point(module_scope)
