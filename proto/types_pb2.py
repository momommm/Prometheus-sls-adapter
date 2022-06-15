# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: types.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0btypes.proto\x12\nprometheus\x1a\x14gogoproto/gogo.proto\"\xf8\x01\n\x0eMetricMetadata\x12\x33\n\x04type\x18\x01 \x01(\x0e\x32%.prometheus.MetricMetadata.MetricType\x12\x1a\n\x12metric_family_name\x18\x02 \x01(\t\x12\x0c\n\x04help\x18\x04 \x01(\t\x12\x0c\n\x04unit\x18\x05 \x01(\t\"y\n\nMetricType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07\x43OUNTER\x10\x01\x12\t\n\x05GAUGE\x10\x02\x12\r\n\tHISTOGRAM\x10\x03\x12\x12\n\x0eGAUGEHISTOGRAM\x10\x04\x12\x0b\n\x07SUMMARY\x10\x05\x12\x08\n\x04INFO\x10\x06\x12\x0c\n\x08STATESET\x10\x07\"*\n\x06Sample\x12\r\n\x05value\x18\x01 \x01(\x01\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\"U\n\x08\x45xemplar\x12\'\n\x06labels\x18\x01 \x03(\x0b\x32\x11.prometheus.LabelB\x04\xc8\xde\x1f\x00\x12\r\n\x05value\x18\x02 \x01(\x01\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\"\x8f\x01\n\nTimeSeries\x12\'\n\x06labels\x18\x01 \x03(\x0b\x32\x11.prometheus.LabelB\x04\xc8\xde\x1f\x00\x12)\n\x07samples\x18\x02 \x03(\x0b\x32\x12.prometheus.SampleB\x04\xc8\xde\x1f\x00\x12-\n\texemplars\x18\x03 \x03(\x0b\x32\x14.prometheus.ExemplarB\x04\xc8\xde\x1f\x00\"$\n\x05Label\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"1\n\x06Labels\x12\'\n\x06labels\x18\x01 \x03(\x0b\x32\x11.prometheus.LabelB\x04\xc8\xde\x1f\x00\"\x82\x01\n\x0cLabelMatcher\x12+\n\x04type\x18\x01 \x01(\x0e\x32\x1d.prometheus.LabelMatcher.Type\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"(\n\x04Type\x12\x06\n\x02\x45Q\x10\x00\x12\x07\n\x03NEQ\x10\x01\x12\x06\n\x02RE\x10\x02\x12\x07\n\x03NRE\x10\x03\"|\n\tReadHints\x12\x0f\n\x07step_ms\x18\x01 \x01(\x03\x12\x0c\n\x04\x66unc\x18\x02 \x01(\t\x12\x10\n\x08start_ms\x18\x03 \x01(\x03\x12\x0e\n\x06\x65nd_ms\x18\x04 \x01(\x03\x12\x10\n\x08grouping\x18\x05 \x03(\t\x12\n\n\x02\x62y\x18\x06 \x01(\x08\x12\x10\n\x08range_ms\x18\x07 \x01(\x03\"\x8b\x01\n\x05\x43hunk\x12\x13\n\x0bmin_time_ms\x18\x01 \x01(\x03\x12\x13\n\x0bmax_time_ms\x18\x02 \x01(\x03\x12(\n\x04type\x18\x03 \x01(\x0e\x32\x1a.prometheus.Chunk.Encoding\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\" \n\x08\x45ncoding\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03XOR\x10\x01\"a\n\rChunkedSeries\x12\'\n\x06labels\x18\x01 \x03(\x0b\x32\x11.prometheus.LabelB\x04\xc8\xde\x1f\x00\x12\'\n\x06\x63hunks\x18\x02 \x03(\x0b\x32\x11.prometheus.ChunkB\x04\xc8\xde\x1f\x00\x42\x08Z\x06prompbb\x06proto3')



_METRICMETADATA = DESCRIPTOR.message_types_by_name['MetricMetadata']
_SAMPLE = DESCRIPTOR.message_types_by_name['Sample']
_EXEMPLAR = DESCRIPTOR.message_types_by_name['Exemplar']
_TIMESERIES = DESCRIPTOR.message_types_by_name['TimeSeries']
_LABEL = DESCRIPTOR.message_types_by_name['Label']
_LABELS = DESCRIPTOR.message_types_by_name['Labels']
_LABELMATCHER = DESCRIPTOR.message_types_by_name['LabelMatcher']
_READHINTS = DESCRIPTOR.message_types_by_name['ReadHints']
_CHUNK = DESCRIPTOR.message_types_by_name['Chunk']
_CHUNKEDSERIES = DESCRIPTOR.message_types_by_name['ChunkedSeries']
_METRICMETADATA_METRICTYPE = _METRICMETADATA.enum_types_by_name['MetricType']
_LABELMATCHER_TYPE = _LABELMATCHER.enum_types_by_name['Type']
_CHUNK_ENCODING = _CHUNK.enum_types_by_name['Encoding']
MetricMetadata = _reflection.GeneratedProtocolMessageType('MetricMetadata', (_message.Message,), {
  'DESCRIPTOR' : _METRICMETADATA,
  '__module__' : 'types_pb2'
  # @@protoc_insertion_point(class_scope:prometheus.MetricMetadata)
  })
_sym_db.RegisterMessage(MetricMetadata)

Sample = _reflection.GeneratedProtocolMessageType('Sample', (_message.Message,), {
  'DESCRIPTOR' : _SAMPLE,
  '__module__' : 'types_pb2'
  # @@protoc_insertion_point(class_scope:prometheus.Sample)
  })
_sym_db.RegisterMessage(Sample)

Exemplar = _reflection.GeneratedProtocolMessageType('Exemplar', (_message.Message,), {
  'DESCRIPTOR' : _EXEMPLAR,
  '__module__' : 'types_pb2'
  # @@protoc_insertion_point(class_scope:prometheus.Exemplar)
  })
_sym_db.RegisterMessage(Exemplar)

TimeSeries = _reflection.GeneratedProtocolMessageType('TimeSeries', (_message.Message,), {
  'DESCRIPTOR' : _TIMESERIES,
  '__module__' : 'types_pb2'
  # @@protoc_insertion_point(class_scope:prometheus.TimeSeries)
  })
_sym_db.RegisterMessage(TimeSeries)

Label = _reflection.GeneratedProtocolMessageType('Label', (_message.Message,), {
  'DESCRIPTOR' : _LABEL,
  '__module__' : 'types_pb2'
  # @@protoc_insertion_point(class_scope:prometheus.Label)
  })
_sym_db.RegisterMessage(Label)

Labels = _reflection.GeneratedProtocolMessageType('Labels', (_message.Message,), {
  'DESCRIPTOR' : _LABELS,
  '__module__' : 'types_pb2'
  # @@protoc_insertion_point(class_scope:prometheus.Labels)
  })
_sym_db.RegisterMessage(Labels)

LabelMatcher = _reflection.GeneratedProtocolMessageType('LabelMatcher', (_message.Message,), {
  'DESCRIPTOR' : _LABELMATCHER,
  '__module__' : 'types_pb2'
  # @@protoc_insertion_point(class_scope:prometheus.LabelMatcher)
  })
_sym_db.RegisterMessage(LabelMatcher)

ReadHints = _reflection.GeneratedProtocolMessageType('ReadHints', (_message.Message,), {
  'DESCRIPTOR' : _READHINTS,
  '__module__' : 'types_pb2'
  # @@protoc_insertion_point(class_scope:prometheus.ReadHints)
  })
_sym_db.RegisterMessage(ReadHints)

Chunk = _reflection.GeneratedProtocolMessageType('Chunk', (_message.Message,), {
  'DESCRIPTOR' : _CHUNK,
  '__module__' : 'types_pb2'
  # @@protoc_insertion_point(class_scope:prometheus.Chunk)
  })
_sym_db.RegisterMessage(Chunk)

ChunkedSeries = _reflection.GeneratedProtocolMessageType('ChunkedSeries', (_message.Message,), {
  'DESCRIPTOR' : _CHUNKEDSERIES,
  '__module__' : 'types_pb2'
  # @@protoc_insertion_point(class_scope:prometheus.ChunkedSeries)
  })
_sym_db.RegisterMessage(ChunkedSeries)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\006prompb'
  _EXEMPLAR.fields_by_name['labels']._options = None
  _EXEMPLAR.fields_by_name['labels']._serialized_options = b'\310\336\037\000'
  _TIMESERIES.fields_by_name['labels']._options = None
  _TIMESERIES.fields_by_name['labels']._serialized_options = b'\310\336\037\000'
  _TIMESERIES.fields_by_name['samples']._options = None
  _TIMESERIES.fields_by_name['samples']._serialized_options = b'\310\336\037\000'
  _TIMESERIES.fields_by_name['exemplars']._options = None
  _TIMESERIES.fields_by_name['exemplars']._serialized_options = b'\310\336\037\000'
  _LABELS.fields_by_name['labels']._options = None
  _LABELS.fields_by_name['labels']._serialized_options = b'\310\336\037\000'
  _CHUNKEDSERIES.fields_by_name['labels']._options = None
  _CHUNKEDSERIES.fields_by_name['labels']._serialized_options = b'\310\336\037\000'
  _CHUNKEDSERIES.fields_by_name['chunks']._options = None
  _CHUNKEDSERIES.fields_by_name['chunks']._serialized_options = b'\310\336\037\000'
  _METRICMETADATA._serialized_start=50
  _METRICMETADATA._serialized_end=298
  _METRICMETADATA_METRICTYPE._serialized_start=177
  _METRICMETADATA_METRICTYPE._serialized_end=298
  _SAMPLE._serialized_start=300
  _SAMPLE._serialized_end=342
  _EXEMPLAR._serialized_start=344
  _EXEMPLAR._serialized_end=429
  _TIMESERIES._serialized_start=432
  _TIMESERIES._serialized_end=575
  _LABEL._serialized_start=577
  _LABEL._serialized_end=613
  _LABELS._serialized_start=615
  _LABELS._serialized_end=664
  _LABELMATCHER._serialized_start=667
  _LABELMATCHER._serialized_end=797
  _LABELMATCHER_TYPE._serialized_start=757
  _LABELMATCHER_TYPE._serialized_end=797
  _READHINTS._serialized_start=799
  _READHINTS._serialized_end=923
  _CHUNK._serialized_start=926
  _CHUNK._serialized_end=1065
  _CHUNK_ENCODING._serialized_start=1033
  _CHUNK_ENCODING._serialized_end=1065
  _CHUNKEDSERIES._serialized_start=1067
  _CHUNKEDSERIES._serialized_end=1164
# @@protoc_insertion_point(module_scope)
