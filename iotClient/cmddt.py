# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cmddt.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .cmd import confupdatedt
from .cmd import rebootdt


@dataclass
class Cmd(betterproto.Message):
    reboot: rebootdt.Rebootopt = betterproto.message_field(1, group="cmd")
    conf_update: confupdatedt.Confupdateopt = betterproto.message_field(2, group="cmd")


@dataclass
class Cmdin(betterproto.Message):
    cmds: List["Cmd"] = betterproto.message_field(1)