# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cmd/rebootdt.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Rebootopt(betterproto.Message):
    perform: bool = betterproto.bool_field(1)
